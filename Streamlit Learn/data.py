import streamlit as st
import pandas as pd 
import numpy as np

import time

st.title('Hello Codex Coder Chapter 2')
st.text('in this Chapter we deal with data and how to present the data')

arr = [1,2,3,4,5,6,7,8]
n = np.array(arr)
nd = n.reshape((2,4))

mydic = {'Name':['Codex Coder','Coder','Prince Singh'],
         'City':['indore','Pithampure','Sagore'],
         'Marks':[98,992,100]}

data = pd.read_csv('Salary_Data.csv')
print(data)

st.dataframe(arr)
st.dataframe(n)
st.dataframe(mydic)
st.dataframe(data,width=700,height=700)



# if data is not large
st.table(data)

# for printing the dic as itis dasta 
st.json(mydic)

st.write(data)

# if we want to skip the function or cashig hwo to work

@st.cache
def realTime(a):
    time.sleep(5)
    return time.time()

if st.checkbox('1'):
    st.write(realTime(1))

if st.checkbox('2'):
    st.write(realTime(2))