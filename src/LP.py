import streamlit as st
import numpy as np
from scipy.optimize import linprog
import pandas as pd

def linearprogramming():
    w1,col1,col2,w2=st.columns((1.5,3,4,3))
    cc1,cc2,cc3 = st.columns((1.5,7,3))
    
    # Define the main function to solve the linear programming problem
    def solve_linear_programming(gasoline_profit, diesel_profit, capacity_A, capacity_B, labor_hours):
        
        # Objective function coefficients
        c = [-gasoline_profit, -gasoline_profit, -diesel_profit, -diesel_profit]

        # Coefficients matrix for inequalities (Ax <= b)
        A = [
            [1, 0, 2, 0],
            [0, 1, 0, 2],
            [1, 2, 0, 0],
            [0, 0, 1, 2]
        ]

        # Right-hand side of inequalities (Ax <= b)
        b = [capacity_A, capacity_B, labor_hours, labor_hours]

        # Variable bounds
        x_bounds = [(0, None), (0, None), (0, None), (0, None)]

        # Solve the linear programming problem
        result = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='highs')

        return result
    
    # Displaying first feature
    with col1:
        st.write("# ")
        st.markdown(f"<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>gasoline_profit</span></p>", unsafe_allow_html=True)
    with col2:
        feature1 = st.number_input("", value=2, key="Feature1")

    # Displaying second feature
    with col1:
        st.write("# ")
        st.markdown(f"<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>diesel_profit</span></p>", unsafe_allow_html=True)
    with col2:
        feature2 = st.number_input("", value=3, key="Feature2")

    # Displaying third feature
    with col1:
        st.write("# ")
        st.write("### ")
        st.markdown(f"<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>capacity_A</span></p>", unsafe_allow_html=True)
    with col2:
        feature3 = st.number_input("", value=4000, step=100, key="Feature3")

    # Displaying fourth feature
    with col1:
        st.write("# ")
        st.markdown(f"<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>capacity_B</span></p>", unsafe_allow_html=True)
    with col2:
        feature4 = st.number_input("", value=6000, step=100, key="Feature4")

    # Displaying fifth feature
    with col1:
        st.write("# ")
        st.markdown(f"<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>labor_hours</span></p>", unsafe_allow_html=True)
    with col2:
        feature5 = st.number_input("", value=8000, step=100, key="Feature5")
    with col2:
        st.write("# ")
        if st.button("Find Optimal Solution"):
            # Solve the linear programming problem
            result = solve_linear_programming(feature1,feature2,feature3,feature4,feature5)
            # Create a DataFrame with the results
            df = pd.DataFrame({
                'Process/Production': ['Gasoline in Process A', 'Gasoline in Process B', 'Diesel in Process A', 'Diesel in Process B', 'Maximum Daily Profit'],
                'Value': [f"{result.x[0]} gallons", f"{result.x[1]} gallons", f"{result.x[2]} gallons", f"{result.x[3]} gallons", f"${-result.fun:.2f}"]
            })
            with cc2:
                # Display the results as a table in Streamlit
                #st.subheader("Optimal Solution:")
                st.table(df)

