Coding:
  
num = int(input())
a=[]
count=0
for i in range(2, num):
    if(num % i) == 0:
       a.append(i)
       count=count+1
if count==0:
    print("PRIME NUMBER")
else:
    print(max(a))
