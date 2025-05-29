from datetime import date, datetime, time
today = date.today()
now = datetime.now()
print("Today's date is", today)
print("\nCurrent Date and time is", now)
print("\nDate components:", today.year, today.month, today.day)
import random  
import time
def getRandomDate(startDate, endDate):  
    print("Printing random date between", startDate, "and", endDate)
    randomGenerator = random.random()
    dateFormat = "%m/%d/%Y"

    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate
print("Random Date = ", getRandomDate("1/1/2016", "12/12/2018"))

def hotel_cost(nights):
    return 140 * nights
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
def rental_car_cost(days):
    if days >= 7:
        return days * 40 - 50
    elif days >= 3:
        return days * 40 - 20
    else:
        return days * 40
def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
print("Cost of car rental:", rental_car_cost(2))
print("Cost of plane ride:", plane_ride_cost("Los Angeles")) 
print("Cost of hotel room: ", hotel_cost(7))
print("Total cost of the trip:", trip_cost("Los Angeles", 7, 500))
print(trip_cost("Tampa", 6, 900))
import calendar 
yy = 2020
mm = 4
print(calendar.month(yy,mm))
