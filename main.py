import pandas as pd
import streamlit as st
import plotly.graph_objects as go

# load data base
df = pd.read_csv('Data/placement.csv')
# pre-processing
x_mean = df['cgpa'].mean()
y_mean = df['package'].mean()
package = 0
num = 0
den = 0

for i in range(df.shape[0]):
    num = num + (df['package'][i] - y_mean) * (df['cgpa'][i] - x_mean)
    den = den + (df['cgpa'][i] - x_mean) * (df['cgpa'][i] - x_mean)

# calculate m, b
m = num/den
b = y_mean - m*x_mean
# take input cgpa
name = st.number_input('cgpa')

package = m*name + b

st.title("Package")
st.header(package)

# graphs of data
st.header('Package of all data')
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=df['cgpa'], y=df['package'], mode='markers', name='Package'))
st.plotly_chart(fig2)
