# DMX Knowledge

DMX512 (or commonly just DMX) is a relatively simple protocol. 

The DMX bus is in an Idle high state between packets. A packet starts with a break of 100 μs, 
followed by a Mark After Break (MAB) of 12 μs, this signifies the start of the frame and the start of the "slots".

Each slot consists of 1 low start bit, 8 data bits, and 2 high stop bits. Each bit of a slot is 4 μs long. This corresponds to a baudrate of 250000 or 250 kbit/s (though due to breaks this is not entirely accurate). There are 512 usable slots (channels) per frame and 513 slots overall. Slot 0 is special as it signifies the type of frame being sent. 0x00 is the normal frame type and corresponds to "standard" lighting data.

A frame can contain any number of slots (beyond the type slot) up to the limit of 513 slots (including type slot). Typically the 512 usable slots are referred to as channels.

The idle period between packets must be at least 92 μs and the MAB must be at least 12 μs. Further a packet must not be longer than 1 second. There are no other requirements on timing, even on inter-slot breaks.

A light will typically take an "address" which is the channel index (starting at 1) which it will listen on. Some lights will use this as a start address and listen on some number of channels above it also if they require more than 8 bits of data.

For example a light might be set to address eight, but listen on channels 8 9, and 10. It could then use each channel as a component of an RGB colour value.

Importantly for writing software relating to DMX, the standard does not specify how to encode different types of data in slots. Therefore, each light manufacturer, or even light, does it differently. There is nothing stopping a manufacturer allowing you to select noncontiguous addresses for each 8 bit value, or any number of more convoluted solutions.