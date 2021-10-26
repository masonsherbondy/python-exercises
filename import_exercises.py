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
#How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

#product('abc', '123') gives 9 results: A1 A2 A3 B1 B2 B3 C1 C2 C3
#product('123', 'abc') also gives the same amount of results: 1A 2A 3A 1B 2B 3B 1C 2C 3C (these are mirror combos)
z = it.product('abc', '123')
#set a counter to zero
count = 0
#start a for loop to count all the items 
for g in z:
    #add 1 to the count for every item
    count +=1
#get twice the amount of the count to account for 'different ways to combine' (reversed order combinations/ mirror combos)
count * 2


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
if __name__ == '__main__':
    print(type(user['isActive']))
for user in profiles:
    if not user['isActive']:
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
avg_balance = round(grand_total / len(profiles), 2)
avg_balance


# In[ ]:


#Exercise 3vi
lowest_balance = min(profiles, key = lambda user: user['balance'])
lowest_balance
lowest_balance['name']


# In[ ]:


#Exercise 3vii
highest_balance = max(profiles, key = lambda user: user['balance'])
highest_balance
highest_balance['name']


# In[ ]:


#Exercise 3viii & 3ix
fruits = []
for user in profiles:
    fruits.append(user['favoriteFruit'])
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

fruit_counts = {
    'strawberries': strawberries,
    'apples': apples,
    'bananas': bananas
}

max(fruit_counts)
min(fruit_counts)


# In[ ]:


#alternatively for 3viii & 3ix
fruits = [user['favoriteFruit'] for user in profiles]

max(fruits, key = fruits.count)
min(fruits, key = fruits.count)


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
from mason_functions import pull_an_integer_from_a_string_with_one_integer as pin

def total_unread_messages(x):
    unread = [pin(user['greeting']) for user in x]
    return sum(unread)

total_unread_messages(profiles)

