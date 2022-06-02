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


def get_author(author_name):
    for author in users:
        if author['name'] == author_name:
            return author
    return None


# def author_average_reads(author_name):
#     # we put our code here
#     author = get_author(author_name)
#     # check if the author is a reviewer
#
#     if author and author.get('type', None) == 'Reviewer':
#         # if author and author['type'] == 'Reviewer': # alternative
#         return 0
#
#     total = 0
#     number_of_published_items = 0
#     if author:
#         items = author.get('items', [])  ## giving an empty list if not found!!
#         for item in items:
#             if item["status"] == "Published":
#                 total += item["reads"]
#                 number_of_published_items += 1
#
#     return int(total / number_of_published_items) if number_of_published_items > 0 else 0


def author_is_popular(author_name):
    author = get_author(author_name)
    # mindblow approach!!!
    return bool(
        author
        and author['items']
        and (sum(
                [article["reads"] for article in author['items']
                  if 'reads' in article and article['status'] == 'Published']) / len(author['items']) > 1000)
    )


if __name__ == '__main__':
    # print("Clark", author_average_reads("Clark"))
    # print("Peter", author_average_reads("Peter"))
    # print("Samantha", author_average_reads("Samantha"))
    # print("Mathilda", author_average_reads("Mathilda"))
    # print("Mario", author_average_reads("Mario"))
    # sample code from task 3
    print("Clark", author_is_popular("Clark"))
    print("Peter", author_is_popular("Peter"))
    print("Samantha", author_is_popular("Samantha"))
    print("Mathilda", author_is_popular("Mathilda"))
    print("Mario", author_is_popular("Mario"))