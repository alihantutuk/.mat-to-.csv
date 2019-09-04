import scipy.io
import numpy as np
import pandas as pd
import csv

mat = scipy.io.loadmat(r'C:\Users\Desktop\qq.mat') #path and file name may change

listValues=list()
datanames=list()
for i in mat.keys():
    datanames.append(i)
    listValues.append(mat[i])

listValues=listValues[3:]
datanames=datanames[3:]


del mat['_globals_']
del mat['_header_']
del mat['_version_']
    
   
Datas=list()  
for i in mat.values():
    for j in i:
        Datas.append(j[0]['data'])

df=pd.DataFrame(Datas[0],columns=[datanames[0]])
for i in range(1,186):
    df2=pd.DataFrame(Datas[i],columns=[datanames[i]])
    df=pd.concat([df,df2],axis=1)

df.to_csv('qq.csv',index=False)  # file name may change
