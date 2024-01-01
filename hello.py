# ask user for their name
name = input("what's your name? ").strip()
name = name.title()

# split user's name into first name and last name
first , last = name.split(" ")


# say hello to user
print("hello" , end="\n")
print(f"\"  {first}  \"" , end=" ")
print("nice to hear from you")


