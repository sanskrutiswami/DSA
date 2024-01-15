# Given an array of random numbers, Push all the zero’s of a given array to the end of the array.
num = [4, 68, 0, 34, 50, 0, 0, 0, 3, 5, 0, 9, 6]; # given array of random numbers.
x = len(num);  #taking the length of the given array to partition it.
print(x)
y = 0; # swapping element 
for i in range(x):  # using for loop over the range of the length of the given array.
    if num[i] != 0: # during the iteration of for loop, if the number is not equal to 0, it will swap position of that number with the zero present in the array.
        num[y], num[i] = num[i], num[y] 
        y += 1 
print(num)