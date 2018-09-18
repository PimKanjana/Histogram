#!/usr/bin/env python
# coding: utf-8

# # Histogram

# ## 1. PNG 

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from PIL import Image

img1 = cv2.imread('testpic.png',0)
hist1,bins = np.histogram(img1.ravel(),256,[0,256])
print(hist1)


# In[2]:


plt.hist(img1.ravel(),256,[0,256]); 
plt.show()


# In[3]:


pic1 = plt.imshow(img1, 'gray')


# ## 2. BMP

# In[4]:


img2 = cv2.imread('testpic.bmp',0)
hist2,bins = np.histogram(img2.ravel(),256,[0,256])
print(hist2)


# In[5]:


plt.hist(img2.ravel(),256,[0,256]); 
plt.show()


# In[6]:


pic2 = plt.imshow(img2, 'gray')


# ## 3. JPEG

# In[7]:


img3 = cv2.imread('testpic.jpeg',0)
hist3,bins = np.histogram(img3.ravel(),256,[0,256])
print(hist3)


# In[8]:


plt.hist(img3.ravel(),256,[0,256]); 
plt.show()


# In[9]:


pic3 = plt.imshow(img3, 'gray')


# ## 4. TIFF

# In[10]:


img4 = cv2.imread('testpic.tiff',0)
hist4,bins = np.histogram(img4.ravel(),256,[0,256])
print(hist4)


# In[11]:


plt.hist(img4.ravel(),256,[0,256]); 
plt.show()


# In[12]:


pic4 = plt.imshow(img4, 'gray')


# In[13]:


plt.subplot(221); pic1 = plt.imshow(img1, 'gray') #png
plt.subplot(222); pic2 = plt.imshow(img2, 'gray') #bmp
plt.subplot(223); pic3 = plt.imshow(img3, 'gray') #jpg
plt.subplot(224); pic4 = plt.imshow(img4, 'gray') #tiff


# ## 5. GIF

# In[14]:


pic = Image.open('testpic.gif').convert('LA')
pic.save('newpic.gif', as_gray = True)
img5 = io.imread('newpic.gif')


# In[15]:


plt.hist(img5.ravel(),256,[0,256]); 
plt.show()


# In[16]:


pic5 = plt.imshow(img5, 'gray')


# # Histogram Equalization

# ## PNG Example

# In[17]:


img_ori = cv2.imread('testpic.png',0)
img_eq = cv2.equalizeHist(img_ori)

hist_ori,bins = np.histogram(img_ori.ravel(),256,[0,256])
print(hist_ori)


# In[18]:


hist_eq,bins = np.histogram(img_eq.ravel(),256,[0,256])
print(hist_eq)


# In[19]:


plt.hist(img_ori.ravel(),256,[0,256]); 
plt.show()


# In[20]:


plt.hist(img_eq.ravel(),256,[0,256]); 
plt.show()


# In[21]:


plt.subplot(121); plt.imshow(img_ori, 'gray')
plt.subplot(122); plt.imshow(img_eq, 'gray')
plt.show()


# In[ ]:




