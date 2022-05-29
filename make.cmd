:: This script is used to
:: 1. setup python .venv with requirements installed
:: 2. run all development tasks within that .venv
@echo off
setlocal
chcp 65001 >nul
pushd %~dp0

if /i "%1" == "init" goto INIT
if /i "%1" == "docs" goto DOCS
if /i "%1" == "deploy-docs" goto DEPLOY-DOCS
if /i "%1" == "serve" goto SERVE
if /i "%1" == "lint" goto LINT
if /i "%1" == "release" goto RELEASE
if /i "%1" == "branch" goto BRANCH
goto :usage

:INIT
    if not exist .venv python -m venv .venv
    call :venv
    call python -m pip install --upgrade pip
    call pip install --upgrade -r docs\requirements.txt
    call pip install --upgrade -r tests\requirements.txt
    goto :eof

:DOCS
    call :venv
    mkdocs build
    goto :eof

:DEPLOY-DOCS
    call :venv
    mkdocs gh-deploy
    goto :eof

:SERVE
    call :venv
    call explorer http://localhost:8000
    mkdocs serve
    goto :eof

:LINT
    call :venv
    black .
    flake8
    goto :eof

:BRANCH
    if "%2"== "" goto :usage
    git checkout -b %2
    goto :eof

:RELEASE
    if "%2"== "" goto :usage
    set st3_changelog=release-st3-%2.md
    set st4_changelog=release-st4-%2.md

    if not exist "messages/%st3_changelog%" (
        echo Missing %st3_changelog%
        exit /b 1
    )
    if not exist "messages/%st4_changelog%" (
        echo Missing %st4_changelog%
        exit /b 1
    )
    git checkout st3176 && git merge st3-develop --no-ff
    if not errorlevel 0 (
        echo Unable to merge st3-develop into st3176!
        exit /b 1
    )
    git checkout master && git merge st4-develop --no-ff
    if not errorlevel 0 (
        echo Unable to merge st4-develop into master!
        exit /b 1
    )
    echo Hit any key to push branches!
    pause
    call git push origin st3176
    if not errorlevel 0 (
        echo Failed to push st3176!
        exit /b 1
    )
    call git push origin master
    if not errorlevel 0 (
        echo Failed to push master!
        exit /b 1
    )
    echo Hit any key to publish release!
    pause
    : create release for ST3
    gh release create --target st3176 -t "MarkdownEditing %2 (ST3176+)" -F "messages/%st3_changelog%" "3176-%2"
    : create release for ST3
    gh release create --target master -t "MarkdownEditing %2 (ST4107+)" -F "messages/%st4_changelog%" "4107-%2"
    git fetch
    goto :eof

:VENV
    call .venv\scripts\activate.bat
    if "%VIRTUAL_ENV%" neq ".venv" exit /b 1
    goto :eof

:USAGE
    echo USAGE:
    echo.
    echo   make ^[init^|docs^|gh-pages^|serve^|lint^|branch^|release^]
    echo.
    echo   init          -- setup .venv and install requirements.
    echo   docs          -- build documentation
    echo   deploy-docs   -- build documentation and publish on Github Pages
    echo   serve         -- build documentation and serve via development server
    echo   lint          -- run black, flake8 and pytest
    echo   branch 3.0.0  -- prepare version branch
    echo   release 3.0.0 -- make a release
    goto :eof
