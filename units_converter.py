def unit_conversion():
    print("Choose the type of unit you want to convert:")
    print("1. Length")
    print("2. Area")
    
    conversion_type = int(input("Choose an option (1/2): "))
    
    if conversion_type == 1:
        print("Choose the unit of length you want to convert:")
        print("1. Centimeters (cm)")
        print("2. Meters (m)")
        print("3. Kilometers (km)")
        print("4. Miles (mi)")
        
        choice = int(input("Choose an option (1/2/3/4): "))
        value = float(input("Enter the value to convert: "))
        
        if choice == 1:
            meters = value / 100
            kilometers = value / 100000
            miles = value / 160934.4
            print(f"{value} cm is {meters} m, {kilometers} km, {miles} mi")
            
        elif choice == 2:
            centimeters = value * 100
            kilometers = value / 1000
            miles = value / 1609.344
            print(f"{value} m is {centimeters} cm, {kilometers} km, {miles} mi")
            
        elif choice == 3:
            centimeters = value * 100000
            meters = value * 1000
            miles = value / 1.609344
            print(f"{value} km is {centimeters} cm, {meters} m, {miles} mi")
            
        elif choice == 4:
            centimeters = value * 160934.4
            meters = value * 1609.344
            kilometers = value * 1.609344
            print(f"{value} mi is {centimeters} cm, {meters} m, {kilometers} km")
            
        else:
            print("Invalid choice.")
    
    elif conversion_type == 2:
        print("Choose the unit of area you want to convert:")
        print("1. Square Centimeters (cm²)")
        print("2. Square Meters (m²)")
        print("3. Square Kilometers (km²)")
        print("4. Acres")
        print("5. Square Miles (mi²)")
        
        choice = int(input("Choose an option (1/2/3/4/5): "))
        value = float(input("Enter the value to convert: "))
        
        if choice == 1:
            square_meters = value / 10000
            square_kilometers = value / 1e+10
            acres = value / 40468564.224
            square_miles = value / 2.59e+10
            print(f"{value} cm² is {square_meters} m², {square_kilometers} km², {acres} acres, {square_miles} mi²")
            
        elif choice == 2:
            square_centimeters = value * 10000
            square_kilometers = value / 1e+6
            acres = value / 4046.8564224
            square_miles = value / 2.59e+6
            print(f"{value} m² is {square_centimeters} cm², {square_kilometers} km², {acres} acres, {square_miles} mi²")
            
        elif choice == 3:
            square_centimeters = value * 1e+10
            square_meters = value * 1e+6
            acres = value * 247.10538146717
            square_miles = value / 2.59
            print(f"{value} km² is {square_centimeters} cm², {square_meters} m², {acres} acres, {square_miles} mi²")
            
        elif choice == 4:
            square_centimeters = value * 40468564.224
            square_meters = value * 4046.8564224
            square_kilometers = value / 247.10538146717
            square_miles = value / 640
            print(f"{value} acres is {square_centimeters} cm², {square_meters} m², {square_kilometers} km², {square_miles} mi²")
            
        elif choice == 5:
            square_centimeters = value * 2.59e+10
            square_meters = value * 2.59e+6
            square_kilometers = value * 2.59
            acres = value * 640
            print(f"{value} mi² is {square_centimeters} cm², {square_meters} m², {square_kilometers} km², {acres} acres")
            
        else:
            print("Invalid choice.")
    
    else:
        print("Invalid conversion type.")

# Run the program
unit_conversion()