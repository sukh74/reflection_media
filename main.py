import streamlit as st
st.title("Refelection Media")
def page2():
    st.title("Second page")

pg = st.navigation([
    st.Page("customer.py", title="Customer"),
    st.Page("job.py", title="Create Job"),
    st.Page("allotment.py", title="Allotment"),
])
pg.run()
