import json

if __name__ == '__main__':

    with open('list.json') as file:
        data = json.load(file)
        print(data) #loads the file as a list with multiple dictionaries in it
        print(f'loaded data is from type: {type(data)}')
        print(f'data elements area from type: {type(data[0])}')

    # Changing the vaulue of a key in an existent record (dict?json object)
    print(data[2]["name"])
    data[2]["name"] = input("type a new name for the record two: ")
    with open('list.json', mode='w') as file:
        json.dump8data, file, indent=2)

    # Adding a new record
    record = {}
    record["name"] = "New User"
    with open('list.json', mode='w') as file:
        json.dump(data, file, indent=2)
