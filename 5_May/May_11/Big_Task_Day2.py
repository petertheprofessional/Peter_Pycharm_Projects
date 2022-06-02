from cars import cars
def insert_new_cars_into_list():
    key_lists = ['Dimensions', 'Engine Information', 'Fuel Information', 'Identification', 'Height', 'Length', 'Width', 'Driveline', 'Engine Type', 'Hybrid', 'Number of Forward Gears', 'Transmission', 'Engine Statistics', 'Horsepower', 'Torque', 'City mpg', 'Fuel Type', 'Highway mpg', 'Classification', 'ID', 'Make', 'Model Year', 'Year']

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
if __name__ == '__main__':
    new_car = []
    new_car.append(insert_new_cars_into_list())
    print(new_car)
















