@echo off
chcp 65001 >nul
echo ================================
echo 开始构建和部署到 GitHub Pages
echo ================================
echo.

REM 1. 清理旧的 git 仓库
echo [1/5] 清理旧的部署文件...
if exist dist\.git (
    rmdir /s /q dist\.git
    echo ✓ 清理完成
) else (
    echo ✓ 无需清理
)
echo.

REM 2. 构建项目
echo [2/5] 正在构建项目...
call pnpm build
if %errorlevel% neq 0 (
    echo 构建失败！
    pause
    exit /b %errorlevel%
)
echo ✓ 构建完成
echo.

REM 3. 进入 dist 目录
echo [3/5] 进入 dist 目录...
cd dist
if %errorlevel% neq 0 (
    echo 错误：找不到 dist 目录
    pause
    exit /b %errorlevel%
)
echo.

REM 4. 初始化 git 并提交
echo [4/5] 准备 Git 提交...
if exist .git (
    rmdir /s /q .git
)
git init
git config user.name "ClarisseMak"
git config user.email "clarisse@example.com"
git add -A
git commit -m "deploy: %date% %time%"
echo ✓ Git 提交完成
echo.

REM 5. 推送到 GitHub
echo [5/5] 推送到 GitHub miaolizi 分支...
git branch -M miaolizi
git remote add origin https://github.com/ClarisseMak/portfolio-for-image.git
git push -f origin miaolizi
if %errorlevel% neq 0 (
    echo 推送失败！请检查：
    echo 1. 是否已修改脚本中的仓库地址
    echo 2. 是否有推送权限
    echo 3. 网络连接是否正常
    cd ..
    pause
    exit /b %errorlevel%
)
echo.

REM 6. 返回项目根目录
cd ..

echo ================================
echo ✓ 部署完成！
echo ================================
echo.
echo 你的网站将在几分钟内更新到：
echo https://blog.clarissemaischamber.website
echo.
pause

