<# Setting registry values to stop windows update #>
$keyUX = 'Registry::HKLM\SOFTWARE\Microsoft\WindowsUpdate\UX\Settings'
$keyAU = 'Registry::HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU'
$dateStart = '0000-01-01T00:00:00Z'
$dateEnd = '3000-12-31T11:59:59Z'
$getWinver = (Get-WmiObject -class Win32_OperatingSystem).Caption
Set-ItemProperty -Path $keyUX -Name 'PauseFeatureUpdatesStartTime' -Value $dateStart
Set-ItemProperty -Path $keyUX -Name 'PauseQualityUpdatesStartTime' -Value $dateStart
Set-ItemProperty -Path $keyUX -Name 'PauseUpdatesStartTime' -Value $dateStart -EA SilentlyContinue
Set-ItemProperty -Path $keyUX -Name 'PauseFeatureUpdatesEndTime' -Value $dateEnd
Set-ItemProperty -Path $keyUX -Name 'PauseQualityUpdatesEndTime' -Value $dateEnd
Set-ItemProperty -Path $keyUX -Name 'PauseUpdatesExpiryTime' -Value $dateEnd
if ($getWinver.Contains("Windows 11")) {
New-Item -Force -Path $keyAU > $null
New-ItemProperty -Force -Path $keyAU -PropertyType DWORD -Name 'NoAutoUpdate' -Value 1 > $null
}

<# Completion message #>
$toast = [Windows.UI.Notifications.ToastTemplateType, Windows.UI.Notifications, ContentType = WindowsRuntime]::ToastText04
$toastTemplate = [Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime]::GetTemplateContent($toast)
$toastTemplate.SelectSingleNode('//text[@id= "1"]').InnerText= 'Windows更新将于3000年12月31日重新启动'
$toastTemplate.SelectSingleNode('//text[@id= "2"]').InnerText= '  '
$toastTemplate.SelectSingleNode('//text[@id= "3"]').InnerText= '您可以通过单击Windows更新窗口中的继续更新按钮来恢复Windows更新功能。'
[Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier(' ').Show($toastTemplate)
