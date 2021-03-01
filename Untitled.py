
# coding: utf-8

# import keyword#basically is header 
# print(keyword.kwlist)
# a=10
# b=10
# z=13
# print(a)
# print(id(a))#gives address of a
# print(id(b))#given the same address as the value of a and b are same memory optimisation
# print(id(z))
# print("the total number of keywords is", len(keyword.kwlist))
# s="this is shashank pandey"#automatically identifies string
# print(s[1])
# s[5:10]#slicing

# In[1]:


#list
a=[10,30,'hello'] # list we can roughy say is array but list can take different data type in a single list
print(a[2])
print(a)
a[1]=20 #list is mutable means we can change list value 
print(a)


# In[2]:


#tuple
a=(1,2,"hello") #one of difference between list and tuple is tuple declare using parenthesis
print(a[1]) #indexing is same as list
a[0]="shashank"#you cannot change any single value in the tuple 
print(a)


# In[ ]:


#set
s={1,2,3,4,"shashank"}
print(s)
s2={2,2,2,3,3,1,1,1}
print(s2)#set do not duplicate values 
print(s[1])#sets do not suport indexing


# In[ ]:


#python dictionary 
s={'a':1,'b':2, 'c':'shashank'}#dictionary have one key and a value assigned to that particular key 
print(s['c'])


# In[ ]:


#data type conversion
float(5)
int(4.0)


# In[ ]:


#input output formating
a=10;b=20
print("the value of a is {} and b is {}".format(a,b))#index of 0 goes to first place and 1 goes to second place


# In[ ]:


print("the name of my father is {name2} and my mother name is {name1}".format(name1="shobha pandey",name2="ramesh pandey"))


# In[ ]:


num=input("enter a number")
print(num)


# In[ ]:


#prime number program
num=int(input("enter a number"))
i=2
isDivisible=False
while i< num:
    if num % i==0:
        isDivisible=True
        print("{} is divided by {}".format(num,i))
    i=i+1
if isDivisible:
    print("{} is a not prime number".format(num))
else:
    print("{} number is a prime number".format(num))


# In[ ]:


for i in range(0,100,2*5):
    print(i)


# In[ ]:


list=["shashank","shalini","shubham","surya","shivam"]
for index in range(len(list)):
    print(list[index])
for ele in list:
    print(ele)


# In[ ]:


num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
for index in range(num1,num2,1):
    if index>1
        isDefault=False;
            for i in range(2,index)
                if index % i==0
                    isDefault=


# In[ ]:


a=1+2j
print(isinstance(a,complex))


# In[ ]:


a=[500,1,2,3]
b=[500,1,2,3]
print(id(a) is id(b))
print(a==b)
print(' ')
print(id(b))
print(id(a))
a==b
print(id(a) is id(b))


# In[ ]:





# In[ ]:


lst=['one','two','three','four']
lst2=['five','six']
#lst.append(lst2)
print (lst)
lst.insert(2,lst2)
print(lst)
lst2.remove('five')
print(lst)


# In[ ]:


lst=[1,2,3,4,5,6,8]
print(lst[:])
print(lst[2:5])


# In[ ]:


lst=[1,2,3,4,5]
for ele in lst:
    print(ele,end=" "),


# In[ ]:


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    #templst=[]
   # lst=[]
    #[[[lst.append([i,j,k])for k in range(z+1) if (i+j+k)<=n] for j in range(y+1)] for i in range(x+1)]
    '''for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                #templst=[i,j,k]
                #lst.append(templst)
                lst.append([i,j,k])'''
                
                
            
    #print(lst)
    print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])


# In[ ]:


T = int(input().strip())

L = []
for t in range(T):
    args = input().strip().split(" ")
    if args[0] == "append":
        L.append(int(args[1]))
    elif args[0] == "insert":
        L.insert(int(args[1]), int(args[2]))
    elif args[0] == "remove":
        L.remove(int(args[1]))
    elif args[0] == "pop":
        L.pop()
    elif args[0] == "sort":
        L.sort()
    elif args[0] == "reverse":
        L.reverse()
    elif args[0] == "print":
        print (L)


# In[ ]:


