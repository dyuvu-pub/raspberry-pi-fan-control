# raspberry-pi-fan-control

A simple Python script that turns a third-party fan on and off for the Raspberry Pi 3.


## Use-case

Third-party fans for the Raspberry Pi need to be powered by a GPIO interface, so the fan is constantly active. You can plug the cable in and out to turn the fan on and off. However, this script is intended for controlling the fan via a command.


## Set alias in prefered shell profile

Add the following alias to your shell profile to run the script with a defined shortcut:
```
alias fc='~/<SCRIPT_PATH>/fan_control.py'
```