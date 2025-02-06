import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(st.secrets["gcp_service_account"], scope)
client = gspread.authorize(creds)

SHEET_NAME = "Sheet1"
sheet = client.open('Sheet1').sheet1

def save_contact_info(name,email,message):
    new_entry = [name,email,message]
    sheet.append_row(new_entry)

st.title("Data Dashboard")
st.subheader("Basic Analysis of your Data")

uploaded_file = st.file_uploader("Choose **CSV** data to upload:", type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    if df.columns[0] == 'Unnamed: 0':
        df.set_index(df.columns[0], inplace=True)

    st.subheader("Data Preview")
    st.write(df.head(10))

    st.subheader("Data Summary")
    st.write(df.describe())

    if 'cleaned_df' not in st.session_state:
        st.session_state.cleaned_df = df.copy()

    num = df.select_dtypes(exclude='object')
    cat = df.select_dtypes(include='object')

    num_null = num.isnull().sum()
    cat_null = cat.isnull().sum()

    st.write("Numeric Columns Null Count:")
    st.write(num_null)
    
    st.write("Categorical Columns Null Count:")
    st.write(cat_null)

    if st.button("Fill Null Values"):
        st.write('Filling missing values...')

        # Fill numeric columns with median
        for col in num.columns:
            if num_null[col] != 0:
                median_value = num[col].median()
                st.session_state.cleaned_df[col].fillna(median_value, inplace=True)

        # Fill categorical columns with mode
        for col in cat.columns:
            if cat_null[col] != 0:
                mode_value = cat[col].mode()[0]  # Most frequent value
                st.session_state.cleaned_df[col].fillna(mode_value, inplace=True)

        st.write("Updated Null Values Count:")
        st.write(st.session_state.cleaned_df.isnull().sum())

    st.subheader("Filter Data")
    columns = df.columns.to_list()
    selected_columns = st.selectbox("Choose column to filter by",columns)
    unique_values = df[selected_columns].unique()
    selected_values = st.selectbox("Choose value",unique_values)

    filtered_df = df[df[selected_columns] == selected_values]
    st.write(filtered_df)

    st.subheader('Group-by Data')
    category_column = st.selectbox("Choose Category",df.select_dtypes(include='object').columns)
    value_column = st.selectbox("Choose value", df.select_dtypes(exclude='object').columns)

    if category_column and value_column:
        grouped_df = df.groupby(category_column)[value_column].sum().reset_index()
        st.write("Total Value (SUM)", grouped_df)

        grouped_df = df.groupby(category_column)[value_column].mean().reset_index()
        st.write("Total Value (AVERAGE)", grouped_df)

        grouped_df = df.groupby(category_column)[value_column].count().reset_index()
        st.write("Total Value (COUNT)", grouped_df)

    st.subheader("Plot Bar Chart")
    x_column = st.selectbox("Select column for x-axis", columns)
    y_column = st.selectbox("Select value for y-axis", columns)

    chart_types = ['Bar Chart', 'Line Chart']

    selected_charts = st.multiselect("Choose any one chart type:", chart_types)

    if st.button('Plot Chart'):
        if 'Bar Chart' in selected_charts:
            st.subheader("Bar Chart Plot")
            st.bar_chart(df.set_index(x_column)[y_column])

        if 'Line Chart' in selected_charts:
            st.subheader("Line Chart Plot")
            st.line_chart(df.set_index(x_column)[y_column])

    cleaned_csv = st.session_state.cleaned_df.to_csv(index=False).encode('utf-8')


    st.write('cleaned of missing values')
    st.download_button(
        label="Download cleaned **CSV** file",
        data=cleaned_csv,
        file_name='cleaned_data.csv',
        mime='text/csv'
    )

else:
    st.write('Waiting for **CSV** file to upload...')


st.subheader("Contact me")

with st.form(key='contact_form'):
    name = st.text_input('Name')
    email = st.text_input('Email address')
    message = st.text_area('Message')

    submit_button = st.form_submit_button(label='Send Message')

    if submit_button:
        if name and email and message:
            save_contact_info(name, email, message)
            st.success("Thank you for reaching out! I will review your message soon")
        else:
            st.error("Please fill all the fields before submitting.")
