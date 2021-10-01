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
fruits_with_only_two_vowels = [fruit for fruit in fruits if sum(1 for x in fruit if x in 'aieou') == 2]


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


# In[10]:


#Exercise 9
fruits_with_letter_a = [fruit for fruit in fruits if any(x == 'a' for x in fruit)]


# In[11]:


#Exercise 10
even_numbers = [n for n in numbers if n % 2 == 0]


# In[13]:


#Exercise 11
odd_numbers = [n for n in numbers if n % 2 != 0]


# In[14]:


#Exercise 12
positive_numbers = [n for n in numbers if n > 0]


# In[15]:


#Exercise 13
negative_numbers = [n for n in numbers if n < 0]


# In[18]:


#Exercise 14
multiple_digits = [n for n in numbers if abs(n) > 9]


# In[19]:


#Exercise 15
numbers_squared = [n ** 2 for n in numbers]


# In[20]:


#Exercise 16
odd_negative_numbers = [n for n in numbers if n < 0 and n % 2 != 0]


# In[21]:


#Exercise 17
numbers_plus_5 = [n + 5 for n in numbers]


# In[ ]:




