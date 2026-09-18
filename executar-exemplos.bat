@echo off
setlocal
cd /d "%~dp0"

set "PYTHON_EXE=python"
where python >nul 2>nul
if errorlevel 1 set "PYTHON_EXE=%USERPROFILE%\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"

set "NODE_DIR=%USERPROFILE%\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin"
where node >nul 2>nul
if errorlevel 1 set "PATH=%NODE_DIR%;%PATH%"

echo === PYTHON: LISTAS ===
"%PYTHON_EXE%" python\listas\lista.py
echo.

echo === PYTHON: ALUNO ===
"%PYTHON_EXE%" python\poo\aluno.py
echo.

echo === PYTHON: CACHORRO ===
"%PYTHON_EXE%" python\poo\cachorro.py
echo.

echo === TYPESCRIPT: VERIFICACAO ===
pushd typescript
call node_modules\.bin\tsc.cmd --noEmit
if errorlevel 1 goto erro

echo Compilacao concluida sem erros.
call node_modules\.bin\tsx.cmd src\app.ts
call node_modules\.bin\tsx.cmd src\variaveis.ts
node src\soma.js
popd

echo.
echo Todos os exemplos foram executados.
pause
exit /b 0

:erro
popd
echo O TypeScript apresentou um erro de compilacao.
pause
exit /b 1

