#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1a
user_input0 = input('What day is it? ')
if user_input0 == 'Monday':
    print('True, today is Monday.')
else: print('Nope, today is Monday')


# In[ ]:


#1b
user_input1 = input('What day is it? ')
if user_input1 in ['Friday', 'Saturday']:
    print("It's the weekend!")
else:
    print("It's a weekday.")


# In[ ]:


#1c
hours_worked = 50.5
hourly_rate = 22
weekly_paycheck = (hours_worked * hourly_rate)
over_time_pay = (hours_worked - 40) * (hourly_rate * 1.5)
if hours_worked >= 40:
    print('The pay for this week is $', weekly_paycheck + over_time_pay)
else:
    print('The pay for this week is $', weekly_paycheck)


# In[ ]:


#2a
i = 5
while i <= 15:
    print(i)
    i = i + 1


# In[ ]:


i1 = 0
while i1 <= 100:
    print(i1)
    i1 = i1 + 2


# In[ ]:


i2 = 100
while i2 >= -10:
    print(i2)
    i2 = i2 - 5


# In[ ]:


i3 = 2
while i3 ** 2 < 1000000:
    print(i3 ** 2)
    i3 = i3 * i3


# In[ ]:


i4 = 100
while i4 > 0:
    print (i4)
    i4 = i4 - 5


# In[ ]:


#2bi
input_number = input('Enter a number: ')
for n in input_number:
    print(int(n), ' x ', 1, ' = ', int(n) * 1)
    print(n, ' x ', 2, ' = ', int(n) * 2)
    print(n, ' x ', 3, ' = ', int(n) * 3)
    print(n, ' x ', 4, ' = ', int(n) * 4)
    print(n, ' x ', 5, ' = ', int(n) * 5)
    print(n, ' x ', 6, ' = ', int(n) * 6)
    print(n, ' x ', 7, ' = ', int(n) * 7)
    print(n, ' x ', 8, ' = ', int(n) * 8)
    print(n, ' x ', 9, ' = ', int(n) * 9)
    print(n, ' x ', 10, ' = ', int(n) * 10)


# In[ ]:


#2bii
for n in range(1,10):
    print(str(n)*n)


# In[ ]:


#2c
print('Enter an odd number between 1 and 50: ')
while True:
    enter_the_odd = input()
    if enter_the_odd.isdigit() == False:
        print('Please enter a number')
        continue
    if int(enter_the_odd) in range(1, 50) and int(enter_the_odd) % 2 != 0:
        break
for n in range(1, 50):
    if n % 2 == 0:
        continue
    if n == int(enter_the_odd):
        print('Yikes, we gon skip this')
    else:
        print('Here is an odd number:', n)


# In[2]:


#2d
print('Enter a positive number ')
while True:
    pos_num = input()
    if pos_num.isdigit() == False:
        print('Please enter a number')
        continue
    if int(pos_num) > 0:
        break
for n in range(int(pos_num) + 1):
    print(n)


# In[ ]:


#2e
print('Enter a positive integer ')
while True:
    pos_int = input()
    if pos_int.isdigit() == False:
        print('Please enter a positive integer')
        continue
    if int(pos_int) > 0:
        break
n1 = int(pos_int) - 1
while n1 > 0:
    print(n1)
    n1 = n1 - 1


# In[1]:


#3
for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')
    elif n % 5 == 0:
        print('Buzz')
    elif n % 3 == 0:
        print('Fizz')
    else:
        print(n)


# In[6]:


#4
print('Enter an integer' )
while True:
    in_put = input()
    if in_put.isdigit() == False: #if it's not a number, keep prompting
        continue
    if int(in_put): #if it's a number, end prompt
        break

for n in range(1, int(in_put) + 1):
    print('number ', n, ' squared ', n ** 2, ' cubed ', n ** 3)

#assume user will enter valid data
while True:
    print('Continue? ')
    continue_i = input()
    if continue_i.isdigit() == False:
        break
    if int(continue_i):
        for n in range(1, int(continue_i) + 1):
            print('number ', n, ' squared ', n ** 2, ' cubed ', n ** 3)


# 

# In[5]:


#5
print('Enter a numerical grade ')
while True:
    user_grade = input()
    if user_grade.isdigit() == False:
        break
    if int(user_grade) in range(88, 101):
        print('A')
    if int(user_grade) in range(80, 88):
        print('B')
    if int(user_grade) in range(67, 80):
        print('C')
    if int(user_grade) in range(60, 67):
        print('D')
    if int(user_grade) in range(60):
        print('F')
    print('Continue? ')
    


# In[ ]:




