# Given an array arr[] of integers, segregate even and odd numbers in the array such that all the even numbers should be present first, and then the odd numbers.
arr = [1,2,3,4,5,6,7,8,9];
x = len(arr);
def array(arr, x) :
    a = -1;
    b = 0;
    while ( b != x ):
        if(arr[b] % 2 == 0):
            a = a+1;



