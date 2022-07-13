import dearpygui.dearpygui as dpg
from pygame import mixer

# SIZE PARAMETERS
window_size = width, height = (525, 250)
button_size = b_width, b_height = (150, 50)
margin = 15

# LOAD AUDIO FILE
mixer.init()
mixer.music.load("mixkit-forest-treasure-138.mp3") 
mixer.music.set_volume(0.5)

# STATE PARAMETER
is_pause = [False]

# BUTTON CALLBACKS
def play_callback(pause):
    if pause:
        mixer.music.unpause()
    else:
        mixer.music.play()
        is_pause[0] = False

def pause_callback():
    mixer.music.pause()
    is_pause[0] = True

def stop_callback():
    mixer.music.stop()
    is_pause[0] = False

# INITIALIZE GUI WINDOW
dpg.create_context()
dpg.create_viewport(width=width, height=height)
dpg.setup_dearpygui()

# INITIALIZE GUI WIDGETS
with dpg.window(label="Python Music Player", width=width, height=height):
    # play button
    dpg.add_button(
        label="PLAY", 
        width=b_width, 
        height=b_height, 
        pos=(margin, height/2 - b_height/2), 
        callback=lambda:play_callback(is_pause[0])
        )
    # pause button
    dpg.add_button(
        label="PAUSE", 
        width=b_width, 
        height=b_height, 
        pos=(b_width + margin*2 , height/2 - b_height/2), 
        callback=pause_callback
        )
    # stop button
    dpg.add_button(
        label="STOP", 
        width=b_width, 
        height=b_height, 
        pos=(b_width*2 + margin*3, height/2 - b_height/2),
        callback=stop_callback
        )

# DISPLAY APPLICATION
dpg.show_viewport()
dpg.start_dearpygui()

# COLLAPSE APPLICATION
dpg.destroy_context()

