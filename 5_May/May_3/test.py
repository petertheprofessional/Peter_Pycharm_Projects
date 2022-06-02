kids = [{"name": "Tim", "age": 4, "hobbies":["soccer", "chess", "volleyball"]},
        {"name": "Peter", "age": 8},
        {"name": "Jon", "age": 4, "hobbies":["baseball", "chess", "football"]}]

def find_kid(name, sport = None):
    stash = []
    for kid in kids:
        #print(kid["name"])
        if kid["name"] == name:
            return kid
        # for hobby in kid.get("hobbies", []):
        #     if hobby == sport:
        #         stash.append(kid)
        for hobby in kid:
    return stash

#print(find_kid("Jon"))
print(find_kid("boy", "chess"))
#print(kids[0]['name'], kids[0]['hobbies'][1])
