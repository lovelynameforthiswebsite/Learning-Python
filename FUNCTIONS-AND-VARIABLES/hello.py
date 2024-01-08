# ask user for their name
name = input("what's your name ? ").title().strip()
# split user's name into first name and last name
first ,last= name.split(" ")


# say hello to user
print("hello",f"{first}")
