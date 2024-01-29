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
- Added a git alias:
```
git config --global alias.yolo '!sh -c "git commit -am \"`curl -sL https://whatthecommit.com/index.txt`\""'

```


## 08.06.2023 22.30 - 22.45 (15 min)

## 11.06.2023 17.45 - 18.46 (1 h 1 min)

## 04.08.2023 18.00 - 22.00 (4 h)
- Vaihdoin kohdetta, että en tänään katsonut usb asioita, vaan katsoin pystynkö vaihtamaan screenillä väriä kun soitan musiikkia.
- Sain tämän onnistumaan
- Made something???


## 05.08.2023 14.00 - 17.00 (3 h)
- Huomasin, miten eilisessä se otti mikin eikä suoraan outputtia, niin latasin vb-audion joka otaa sound outputin, ja laittaa sen inputiksi.
- Yritän nyt selvittää miten voin tehdä että se menee outputtiin ja inputtiin, koska muuten en kuule musiikkia.
- En usko että riittää pelkkä virtuaalinen kaapeli, mä tartten luultavasti virtuaaliseta mikseriä, joka osottaa outputin kumpaankin.
- Lataan Virtual Audio Mixerin VOICEMEETER
- Tämä toimi
- Sain toimimaan, sain eri värejä myöskin näkymään.
- Kokeilin myös laskea miten eri frequency toimivat, ja en tee enää intensiteetillä vaan freq_countilla
  
## 05.08.2023 19.30 - 23.30 (4 h)
- Continued on test/test8/test3.py
- Tried to count more, it just counts couple
- Mä saan koodin helposti reagoimaan ääneen, mutta sen jakamisessa eri taajuuksiin on vaikeaa. Nyt se näyttää vaan jollain tasolla intensiivityyden
- tutkin erilaisia frequency analyzereita, ja en saanut vielä toimimaan. Mutta nämä luultavasti auttavat löytämään ratkaisun.

## 29.01.2024 14.30 - 18.30
- Yritän tutkia missä olin tutkimusten kanssa, koska en muista mitä olin tekemässä.
- Paljon ongelmia sen kanssa, että OpenDMX laitteita ei voi kontrolloida normaaleilla serial kirjastoilla, esimerkiksi PySerial. Varsinkin kun monia kirjastoja löytyy mitkä toimii Pro version kanssa.
- Mun pitää tehdä WinUSB Driveri jotta saan edes kokeiltua toimiiko tämä.