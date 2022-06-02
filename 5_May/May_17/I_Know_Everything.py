import json

def load_data():
    with open("Wine.json") as file:
        return json.load(file)
def get_number_of_states():
    data = load_data()
    states = len(data)
    print(states)
def clean_up():

    data = load_data()
    for datum in data:
        clean = datum["Still Wines/Production"].replace(',','')
    return clean


def state_wine_by_production():
    data = load_data()
    for datum in data:
        datum["Still Wines/Production"] = int(datum["Still Wines/Production"])
    print(datum)




if __name__ == '__main__':
    print(clean_up())