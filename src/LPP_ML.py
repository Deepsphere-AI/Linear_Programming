import streamlit as st
from src.ML_processes import ML_methode
from src.LP import linearprogramming
def prev1():
    st.session_state['preview1']="No"
def prev2():
    st.session_state['preview2']="No"
def prev3():
    st.session_state['preview3']="No"

def LPP_ml():
    w1,col1,col2,w2=st.columns((1.5,3,4,3))
    cc2,cc1,cc3=st.columns((2,6,0.2))
    col11,col22,col33=st.columns((2,8,0.2))
    with col1:
        st.write("## ")
        st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Select Method</span></p>", unsafe_allow_html=True)
    with col2:
        vAR_app = ['Linear Programmimg','Machine Learning']
        vAR_input_methode = st.radio(' ',vAR_app,horizontal=True)

    if vAR_input_methode == 'Linear Programmimg':
        linearprogramming()
    elif vAR_input_methode == 'Machine Learning':
        ML_methode()
