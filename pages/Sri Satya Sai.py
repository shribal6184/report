import streamlit as st
import pandas as pd
import openpyxl
st.set_page_config(page_title="Andhra Pradesh Micro irrigation project Data", page_icon="-----", layout="wide")
st.title("Andhra Pradesh Micro irrigation project Data:     Sri Satya Sai" )
apmip2 = pd.read_excel("SSAI Data.xlsx")
st.write(apmip2)

print(apmip2.columns)
apmip2_pivot = apmip2.pivot_table(index="EMP", values=['Area', 'Boq Amount', 'Farmer Contribution'], aggfunc="sum")
apmip2_pivot_month = apmip2.pivot_table(index="FC Paid Details", values='Farmer Contribution', aggfunc="sum")
apmip2_pivot_mandal = apmip2.pivot_table(index="Mandal", values=['Boq Amount', 'Farmer Contribution'], aggfunc="sum")
apmip2_material = apmip2[['EMP', 'Material', 'Final Invoice', 'Boq Amount']]
print(apmip2_material)
apmip2_pivot_material = apmip2_material.pivot_table(index='EMP', columns='Material', aggfunc="count")
apmip2_pivot_dealer = apmip2[[' Dealer Name','Material', 'Boq Amount',]]
apmip2_pivot_dealer = apmip2_pivot_dealer.pivot_table(index=' Dealer Name', columns='Material', aggfunc="sum")
tab3, tab4, tab5, tab6, tab7 = st.tabs(['Employee', 'Mandal', 'FC with Transaction', 'Material Supply', 'Dealer Sale'])
with tab3:
    st.header("Employee")
    tab3.write(apmip2_pivot)
with tab4:
    st.header("Mandal")
    tab4.write(apmip2_pivot_mandal)
with tab5:
    st.header("FC with Transaction")
    tab5.write(apmip2_pivot_month)
with tab6:
    st.header("Material Supply")
    tab6.write(apmip2_pivot_material)
with tab7:
    st.header("Dealer Sale")
    tab7.write(apmip2_pivot_dealer)

