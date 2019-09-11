import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import PressKey, W, A, S, D

def screen_record():
    template = cv2.imread('template.png', 0)
    last_time = time.time()
    while(True):
        # 800x600 windowed mode
        #PressKey(W)
        press=False

        printscreen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()


        img_rgb = printscreen
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)


        w, h = template.shape[::-1]

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.6
        loc = np.where(res >= threshold)

        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
            press= True

        #if press == True:
            #PressKey(W)

        cv2.imshow('window',cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB))
        #time.sleep(0.5)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()

            break
screen_record()
