secret_password = input("Please enter your secret password: ").strip()
print(f"Your password hint:\n\tIt starts with {secret_password[0].upper()} and ends with {secret_password[-1].upper()}")
