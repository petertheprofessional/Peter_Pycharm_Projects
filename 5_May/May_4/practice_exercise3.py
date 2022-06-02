users = [
    {
        "name": "Clark",
        "type": "Publisher",
        "items": [
            {
                "title": "The ABC of Blockchain",
                "status": "Draft",
                "reads": 10
            }
        ]
    },
    {
        "name": "Peter",
        "type": "Publisher",
        "items": []
    },
    {
        "name": "Samantha",
        "type": "Publisher",
        "items": [
            {
                "title": "The ABC of JavaScript",
                "status": "Published",
                "reads": 3254
            },
            {
                "title": "The XYZ of JavaScript",
                "status": "Published",
                "reads": 226
            }
        ]
    },
    {
        "name": "Mathilda",
        "type": "Reviewer",
        "items": [
            {
                "title": "The ABC of Blockchain",
                "status": "Pending"
            }
        ]
    }
]
def is_publisher(author_name):
    for user in users:
        #print(user)
        print(user['name'] == author_name, author_name, user['type'], user['name'])
        if user['name'] == author_name and user['type'] == "Publisher":
            return True
    return False

# def has_hits(author):
#     publisher = is_publisher(author)
#     if publisher == True:
#         for user in users:
#             if user['name'] == author:
#                 print(user)
#     return print("Try again")

is_publisher("Samantha")


# print("Clark", has_hits("Clark"))
# print("Peter", has_hits("Peter"))
# print("Samantha", has_hits("Samantha"))
# print("Mathilda", has_hits("Mathilda"))
# print("Mario", has_hits("Mario"))

#print(users[2]["items"][])
