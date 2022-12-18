import streamlit as st
import pandas as pd
import openpyxl
st.set_page_config(page_title="Andhra Pradesh Micro irrigation project Data", page_icon="-----", layout="wide")
st.title("Andhra Pradesh Micro irrigation project Data: Anantapuram " )
atp = pd.read_excel("Anantapur.xlsx")
st.write(atp)

print(atp.columns)
atp_pivot = atp.pivot_table(index="EMP", values=['Area', 'Boq Amount', 'Farmer Contribution'], aggfunc="sum", margins=True)
atp_pivot_month = atp.pivot_table(index="FC Paid Details", values='Farmer Contribution', aggfunc="sum", margins=True)
atp_pivot_mandal = atp.pivot_table(index="Mandal", values=['Boq Amount', 'Farmer Contribution'], aggfunc="sum", margins=True)
atp_material = atp[['EMP', 'Material', 'Invoice Done', 'Boq Amount']]
print(atp_material)
atp_pivot_material = atp_material.pivot_table(index='EMP', columns='Material', aggfunc="count")
atp_pivot_dealer = atp[['Dealer Name','Material', 'Boq Amount',]]
atp_pivot_dealer = atp_pivot_dealer.pivot_table(index='Dealer Name', columns='Material', aggfunc=['count', 'sum'],
                                                margins=True)
tab3, tab4, tab5, tab6, tab7 = st.tabs(['Employee', 'Mandal', 'FC with Transaction', 'Material Supply', 'Dealer Sale'])
with tab3:
    st.header("Employee")
    tab3.write(atp_pivot)
with tab4:
    st.header("Mandal")
    tab4.write(atp_pivot_mandal)
with tab5:
    st.header("FC with Transaction")
    tab5.write(atp_pivot_month)
with tab6:
    st.header("Material Supply")
    tab6.write(atp_pivot_material)
with tab7:
    st.header("Dealer Sale")
    tab7.write(atp_pivot_dealer)

