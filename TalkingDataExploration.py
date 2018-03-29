
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import os 
from matplotlib import pyplot as plt


# In[3]:

#os.chdir("C:\\Users\\test\\Desktop\\Nicola\\Talking data")
os.getcwd()


# In[4]:

data = pd.read_csv("data/train_sample.csv")
data.head()


# In[5]:

print("Numero totale IP: "+str(len(data.ip.unique())))
print("Numero totale APP: "+str(len(data.app.unique())))
print("Numero totale DEVICE: "+str(len(data.device.unique())))
print("Numero totale OS: "+str(len(data.os.unique())))
print("Numero totale CHANNEL: "+str(len(data.channel.unique())))
print("Intervallo rilevazione: "+str(min(data.click_time)+" - "+str(max(data.click_time))))


# In[6]:

def exploreCategoricalVariable(var):
    print("median = "+str(var.value_counts().median()))
    print(var.value_counts().describe())
    bins = np.arange(1,max(var.value_counts())+20,1)
    plt.figure(1)
    plt.figure(figsize=(15,7))
    plt.subplot(121)
    plt.hist(var.value_counts(),bins)
    plt.xscale("log",nonposy='clip')
    plt.yscale("log",nonposy='clip')


    plt.subplot(122)
    plt.boxplot(list(var.value_counts()))
    plt.xscale("log",nonposy='clip')
    plt.yscale("log",nonposy='clip')
    plt.show()


# In[7]:

exploreCategoricalVariable(data.ip)


# In[ ]:

exploreCategoricalVariable(data.app)


# In[ ]:

exploreCategoricalVariable(data.device)


# In[ ]:

exploreCategoricalVariable(data.os)


# In[ ]:

exploreCategoricalVariable(data.channel)


# In[ ]:



