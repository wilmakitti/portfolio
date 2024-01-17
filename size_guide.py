print("Size guide")

user_choice = input("Please choose a garment for which you would like to check the correct size (top/bottom/dress): ").lower().strip()

bust_measurement = 0
waist_measurement = 0
hip_measurement = 0

if user_choice == "top":
    print("Please enter your measurements to find the right size for your top.")
    bust_measurement = float(input("Bust (in cm): "))
    waist_measurement = float(input("Waist (in cm): "))
elif user_choice == "bottom":
    print("Please enter your measurements to find the right size for your bottom.")
    waist_measurement = float(input("Waist (in cm): "))
    hip_measurement = float(input("Hips (in cm): "))
elif user_choice == "dress":
    print("Please enter your measurements to find the right size for your dress.")
    bust_measurement = float(input("Bust (in cm): ")) 
    waist_measurement = float(input("Waist (in cm): "))
    hip_measurement = float(input("Hips (in cm): "))
else:
    print(input("Unfortunately an error occured. Please enter a valid input (bra/bottom/dress): "))

# the application calculates the average of two different values and the recommendation is given according to it.

top_average = (bust_measurement + waist_measurement) / 2

bottom_average = (waist_measurement + hip_measurement) / 2

dress_average = (waist_measurement + hip_measurement + bust_measurement) / 3

if user_choice == "top":
    if bust_measurement <= 86:
        print("The recommended size for top is XS")
    elif bust_measurement <= 92:
        print("The recommended size for top is S")
    elif bust_measurement <= 98:
        print("The recommended size for top is M")
    elif bust_measurement <= 104:
        print("The recommended size for top is L")
    elif bust_measurement > 105:
        print("The recommended size for top is XL") 

if user_choice == "bottom":
    if bottom_average <= 78:
        print("The recommended size for bottom is XS")
    elif bottom_average <= 84:
        print("The recommended size for bottom is S")
    elif bottom_average <= 90:
        print("The recommended size for bottom is M")
    elif bottom_average <= 96:
        print("The recommended size for bottom is L")
    elif bottom_average >= 97:
        print("The recommended size for bottom is XL") 

if user_choice == "dress":
    if dress_average <= 80.66:
        print("The recommended size for the dress is XS")
    elif dress_average <= 86.66:
        print("The recommended size for the dress is S")
    elif dress_average <= 92.66:
        print("The recommended size for the dress is M")
    elif dress_average <= 98.66:
        print("The recommended size for the dress is L")
    elif dress_average > 98.66:
        print("The recommended size for the dress is XL")

