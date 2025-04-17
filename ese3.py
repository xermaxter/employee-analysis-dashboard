import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

data = pd.read_csv(r"C:\Users\alphi\Downloads\archive (12)\whole data.csv")

st.set_page_config(layout="wide")

col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    st.image(r"C:\Users\alphi\Downloads\employee.jpg", width=130)  
with col2:
    st.markdown("<h1 style='text-align: center; color: White;'>Employee Dataset Analysis</h1>", unsafe_allow_html=True)

st.subheader("Data Summary")
st.write(data.describe(include='all'))

st.header("Visualize Employee Attributes")

numeric_cols = data.select_dtypes(include=['int64', 'float64']).columns.tolist()

st.subheader("Line Chart")
x_line = st.selectbox("Select X-axis column for line chart:", numeric_cols, key='x_line')
y_line = st.selectbox("Select Y-axis column for line chart:", numeric_cols, key='y_line')

if x_line and y_line:
    st.write(f"### Line Chart: {y_line} over {x_line}")
    line_c1, line_c2, line_c3 = st.columns([1, 2, 1])
    with line_c2:
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        ax2.plot(data[x_line], data[y_line], marker='o', linestyle='-')
        ax2.set_xlabel(x_line)
        ax2.set_ylabel(y_line)
        ax2.set_title(f"{y_line} over {x_line}")
        st.pyplot(fig2)

st.subheader("Histogram")
hist_col = st.selectbox("Select a column for histogram:", numeric_cols, key='hist_col')
bins = st.slider("Select number of bins:", min_value=5, max_value=50, value=20)

if hist_col:
    st.write(f"### Histogram of {hist_col}")
    hist_c1, hist_c2, hist_c3 = st.columns([1, 2, 1])
    with hist_c2:
        fig3, ax3 = plt.subplots(figsize=(6, 4))
        ax3.hist(data[hist_col], bins=bins, color='skyblue', edgecolor='black')
        ax3.set_xlabel(hist_col)
        ax3.set_ylabel("Frequency")
        ax3.set_title(f"Distribution of {hist_col}")
        st.pyplot(fig3)

st.header("Feedback Form")
st.write("Fill out the form below and click submit.")
with st.form("user_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.number_input("Age", min_value=18, max_value=100)
    feedback = st.text_area("Your feedback")
    submitted = st.form_submit_button("Submit")
if submitted:
    st.success("Form Submitted Successfully!")
    st.write(f"Name: {name}")
    st.write(f"Email: {email}")
    st.write(f"Age: {age}")
    st.write(f"Feedback: {feedback}")

st.markdown("---")
st.markdown("""
<div style='text-align: center;'>
    <p>Developed By</p>
    <p>Name: Shaina Doraiswamy<br>Enrollment Number: 24225026</p>
    <p>Name: Anurag Toppo<br>Enrollment Number: 24225046</p>
    <p>Name: Alphin Shybu<br>Enrollment Number: 24225047</p>
</div>
""", unsafe_allow_html=True)
