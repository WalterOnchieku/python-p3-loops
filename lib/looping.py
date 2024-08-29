#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i>0:
        print(i)
        i-=1
    print('Happy New Year!')    
            

   

def square_integers(int_list=[1, 2, 3, 4, 5]):
    int_list2=[]
    for i in int_list:
        int_list2.append(i**2)
        print (int_list2)


def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
