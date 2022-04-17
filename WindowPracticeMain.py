from tkinter import *
from tkinter.ttk import *
import requests
import time
import apiRequest as api
import ScreenShot
import urllib
import cv2
import numpy as np
from PIL import Image
import keyboard

# Looks to see if the given seachable tag is in the json file lookup


def create_image_dir():
    obj1 = api.apiRequest()
    urls = []
    for items in obj1:
        all_info = []
        all_info.append(list(items.values()))

        together = [all_info[0][15], all_info[0][1]]
        urls.append(together)
    for url in urls:
        print(f'Starting Image for {url[1]} @ {url[0]}')
        try:
            urllib.request.urlretrieve(url[0], f'{url[1]}.png')
            img = Image.open(f'{url[1]}.png')
            img.save(
                f'C:/Users/camer/PycharmProjects/WindowPractice/Tarkov Images/{url[1]}.png')
        except:
            print(
                f'--------ITEM FAILURE ON IMAGE LOAD--------{url[1]} @ {url[0]}')


class Tarkov_Item():
    def __init__(self, name, price, category, image=None,):
        self.name = name
        self.price = price
        self.category = category
        try:
            self.image = cv2.cvtColor(
                np.array(Image.open(f'{self.name}.png')), cv2.COLOR_RGB2BGR)
        except:
            self.image = cv2.cvtColor(
                np.array(Image.open('zzzzErrorImage.png')), cv2.COLOR_RGB2BGR)

    def __str__(self):
        return self.name + ' is worth \u20bd' + str(self.price)

    def show_item(self):
        self.image.show()

    def get_image(self):
        return self.image


def image_lookup_in_image(tarkovAllItems):
    screen = ScreenShot.take_screenshot()
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
    # cv2.imshow('img',screen)
    item_count = 0
    itemFound = []
    for item in tarkovAllItems:
        item_count = item_count + 1
        item_img = item.image
        try:
            result = cv2.matchTemplate(screen, item_img, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            if max_val > 0.78:
                itemFound.append(item)
        except:
            print(str(item) + 'ERROR')
    clear_Window()
    item_lookup(itemFound)


def object_creation(json_file):
    tarkovAllItems = []
    for items in json_file:
        all_info = []
        all_info.append(list(items.values()))
        print(all_info[0][2][0])
        if all_info[0][2][0] == 'Barter':
            tarkov_item = Tarkov_Item(
                all_info[0][1], all_info[0][4], all_info[0][2][0])

            tarkovAllItems.append(tarkov_item)
    return tarkovAllItems


def item_lookup(tarkovAllItems):
    rowNum = 0
    for item in tarkovAllItems:
        rowNum = rowNum + 1
        # creates the labels for titles and prices if they are found in the json lookup
        name_label = Label(frame, text=item.name)
        name_label.grid(row=rowNum, column=0, sticky='w')
        name_spacer = Label(frame, text='\t\t')
        name_spacer.grid(row=rowNum, column=1)
        price_label = Label(frame, text='\u20bd' + str(item.price))
        price_label.grid(row=rowNum, column=1, sticky='e')

        # makes sure the look up value for cost is above zero because some values are zero and are duplicates
        if item.price <= 0:
            print(type(item.price))
            price_label.destroy()
            name_label.destroy()


def key_press(event):
    print('User Input Detected')
    global tarkovAllItems
    if event.char == 'm':
        image_lookup_in_image(tarkovAllItems)


def clear_Window():
    # clears the frame window
    for widget in frame.winfo_children():
        widget.destroy()
    field.delete(0, END)


# creates the parsed jason into the obj object
tarkovAllItems = object_creation(api.apiRequest())
# UI works
root = Tk()
root.title('Tarkov Price Lookup')
root.geometry('800x200')
frame = LabelFrame(root)
utility_frame = LabelFrame(root)
label = Label(utility_frame, text='Enter name of object here:')
field = Entry(utility_frame)
#button = Button(utility_frame,text = 'Submit',command = lambda: item_lookup(tarkovAllItems))
root.bind('<Key>', key_press)
lookup_button = Button(utility_frame, text='Start',
                       command=lambda: image_lookup_in_image(tarkovAllItems))
lookup_button.grid(row=5, column=0)
clear_button = Button(utility_frame, text='clear', command=clear_Window)
update_button = Button(
    utility_frame, text='Update images', command=create_image_dir)
update_button.grid(row=4, column=0)
label.grid(row=0, column=0, sticky='nw')
utility_frame.grid(row=0, column=0, sticky='nw')
field.grid(row=1, column=0, sticky='nw')
#button.grid(row = 2, column = 0,sticky = 'nw')
clear_button.grid(row=3, column=0, sticky='nw')
frame.grid(row=0, column=1, sticky='e')


root.mainloop()
