import streamlit as st
import numpy as np
from scipy.optimize import linprog

def linearprogramming():
    cc2,cc1,cc3=st.columns((2,6,2))
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
    with cc1:
    # Streamlit app
        st.title("Oil and Gas Linear Programming Solver")
        # st.markdown("<hr style=height:2.5px;margin-top:0px;background-color:gray;>",unsafe_allow_html=True)
        # Input parameters
        gasoline_profit = st.number_input("Profit per gallon of gasoline ($):", value=2)
        diesel_profit = st.number_input("Profit per gallon of diesel ($):", value=3)
        capacity_A = st.number_input("Capacity of Process A (gallons/day):", value=4000, step=100)
        capacity_B = st.number_input("Capacity of Process B (gallons/day):", value=6000, step=100)
        labor_hours = st.number_input("Total Available Labor Hours (hours/day):", value=8000, step=100)
    with cc1:
        if st.button("Find Optimal Solution"):
            # Solve the linear programming problem
            result = solve_linear_programming(gasoline_profit, diesel_profit, capacity_A, capacity_B, labor_hours)

            # Display the results
            st.subheader("Optimal Solution:")
            st.write(f"Production of Gasoline in Process A: {result.x[0]} gallons")
            st.write(f"Production of Gasoline in Process B: {result.x[1]} gallons")
            st.write(f"Production of Diesel in Process A: {result.x[2]} gallons")
            st.write(f"Production of Diesel in Process B: {result.x[3]} gallons")
            st.subheader("Maximum Daily Profit:")
            st.success(f"${-result.fun:.2f}")
