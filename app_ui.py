import streamlit as st

st.title("Quantum AI Path Planning")

if st.button("Run A* Algorithm"):
    import classical.astar
    st.success("Algorithm executed successfully!")