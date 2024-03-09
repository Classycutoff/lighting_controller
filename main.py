import time
import tkinter as tk
from tkinter import PhotoImage

import utils._global as _global
from utils.DMXClient import DMXClient
from utils.audio_tools import get_audio_stream
from utils.tkinter_func import def_tkinter
from effects.DMX_Effects import ef_all_on, ef_rotate, ef_forward_backward
from effects.DMX_Effects import *
from utils.buttons import *

dmx_channel = 0
counter = 0
dmx_dict = {0: 255, 1: 255, 2: 255}
test = {}
beginning_dict = dmx_dict
end_dict = dmx_dict


def main():
    # def_tkinter()
    KEEP_CONNECTION_UP = False
    try:
        while True:
            try:
                _global.dmxClient.connect()
                while True:
                    root = _global.root
                    root.configure(bg="#cfcfcf")
                    root.geometry("500x200")
                    root.title("DMX Controller App")
                    top = tk.Frame(root, bg="#cfcfcf")
                    bottom = tk.Frame(root, bg="#cfcfcf")
                    top.pack(side="top", pady=10)
                    bottom.pack(side="bottom", fill="both", expand=True)

                    # Create a button to perform the calculation
                    lights_on = tk.Button(
                        root, text="LIGHTS ON!!!!", command=turn_on_all
                    )
                    lights_on.pack(in_=top, side="left", padx=10, pady=5)

                    audio_analysis = tk.Button(
                        root, text="Analyse Audio!!!", command=audio_to_dmx
                    )
                    audio_analysis.pack(in_=top, side="left", padx=10, pady=5)

                    image = PhotoImage(file="stairville_bar.png")
                    image_label = tk.Label(root, image=image)
                    image_label.image = image  # type: ignore
                    image_label.pack(in_=bottom, side="bottom", padx=10, pady=10)

                    # Run the main event loop
                    root.mainloop()

                    # audio_stream_var, dmx_values = get_audio_stream(
                    #     _global.stream, _global.divided_freq_chunks
                    # )
                    # _global.dmxClient.write_DMX(dmx_values)

                    # time.sleep(
                    #     0.04
                    # )  # Added so that KeyBoardInterrupt has time to work.
                    # _global.stream, _global.divided_freq_chunks = audio_stream_var
            except Exception as e:
                print(repr(e))
                _global.dmxClient.close()
                if not KEEP_CONNECTION_UP:
                    break

                _global.dmxClient = DMXClient("DMX_Pipe")
                _global.root = tk.Tk()

    except KeyboardInterrupt as k:
        print(k)
        _global.dmxClient.close()
    except Exception as e:
        print(e)
        _global.dmxClient.close()
        raise e

    _global.dmxClient.close()


if __name__ == "__main__":
    main()
