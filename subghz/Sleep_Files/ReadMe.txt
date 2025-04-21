# Blank SUB files for pausing playlists

NOTE: It appears these files may have stopped working on some custom firmware(s) recently ( https://github.com/UberGuidoZ/Flipper/issues/514 ). There is a workaround discovered but it creates much larger files. Since larger files, that risk crashing the FDlipper in certain circumstances, is better than no working files at all, I'd like to provide a ZIP file (thanks martineliascz!) of the new files that appear to work correctly. The temp/workaround files can be downloaded here https://github.com/UberGuidoZ/Flipper/files/14022645/flipper_sleep_files.zip. Hopefully there will be an update soon and we'll be able to revert back to something a bit more managable.

While using the SubGHz Playlist included in most custom firmware, it's been a common question as to how to pause the playlist to wait for something to finish before continuing. While you could record raw data for the needed time, you might pick up other signals that you don't wish to replay. Plus, then you're sitting there recording a long RAW or chaining together a bunch of short ones.

Thanks to darmiel (creator of SubGHz Playlist), the issue is solved! I've confirmed via a pulse plotter and a HackRF these files send "nothing" when played back. They are manually generated, not recorded, and are designed to "pause" playlists by filling the space with nothing. I've sorted the files into Seconds, Minutes, and Hours for ease of finding what you need.

If you'd like to make a custom time, you can do so easily. You'll only need to change one number to the appropriate amount of time needed.

Filetype: Flipper SubGhz RAW File
Version: 1
Frequency: 433920000
Preset: FuriHalSubGhzPresetOok650Async
Protocol: RAW
RAW_Data: 1000 -9999000

The very last number, or -9999000 in the above example, is the amount of time in microseconds. This should be just under the time you want by 1/1000 of a second as the first 1000 counts as one. In the above example, this is 9.999 seconds, which is 10 seconds when you add the first 1000 pulse.

So, to set your own, it's the same as adding 6 zeros to the amount of time in seconds, then subtracting 1/1000. For example, 45 seconds would be -45000000 minus 1/1000 which is -44999000 and the full file would be:

Filetype: Flipper SubGhz RAW File
Version: 1
Frequency: 433920000
Preset: FuriHalSubGhzPresetOok650Async
Protocol: RAW
RAW_Data: 1000 -44999000

To use these, simply put the SUB file in the spot of your playlist where you need it to pause. The Flipper will still appear to be sending something, but in fact it's sending a blank signal for the specified time.
