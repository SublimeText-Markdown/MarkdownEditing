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

    for %%d in ("%~dp0.") do set package=%%~nxd

    echo Createing assets for "%package%"...

    :: create downloadable asset for ST4126+
    set build=3176
    set archive=%package%-%2-st%build%.sublime-package
    set assets="%archive%#%archive%"
    call git tag -f %build%-%2 st%build%
    call git archive --format zip -o "%archive%" %build%-%2

    :: create downloadable asset for ST4134+
    set build=4107
    set archive=%package%-%2-st%build%.sublime-package
    set assets=%assets% "%archive%#%archive%"
    call git tag -f %build%-%2 master
    call git archive --format zip -o "%archive%" %build%-%2

    :: create the release
    call git push --tags --force
    gh release create --target master -t "%package% %2" "%build%-%2" %assets%
    del /f /q *.sublime-package
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
