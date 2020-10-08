def position_velocity(v,t): #csQ1
    g=9.81
    position = v*t - 0.5*g*t**2
    velocity = v - g*t
    return round(position,2), round(velocity,2)

print(position_velocity(5.0,10.0))
print(position_velocity(5.0,0.0))
print(position_velocity(0.0,5.0))

def bmi(w,h): #csQ2
    h=h/100
    bmi=w/(h**2)
    return round(bmi,1)

weight=float(input("Weight in kilograms"))
height=float(input("Height in cm"))
print(bmi(60,120))
print(bmi(50,150))
print(bmi(43.5,142.3))
print(bmi(weight,height))


######################
#import test2 as t 
from test2 import asd #csQ3

asd(3)

print(c.x)

def area_of_triangle(p1,p2,p3):
    side1=distance(p1,p2)
    side2=distance(p2,p3)
    side3=distance(p3,p1)
    s=calculate_s(side1,side2,side3)
    area = (s*(s-side1)*(s-side2)*(s-side3))**0.5
    return round(area,2)
    
def calculate_s(side1,side2,side3):
    s = (side1+side2+side3)/2
    return s

def distance(p1,p2):
    d=((p1.x-p2.x)**2 + (p1.y-p2.y)**2)**0.5
    return d

print (" Test Case 1")
p1= Coordinate()  ##p1 accessing Coordinate class
p1.x =1.5
p1.y= -3.4
p2= Coordinate()  ##p2 accessing Coordinate class
p2.x =4.6
p2.y=5
p3= Coordinate()  ##p3 accessing Coordinate class
p3.x =9.5
p3.y= -3.4

print(distance(p1,p2))


ans= area_of_triangle (p1 ,p2 ,p3)
print (ans)


def describe_bmi(bmi): #csQ5
    if(bmi<18.5):
        return "nutritional deficiency"
    elif(bmi<23 and bmi>=18.5):
        return "low risk"
    elif(bmi<27.5 and bmi>=23):
        return "moderate risk"
    elif(bmi>=27.5):
        return "high risk"
    else:
        print("please enter an appropriate value")

describe_bmi(float(input("enter bmi")))


def letter_grade(mark): #csQ6
    if(mark>=90 and mark<=100):
        return "A"
    elif(mark<90 and mark>=80):
        return "B"
    elif(mark<80 and mark>=70):
        return "C"
    elif(mark<70 and mark>=60):
        return "D"
    elif(mark<60 and mark>=0):
        return "E"
    else:
        return None


x=letter_grade(int(input("grade")))
print(x)


class Coordinate(): #csQ7
    x=0.0
    y=0.0

def is_in_square(center1,side1,center2,side2): 
    boundary1Left=center1.x-(side1)/2 #setting square1 boundaries 
    boundary1Right=center1.x+(side1)/2
    boundary1Top=center1.y+(side1)/2
    boundary1Bottom=center1.y-(side1)/2
    
    boundary2Left=center2.x-(side2)/2 #setting square2 boundaries
    boundary2Right=center2.x+(side2)/2
    boundary2Top=center2.y+(side2)/2
    boundary2Bottom=center2.y-(side2)/2
    
    
    if(((boundary2Right<=boundary1Right and boundary2Right>=boundary1Left) or (boundary2Left<=boundary1Right and boundary2Left>=boundary1Left)) and((boundary2Top<=boundary1Top and boundary2Top>=boundary1Bottom) or (boundary2Bottom<=boundary1Top and boundary2Bottom>=boundary1Top))): #SQ2 left or right boundary in place and top and bottom boundary in place
        print("1")
        return True
    elif(((boundary2Top<=boundary1Top and boundary2Top>=boundary1Bottom) or (boundary2Bottom<=boundary1Top and boundary2Bottom>=boundary1Bottom) )and ((boundary2Right<=boundary1Right and boundary2Right>=boundary1Left) or (boundary2Left<=boundary1Right and boundary2Left>=boundary1Left) )): #SQ2 top and bottom boundary in place and left and right boundary in place
        print("2")
        return True
    elif(((boundary1Right<=boundary2Right and boundary1Right>=boundary2Left) or (boundary1Left<=boundary2Right and boundary1Left>=boundary2Left)) and((boundary1Top<=boundary2Top and boundary1Top>=boundary2Bottom) or (boundary1Bottom<=boundary2Top and boundary1Bottom>=boundary2Top))): #SQ1 left or right boundary in place and top and bottom boundary in placeabs
        print("3")
        return True
    elif(((boundary1Top<=boundary2Top and boundary1Top>=boundary2Bottom) or (boundary1Bottom<=boundary2Top and boundary1Bottom>=boundary2Bottom) )and ((boundary1Right<=boundary2Right and boundary1Right>=boundary2Left) or (boundary1Left<=boundary2Right and boundary1Left>=boundary2Left) )): #SQ1 top and bottom boundary in place and left and right boundary in place
        print("4")
        return True
    else:
        return False

s1 = Coordinate() 
s1.x,s1.y = 10,10 #square1 center coordinate
s2 = Coordinate()
s2.x,s2.y = 20,10 #square2 center coordinate
is_in_square(s1,5,s2,4)

