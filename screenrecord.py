import cv2, numpy, pyautogui, keyboard

filename = "record"
screen_size =(1920, 1080)
codec = cv2.VideoWriter_fourcc(*'mp4v')
vid = cv2.VideoWriter(filename + '.mp4', codec, 30.0, screen_size)
while True:
    img = pyautogui.screenshot()
    numpy_frame = numpy.array(img)
    frame = cv2.cvtColor(numpy_frame, cv2.COLOR_BGR2RGB)
    if (keyboard.is_pressed('x')):
        break

cv2.destroyAllWindows()
vid.release()