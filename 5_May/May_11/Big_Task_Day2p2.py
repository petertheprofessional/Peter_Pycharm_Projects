from small import cars

key_lists = ['Dimensions', 'Engine Information', 'Fuel Information', 'Identification', 'Height', 'Length', 'Width',
             'Driveline', 'Engine Type', 'Hybrid', 'Number of Forward Gears', 'Transmission', 'Engine Statistics',
             'Horsepower', 'Torque', 'City mpg', 'Fuel Type', 'Highway mpg', 'Classification', 'ID', 'Make',
             'Model Year', 'Year']

def show_options():
    entries = []
    for list in key_lists[0:4]:
        print(f"{list}")
    print("What category would you like to adjust >>> ", end='')
    choice = input()
    if choice == 'Dimensions':
        for list in key_lists[4:7]:
            print(f"{list}")
        print("What would you like to adjust >>> ", end='')
        choice1 = input()
        entries.append(choice1)
    elif choice == 'Fuel Information':
        for list in key_lists[15:18]:
            print(f"{list}")
        print("What would you like to adjust >>> ", end='')
        choice1 = input()
        entries.append(choice1)
    elif choice == 'Identification':
        for list in key_lists[18:23]:
            print(f"{list}")
        print("What would you like to adjust >>> ", end='')
        choice1 = input()
        entries.append(choice1)
    elif choice == 'Engine Information':
        for list in key_lists[7:13]:
            print(f"{list}")
        print("What would you like to adjust >>> ", end='')
        choice1 = input()
        entries.append(choice1)
    entries.append(choice)
    return entries





def updating_a_car(name, change1, change2, value):
    for car in cars:
        if name == car['Identification']["ID"]:
            if change1 == 'Dimensions' or change1 == 'Fuel Information' or change1 == 'Identification':
                car[change1][change2] = value
                return car
            elif change1 == 'Engine Information':
                for list in key_lists[13:15]:
                    print(f"{list}")
                print("What would you like to adjust >>> ", end='')
                change3 = input()
                car[change1][change2][change3] = value
                return car

if __name__ == '__main__':
    print(f"What is name of the specific car", end='')
    car_name = input()

    results2 = show_options()
    print(f"What is the new value of {results2[0]}", end='')
    adjustment = input()

    final_results = updating_a_car(car_name, results2[1], results2[0], adjustment)
    print(final_results)















