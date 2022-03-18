import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(2)
position1 = pt.locateOnScreen("smiley.png", confidence=.6)
x = position1[0]
y = position1[1]


# gets message
def get_message():
    global x, y

    position = pt.locateOnScreen("smiley.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration=.5)
    pt.moveTo(x + 110, y - 70, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12, 15)
    pt.click()
    whatsapp_message = pyperclip.paste()
    print("message received:" + whatsapp_message)
    return whatsapp_message


# posts msgs
def post_response(message):
    global x, y
    position = pt.locateOnScreen("smiley.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x + 200, y + 20, duration=.5)
    pt.click()
    pt.typewrite(message, interval=.01)

    # pt.typewrite("\n", interval=.01)  # enter key


# processing response
def process_response(message):
    random_no = random.randrange(3)
    if "?" in str(message).lower():
        return "don't ask me any question!"

    if random_no == 0:
        return "that's cool"
    elif random_no == 1:
        return "hey this is  bot"
    else:
        return "but why !!!"


# check for new msgs
def check_for_new_messages():
    pt.moveTo(x + 110, y - 70, duration=.05)

    while True:
        # continues check on new msgs (checks for green dot )
        try:
            position = pt.locateOnScreen("green_circle.png", confidence=.7)
            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100, 0)
                pt.click()
            sleep(.5)  # check for new msgs every .5 seconds

        except(Exception):
            print("no new msgs on the user")

        if pt.pixelMatchesColor(int(x + 110), int(y - 55), (35, 45, 54), tolerance=10):
            print("it is white")
            processed_message = process_response(get_message())
            post_response(processed_message)
        else:
            print("no new msgs yet ... ")
        sleep(5)  # check for every 5s inside every chat


check_for_new_messages()    # checks for the green dot and also inside chat new msg
# post_response(get_message())
# processed_message = process_response(get_message())
# post_response(processed_message)
