from time import sleep
from PIL import Image
from mss import mss
import numpy as np
import cv2, keyboard
x = mss()
count = 0
while True:
    x.get_pixels({'top': 200, 'left': 160, 'width': 800, 'height': 200})
    y = np.array(Image.frombytes('RGB', (x.width, x.height), x.image))
    obj2 = y[125:155 , 110:155]
    gray = cv2.cvtColor(obj2, cv2.COLOR_BGR2GRAY)
    th, threshed = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
    cnts = cv2.findContours(threshed, cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[-2]
    count = len(cnts)
    if count >= 1:
        keyboard.press_and_release('space')
    cv2.putText(y, str(count), (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
    cv2.imshow('bot', np.array(y))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break