# If execution policy is not set to Unrestricted, change it
if ($executionPolicy -ne "Unrestricted") {
    Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser -Force
}

# Set Windows Update service to manual start
Set-Service -Name wuauserv -StartupType Manual

# Stop Windows Update service
Stop-Service -Name wuauserv

# Disable Windows Update scheduled tasks
Disable-ScheduledTask -TaskPath '\Microsoft\Windows\WindowsUpdate' -TaskName 'Scheduled Start' -ErrorAction SilentlyContinue
Disable-ScheduledTask -TaskPath '\Microsoft\Windows\WindowsUpdate' -TaskName 'Scheduled Start With Network' -ErrorAction SilentlyContinue
Disable-ScheduledTask -TaskPath '\Microsoft\Windows\WindowsUpdate' -TaskName 'Scheduled Start With Automatic Maintenance' -ErrorAction SilentlyContinue

# Create a registry key to block Windows Update
$registryPath = 'HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate'
New-Item -Path $registryPath -Force | Out-Null
New-ItemProperty -Path $registryPath -Name 'AUOptions' -Value 1 -PropertyType DWORD -Force | Out-Null

# Disable Windows Update Orchestrator service
Set-Service -Name "UsoSvc" -StartupType Disabled

# Disable Windows Update Medic service
Set-Service -Name "waaSMedicSvc" -StartupType Disabled

Write-Host 'Windows updates have been blocked.'

# Restart the computer to apply changes
Restart-Computer -Confirm