import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np
iris = pd.read_csv(r"C:\Users\shali\Downloads\iris2.csv")
#print(iris)
#print(iris.shape)
#print(iris.columns)
#print(iris)
''''iris["species"].value_counts()
iris.plot(kind='scatter', x='sepal_length' ,y='sepal_width');
plt.show()
sns.set_style("darkgrid");
sns.FacetGrid(iris,hue='species',size=4).map(plt.scatter,'sepal_length','sepal_width').add_legend();
iris.plot(kind='scatter',x='petal_length',y='petal_width');
plt.show();
sns.set_style("whitegrid");
sns.FacetGrid(iris,hue='species',size=10).map(plt.scatter,'petal_length','petal_width').add_legend();
plt.close();
sns.pairplot(iris,hue="species",size=3);
plt.show();'''
iris_setosa=iris.loc[iris['species']=='setosa']
iris_virginica=iris.loc[iris['species']=='virginica']
iris_versicolor=iris.loc[iris['species']=='versicolor']
plt.plot(iris_setosa['petal_length'],np.zeros_like(iris_setosa['petal_length']))
plt.plot(iris_virginica['petal_length'],np.zeros_like(iris_virginica['petal_length']))
plt.plot(iris_versicolor['petal_length'],np.zeros_like(iris_versicolor['petal_length']))
sns.FacetGrid(iris,hue='species',size=4).map(sns.distplot,'petal_length').add_legend()
plt.show()


# In[ ]:


def count_substring(string, sub_string):
    #string, substring = (input().strip(), input().strip())
        #return(sum([ 1 for i in range(len(string)-len(sub_string)+1) if string[i:i+len                (sub_string)] == sub_string]))
    J=1
    for i in range(len(string)-len(sub_string)+1):
        if string[i:i+len(sub_string)]==sub_string:
            return J=J+1

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


# In[ ]:


N=int(input())
lst=list(input().split(" "))
lst.sort()
print(lst)
sum=0
max_counter=0 
max_value=0
for ele in range(len(lst)):
    sum=sum+int(lst[ele])
