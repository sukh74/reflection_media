import streamlit as st

tab_video, tab_Album = st.tabs(["Video", "Audio"])

with tab_video:
	st.header("Video Job")
	option_event_cnt = st.selectbox('Number of Events',(1,2,3,4,5,6,7,8,9,10))
	col_sl,col_particular,col_camera_count,col_dron,col_event,col_date,col_book_date,col_delivery_date=st.columns(8,gap="small", vertical_alignment="top")
	with col_sl:
		st.text("sl")
	with col_particular:
		st.text("Particulars")
	with col_camera_count:
		st.text("No of camera’s used")
	with col_dron:
		st.text("Dron Camera")
	with col_event:
		st.text("Title of the event")
	with col_date:
		st.text("Event Date")
	with col_book_date:
		st.text("Date of booking job")

	with col_delivery_date:
		st.text("Date of Delivery")

	with col_sl:
		for num in range(1, option_event_cnt+1):
			st.text(num)


