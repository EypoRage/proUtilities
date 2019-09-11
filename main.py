import time
import random
import directkeys
import cv2
import numpy as np
from PIL import ImageGrab

import pyautogui


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
        threshold = 0.4
        loc = np.where(res >= threshold)

        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
            press = True
            print pt


        if press != True:
            directkeys.PressKey(directkeys.A)
            time.sleep(1 * random.random())
            directkeys.ReleaseKey(directkeys.A)
            directkeys.PressKey(directkeys.D)
            time.sleep(1 * random.random())
            directkeys.ReleaseKey(directkeys.D)
            directkeys.PressKey(directkeys.FOUR)
            time.sleep(1 * random.random())
            directkeys.ReleaseKey(directkeys.FOUR)

        else:
            '''
            directkeys.PressKey(directkeys.THREE)
            time.sleep(1 * random.random())
            directkeys.ReleaseKey(directkeys.THREE)
            directkeys.click()
         '''
            pyautogui.moveTo(pt[0]+16,pt[1]+40+16)

        cv2.imshow('window',cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB))

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


screen_record()
