import time
import pyautogui
import keyboard
import random
import decimal
from plyer import notification

funcShouldStop = False
humanVerification = False
humanVerificationTime = None
verificationCompleteTime = None
cooldown=3

def checkHumanVerification():
    global humanVerification

    # Get current time
    current_time = time.time()

    # Check if verificationCompleteTime is within the last (cooldown * 20) seconds
    if verificationCompleteTime is not None and (current_time - verificationCompleteTime) <= (cooldown * 20):
        return  # Exit function early
    
    # Check if there is a verify captcha is visible
    captchaEmbed = pyautogui.locateOnScreen("captcha_embed.png", grayscale=True, confidence=0.5)

    if captchaEmbed is not None:
        print("humanVerify")
        humanVerification = True
        return toggleStop()
    
    # Find an embed explaining that a captcha is present
    verifyEmbed = pyautogui.locateOnScreen("verify_embed.png", grayscale=False, confidence=0.5)

    if verifyEmbed is not None:
        print("humanVerify")
        humanVerification = True
        return toggleStop()

def checkIfVerified():
    global verificationCompleteTime

    print("Checking if verification is complete")
    verifyCompleteMsg = pyautogui.locateOnScreen("verify_complete.png", grayscale=False, confidence=0.7)

    if verifyCompleteMsg is not None:
        # Save current time
        verificationCompleteTime = time.time()
        print("verificationComplete")
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
        notification.notify(
            title = "Stopping Automation",
            message = "The automation has been stopped",
            app_icon = None,
            timeout = 10
        )
    else:
        print("Resuming automation")
        funcShouldStop = False
        notification.notify(
            title = "Resuming Automation",
            message = "The automation has been resumed",
            app_icon = None,
            timeout = 10
        )

# Bind the 'esc' key to the stop function
keyboard.add_hotkey('esc', toggleStop)

while True:
    # If the function is set to stop
    if funcShouldStop == False:
        # Run the button-clicking function
        clickButton()
        # Check if the human verification prompt has appeared
        checkHumanVerification()

        # Pause for a random amount of seconds between cooldown and cooldown + 1
        time.sleep(float(decimal.Decimal(random.randrange(cooldown, cooldown + 1))))
    elif humanVerification == True:
        # Pause for a 5 minutes
        time.sleep(300)
        checkIfVerified()