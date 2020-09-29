#!/usr/bin/env python
# coding: utf-8

# In[1]:


st_lines = [line for line in open("star_trek.txt")]
eq_lines = [line.strip("\n") for line in open("The_Philosophy_of_Earthquakes_Natural_Religious.txt")]


# In[2]:


st_lines


# In[3]:


eq_words = [word for eq_lines in eq_lines for word in eq_lines.split()]


# In[4]:


eq_words


# In[5]:


import random


# In[89]:


random_eq_words = random.choices([x for x in eq_words if len(x) >= 5],k=6)


# In[90]:


random_eq_words


# In[91]:


for lineX, wordX in zip(st_lines, random_eq_words):
    print('',"".join([lineX.replace('\n'," "+wordX)]))


# In[ ]:




