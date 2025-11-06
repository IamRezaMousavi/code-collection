if (-not(Test-Path $PROFILE)) {
	New-Item -Path $PROFILE -ItemType File -Force | Out-Null
	Write-Host "Profile created!" -ForegroundColor Green
}

$content = Get-Content $PROFILE -ErrorAction SilentlyContinue
if ($content -match "startship init powershell") {
	Write-Host "Starship command exists" -ForegroundColor Yellow
} else {
	Add-Content -Path $PROFILE -Value "Invoke-Expression (&starship init powershell)"
	Write-Host "Starship command added" -ForegroundColor Green
}

New-Item -Path ~/.config -Type Directory -Force | Out-Null
New-Item ~/.config/starhip.toml | Out-Null
Write-Host "Starship installation is complete" -ForegroundColor Green

