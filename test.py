from epilepsy_test import frame_test

#---Test that flashing gifs are detected as flashing, non-flashing gifs are not---
frame_test('gifs/flashing2.gif')

print('----------break----------')

frame_test('gifs/flashing.gif')

print('----------break----------')

frame_test('gifs/animation.gif')

print('----------break----------')

frame_test('gifs/this nuts.gif')



