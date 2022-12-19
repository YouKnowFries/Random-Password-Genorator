import random
import string

def generate_password(length):
  # Generate a random password using the specified length
  password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
  return password

# Generate a random password
password = generate_password(12)

# Write the password to a text file
with open("password.txt", "w") as f:
  f.write(password)

print(f"Random password saved to 'password.txt': {password}")
