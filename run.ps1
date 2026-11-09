# Run Abrham's Streamlit Portfolio
Set-Location -Path $PSScriptRoot
Write-Host "Starting Abrham Mosye Belsty's Portfolio Website..." -ForegroundColor Cyan
& "$PSScriptRoot\venv\Scripts\streamlit.exe" run "$PSScriptRoot\app.py"
