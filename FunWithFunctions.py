# Odd/Even

print "Odd or Even numbers:"
print "================================================="



def odd_even():
    for i in range (1, 2000):
        if i%2 == 0:
            print "Number is {}. This is an even number.".format(i)
        else:
            print "Number is {}. This is an odd number.".format(i)

odd_even()
print "================================================= \n"

print "Function Multiples: \n"

a = [2, 4, 10, 16]
new_arr=[]
def multiply(arr):
    for item in arr:
        new_arr.append(item*5)
    return new_arr

print "The list before the function call is: {}".format(a)
print "The list before the function call is: {}".format(multiply(a))

print "================================================= \n"


