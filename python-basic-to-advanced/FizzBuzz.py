import random

# random_number=int(input("Enter your number: ") )                      
random_number=random.randint(1,100);
print(random_number)

if(((random_number%3)==0)and ((random_number%5)==0)):
    print("FizzBuzz")

elif((random_number%3)==0):
    print("Fizz");
elif((random_number%5)==0):
    print("Buzz")
else:
    print("none")