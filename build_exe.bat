@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

title Tarkov Grenade Calculator Auto Builder

echo.
echo ============================================================
echo  Tarkov Grenade Calculator Auto Builder
echo  自动识别当前目录下的 Python 文件并使用 PyInstaller 打包
echo ============================================================
echo.

cd /d "%~dp0"

echo 当前工作目录:
echo %cd%
echo.

set "PY_CMD="

py --version >nul 2>nul
if not errorlevel 1 (
    set "PY_CMD=py"
) else (
    python --version >nul 2>nul
    if not errorlevel 1 (
        set "PY_CMD=python"
    )
)

if "%PY_CMD%"=="" (
    echo [错误] 未检测到 Python。
    echo 请先安装 Python，并确保 py 或 python 命令可用。
    echo.
    pause
    exit /b 1
)

echo [信息] 使用 Python 命令: %PY_CMD%
echo.

%PY_CMD% -m PyInstaller --version >nul 2>nul
if errorlevel 1 (
    echo [提示] 未检测到 PyInstaller，正在自动安装...
    echo.
    %PY_CMD% -m pip install pyinstaller
    if errorlevel 1 (
        echo.
        echo [错误] PyInstaller 安装失败。
        echo 请手动执行:
        echo %PY_CMD% -m pip install pyinstaller
        echo.
        pause
        exit /b 1
    )
)

echo [信息] PyInstaller 已就绪。
echo.

set /a COUNT=0

for %%F in (*.py) do (
    set "FILE_NAME=%%~nxF"
    set "BASE_NAME=%%~nF"

    if /i not "!FILE_NAME!"=="setup.py" (
        set /a COUNT+=1
        set "PY_FILE_!COUNT!=%%~nxF"
        set "PY_BASE_!COUNT!=%%~nF"
        echo [!COUNT!] %%~nxF
    )
)

echo.

if %COUNT% EQU 0 (
    echo [错误] 当前目录下没有找到可打包的 .py 文件。
    echo.
    pause
    exit /b 1
)

if %COUNT% EQU 1 (
    set "TARGET_FILE=!PY_FILE_1!"
    set "TARGET_BASE=!PY_BASE_1!"
) else (
    set /p SELECT_INDEX=检测到多个 .py 文件，请输入要打包的编号: 

    if "!SELECT_INDEX!"=="" (
        echo.
        echo [错误] 未输入编号。
        echo.
        pause
        exit /b 1
    )

    if not defined PY_FILE_!SELECT_INDEX! (
        echo.
        echo [错误] 编号无效。
        echo.
        pause
        exit /b 1
    )

    set "TARGET_FILE=!PY_FILE_%SELECT_INDEX%!"
    set "TARGET_BASE=!PY_BASE_%SELECT_INDEX%!"
)

echo.
echo [信息] 目标 Python 文件:
echo %TARGET_FILE%
echo.

set "EXE_NAME=%TARGET_BASE%"

echo [信息] 输出 EXE 名称:
echo %EXE_NAME%.exe
echo.

echo ============================================================
echo  开始打包
echo ============================================================
echo.

%PY_CMD% -m PyInstaller -F -w -n "%EXE_NAME%" "%TARGET_FILE%"

if errorlevel 1 (
    echo.
    echo ============================================================
    echo  [错误] 打包失败
    echo ============================================================
    echo.
    pause
    exit /b 1
)

echo.
echo ============================================================
echo  打包完成
echo ============================================================
echo.
echo 生成文件位置:
echo %cd%\dist\%EXE_NAME%.exe
echo.

pause
exit /b 0