BIG CHANGES COMING TO THIS! Need to update info as the below is no longer (entirely) true.

Some files that are fun to use. Starting to get a better idea on the structure (Flipper format) of NFC files and payloads.

Some great reading about [Hacking MIFARE & RFID] https://hackmethod.com/hacking-mifare-rfid/?v=7516fd43adaa

----------------------------------------------

Flipper Zero can read the following:
- T5777 Card Freq 125K
- 125 kHz RFID (MiFare Classic Card)
- NFC MiFare Classic Clear Tag
- NFC HID Card Freq 125KHZ
- 125 kHz RFID FourPoints.Com Card NFC
- NFC Mifare Ultral/NTAG Gen1A 1k S50 HF RFID Card
- NFC UID Freq 13.56MHZ Card | NFC Hotel KeyCards
- NFC ValuProx 125kHz ISO

----------------------------------------------

Block_0_Explained https://user-images.githubusercontent.com/57457139/182469731-5b5f2ad0-8ebc-4418-9375-ab97f19a3aeb.png

----------------------------------------------

Example using the RickRoll.nfc file. Leave the data in pages 1 through 6 alone (though not always true, but it is for YouTube links.)

```
 Page 7: 79 6F 75 74
 Page 8: 75 2E 62 65
 Page 9: 2F 64 51 77
Page 10: 34 77 39 57
Page 11: 67 58 63 51
```

This is simply the YouTube share link encoded into HEX and split into 4 byte chunks. See for yourself...

HEX from above: 79 6F 75 74 75 2E 62 65 2F 64 51 77 34 77 39 57 67 58 63 51
[Converted] https://www.binaryhexconverter.com/hex-to-ascii-text-converter : youtu.be/dQw4w9WgXcQ

The last byte in page 6 (0x04) defines what type of encoding https://www.nxp.com/docs/en/data-sheet/NTAG213_215_216.pdf and https://learn.adafruit.com/adafruit-pn532-rfid-nfc/ndef | To convert your link to HEX, use anything such as an online tool: https://onlinehextools.com/convert-ascii-to-hex Read up on https://github.com/RfidResearchGroup/proxmark3/blob/master/doc/cloner_notes.md as they may exist and may be needed to access information.

One limitation is the URL will be truncated if it goes beyond page 11! If your URL is less than exact, pad it with 00, making sure page 12 stays as "FE 00 00 00". Note that TinyURL links appear to fit well and conversion/use is free. If your link doesn't launch automatically when scanned, try using a different URI identifier.
