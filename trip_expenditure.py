def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if "Charlotte" == city:
        return 183
    elif "Tampa" == city:
        return 220
    elif "Pittsburgh" == city:
        return 222
    elif "Los Angeles" == city:
        return 475

def rental_car_cost(days):
    if days >= 7:
        return 40 * days - 50
    elif days >= 3:
        return 40 * days - 20
    else:
        return 40 * days

def trip_cost(city, days, spending_money):
    return plane_ride_cost(city) + hotel_cost(days) + rental_car_cost(days) + spending_money
print("cost of car rental:", rental_car_cost(5))
print("cost of hotel room:", hotel_cost(7))
print("cost of plane ride:", plane_ride_cost("Los Angeles"))
print("total cost of trip:", trip_cost("Los Angeles", 7, 500))
print(trip_cost("Tampa", 6, 500))