# README

- Owner: Eliel Taskinen
- Student Code: AA3737
- Email: elieltaskinen@gmail.com

This is the Thesis git for Eliel Taskinen. It is meant to make a lighting controller, which in the final form can be made to recognize sound and make a "vizual equalizer" with two LED bars (Stairville, Led Bar 120/4).


Code to run the env: `source start.sh`

deactivate env: `deactivate`

# Time Spent on this project

10.3.23: 1.5 h

# TODO List

 - [X] Check the lights and Enttec OpenDMX works
	 - This is Achieved by testing the dmx with another lighting control software(I used Freestyler) and nothing is broken.
 - [X] Find The Correct USB
	 - I have a file find_usb.py that outputted all of the USB's, and I compared the output before and after I took Enttec OpenDMX off.
 - [ ] Make the USB work by sending some signal.
 - [ ] Make the DMX work by using python.
 - [ ] Make the correct lights (RGB) work.
 - [ ] Make sequences of the lights.
 - [ ] Make fades work.
 - [ ] Make a user interface.
	 - [ ]  Make it so that you can configure the sequences in it and to make new sequences to it.
	 - [ ] Control RGB inside the UI.
	 - [ ] Visualize the light?
 - [ ] Make the visual equalizer.
	 - [ ] Analyze sound.
		 - [ ] How?
	 - [ ] Section it off logarithmically.
	 - [ ] Connect it to the lights.


# Sequence structure

```
{
    name: Sequence Name,
    time: Time Between Segments in Seconds,
    stay: Time The Sequence stays in the segments,
    seq: List of RGB tuple values, that say what the segments will be. Example: [(0,0,0), (125,125,125), (255,0,0), (0,255,0)]
}
```
