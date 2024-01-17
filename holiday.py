# a program to calculate a user's total cost inlcuding plane, hotel and car-rental cost


def hotel_cost(num_nights): # if statement for choosing the location
    while True:
            if city_flight == "Rome":
                hotel_cost = 290 * hotel_nights
            elif city_flight == "Paris":
                hotel_cost = 300 * hotel_nights
            elif city_flight == "Berlin":
                hotel_cost = 214 * hotel_nights
            elif city_flight == "Praque":
                hotel_cost = 180 * hotel_nights
            elif city_flight == "Madrid":
                hotel_cost = 129 * hotel_nights
            break
    return hotel_cost

def plane_cost(city_flight): # if statement for choosing the location
    while True:
        try:
            if city_flight == "Rome":
                plane_cost = 135
            elif city_flight == "Paris":
                plane_cost = 210
            elif city_flight == "Berlin":
                plane_cost = 85
            elif city_flight == "Praque":
                plane_cost = 109
            elif city_flight == "Madrid":
                plane_cost = 73
            else:
                print("Unfortunately there was an error.")
                continue
            break
        except ValueError:
            print("Please enter a valid input (Rome/Paris/Berlin/Praque/Madrid): ").capitalize().strip()
    return plane_cost

def car_rental(car_rental_days):
    total = car_rental_days * 60
    return total

def people_count(x):
    while True:
        try:
            if x > 0:
                break
            else:
                print("The number must be positive")
        except ValueError as e:
            print("Please enter number bigger than 0: ")
    return x


def holiday_cost(hotel_cost, plane_cost):
    total = (hotel_cost + plane_cost)
    return total

city_flight = input("Please enter the city you would like to fly to (Rome/Paris/Berlin/Praque/Madrid): ").capitalize().strip()
hotel_nights = int(input("How many nights would you like to stay over? "))
car_rental_days = int(input("How many days will you need to rent a car for? "))
how_many_people = int(input("How many people are you booking for? "))

hotel_cost = hotel_cost(hotel_nights)
plane_cost = plane_cost(city_flight)
car_rental = car_rental(car_rental_days)
total_cost = holiday_cost(hotel_cost, plane_cost)
people_count = people_count(how_many_people)

total_cost = total_cost * people_count + car_rental

print(f"The total of {hotel_nights} nights in {city_flight}, and {car_rental_days} days of renting a car for {people_count} people is: £{total_cost}")