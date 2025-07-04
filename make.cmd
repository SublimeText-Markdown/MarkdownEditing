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
    set version=%2

    git checkout master && git merge st4-develop --no-ff
    if not errorlevel 0 (
        echo Unable to merge st4-develop into master!
        exit /b 1
    )

    call git push origin master
    if not errorlevel 0 (
        echo Failed to push master!
        exit /b 1
    )

    for %%d in ("%~dp0.") do set package=%%~nxd

    echo Createing assets for "%package%"...

    :: create tag and download asset for ST4152+
    set build=4107
    set branch=st%build%
    set tag=%build%-%version%
    set archive=%package%-%version%-st%build%.sublime-package
    set assets="%archive%#%archive%"
    call git push origin %branch%
    call git tag -f %tag% %branch%
    call git push --force origin %tag%
    call git archive --format zip -o "%archive%" %branch%

    :: create tag and download asset for ST4200+ (master branch)
    set build=4200
    set branch=master
    set tag=%build%-%version%
    set archive=%package%-%version%-st%build%.sublime-package
    set assets=%assets% "%archive%#%archive%"
    call git push origin %branch%
    call git archive --format zip -o "%archive%" %branch%

    :: create the release
    gh release create --target %branch% -t "%package% %version%" "%tag%" %assets%
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
