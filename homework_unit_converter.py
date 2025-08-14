# Homework: Unit Converter

# TODO: Create a main program loop that continues until the user chooses to quit.
# Inside the loop, present the user with a menu of options:
# 1. Kilometers to Miles
# 2. Celsius to Fahrenheit
# 3. Quit
#
# Based on their choice, prompt for the required input and print the converted value.
# If they choose to quit, print "Goodbye!" and break the loop.
# Handle invalid menu choices gracefully.

while True:
    print("\nUnit Converter Menu:")
    print("1. Kilometers to Miles")
    print("2. Celsius to Fahrenheit")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        # TODO: Get kilometers from user, convert to miles, and print the result.
        # Formula: miles = km * 0.621371
        print("Feature not implemented yet.")
    elif choice == '2':
        # TODO: Get Celsius from user, convert to Fahrenheit, and print the result.
        # Formula: fahrenheit = (celsius * 9/5) + 32
        print("Feature not implemented yet.")
    elif choice == '3':
        # TODO: Print a goodbye message and exit the loop.
        print("Feature not implemented yet.")
        break # Placeholder
    else:
        # TODO: Handle invalid input.
        print("Feature not implemented yet.")

