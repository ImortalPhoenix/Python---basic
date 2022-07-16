# string concatenation(aka how to put strings together)
# suppose we want to create a string that says "subscribe to _____"
youtuber = "Arpit Dhore" # some string variable

# a few ways to do this
# print("sbuscribe to " + youtuber)
# print("subscibe to {}". format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Comuputer programming is so {adj}! It makes me so exited all the time because  I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)