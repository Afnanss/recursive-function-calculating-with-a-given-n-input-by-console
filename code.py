#The Fibonacci sequence is calculated using the following formula: 
#F(n)={█(0 if n=0@1 if n=1@F(n-1)+F(n-2)  if n>1)┤
#Write a recursive function calculating (𝑛) with a given n input by console.



def fb(n):
    if n == 0:
        return 0 
    if n == 1:
        return 1
    if n > 1:
        return fb(n-1) + fb(n-2)


print("Enter a number:")
a = int(input())
print("Fibonacci sequence of ", a, "is",fb(a))



#Write a recursive function calculating the Factorial of a number (𝑛) with n is an input by the console.

def fc(n):
      
    if n == 0:
        return 1
     
    return n * fc(n-1)
  

print("Enter a number:")
num = int(input())
print("Factorial of", num, "is",fc(num))
  

