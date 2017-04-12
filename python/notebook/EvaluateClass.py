
# coding: utf-8

# In[1]:

from functools import reduce
import math

class Evaluate:
    def average(self, scores):
        return reduce(lambda a, b: a + b, scores)/len(scores)
        
    def variance(self, scores, avrg):
        return reduce(lambda a, b: a + b, map(lambda s:(s-avrg)**2, scores))/len(scores)


# In[ ]:



