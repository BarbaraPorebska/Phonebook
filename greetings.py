name = input("What's your name?") 

print("Hello", name, "I am your phone book.")

age_input = input("How old are you?")

if age_input.isnumeric():
    age = int(age_input)
    if age > 0 and age <= 18:
        print("You are so young! Life is ahead of you!")
    elif age > 18 and age < 40:
        print("That's a nice age!")
    elif age > 40:
        print("You must be very wise!")
   
else:
    print("That doesn't seem to be an integer.") 