mean=sum/N 
print(mean)
if len(lst)%2!=0:
    median=lst[N//2]
    print(median)
else:
    median=(int(lst[len(lst)//2])+int(lst[(len(lst)//2)+1]))/2
    print(median)
for i in range(len(lst)):
    counter=0
    for j in range(len(lst)):
        if lst[i]==lst[j]:
            counter=counter+1
    if counter > max_counter:
        max_counter=counter
        max_value=int(lst[i])
print(max_value)


# In[ ]:


a,b=257,257;
print(id(b))
print(id(a))
print(a is b)


# In[ ]:


lst1 =[1,2,3]
lst2 = [4,5]
product=[(ele1,ele2) for ele1 in lst1 for ele2 in lst2 ]
print(product)


# In[ ]:


lst=list(map(int,input().split(",")))
s=set(lst)
lst1=list(s)
if len(lst1)>2:
    print(lst1[-2])


# In[ ]:


lst=list(map(int,input().split(",")))
if(len(lst)<2 and len(lst)>100000):
    print("Error")
else:
    first_max=lst[0];
    second_max=lst[0];
    for ele in lst:
        if(ele>first_max):
            second_max=first_max;
            first_max=ele;
    if(first_max==second_max):
        print("Error")
        exit();
    else:
        print(second_max);


# In[ ]:


lst=list(map(int,input().split(",")))
if(len(lst)<2):
    print("Error")
else:
    s=set(lst)
    if(len(s)==1):
        print("Error")
    else:
        lst1=list(sorted(s))
        print(lst1[-2])
       


# In[ ]:


n=int(input())
for i in range(1,n):
    if i%3==0 and i%5==0:
        print("FizzBuzz",end=",");
    elif i%3==0:
        print("Fizz",end=",");
    elif i%5==0:
        print("Buzz",end=",");
    else:
        print(i,end=",");
        


# In[ ]:


n=int(input())
for i in n:
    if i%3==0 and i%5==0:
        print("FizzBuzz",end=",");
    elif i%3==0:
        print("Fizz",end=",");
    elif i%5==0:
        print("Buzz",end=",");
    elif print(i,end=",");
        


# In[ ]:


#factorial
from functools import reduce
n=int(input())
def factorial(n):
    if(n==0):
        print("factorial is {0}".format(1));
    elif(n<0):
        print("Factorials are not defined");
    else:
        lst = list(range(1,n+1))
        return reduce(lambda x,y:x*y,lst);
print(factorial(n))
    


# In[ ]:


from functools import reduce
n=int(input())
if(n==0):
    print("n factorial is {0}".format(1))
elif(n<0):
    print("n! is not defined for negative numbers");
else:
    lst=list(range(1,n+1));
    print(reduce(lambda x,y:x*y,lst));


# In[ ]:


#uncoupled integer
lst=list(map(int,input().split(",")))
for ele in lst:
    x=lst.count(ele)
    if(x==1):
        print(ele)
    else:
        continue;
    


# In[ ]:


n=int(input())
def fib(n):
    if(n==1 or n==2):
        return 1;
    elif(n==0):
        return 0;
    else:
        return fib(n-1) + fib(n-2);
print(fib(n));


# In[ ]:


'''10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50'''
from collections import Counter
numberOfShoes= int(input())
shoeSize=Counter(list(map(int,input().split())))
print(shoeSize)
print(shoeSize.keys())
numberOfCustomers=int(input())
income=0
#customerDict={key:values for key=int(input()),values=int(input()) in range (numberOfCustomers)}
for i in range(numberOfCustomers):
    line=list(input().split())
    size=int(line[0])
    price=int(line[1])
    if(size==shoeSize.keys()):
        shoeSize['size']=shoeSize['size']-1
        income=income+price;
    
        
        
    


# In[ ]:


import time
start_time=time.time()
from collections import Counter
stock=int(input())
shoeSize=list(map(int,input().split()))
new=Counter(shoeSize)
temp= input()
numberOfCustomers=int(temp)
income=0
print(numberOfCustomers, range(numberOfCustomers))
for i in range(numberOfCustomers):
    line=input().split()
    print(line)
    size=int(line[0])
    price=int(line[1])
    if(size in new.keys()):
        if(new[size]):
            new[size]=new[size]-1
            income=income+price;
        else:
            print("size is no longer available")
    else:
        print("shoeSize not in the stock")
print(income)
end_time=time.time()
print(end_time-start_time)


# In[8]:


from itertools import permutations
lst=input().split()
if(lst[0].isupper()):
    newlst=[ch for ch in lst[0]]
    items=sorted([''.join(x) for x in permutations(newlst,int(lst[1]))])
    for ele in items:
        print(ele)


# In[3]:


#insertion sort
import time
start_time=time.time()
lst= list(map(int,input().split()))
i=1
for i in range(len(lst)):
    j=i-1
    key=lst[i]
    while(j>=0 and lst[j]>key):
        lst[j+1]=lst[j];
        j=j-1;
    lst[j+1]=key;
print(lst)
end_time=time.time()
print(end_time-start_time)
        


# In[26]:


from itertools import combinations
n=int(input())
lst=list(input().split())
size=int(input())
ch=str(input().strip())
comb=list(''.join(x) for x in combinations(lst,size))
i=0
space=len(comb);
for ele in comb:
    if ch in ele:
        i+=1
prob=i/len(comb)
print(prob)


# lst=[987,765,543,325]
# for i in lst:
#     ele=lst[i]+;
# print(lst)

# In[3]:


from itertools import combinations_with_replacement
lst=input().split()
newlst=sorted([ch for ch in lst[0]])
comb=sorted(list(''.join(x) for x in combinations_with_replacement(newlst,int(lst[1]))))
print(comb)
for ele in comb:
    print(ele)


# In[31]:


from itertools import groupby
from collections import Counter
lst = list(map(str,input().strip()))
def c(x):
    count=0
    for ele in lst:
        if(x==ele):
            count=count+1
    return count
group_id=groupby(lst,key=c)


# In[13]:


from itertools import product  
line,modulo=map(int,input().split())
matrix=[]
def mod(x):
    sum=0
    for i in x:
        sum=sum+i**2
    return(sum%modulo)
            
for i in range(int(line)):
    matrix.append(list(map(int,input().split()))) 
print(matrix)
mul=list(product(*[matrix[i] for i in range(len(matrix))]))
print(mul)
results=map(lambda x: mod(x),mul)
print(max(results))



#   
# for i in range(2): 
#       
#     # Append an empty sublist inside the list 
#     #matrix.append([]) 
#       
#     #for j in range(2): 
#         matrix.append(list(map(int,input().split()))) 
#           
# print(matrix) 
