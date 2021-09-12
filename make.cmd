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
    black --check .
    flake8
    goto :eof

:VENV
    call .venv\scripts\activate.bat
    if "%VIRTUAL_ENV%" neq ".venv" exit /b 1
    goto :eof

:USAGE
    echo USAGE:
    echo.
    echo   make ^[init^|docs^|gh-pages^|serve^|lint^]
    echo.
    echo   init        -- setup .venv and install requirements.
    echo   docs        -- build documentation
    echo   deploy-docs -- build documentation and publish on Github Pages
    echo   serve       -- build documentation and serve via development server
    echo   lint        -- run black, flake8 and pytest
    goto :eof
