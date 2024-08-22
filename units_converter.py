def unit_conversion():
    print("Choose the unit you want to convert:")
    print("1. Centimeters (cm)")
    print("2. Meters (m)")
    print("3. Kilometers (km)")
    print("4. Miles (mi)")
    
    choice = int(input("Choose an option (1/2/3/4): "))
    
    # Get the value from the user
    value = float(input("Enter the value to convert: "))
    
    # Unit conversion
    if choice == 1:
        # Centimeters to meters, kilometers, miles
        meters = value / 100
        kilometers = value / 100000
        miles = value / 160934.4
        print(f"{value} cm is {meters} m, {kilometers} km, {miles} mi")
        
    elif choice == 2:
        # Meters to centimeters, kilometers, miles
        centimeters = value * 100
        kilometers = value / 1000
        miles = value / 1609.344
        print(f"{value} m is {centimeters} cm, {kilometers} km, {miles} mi")
        
    elif choice == 3:
        # Kilometers to centimeters, meters, miles
        centimeters = value * 100000
        meters = value * 1000
        miles = value / 1.609344
        print(f"{value} km is {centimeters} cm, {meters} m, {miles} mi")
        
    elif choice == 4:
        # Miles to centimeters, meters, kilometers
        centimeters = value * 160934.4
        meters = value * 1609.344
        kilometers = value * 1.609344
        print(f"{value} mi is {centimeters} cm, {meters} m, {kilometers} km")
        
    else:
        print("Invalid choice.")

# Run the program
unit_conversion()