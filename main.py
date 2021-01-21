import time
import random

from pip._vendor.distlib.compat import raw_input

import directkeys
import cv2
import numpy as np
from PIL import ImageGrab
import pyautogui
import keyboard
from playsound import playsound



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
    pyautogui.FAILSAFE = False

    timestamp = 0
    direction=""
    global hasFalseSwiped
    global hasShinyFound
    hasFalseSwiped = False
    hasShinyFound =False

    templ_pkm = cv2.imread('template.png', 0)
    templ_shiny = cv2.imread('shiny.png',0)
    templ_snivy = cv2.imread('snivy.png', 0)
    templ_mofo = cv2.imread('slowpoke.png', 0)
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
        printscreen = np.array(ImageGrab.grab(bbox=(0,0,2560,1440)))
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        # prepare compare
        img_rgb = printscreen
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)


        """
        in_pokecenter, img_rgb, pt_pc = template_match(templ_pokecenter, img_gray, img_rgb, 0.8)
        if not in_pokecenter:
            # search for in fight
            in_fight, img_rgb, pt_fight = template_match(templ_in_fight, img_gray, img_rgb, 0.6)
            if in_fight:
                if direction != "":
                    directkeys.ReleaseKey(direction)
                #time.sleep(6)
                # sarch for own pokemon
                own_pkm_fainted, img_rgb, pt_own = template_match(templ_fainted, img_gray, img_rgb,0.9)
                if not own_pkm_fainted:
                    # search for catch pokemon
                    shiny_found, img_rgb, pt_shiny = template_match(templ_shiny, img_gray, img_rgb, 0.9)
                    pkm_found, img_rgb, pt = template_match(templ_snivy, img_gray, img_rgb,0.5)
                    pkm2_found, img_rgb, pt = template_match(templ_mofo, img_gray, img_rgb,0.5)
                    if shiny_found :
                        hasShinyFound = True
                        time.sleep(3)
                        pyautogui.moveTo(pt_shiny[0],pt_shiny[1])
                        time.sleep(3)
                        pyautogui.moveRel(270,200)
                        time.sleep(3)
                        pyautogui.click()
                        time.sleep(3)

                    if  pkm_found or pkm2_found or shiny_found:
                        playsound('audio.mp3')

                        if not hasFalseSwiped:
                            hasFalseSwiped = True
                            time.sleep(5)
                            pyautogui.press('1')
                            time.sleep(5)
                            pyautogui.press('1')


                        time.sleep(7)

                        pyautogui.press('3')
                        pyautogui.moveTo(680, 165)  # pokeball
                        pyautogui.click()  # pokeball
                        '''
                        if (not timestamp):
                            timestamp = time.time() + random.random()
                            direction = directkeys.THREE
                            directkeys.PressKey(direction)
                        if (time.time() > timestamp):
                            timestamp = time.time() + random.random()
                            directkeys.ReleaseKey(direction)
                            pyautogui.moveTo(650, 90)  # pokeball
                            pyautogui.click()  # pokeball
                            #pyautogui.moveTo(pt[0] + 16, pt[1] + 40 + 16)
                            timestamp = 0
                        '''
                    else:
                        hasFalseSwiped = False
                        hasShinyFound = False
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
                hasFalseSwiped = False
                hasShinyFound = False

        else:
            keyboard.play(record, 1)
        """

        # search for catch pokemon
        shiny_found, img_rgb, pt_shiny = template_match(templ_shiny, img_gray, img_rgb, 0.9)
        pkm_found, img_rgb, pt = template_match(templ_snivy, img_gray, img_rgb, 0.5)
        pkm2_found, img_rgb, pt = template_match(templ_mofo, img_gray, img_rgb, 0.5)

        if pkm_found or pkm2_found or shiny_found:
            playsound('audio.mp3')
            time.sleep(15)

        # render
        cv2.imshow('window',cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB))

        # quit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
record= ""
print('should path be recorded?')
if raw_input() =='yes':
    record = record_path()
    print('\npath recorded. do you want to play it now?')
    if raw_input() =='yes':
        time.sleep(3)
        keyboard.play(record,1)

screen_record(record)

