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

def get_user(author_name):
    # for user in users:
    #     if user['name'] == author_name and user['type'] == "Publisher":
    #         return True
    # return False
    return next((user for user in users if user["name"] == author_name and user['type'] == "Publisher"), None)

def call_items(items):
    reads_list = []
    for item in items:
        read = item['reads']
        if item['status'] == 'Published':
            reads_list.append(read)
    average = sum(reads_list)/ len(reads_list) if len(reads_list) else 0
    return (average > 1000)


def author_is_popular(author_name):
    author = get_user(author_name)

    return bool((author and author['items'] and call_items(author['items'])))


if __name__ == '__main__':
    print("Clark", author_is_popular("Clark"))
    print("Peter", author_is_popular("Peter"))
    print("Samantha", author_is_popular("Samantha"))
    print("Mathilda", author_is_popular("Mathilda"))
    print("Mario", author_is_popular("Mario"))
