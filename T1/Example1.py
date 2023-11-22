# Sum of even numbers: Write a program that sums all the even numbers from 1 to 100.
#result= []

#for i in range (1, 100):
#    if i/2= 0:
#        i+=result
#        print(result)

def calculation():
    # Method 2: Using loop
    result = 0
    number = 2
    while number <= 100:
        result += number
        number += 2
    print("Sum of even numbers (Method 2):", result)


def func1():
    # Method 1: Using a for loop
    sum_even = 0
    for number in range(2, 101, 2): # Start from 2, go up to 100, increment by 2
        sum_even += number
        number += 2
    print("Sum of even numbers (Method 2):", sum_even)


def main():
    calculation()

if __name__ == "__main__":
    main()