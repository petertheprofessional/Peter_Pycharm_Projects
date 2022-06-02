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

def author_average_reads(author):
    publications = 0
    result = 0
    for user in users:
        if author == user["name"]:
            for item in user["items"]:
                if "reads" in item and item["status"] == "Published":
                    result += item["reads"]
                    publications += 1
    if publications > 0:
        return int(result / publications)
    else:
        return result

print("Clark", author_average_reads("Clark"))
print("Peter", author_average_reads("Peter"))
print("Samantha", author_average_reads("Samantha"))
print("Mathilda", author_average_reads("Mathilda"))
print("Mario", author_average_reads("Mario"))