# Changes for the User NFC Key Dictionary (Updated Aug 28, 2022)

Official firmware has introduced a user dict file option which will allow you to update firmware and not lose any added NFC keys! This is great, but requires a slight change in the way things were done previously. I've removed all the NFC keys that are in the original `mf_classic_dict.nfc` provided by Official firmware as of July 26, 2022 and converted what's left over to the new mf_classic_dict_user.nfc file.

-----

Unleashed / RogueMaster have already merged this into their default dict file so no need to grab it!

-----

To use, move the `mf_classic_dict_user.nfc` file into the SD Card -> nfc -> assets folder.

No need to overwrite anything or rename anything. Do that and you're done! Now verify the new keys are recognized
Head over to Flipper -> NFC -> Extra Actions -> Mf Classic Keys and you should see something like this:

You can add more easily using the center button if you discover more!
