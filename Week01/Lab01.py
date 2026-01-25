
#Sample Coding Question 01 Week 01

#Name:Camille Yu


# Question 02: Defining an array(list)

python_array=[1,2,3,4,5]

print(python_array)



# Question 3: Order of Operations


#// ---> floor division (divides and rounds DOWN to whole number)
# ** -----> power/exponent (example: 2 ** 3 means 2³ = 8)
# % ----> modulo (gives the remainder after division)




a = 2
b = 2
c = 5
d = 6

# Original expression:
# e = a - b ** c // d + a % c

# Fully-Bracketed Version:
e = (a - ((b ** c) // d)) + (a % c)

print("Question 3 result:", e)



# Question 4: Formatting

# temperature = 32.6 creates a variable storing the number
# {:.3f} is a placeholder that means:
# {} = "put a value here"
# :.3f = "show 3 decimal places" (f stands for "float" which means decimal number)
# .format(temperature) tells Python to put the temperature value in the placeholder
# The output will show 32.600 (the extra zeros are added automatically)


temperature = 32.6
print("The temperature today is: {:.3f} degrees Celsius".format(temperature))





# question 05:
userAge = int(input("Enter your age: ")) 


userAge = userAge + 22
print("Now showing the shop items filtered by age: " , userAge)