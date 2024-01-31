#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def find_largest_plot(N, houses):
  
    houses.sort(key=lambda x: x[1])
    
    max_plot = 0
    house1 = 0
    house2 = 0
    
   
    for i in range(1, N):
        plot_size = houses[i][1] - houses[i-1][1]
        if plot_size > max_plot:
            max_plot = plot_size
            house1 = houses[i-1][0]
            house2 = houses[i][0]
    
    return house1, house2


N = int(input())
houses = []
for _ in range(N):
    house_num, pos = map(int, input().split())
    houses.append((house_num, pos))


house1, house2 = find_largest_plot(N, houses)


print(house1, house2)


# In[ ]:




