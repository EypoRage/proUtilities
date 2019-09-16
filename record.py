import keyboard

recorded = keyboard.record(until='esc')

keyboard.play(recorded, speed_factor=1)