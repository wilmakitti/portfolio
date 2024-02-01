# Program to calculate the contestants time in thriathlon race

# Ask the users input for each time

swim_time = int(input("Time spent for swimming in minutes: "))
cycling_time = int(input("Time spent for cycling in minutes: "))
running_time = int(input("Time spent for running in minutes: "))

# Calculate the total of each part of thriathlon

sum_of_all = swim_time + cycling_time + running_time
print(f"The total time is {sum_of_all} minutes.")

# Print out the results and the according award for the contestant

if sum_of_all <= 100:
    print("The award: provincial colours")
elif sum_of_all <= 105:
    print("The award: provincial half colours")
elif sum_of_all <= 110:
    print("The award: provincial scroll")
else:
    print("No award")


