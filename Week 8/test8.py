from pynput.keyboard import Key, Listener

def on_press(key):
    print(key)
    print('{0} pressed'.format(
        key))
    

def on_release(key):
    
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False
    

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
    
    
class Line(object):
    
    def __init__(self,c0=0,c1=0):
        self.c0 = c0
        self.c1 = c1
        
    def __call__(self,x):
        y = self.c0 + self.c1 * x
        return y
        
        
line=Line(1,2)
line(2)



class Property:
    def __init__(self,value):
        self._value = value
        
    def get_x(self):
        return self._value
    def set_x(self,value):
        self._value=value
        
    value = property(get_x,set_x)

p = Property(7)
print(p.value)
p.value = 9
p.value
