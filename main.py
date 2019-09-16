import time
import random
import directkeys
import cv2
import numpy as np
from PIL import ImageGrab
import pyautogui
import keyboard


def record_path():
    recorded = keyboard.record(until='esc')
    return recorded




def template_match(template, img_gray, img_rgb,threshold):
    found= False
    pt = ""
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = threshold
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
        found = True
        print(pt)
    return found, img_rgb, pt



def screen_record(record):
    timestamp = 0

    templ_pkm = cv2.imread('template.png', 0)
    templ_in_fight = cv2.imread('templ_in_fight.png', 0)
    templ_own_pkm = cv2.imread('templ_own_pkm.png', 0)
    templ_fainted = cv2.imread('templ_fainted.png', 0)
    templ_pokecenter = cv2.imread('templ_pokecenter.png', 0)
    last_time = time.time()

    # bot loop
    while(True):
        # 800x600 windowed mode
        found=False
        # get image
        printscreen = np.array(ImageGrab.grab(bbox=(0,40,800,640)))
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        # prepare compare
        img_rgb = printscreen
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

        in_pokecenter, img_rgb, pt_pc = template_match(templ_pokecenter, img_gray, img_rgb, 0.8)
        if not in_pokecenter:
            # search for in fight
            in_fight, img_rgb, pt_fight = template_match(templ_in_fight, img_gray, img_rgb, 0.6)
            if in_fight:
                directkeys.ReleaseKey(direction)
                #time.sleep(6)
                # sarch for own pokemon
                own_pkm_fainted, img_rgb, pt_own = template_match(templ_fainted, img_gray, img_rgb,0.9)
                if not own_pkm_fainted:
                    # search for catch pokemon
                    pkm_found, img_rgb, pt = template_match(templ_pkm, img_gray, img_rgb,0.4)
                    if pkm_found:
                        if (not timestamp):
                            timestamp = time.time() + random.random()
                            direction = directkeys.THREE
                            directkeys.PressKey(direction)
                        if (time.time() > timestamp):
                            timestamp = time.time() + random.random()
                            directkeys.ReleaseKey(direction)
                            pyautogui.moveTo(670, 180)  # pokeball
                            pyautogui.click()  # pokeball
                            pyautogui.moveTo(pt[0] + 16, pt[1] + 40 + 16)
                            timestamp = 0

                    else:

                        if (not timestamp):
                            timestamp = time.time() + random.random()
                            direction = directkeys.FOUR
                            directkeys.PressKey(direction)
                        if (time.time() > timestamp):
                            timestamp = time.time() + random.random()
                            directkeys.ReleaseKey(direction)
                            timestamp = 0
                else:
                    pyautogui.press("esc")
                    pyautogui.moveTo(400,385)
                    pyautogui.click() # logout
                    pyautogui.moveTo(320, 540)
                    pyautogui.click()  # login

            else:

                if(not timestamp):
                    timestamp = time.time() + random.random()
                    direction = directkeys.A
                    directkeys.PressKey(direction)

                if(time.time() > timestamp):
                    timestamp = time.time() + random.random()
                    directkeys.ReleaseKey(direction)
                    if(direction == directkeys.A):
                        direction = directkeys.D
                    else:
                        direction = directkeys.A
                    directkeys.PressKey(direction)
                    timestamp = 0

        else:
            keyboard.play(record, 1)


        # render
        cv2.imshow('window',cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB))

        # quit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
record= ""
print('should path be recorded?')
if input() =='yes':
    record = record_path()
    print('\npath recorded. do you want to play it now?')
    if input() =='yes':
        time.sleep(3)
        keyboard.play(record,1)

screen_record(record)

