import time

score = 0
special_char = r"!#$%&'()*+,-./:;<=>?@[\]^_`{|}~" 
numbers = "0123456789"
letters = "abcdefghijklmnopqrstuvwxyz"
capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("Password score is out of 10")
time.sleep(.1)
#password input 

password = input(f"What is your password?:")

#length check

if len(password) >= 16:
    score += 3
elif 6 <= len(password) <= 15:
    score += 1 
    print("It is recomended to have 16 characters in a password")
else:
    score += 0 
    print("Your password is to short. Please make your password at least 16 characters")

# Special Character check
if sum(1 for s in password if s in special_char) >= 2:
    score += 3
elif sum(1 for s in password if s in special_char) == 1:
    score += 1 
    print("It is recomended to add another special character")
else:
    score += 0 
    print("Please add a special character")
# Number check

if sum(1 for n in password if n in numbers) >= 3:
    score += 2 
elif sum(1 for n in password if n in numbers) == 1:
    score += 1 
    print("We recomend having at least 3 numbers in your password")
else:
    score += 0 
    print("Please include at least 3 numbers in your password")

# Letter Check

if sum(1 for l in password if l in letters) >= 3:
    score += 1
else:
    score += 0 
    print("Please include at least 3 lowercase letters")

# Upper case letters


if sum(1 for c in password if c in capital_letters) >= 1:
    score += 1
else:
    score += 0 
    print("Please include a capital letter")

if score == 10:
    print("Your Password is compliant with various industry security standards") 
    print(f"Your score is: {score}/10")
elif 7 < score <= 9:
    print("Your password is good for personal use but not compliant with industry standard") 
    print(f"Your score is {score}/10")
else: 
    print("Your password is not compliant with industry standards nor suitable for personal use") 
    print(f"Your score is {score}/10")

    



