#!/usr/bin/env python
# coding: utf-8

# In[10]:


days_with_movies = {
    "The Little Mermaid": 3,
    "Brother Bear": 5,
    "Hercules": 1
}

price_per_day = 3
Total_price = (days_with_movies["The Little Mermaid"] + days_with_movies["Brother Bear"] + days_with_movies["Hercules"]) * price_per_day
Total_price


# In[12]:


google_rate = 400
amazon_rate = 380
facebook_rate = 350
hrs_fb = 10
hrs_google = 6
hrs_amzn = 4
payment = hrs_fb * facebook_rate + hrs_google * google_rate + hrs_amzn * amazon_rate
payment


# In[7]:


does_class_have_room = True
does_class_fit_in_schedule = True
can_be_enrolled = does_class_have_room and does_class_fit_in_schedule
can_be_enrolled


# In[8]:


bought_more_than_2 = True or False
is_offer_to_date = True or False
is_customer_member = True or False
can_apply_offer = bought_more_than_2 or is_customer_member and is_offer_to_date
can_apply_offer


# In[11]:


username = 'codeup'
password = 'notastrongpassword'
password_is_good = len(password) >= 5
username_good = len(username) <= 20
pass_no_misma_user = username != password
no_capes = username[0] and username[-1] and password[0] and password[-1] not in ' '
conditions_are_met = password_is_good and username_good and pass_no_misma_user and no_capes
conditions_are_met

