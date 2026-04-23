##print hello world
print("Hello World")
# get user to give their dob and return their age on the 11.05/2039
from datetime import datetime

print("Hello World")

dob_input = input("Enter your date of birth (YYYY-MM-DD): ")
dob = datetime.strptime(dob_input, "%Y-%m-%d")

target_date = datetime(2039, 5, 11)

age = target_date.year - dob.year

# adjust if birthday hasn't happened yet that year
if (target_date.month, target_date.day) < (dob.month, dob.day):
    age -= 1

print(f"You will be {age} years old on 11/05/2039")