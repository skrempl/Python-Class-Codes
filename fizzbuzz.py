# write a program that prints the numbers of 1 to 100
# but for multiples of three print "Fizz" instead of the number
# and for multiples of five print "Buzz"
#for multiples of three and five print "FizzBuzz"

# Hint: % (modulo) tells you what's left over when you divide one number
# by another number ex. number % 3 == 0 will return true if number is 
# divisible by 3, and false if it is not.

Emma = range(1,1001)

for Hickory in Emma:
    if (Hickory % 3 == 0) and (Hickory % 5 == 0):
        print("FizzBuzz")
    elif(Hickory % 3 == 0):
        print ("Fizz")
    elif(Hickory % 5 == 0):
        print ("Buzz")
    else:
        print(Hickory)

