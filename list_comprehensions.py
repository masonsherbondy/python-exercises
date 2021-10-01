#!/usr/bin/env python
# coding: utf-8

# In[1]:


fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]


# In[2]:


#Exercise 1
uppercased_fruits = [fruit.upper() for fruit in fruits]


# In[3]:


#Exercise 2
capitalized_fruits = [fruit[0].upper() + fruit[1:] for fruit in fruits]


# In[4]:


#Exercise 3
fruits_with_more_than_two_vowels = [fruit for fruit in fruits if sum(1 for x in fruit if x in 'aieou') > 2]


# In[5]:


#Exercise 4
fruits_with_only_two_vowels = [fruit for fruit in fruits if sum(1 for x in fruit if x in 'aieou') ==2]


# In[6]:


#Exercise 5
fruit_strings_with_more_than_five_characters = [fruit for fruit in fruits if sum(1 for x in fruit) > 5]


# In[7]:


#Exercise 6
fruits_with_five_characters = [fruit for fruit in fruits if sum(1 for x in fruit) == 5]


# In[8]:


#Exercise 7
fruits_with_less_than_five_characters = [fruit for fruit in fruits if sum(1 for x in fruit) < 5]


# In[9]:


#Exercise 8
number_of_characters_in_fruits = [len(fruit) for fruit in fruits]


# In[ ]:


#Exercise 9

