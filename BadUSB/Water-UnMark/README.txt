# Water-UnMark

A payload to get rid of the ugly windows activation watermark.

## Description
This script will get rid of the ugly windows watermark. This script will automatically reboot the device. This is not activating your computer!!

## Getting Started

### Dependencies

* Unactivated Windows 10 


### Executing program

* Plug in your device

Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\svsvc" -Name Start -Value 4 -Force



## Contributing

All contributors names will be listed here:

[atomiczsec] https://github.com/atomiczsec


## Version History

* 0.1
    * Initial Release

## Acknowledgments

* [Hak5] https://hak5.org/
* [I-Am-Jakoby] https://github.com/I-Am-Jakoby


