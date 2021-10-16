#!/usr/bin/env python
# coding: utf-8

# In[ ]:


fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]


# In[ ]:


#Exercise 1
uppercased_fruits = [fruit.upper() for fruit in fruits]


# In[ ]:


#Exercise 2
capitalized_fruits = [fruit[0].upper() + fruit[1:] for fruit in fruits]


# In[ ]:


#Exercise 3
fruits_with_more_than_two_vowels = [fruit for fruit in fruits if sum(1 for x in fruit if x in 'aieou') > 2]


# In[ ]:


#Exercise 4
fruits_with_only_two_vowels = [fruit for fruit in fruits if sum(1 for x in fruit if x in 'aieou') == 2]


# In[ ]:


#Exercise 5
fruit_strings_with_more_than_five_characters = [fruit for fruit in fruits if sum(1 for x in fruit) > 5]


# In[ ]:


#Exercise 6
fruits_with_five_characters = [fruit for fruit in fruits if sum(1 for x in fruit) == 5]


# In[ ]:


#Exercise 7
fruits_with_less_than_five_characters = [fruit for fruit in fruits if sum(1 for x in fruit) < 5]


# In[ ]:


#Exercise 8
number_of_characters_in_fruits = [len(fruit) for fruit in fruits]


# In[ ]:


#Exercise 9
fruits_with_letter_a = [fruit for fruit in fruits if any(x == 'a' for x in fruit)]


# In[ ]:


#Exercise 10
even_numbers = [n for n in numbers if n % 2 == 0]


# In[ ]:


#Exercise 11
odd_numbers = [n for n in numbers if n % 2 != 0]


# In[ ]:


#Exercise 12
positive_numbers = [n for n in numbers if n > 0]


# In[ ]:


#Exercise 13
negative_numbers = [n for n in numbers if n < 0]


# In[ ]:


#Exercise 14
multiple_digits = [n for n in numbers if abs(n) > 9]


# In[ ]:


#Exercise 15
numbers_squared = [n ** 2 for n in numbers]


# In[ ]:


#Exercise 16
odd_negative_numbers = [n for n in numbers if n < 0 and n % 2 != 0]


# In[ ]:


#Exercise 17
numbers_plus_5 = [n + 5 for n in numbers]


# In[ ]:


#Bonus
import sympy as sp
primes = [n for n in numbers if sp.isprime(n)]
primes

