import time
import pyautogui
import keyboard
import random
import decimal

funcShouldStop = False
humanVerification = False

def checkHumanVerification():
    global humanVerification
    
    # Check if there is a verify captcha is visible
    captchaEmbed = pyautogui.locateOnScreen("captcha_embed.png", grayscale=True, confidence=0.5)

    if captchaEmbed is not None:
        print("humanVerify")
        return toggleStop()
    
    # Find an embed explaining that a captcha is present
    verifyEmbed = pyautogui.locateOnScreen("verify_embed.png", grayscale=False, confidence=0.5)

    if verifyEmbed is not None:
        print("humanVerify")
        return toggleStop()

def clickButton():
    # Find the button on the screen
    button = pyautogui.locateOnScreen("fish_again_button.png", grayscale=True, confidence=0.9)

    # Ensure button exists
    if button is not None:
        # Get the coordinates of the button
        buttonX, buttonY = pyautogui.center(button)

        # Click the button
        pyautogui.click(buttonX, buttonY)

def toggleStop():
    global funcShouldStop
    # Toggle stop
    if funcShouldStop == False:
        print("Stopping automation")
        funcShouldStop = True
    else:
        print("Resuming automation")
        funcShouldStop = False

# Bind the 'esc' key to the stop function
keyboard.add_hotkey('esc', toggleStop)

while True:
    # If the function is set to stop
    if funcShouldStop == False:
        # Run the button-clicking function
        clickButton()
        # Check if the human verification prompt has appeard
        checkHumanVerification()

        # Pause for a random amount of seconds between 3 and 4
        time.sleep(float(decimal.Decimal(random.randrange(3, 4))))
