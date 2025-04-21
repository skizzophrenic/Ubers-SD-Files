# flipperzero-lrs-pagers
FlipperZero Brute force of LRS Pager System from JimiLinuxGuy

Removed the 433 version as it was confirmed to not work for any pagers. (EU is 467 too!)
For the standard 467 version, you'll need to modify the Flipper firmware. See warning below.

This should brute force all resturaunt IDs and pager ids and alert/beep each one for 30s. Verified that this works at Chilis.

Officially supported frequencies: 300-348 MHz, 387-464 MHz, and 779-928 MHz (from CC1101 chip docs)
Unofficially supported frequencies: 281-361 MHz, 378-481 MHz, and 749-962 MHz (from YARD Stick One CC1111 docs)

Official currently does not allow anything outside of the officially supported CC1101 specs.
RogueMaster & CodeGrabber (Unleashed) allows unofficially supported frequencies with the extend_range and dangerous_settings files.

**NOTE: Going outside the officially supported frequencies may DAMAGE YOUR FLIPPER AMP.
Please understand what you're doing if trying to break out of official frequencies.**

You'll need to edit some code and recompile if you want to break outside of the officially supported frequencies.

Referenced Work:
* [LRS Paging Systems]
* [Mayhem Portapack Firmware]
* [Tony-Tiger - Hacking Restaurant Pagers with HackRF]
