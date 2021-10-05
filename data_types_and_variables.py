#!/usr/bin/env python
# coding: utf-8

# In[1]:


days_with_movies = {
    "The Little Mermaid": 3,
    "Brother Bear": 5,
    "Hercules": 1
}

price_per_day = 3
Total_price = (days_with_movies["The Little Mermaid"] + days_with_movies["Brother Bear"] + days_with_movies["Hercules"]) * price_per_day


# In[2]:


Total_price


# In[1]:


google = 400
amazon = 380
facebook = 350
hours_fb = 10
hours_google = 6
hours_amzn = 4
payment = hours_fb * facebook + hours_google * google + hours_amzn * amazon
print(payment)


# In[7]:


does_class_have_room = True
does_class_fit_in_schedule = True
can_be_enrolled = does_class_have_room and does_class_fit_in_schedule
print(can_be_enrolled)


# In[11]:


bought_more_than_2 = True or False
is_offer_to_date = True or False
is_customer_member = True or False
can_apply_offer = bought_more_than_2 or is_customer_member and is_offer_to_date


# In[12]:


can_apply_offer


# In[28]:


username = 'codeup'
password = 'notastrongpassword'
print(len(password) >= 5)
print(len(username) < 20)
print(username != password)
print(username[0] and username[-1] and password[0] and password[-1] not in ' ')


# In[27]:





# In[ ]:




