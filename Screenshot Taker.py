import pyautogui as pg
import easygui as eg
import time
import os


def create_image():
    save_path = r"C:\Users\user\Pictures\M-J ScreenShots"
    image_code = '\mj_ss-'
    image_num = 900000000001
    image_path = save_path + image_code + str(image_num) + '.png'
    while os.path.exists(image_path):
        image_num += 1
        image_path = save_path + image_code + str(image_num) + '.png'
    print('Done')
    return image_path


def takess():
    pg.screenshot().save(create_image())


def showD():
    x = (eg.buttonbox(
        msg='Take a screenshot',
        title='Mj ss',
        choices=['Take'
        ]
    ))
    if x == 'Take':
        time.sleep(0.1)
        takess()

if __name__ == '__main__':
    showD()
