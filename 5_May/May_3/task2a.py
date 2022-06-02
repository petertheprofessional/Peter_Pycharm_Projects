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

# task 2



def get_author(author_name):
    for user in users:
        if user['name'] == author_name:
            return user
    return None

def author_average_reads(author_name):
    author = get_author(author_name)
    if author and author['type'] == 'Reviewer':
        return 0
    # averages!
    # print(author.get('items'))
    average = 0

    if author:
        items = author.get('items', [])  # giving an empty list if not found
        published_items = []
        for item in items:
            if item ["status"] == "Published":
                published_items.append(item)

        total = 0
        for published_item in published_items:
            total = total + published_item['reads']
        if published_items:
            #print("Items has stuff")
            average = total / len(published_items)
        else:
            average = 0
    return average

if __name__ == '__main__':
    print("Clark", author_average_reads("Clark"))
    print("Peter", author_average_reads("Peter"))
    print("Samantha", author_average_reads("Samantha"))
    print("Mathilda", author_average_reads("Mathilda"))
    print("Mario", author_average_reads("Mario"))