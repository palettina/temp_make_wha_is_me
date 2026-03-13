cd /d "%~dp0"
git add -A
git commit -m "addition"
git push
pwsh -NoLogo -NoProfile -ExecutionPolicy Bypass -File "%~dp0auto_jules.ps1" %*
