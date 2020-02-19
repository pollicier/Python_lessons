print("Welcome to the Letter Counter App")

name = input("\nWhat is your name: ")
print("Hello, " + name.title() + "!")

print("I will count the number of times that a specific letter occurs in a message.")

message = input("\nPlease enter a message: ")
message = message.lower()

letter = input("Which letter would you like to count the occurrences of: ")
letter = letter.lower()

count = message.count(letter)

print(name.title() + ", your message has " + str(count) + " " + letter + "'s in it.")
