import streamlit as st

st.title("New Customer Registration")
with st.form("my_form"):
	customer_name= st.text_input("Customer Name","")
	customer_contact= st.text_input("Contact Number","")
	customer_email= st.text_input("Email ID","")
	customer_Address= st.text_input("Address","")
	customer_GSTIN= st.text_input("GSTIN","")
	customer_Job= st.text_input("Job Details","")
	st.form_submit_button('Submit Customer Detail')

