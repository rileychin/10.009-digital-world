def fahrenheit_to_celsius(temp): #hwQ1
    C = (temp-32)/(9/5)
    return C

print(fahrenheit_to_celsius(32))
print(fahrenheit_to_celsius(-40))
print(fahrenheit_to_celsius(212))

def celsius_to_fahrenheit(temp): #hwQ2
    F = temp*9/5 + 32
    return F

print ( celsius_to_fahrenheit (0))
print ( celsius_to_fahrenheit (-40))
print ( celsius_to_fahrenheit (100))

import math
def area_vol_cylinder(r,l): #hwQ3
    area = r**2*(math.pi)
    vol = area * l
    return round(area,2), round(vol,2)

print(area_vol_cylinder(1.0,2.0))
print(area_vol_cylinder (2.0 ,2.3))
print(area_vol_cylinder (1.5 ,4))
print(area_vol_cylinder (2.2 ,5.0))

def wind_chill_temp(tempF,windV): #hwQ4
    windChill = 35.74+0.6215*tempF-35.75*(windV**0.16)+0.4275*tempF*(windV**0.16)
    return round(windChill,11)

print(wind_chill_temp(5.3,6))
print(wind_chill_temp(2.2,4))

tempF=float(input("input temperature in fahrenheit"))
windV=float(input("input wind speed"))
print("Outside temperature in Fahrenheit: ",tempF)
print("Wind speed in miles per hour", windV)
print("wind chill index " , wind_chill_temp(tempF,windV))

print(minutes_to_years_days(527040))

def minutes_to_years_days(m): #hwQ5
    year = m//525600
    day = m %525600
    remainingDays = day // 1440
    return year, remainingDays
print(minutes_to_years_days(527040))
print(minutes_to_years_days(1000000000))


def investment_val(invest,interest,year): #hwQ6
    futureInvest= invest*(1+interest/(1200))**(year*12)
    return round(futureInvest,2)

print(investment_val(1000,4.25,1))
print(investment_val(1500,3.25,2))
print(investment_val(1000,2.25,0.5))
print(investment_val(2000,4.25,3))

invest = float(input("Enter investment amount:"))
interest = float(input("Enter annual interest rate (%):"))
year = float(input("Enter number of years:"))
print("Accumulated value is,", investment_val(invest,interest,year))


def is_larger(n1,n2): #hwQ7
    if n1>n2:
        return True
    else:
        return False

print(is_larger(2,-1))
print(is_larger(-1,2))
print(is_larger(2,2))


def check_value(n1,n2,n3,x): #hwQ8
    if x>n1 and x>n2 and x<n3:
        return True
    else:
        return False

print (" Test case 1: check_value (1 ,4 ,8 ,7)")
print ("ans = True ")
ans= check_value (1 ,4 ,8 ,7)
print (ans)

print (" Test case 2: check_value (10 ,4 ,8 ,7)")
print ("ans = False ")
ans= check_value (10 ,4 ,8 ,7)
print (ans)

print (" Test case 3: check_value (1 ,10 ,8 ,7)")
print ("ans = False ")
ans= check_value (1 ,10 ,8 ,7)
print (ans)

print (" Test case 4: check_value (1 ,4 ,5 ,7)")
print ("ans = False ")
ans= check_value (1 ,4 ,5 ,7)
print (ans)
