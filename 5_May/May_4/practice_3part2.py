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
        if user['name'] == author_name and user['type'] == "Publisher":
            return True
    return 0


def author_average_reads(average_reads):
    publisher = is_publisher(average_reads)
    if publisher:
        for user in users:
            if user['name'] == average_reads:
                items = user['items']
                status = user['items']
                reads = [x['reads'] for x in status]
                st_dic = [x['status'] for x in status]
                total = sum(reads) / len(reads) if len(reads) else 0 #falsy
                if 'Published' not in st_dic:
                    return 0
                if total > 0:
                    return total

    return 0



print("Clark", author_average_reads("Clark"))
print("Peter", author_average_reads("Peter"))
print("Samantha", author_average_reads("Samantha"))
print("Mathilda", author_average_reads("Mathilda"))
print("Mario", author_average_reads("Mario"))