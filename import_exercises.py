#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Exercise 1b
from function_exercises import calculate_tip
print(calculate_tip(.35, 20))


# In[ ]:


#Exercise 1c
from function_exercises import get_letter_grade as glg
glg(82)


# In[ ]:


#Exercise 2
import itertools as it


# In[ ]:


#Exercise 2a
z = it.permutations('abc123')
count = 0
for g in z:
    count +=1
count


# In[ ]:


#Exercise 2b
x = it.combinations('abcd', 2)
count = 0
for c in x:
    count +=1
count


# In[ ]:


#Exercise 2c
y = it.permutations('abcd', 2)
count = 0
for p in y:
    count += 1
count


# In[ ]:


#Exercise 3
import json
json.load(open('profiles.json'))


# In[ ]:


#Exercise 3i
profiles = json.load(open('profiles.json'))
profiles[0]
count = 0
for user in range(len(profiles)):
    count += 1
count


# In[ ]:


#Exercise 3ii
count = 0
for user in profiles:
    if user['isActive']:
        count += 1
count


# In[ ]:


#Exercise 3iii
count = 0
for users in profiles:
    if not users['isActive']:
        count += 1
count


# In[ ]:


#Exercise 3iv
from function_exercises import handle_commas as hc
grand_total = 0
for user in profiles:
    grand_total += hc(user['balance'])
grand_total


# In[ ]:


#Exercise 3v
grand_total = 0
for user in profiles:
    grand_total += hc(user['balance'])
avg = grand_total / len(profiles)
avg


# In[ ]:


#Exercise 3vi
lowest_balance = min(profiles, key = lambda user: user['balance'])
lowest_balance
lowest_balance['name']


# In[ ]:


#Exercise 3vii
highest_balance = max(profiles, key = lambda user: user['balance'])
highest_balance['name']


# In[ ]:


#Exercise 3viii & 3ix
fruits = []
for user in profiles:
    fruits += user['favoriteFruit']
if __name__ == '__main__':
    print(fruits)
strawberries = 0
apples = 0
bananas = 0
for user in profiles:
    if user['favoriteFruit'] == 'strawberry':
        strawberries += 1
    elif user['favoriteFruit'] == 'apple':
        apples += 1
    else:
        bananas += 1

fruit_comparison = {
    'strawberries': strawberries,
    'apples': apples,
    'bananas': bananas
}

max(fruit_comparison)
min(fruit_comparison)


# In[ ]:


#Exercise 3x
import re
from itertools import chain
def unread_messages(x):
    unread = []
    for user in profiles:
        unread.append(re.findall(r'\d+', user['greeting']))
    unread_int = list(chain.from_iterable(unread))
    for n in range(len(unread_int)):
        unread_int[n] = int(unread_int[n])
    return sum(unread_int)

if __name__ == '__main__':
    print(unread_messages(profiles))


#alternatively
def pull_number_from_a_string_with_one_number(string):
    number = ''
    for n in string:
        if n.isdigit():
            number += n
    return int(number)

def total_unread_messages(x):
    unread = []
    for user in x:
        unread.append(pull_number_from_a_string_with_one_number(user['greeting']))
    return sum(unread)

total_unread_messages(profiles)

