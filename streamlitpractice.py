import streamlit as st
st.title("My first webapp")
criteria_annual_salary=50000
criteria_year_of_work=5
annual_salary=st.number_input("Please enter your annual salary: ")
year_of_work=st.number_input("Please enter year of work: ")
if st.button("submit"):
    if annual_salary>= criteria_annual_salary and year_of_work >criteria_year_of_work:
        st.write("congratulation, your application has accepted")
    else:
        st.write("Sorry,your application has rejected")