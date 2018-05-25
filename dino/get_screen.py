import numpy as np
import cv2
from PIL import ImageGrab

def get_screen(positions=(250,400,900,700)):
    return cv2.cvtColor(np.array(ImageGrab.grab(bbox=(250,400,900,700))),cv2.COLOR_BGR2GRAY)
if __name__ == '__main__':
    while(True):
        frame = get_screen()
        cv2.imshow('WindowName', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
