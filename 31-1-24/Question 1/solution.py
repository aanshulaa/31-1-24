#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re

def sum_of_numbers(input_str):
    numbers = re.findall(r'\d+', input_str)  # Find all numeric substrings
    return sum(int(num) for num in numbers)

def sum_of_adjacent_digits(input_str):
    numbers = re.findall(r'\d+', input_str)  # Find all numeric substrings
    return sum(int(num) for num in numbers)

# Example usage:
input_str1 = "1abd23"
input_str2 = "Fa33ce1"
print(sum_of_numbers(input_str1))  # Output: 24
print(sum_of_adjacent_digits(input_str1))  # Output: 24
print(sum_of_numbers(input_str2))  # Output: 34
print(sum_of_adjacent_digits(input_str2))  # Output: 34


# In[ ]:




