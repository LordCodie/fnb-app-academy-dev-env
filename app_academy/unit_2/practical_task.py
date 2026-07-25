first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
bio_message = input("Please enter your bio message: ")

username = f"{first_name[0].lower() + last_name.lower()}"

print(f"Full Name: {(first_name + " " + last_name).title()}")

print(f"Number of characters in bio: {len(bio_message)}")
 
print(f"username {username}:\n {bio_message.strip().replace("I am", "I'm")}")