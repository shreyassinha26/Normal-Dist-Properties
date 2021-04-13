import csv
import pandas as pd
import plotly.figure_factory as pf
import statistics as st
filedata=pd.read_csv('txt/StudentsPerformance.csv')

arr=filedata['reading score']
mean=st.mean(arr)
median = st.median(arr)
mode=st.mode(arr)
std=st.stdev(arr)
rangeL1=mean-std
rangeH1=mean+std
arr2=[]
for i in arr:
    if(rangeL1<i<rangeH1):
        arr2.append(i)
print((len(arr2)*100)/len(arr))
rangeL1=mean-std-std
rangeH1=mean+std+std
arr2=[]
for i in arr:
    if(rangeL1<i<rangeH1):
        arr2.append(i)
print((len(arr2)*100)/len(arr))
rangeL1=mean-std-std-std
rangeH1=mean+std+std+std
arr2=[]
for i in arr:
    if(rangeL1<i<rangeH1):
        arr2.append(i)
print((len(arr2)*100)/len(arr))
