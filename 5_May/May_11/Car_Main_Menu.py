from cars import cars

key_lists = ['Dimensions', 'Engine Information', 'Fuel Information', 'Identification', 'Height', 'Length', 'Width',
             'Driveline', 'Engine Type', 'Hybrid', 'Number of Forward Gears', 'Transmission', 'Engine Statistics',
             'Horsepower', 'Torque', 'City mpg', 'Fuel Type', 'Highway mpg', 'Classification', 'ID', 'Make',
             'Model Year', 'Year']

def menu():
    print('1. Get a car by name')
    print('2. Get cars by the number of gears')
    print('3. Get cars by Manufacturer')
    print('4. Get a car by average consumption')
    print('5. Get a car by the year')
    print('6. Insert new car')
    print('7. Update a car')
    print('0. Exit')
    print("Select the number from the menu you would like to explore >>> ", end='')
    option = input()
    return int(option)

def get_car_by_name(name):
    results = []
    for car in cars:
        x = car['Identification']["ID"].find(name)
        if x >= 0:
            results.append(car['Identification']["ID"])
    return results

def get_car_by_number_of_gears(number_of_gears):
    results = []
    for car in cars:
        if car['Engine Information']['Number of Forward Gears'] == number_of_gears:
            results.append(car['Identification']["ID"])
    return results

def get_car_by_manufacturer(manufacturer):
    results = []
    for car in cars:
        x = car['Identification']["Make"].find(manufacturer)
        if x >= 0:
            results.append(car['Identification']["ID"])
    return results

def get_car_by_average_comsumption(desired_consumption):
    results_city = []
    results_hi = []
    results_make = []
    for car in cars:
        if car['Fuel Information']['City mpg'] >= 0:
            results_city.append(car['Fuel Information']["City mpg"])
        if car['Fuel Information']['Highway mpg'] >= 0:
            results_hi.append(car['Fuel Information']["Highway mpg"])
        if car['Fuel Information']['Highway mpg'] >= 0:
            results_make.append(car['Identification']["ID"])
    results_comined = [x + y for (x, y) in zip(results_city, results_hi)]
    results_averaged = [x / 2 for x in results_comined]
    mpg_dictionary = dict(zip(results_make, results_averaged))
    for key, content in mpg_dictionary.items():
        if content >= desired_consumption:
            print(f"{key} = {content}")

def get_car_by_year(year):
    results = []
    for car in cars:
        x = car['Identification']["Model Year"].find(year)
        if x >= 0:
            results.append(car['Identification']["ID"])
    return results

def insert_new_cars_into_list():
    values_lists = []
    sub_list = []
    two_list = []
    three_list = []
    four_list = []
    for dimensions in key_lists[4:7]:
        values_lists.append(input(f"Please enter {dimensions} >>> "))
    dic_dimensions = dict(zip(key_lists[4:7], values_lists))
    dic_master_dimensions = dict.fromkeys(key_lists[0:1], dic_dimensions)
    for engine_stat in key_lists[13:15]:
        sub_list.append(input(f"Please enter {engine_stat} >>> "))
    dic_engine_stat = dict(zip(key_lists[13:15], sub_list))
    dic_engine_stats = dict.fromkeys(key_lists[12:13], dic_engine_stat)
    for engine_info in key_lists[7:12]:
        two_list.append(input(f"Please enter {engine_info} >>> "))
    dic_engine_info = dict(zip(key_lists[7:13], two_list))
    dic_master_engine = dict.fromkeys(key_lists[1:2], dic_engine_info)
    dic_master_engine.update(dic_engine_stats)
    for fuel in key_lists[15:18]:
        three_list.append(input(f"Please enter {fuel} >>> "))
    dic_fuel = dict(zip(key_lists[15:18], three_list))
    dic_master_fuel = dict.fromkeys(key_lists[2:3], dic_fuel)
    for id in key_lists[18:23]:
        four_list.append(input(f"Please enter {id} >>> "))
    dic_id = dict(zip(key_lists[18:23], four_list))
    dic_master_id = dict.fromkeys(key_lists[3:4], dic_id)
    dic_master = dict(dic_master_dimensions, **dic_master_engine, **dic_master_fuel, **dic_master_id)
    return dic_master

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
    loop = 1
    while loop == 1:
        choice = menu()
        if choice == 1:
            print("What is the name of the car >>> ", end='')
            car_name = input()
            results1 = get_car_by_name(car_name)
            for result1 in results1:
                print(result1)
        elif choice == 2:
            print("How many gears >>> ", end='')
            num_gears = int(input())
            results2 = get_car_by_number_of_gears(num_gears)
            for result2 in results2:
                print(result2)
        elif choice == 3:
            print("What is the name of the manufacturer >>> ", end='')
            car_make = input()
            results3 = get_car_by_manufacturer(car_make)
            for result3 in results3:
                print(result3)
        elif choice == 4:
            print("What range of mpg would you like? >>> ", end='')
            desired_consumption = float(input())
            print(get_car_by_average_comsumption(desired_consumption))
        elif choice == 5:
            print("Please enter year of car manufacture >>> ", end='')
            model_year = input()
            results4 = get_car_by_year(model_year)
            for result4 in results4:
                print(result4)
        elif choice == 6:
            new_car = []
            new_car.append(insert_new_cars_into_list())
            print(new_car)
        elif choice == 7:
            print(f"What is name of the specific car ", end='')
            car_name = input()

            results2 = show_options()
            print(f"What is the new value of {results2[0]}", end='')
            adjustment = input()

            final_results = updating_a_car(car_name, results2[1], results2[0], adjustment)
            print(final_results)
        elif choice == 0:
            loop = 0
        else:
            print("please enter a value from the list")
