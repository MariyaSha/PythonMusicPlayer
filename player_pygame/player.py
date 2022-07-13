import pygame
import pygame_gui
from pygame import mixer

# SIZE PARAMETERS
window_size = width, height = (550, 100)
button_size = b_width, b_height = (150, 50)
margin = 15

# LOAD AUDIO FILE
mixer.init()
mixer.music.load("mixkit-forest-treasure-138.mp3") 
mixer.music.set_volume(0.5)

# INITIALIZE PYGAME WINDOW
pygame.init()
pygame.display.set_caption("Simple MP3 Player")
window_surface = pygame.display.set_mode(window_size)

# INITIALIZE UI
background = pygame.Surface(window_size)
background.fill(pygame.Color('darkgrey'))
manager = pygame_gui.UIManager(window_size)

# CREATE GUI WIDGETS
play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((margin, height/2 - b_height/2), button_size),
                                         text="PLAY",
                                         manager=manager)

pause_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((width/3 + margin, height/2 - b_height/2), button_size),
                                         text="PAUSE",
                                         manager=manager)

stop_button = pygame_gui.elements.UIButton(
	relative_rect=pygame.Rect((width/3*2 + margin, height/2 - b_height/2), button_size),
	text="STOP",
	manager=manager)

# TIME COUNTER
clock = pygame.time.Clock()

# STATE PARAMETERS
is_running = True
is_pause = False

# APP DURATION
while is_running:

	# update display in fixed time intervals
	time_delta = clock.tick(60)/1000.0

	# event handler
	for event in pygame.event.get():

		# exit button is pressed
		if event.type == pygame.QUIT:
		    is_running = False

		# any of the action buttons is pressed
		if event.type == pygame_gui.UI_BUTTON_PRESSED:

			# play button
			if event.ui_element == play_button:
				# if playback was already paused - unpause it
				if is_pause:
					pygame.mixer.music.unpause()
					is_pause = False
					pause_button.set_text(text="PAUSE")
				# if 'play' is pressed for the very first time
				else:
					mixer.music.play()

			# pause button
			if event.ui_element == pause_button:
				mixer.music.pause()
				pause_button.set_text(text="PAUSED")
				is_pause = True
				
			# stop button
			if event.ui_element == stop_button:
				mixer.music.stop()

	# display UIManager elements and update them
	manager.process_events(event)
	manager.update(time_delta)
	window_surface.blit(background, (0, 0))
	manager.draw_ui(window_surface)
	pygame.display.update()

pygame.quit()