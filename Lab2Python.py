
# coding: utf-8

# In[1]:


import arcpy


# In[2]:


# set environment properties
arcpy.env.workspace= r"C:\HelsleyGIS\data\rrg_build.gdb"
arcpy.env.overwriteOutput = True 
# use dot notation to find correct tools, functions, properties, etc.


# In[3]:


featureList = arcpy.ListFeatureClasses()
print(featureList)


# In[4]:


# get list of feature classes in our database
# and print them to the screen
rasterList = arcpy.ListRasters()
print(rasterList)


# In[5]:


# location of output gdb: C:\HelsleyGIS\Lab02\output.gdb


# In[7]:


# vector clip of area of interest
arcpy.Clip_analysis ("ky_gnis_1808","area_of_interest",r"C:\HelsleyGIS\Lab02\output.gdb\gnis")


# In[12]:


arcpy.management.Clip("Landcover_2012_30m", "#", r"C:\HelsleyGIS\Lab02\output.gdb\Landcover_2012_30m_Clip", "area_of_interest", 255, "NONE", "NO_MAINTAIN_EXTENT")

