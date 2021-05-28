from gif_test import frame_brightness_test

#---Test that flashing gifs are detected as flashing, non-flashing gifs are not---
frame_brightness_test('gifs/flashing2.gif')

print('----------break----------')

frame_brightness_test('gifs/flashing.gif')

print('----------break----------')

frame_brightness_test('gifs/animation.gif')

print('----------break----------')

frame_brightness_test('gifs/this nuts.gif')



