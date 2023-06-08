# Diary

This is what I've done every time I've worked on this.

## 10.3.2023 3h

- Started with the thesis project.
- Tested that lights and OpenDMX work.
- Started the work on git.
- Started using Pyusb, and how I could do this.
- Found couple of direct USB to DMX gits, but I don't want to use them. I want to learn them by myself.
- Foundout what the VendorID and ProductID is for OpenDMX (find_usb dir).
- Did Readme and TODO list.
- Used couple of tutorials to get it working: [Pyusb tutorial](https://github.com/pyusb/pyusb/blob/master/docs/tutorial.rst)..
- OpenDMX doesn't have drivers, so have to install Zadig to install WinUSB [How to use Libusb on Windows](https://github.com/libusb/libusb/wiki/Windows#How_to_use_libusb_on_Windows).
  - libusb is the backend for pyusb.

## 06.06.2023 3 h
- Worked on connecting the lamp to the software
- Piti ladata WinUSB koska kuulemma pyusb ei toimi suoraan Windowsilla
- https://stackoverflow.com/questions/31960314/pyusb-1-0-notimplementederror-operation-not-supported-or-unimplemented-on-this
- https://github.com/libusb/libusb/wiki/Windows#How_to_use_libusb_on_Windows
- https://zadig.akeo.ie/
- Open Enttex had it's own driver, but i had to swap it to another one with Zadig.

## 07.06.2023 21.15 - 22.03 (0h 48 min)
- Worked on the env
- Made the virtualenv, requirements.txt etc


## 08.06.2023 19.40 - 22.17 (2 h 37 min)
- Worked on git
  - Cloned my thesis git to github.
- Tried to get the communication working
- Managed to untangle the driver fiasco. Turns out I didn't need the Win or lib drivers
- I had to find the port, which required uninstalling third party drivers.
- I can now again control the light from the lighting software
- I cannot get it working from the code. Frustrating
- Testi
