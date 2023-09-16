import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def ML_methode():
    w1,col1,col2,w2=st.columns((1.5,3,4,3))
    cc2,cc1,cc3=st.columns((1.5,7,3))
    col11,col22,col33,col44=st.columns((1.5,3,4,3))

    with col1:
        st.write("# ")
        st.write("### ")
        st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Upload Dataset</span></p>", unsafe_allow_html=True)
    with col2:
        vAR_uploaded_file = st.file_uploader("", type="csv")
    if vAR_uploaded_file:
        data = pd.read_csv(vAR_uploaded_file)
        
        with cc1:
            st.write(data.head())
            # Splitting the data
            X = data.iloc[:, :-1]  # All columns except the last one
            y = data.iloc[:, -1]   # Only the last column
            
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            
            # Training the model
            model = LinearRegression()
            model.fit(X_train, y_train)

        columns = data.columns
        
        # Displaying first feature
        with col22:
            st.write("# ")
            st.write("# ")
            st.write("### ")
            st.markdown(f"<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>{columns[0]}</span></p>", unsafe_allow_html=True)
        with col33:
            st.write("# ")
            st.write(" ")
            feature1 = st.number_input("", step=1, key="Feature1")

        # Displaying second feature
        with col22:
            st.write("# ")
            st.markdown(f"<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>{columns[1]}</span></p>", unsafe_allow_html=True)
        with col33:
            feature2 = st.number_input("", step=1, key="Feature2")

        # Displaying third feature
        with col22:
            st.write("# ")
            st.markdown(f"<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>{columns[2]}</span></p>", unsafe_allow_html=True)
        with col33:
            feature3 = st.number_input("", step=1, key="Feature3")

        # Displaying fourth feature
        with col22:
            st.write("# ")
            st.write(" ")
            st.markdown(f"<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>{columns[3]}</span></p>", unsafe_allow_html=True)
        with col33:
            feature4 = st.number_input("", step=1, key="Feature4")

        # Displaying fifth feature
        with col22:
            st.write("# ")
            st.markdown(f"<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>{columns[4]}</span></p>", unsafe_allow_html=True)
        with col33:
            feature5 = st.number_input("", step=1, key="Feature5")

        # Displaying sixth feature
        with col22:
            st.write("# ")
            st.markdown(f"<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>{columns[5]}</span></p>", unsafe_allow_html=True)
        with col33:
            feature6 = st.number_input("", step=1, key="Feature6")

        # Displaying seventh feature
        with col22:
            st.write("# ")
            st.markdown(f"<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>{columns[6]}</span></p>", unsafe_allow_html=True)
        with col33:
            feature7 = st.number_input("", step=1, key="Feature7")

        # Displaying eighth feature
        with col22:
            st.write("# ")
            st.markdown(f"<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>{columns[7]}</span></p>", unsafe_allow_html=True)
        with col33:
            feature8 = st.number_input("", step=1, key="Feature8")

        # Displaying ninth feature
        with col22:
            st.write("# ")
            st.markdown(f"<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>{columns[8]}</span></p>", unsafe_allow_html=True)
        with col33:
            feature9 = st.number_input("", step=1, key="Feature9")

        # Create a list and append all the feature values
        input_features = [feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8, feature9]

        with col33:
            # When user clicks the 'Predict' button, make a prediction
            if st.button('Predict'):
                prediction = model.predict([input_features])
                st.success(f'Maximum Profit: {prediction[0]:.2f}')