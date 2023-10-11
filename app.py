import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set the title of your Streamlit app
st.set_page_config(page_title="Data Viz App", page_icon=":chart_with_upwards_trend:")

# Streamlit app title
st.title('Data Visualization App')

# Upload a CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Display the data as a table
    st.subheader('Data Table:')
    st.write(df)

    # Create a bar chart based on the first two columns (assumes they are numeric)
    st.subheader('Bar Chart:')
    fig, ax = plt.subplots()
    ax.bar(df.iloc[:, 0], df.iloc[:, 1])
    st.pyplot(fig)

