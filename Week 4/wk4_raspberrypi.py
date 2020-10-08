import RPi.GPIO as GPIO
from time import sleep
from libdw import pyrebase


url = ''  # URL to Firebase database
apikey = ''  # unique token used for authentication

config = {
    "apiKey": apikey,
    "databaseURL": url,
}

# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto 
# the database and also retrieve data from the database.
firebase = pyrebase.initialize_app(config)
db = firebase.database()

# Use the BCM GPIO numbers as the numbering scheme.
GPIO.setmode(GPIO.BCM)

# Use GPIO12, 16, 20 and 21 for the buttons.

# Set GPIO numbers in the list: [12, 16, 20, 21] as input with pull-down resistor.

# Keep a list of the expected movements that the eBot should perform sequentially.
movement_list = []


done = False

while not done:

    # Write your code here

    '''
    We loop through the key (button name), value (gpio number) pair of the buttons
    dictionary and check whether the button at the corresponding GPIO is being
    pressed. When the OK button is pressed, we will exit the while loop and 
    write the list of movements (movement_list) to the database. Any other button
    press would be stored in the movement_list.

    Since there may be debouncing issue due to the mechanical nature of the buttons,
    we can address it by putting a short delay between each iteration after a key
    press has been detected.
    '''
    pass


# Write to database once the OK button is pressed

