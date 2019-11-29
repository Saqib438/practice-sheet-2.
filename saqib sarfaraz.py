#!/usr/bin/env python
# coding: utf-8

# # Python User Define Function Practice Activity - 2 

# Asst. Prof. Syed Faisal Ali              $\;\;\;\;\;\;$              Programming Fundamentals - FALL 2019 $\;\;\;\;\;\;$ Software Engineering                     $\;\;\;\;\;\;$                   Dated: 27 Nov 2019

# Question 1: Create a function to find the following:
# If the base of triangle is 3 cm long and its equilateral triangle and the radius of circle is 1.5 cm then find the area of triangle shaded. 
# 

# ![proj](q1.jpg)

# In[1]:


def area(b,r):
    h=(b)*r/2
    return h
area(3,1.5)


# Question 2: Create a function which can read a dictionary of your family members such as 5 members. 
# 1 Abbu, 1 Ammi, 2 Brothers 1 Sister. Now feed this data in dictionary in terms of name and relations.
# The UDF will ask findrelation() in this you will enter Brother it will return the names of two brothers you have inserted. In case if the relation is not found it will return “Sorry the relation doesn’t exist in your family.” 
# 

# In[7]:


def findrelation(s):
    dic={'father':'sarfaraz','brother':'ali,danish','sister':'aliza'}
    a = dic[s]
    return a
findrelation('brother')


# Question 3: Create a function to find the following:
# If the base of triangle is 5 cm long and its equilateral triangle and the radius of circle is 2.25 cm then find the area of triangle shaded. 
# 

# ![proj](q3.jpg)

# In[11]:


import math
def func(b):
    h=b**2*((math.sqrt(3))/4)
    return h
func(5)


# Question 4:
# Create a function that takes a list of random numbers from users and add only those which are even. If all the numbers are odd it will return sorry no even number found.
# 

# In[34]:


def ev(l):
    s=0
    for i in l:
        if i%2==0:
            print(i)
            s = s+i
            print("sum of even no:",s)
        else:
            print("no even is found!")
print(ev([1,2,3,4,5,6,7,8]))            


# Question 5:
# Write a function which can take a list of numbers and it will return sorted list.
# 

# In[35]:


def so(l):
    return sorted(l)
print(so(['3','a','4','5']))


# Question 6:
# Write a function that will take the radius and return the perimeter and area of circle with 5% increment.
# 

# In[40]:


from math import pi
def area_circle(r):
    area=pi*(r**2)
    b=area+(area*0.05)
    print("perimeter:",2*pi*r)
    print("area of cirlce:",area)
    print("area of the cirlce after increment:",b)
    return ""
print(area_circle(6))


# Question 7:
# Write a function that will take the strings as argument and return number of vowels and consonants.
# 

# In[68]:


def str(vc):
    s=vc
    countv =0
    countc =0
    for i in s:
        if i in "AEIOU" or i in "aeiou":
            countv +=1
        else:
            countc +=1
    print("number of vowels:",countv)
    print("number of consonent:",countc)
            
str('saqib')                  


# Question 8:
# Write a function that will take length and breadth for a rectangle and return perimeter and area of rectangle with 8% increment.
# 

# In[72]:


def rec(l,b):
    area=l*b
    a=area+(area*0.08)
    print("Area of rectangle:",a)
    print("perimeter",2*(l+b))
rec(5,7)    


# Question 9:
# Write a function that can take the numbers in strings. From string find which number is even and which one is odd. Save them in two different lists and generate the result.
# 

# In[77]:


s="12345678"
e=0
o=0
e1 =[]
o1= []
for i in s:
    if int(i)%2==0:
        e+=1
        e1.append(i)
    else:
        o+=1
        o1.append(i)
print("number of even:",e)
print("number of odd:",o)
print("list of even",e1)
print("list of odd:",o1)


# Question 10:
# Write a function which will take the string from the user and return how many alphabets have been used in it and which alphabets are missing.
# 

# In[94]:


s='saqib'
n=0
az='abcdefghijklmnopqrstuvwxyz'
for i in s:
    az=az.replace(i,"")
    n+=1
print(n)
#
print(az)


# Question 11:
# Write a function that will take verbs in words and return a list of verbs with continuous tense by adding (ing) at the end of each verb.
# 

# In[78]:


def verb(s):
    if s[-1] =='e':
        s=s.replce(s[-1],"")
        print("verb",s+"ing")
    else:
        print("verb",s+"ing")
verb('read')        


# Question 12:
# Make a function which can take two radius of circles and find the areas of it and subtract smaller one from larger one and tell the remaining area of circle.
# 

# In[80]:


from math import pi
def cc(r,rr):
    a=pi*(r**2)
    aa=pi*(rr**2)
    if a>aa:
        fa=(aa-a)
    else:
        fa=(aa-a)
    return abs(fa)    
print(cc(50,10))


# Question 13:
# Write a function that will take a string and calculate number of Upper case letters and lower case letters.
# 

# In[85]:


def ss(a):
    nu=0
    nl=0
    u='ABCDEFQHIJKLMNOPQRSTVUWXYZ'
    I='abcdefghijklmnopqrstvuwxyz'
    for i in a :
        if i in u:
            nu=nu+1
        if i in I:
            nl=nl+1
    print(nl,nu)
print(ss("saqib"))    


# Question 14:
# Write a function which will take length and breadth of two rectangles. Subtract the smaller rectangle from the larger rectangle and return the area left behind.
# 

# In[87]:


def ss(l,b,ll,bb):
    a=l*b
    aa=ll*bb
    if a>aa:
        fa=(aa-a)
    else:
        fa=(a-aa)
    return abs(fa) 
print(ss(6,8,4,10))


# Question 15:
# Create a function that can add the fractions in series such as 1 to 8 = 1/8+1/7+1/6+1/5 …… ½ and return the result in fraction not in decimal.
# 

# In[101]:


from fractions import Fraction
l-1
f-8
ff-0
for 11 in range (i,f):
    ff=ff+fraction(1,11)
print(ff)    


# Question 16:
# Write a function which will take height and base for a triangle and 
# 

# In[ ]:





# Question 17:
# Write a function which will take a list of fruits names. The function will return how many alphabets are repetitive in the names of fruits and how many are unique letters.
# 

# In[92]:


s='mango'
ss=""
nn=0
for i in s:
    n=s.count(i)
    if n>1:
        nn=nn+1
print('rep',nn)        


# Question 18:
# Write a function that can take square length and radius of circle. Find the area of both and subtract the smallest shape from largest one and return the remaining shape area.
# 

# In[93]:


def ss(l,r):
    sa=l*l
    ca=3.142*(r**2)
    print(sa)
    print(ca)
    if sa > ca:
        fa =(ca-sa)
    else:
        fa=(sa-ca)
    return abs(fa)
ss(8,8)


# In[ ]:




