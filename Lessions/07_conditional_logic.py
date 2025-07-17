#logical operators are either "ture or false" or "yes or no" or "on or off" or "1 or 0"
# they are used to compare values and make decisions in code

# equal to                   ==
# not equal to               !=
# less than                  <
# greater than               >
# less than or equal to      <=
# greater than or equal to   >= 

# 4 equal to 4

#print(4 ==4) # True
#print(4!= 4) # False
#print(4 < 4)  # False
#print (3<4)  # True
#print(4 > 3)  # True
#print(3 <= 1) # True
#print(4 >= 4) # True

# application of logical operators
#Hammad = 4
#age_at_school =5
#print (hammad == age_at_school) # False

#age_at_school = 5
#hammad_age= input("how old is hammad? ") #input function
#hammad_age = int(hammad_age)  # convert input to integer
#print(type(hammad_age))  # <class 'int'>
#print(hammad_age >= age_at_school) # False

# convert input 

# i want to write a program that checks if a person is eligibale to vote
# a person is eligible to vote if they are 18 or older

age_elegible = 18
voter_age =input("how old is the voter? ")
voter_age =int(voter_age)  # convert input to integer
if voter_age >= age_elegible:
    print("The voter is eligible to vote")
else :
    print("The voter is not eligible to vote")
    
    