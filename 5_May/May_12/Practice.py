#Exercise 1Task 1

# city = 'London'
# print(city)

#Exercise 1Task 2

# city = 'berlin'
# population = 3645000
# print(f"{city.capitalize()} : {population}")

#Exercise 1Task 3 Check his answer

# city = 'london'
# population = 9000000



#Exercise 1Task 4

# text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's Capital"
# print(text.find('Capital'))


#Exercise 1Task 5

# text = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."
# new = text.split()
# print(new)

#Exercise 1Task 6

# text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."
# new = text.replace('capital', 'capital of Germany')
# print(new)

#######################################################################################################################

#Exercise 2 Task 1

# text = "Berlin is a world city of culture, politics, media and science."
# print(len(text))

#Exercise 2 Task 2

# text = "Berlin is a world city of culture, politics, media and science."
# print(text[0])

#Exercise 2 Task 3

# text = "Berlin is a world city of culture, politics, media and science."
# print(text[0:3])

#Exercise 2 Task 4

# text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital"
# print(f"B appears:", text.count("B"), "times")

#Exercise 2 Task 5

# text = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."
# new = text[-10:]
# print(new)

#Exercise 2 Task 6

# text = "---Python programming---"
# new = text.replace('-', '')
# print(new)

#Exercise 2 Task 7

# first = "Peter"
# last = "Kelly"
#
# print(first + " " + last)

#######################################################################################################################

#Exercise 3

the_secret = "this_is_my_secret"
love_name = "Max"
year_of_birth = "1982"

print(((the_secret + "" + love_name)[::-1]) + "" + year_of_birth)

#Exercise 4
#
# def task4(text):
#     vowel = 'aeiou'
#     text2 = len(text)
#     if text[-1] in vowel:
#         print(f"{text}-inator {text2}000")
#     else:
#         print(f"{text}inator {text2}000")
#
# if __name__ == '__main__':
#     text = input("Enter the String: ")
#     print(task4(text))