# Loops in Python


"""
Question 
1. Print numbers from 1 to 100
2. Print numbers from 100 to 1
3. Print multiplication numbers of a number n
4. Print the elements of the following list using a loop 
[1,4,9,16,52,36,49,64,81,100]

5. Search for a number x in this tuple using loop
[1,4,9,16,52,36,49,64,81,100]



# Question - 1

i=1
while i<=100:
    print(i)
    i+=1

#  Question - 2   
j = 100
while(j>=1):
   print(j)
   j-=1


# Question -3
   
i = 1
n=5
while(i<=10):
    print(i*n)   
    i+=1

# Question - 4
    
nums = [1,4,9,16,52,36,49,64,81,100,81,64,49,36,25,16,9,4,1]
i=0
while i<=len(nums)-1:
    print(nums[i])
    i+=1

"""

# Question - 5

nums = [1,4,9,16,52,36,49,64,81,100]

i = 0
search = 10
ans = False
while i<len(nums):
    if(nums[i]==search):
       ans = True
       break
    else:
        ans = False
        i+=1

if(ans==True):
  print("Yes Found it Finally !")
else:
    print("Not Found ")


#  Using for loop
"""

Print the elements of the following list using a loop 
[1,4,9,16,52,36,49,64,81,100]

Search for a number x in this tuple using loop
[1,4,9,16,52,36,49,64,81,100]

"""   

# Question -1 

nums = [1,4,9,16,52,36,49,64,81,100]

for val in nums:
   print(val)

# Question - 2

string = ["a","b","c","d","e","f","g","h","i"]
       
searchStr = "b"
for value in string:
 if(value == searchStr):
    print("I got you")
    break
else:
   print("OOps")


# Range 

for i in range(5):  
   print(i)


for i in range(2,10):
   print(i)


for i in range(2,10,2):   # range (start, stop, step)
   print(i)


#   WAP to find the sum of n natural numbers

sum = 0

n = 50
for i in range(1,n):
   sum+=i

print(sum) 

#  WAP to find the factorial of first n numbers

n = 5
factorial = 1
for i in range(1,n+1):
   factorial*=i

print(factorial)   