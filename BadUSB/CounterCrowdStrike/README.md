# CounterCrowdStrike DuckyScript

## Author: ooovenenoso

This DuckyScript automates the removal of problematic CrowdStrike files causing BSOD on Windows. The script opens PowerShell as an administrator, sets the execution policy to bypass restrictions, checks for specific CrowdStrike files, deletes them if found, and restarts the computer to complete the fix.

## Background

On July 19, 2024, a CrowdStrike update caused widespread BSOD issues on Windows systems globally, impacting many organizations, including the ABC, Foxtel, the Commonwealth Bank, and more. This incident affected systems in regions such as EU-1, US-1, US-2, and US-GOV-1, causing massive disruptions across various sectors.

## How to Use

1. **Prepare the script**:
   - Copy the DuckyScript provided below and save it as `CounterCrowdStrike.txt`.

2. **Load the script onto the device**:
   - Load the `CounterCrowdStrike.txt` file onto the USB Rubber Ducky or Flipper Zero.

3. **Execute the script**:
   - Insert the USB Rubber Ducky or Flipper Zero into the target computer.
   - The script will run automatically, performing the necessary actions.
