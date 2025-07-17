#hammad_age=4
school_going_age=5
input_age = input("Enter Hammad's age: ")
if int(input_age) == school_going_age:
    print("Congratulations Hammad! You are now old enough to go to school.")
elif int(input_age) > school_going_age:
    print("Hammad should join higher secondary school.")
elif  int(input_age) <= 2:
    print("Hammad shoud stay at home with mama.")
else:
    print("Sorry Hammad, you are not old enough to go to school yet.")
