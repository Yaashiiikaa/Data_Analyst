n=int(input())
fact=1
if(n==0 and n==1):
  fact=1
else:
   for i in range(2,n+1):
      fact=fact*i
print(fact)
