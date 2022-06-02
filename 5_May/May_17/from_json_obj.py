import json

if __name__ == '__main__':

    with open('simple_object.json') as file:
        data = json.load(file)
        print(data)
        print(type(data)) #see what type of info is in json file like if its a string or dictionary or list

    with open('simple_object.json', mode='r') as file:
        data = json.load(file)
        print(data["name"]) # call information from dictionary in the json file

    # with open('simple_object.json', mode='w') as file:
    #     data["name"] = "Mathias" # or create a new value with input("Type a name: ")
    #     json.dump(data, file, indent=2)

    #adding a key value pair
    # key = input("type key")
    # value = input("tpye value")
    # data[key] = value
    # print(data[key])
    # with open('simple_object.json', mode='w') as file:
    #     json.dump(data, file, indent=2)

