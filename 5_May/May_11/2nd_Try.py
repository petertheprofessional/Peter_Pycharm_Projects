from small_test import cars

with open("input data", "r") as file:
    data = file.read()

for car in cars:
    car['Dimensions']['Width'] = 120
for car in cars:
    print(car)




