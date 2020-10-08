# from pynput.keyboard import Key, Listener

# def on_press(key):
#     space = Key.space
#     if key == space:
#         print(key,'pressed')     
#         return True

# def on_release(key):
#     print('{} release'.format(
#         key))            
#     if key == Key.esc:
#         # Stop listene
#         return False

# # Collect events until release    
# with Listener(on_press=on_press) as listener:
#     listener.join()
#     if on_press == True:
#         print('loop')




import keyboard  # using module keyboard   
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('You Pressed A Key!')
            break  # finishing the loop
    except:
        break  # if user pressed a key other than the given key the loop will break
        
import keyboard
while True:
    if keyboard.is_pressed('q'):
        print('hello')
        break
    print('orange')