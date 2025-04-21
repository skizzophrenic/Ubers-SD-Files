# Fun with Restaurant Pagers

Officially supported frequencies: 300-348 MHz, 387-464 MHz, and 779-928 MHz (from CC1101 chip docs)
Unofficially supported frequencies: 281-361 MHz, 378-481 MHz, and 749-962 MHz (from YARD Stick One CC1111 docs)

Official currently does not allow anything outside of the officially supported CC1101 specs.
RogueMaster & CodeGrabber (Unleashed) allows unofficially supported frequencies with the `extend_range` and `dangerous_settings` files.

**NOTE: Going outside the officially supported frequencies may DAMAGE YOUR FLIPPER AMP.
Please understand what you're doing if trying to break out of official frequencies.**

The frequency range of the chip is always tested in the verification tests and there is always some design margin included before
the VCO and/or PLL has problems operating for a specified frequency range. Working outside the frequency range can cause issues
with the VCO and/or PLL and/or divider not operating correctly. If the VCO is operating outside it's standard frequency range,
there are risks of unwanted emissions and no oscillation. The PLL can also fail to lock if operating outside it's standard
frequency range and will still apply power to the antenna.

Risks with antenna mismatch are increased harmonics, reduced output power and increased current consumption. Generally, the antenna
mismatch can be large and the output stage will not be damaged when presented with a large mismatch for short periods of time.
However, if the antenna mismatch is very poor for long periods of time, then this can effect the longevity of the chip especially
if further stressed with maximum voltage and maximum temperature. Recommend keeping VSWR better than 5:1 for worst case scenarios.
