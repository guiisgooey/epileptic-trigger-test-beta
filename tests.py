from gif_test import frame_brightness_test

#---Test that flashing gifs are detected as flashing, non-flashing gifs are not---
assert frame_brightness_test('gifs/flashing2.gif') == True

print('----------break----------')

assert frame_brightness_test('gifs/flashing.gif') == True

print('----------break----------')

assert frame_brightness_test('gifs/animation.gif') == False

print('----------break----------')

assert frame_brightness_test('gifs/this nuts.gif') == True



