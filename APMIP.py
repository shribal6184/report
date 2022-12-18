import streamlit as st
import pandas as pd
import openpyxl

st.set_page_config(
    page_title="Reports",
    page_icon="$$$"
)
st.title("MIS Reports")
st.sidebar.success("Select Page below for District wise Report")
st.title("Andhra Pradesh  and Telangana Sales")

sales = pd.read_excel("AP Sales upto 161222.xlsx")
print(sales.columns)

sales_pivot = sales[['district_desc', 'state_desc', 'book_amt', 'yyyymm']]
sales_pivot = sales.pivot_table(index="state_desc", values=['book_amt', 'district_desc'], aggfunc="sum", sort=True,
                                margins_name="All", margins=True)
print(sales_pivot)
sales_pivot_dis = sales.pivot_table(index=["state_desc", "district_desc"], values='book_amt', aggfunc="sum",
                                    margins=True, margins_name="All")
print(sales_pivot_dis)
print(sales_pivot)
col1, col2 = st.columns([2,2])
with col1:
    st.subheader("State wise Total Sales")
    st.write(sales_pivot)
with col2:
    st.subheader("District wise total Sales")
    st.write(sales_pivot_dis)
