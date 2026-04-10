import streamlit as st
import numpy as np
from classical.astar import a_star

st.title("Quantum AI Path Planning")

if st.button("Run A* Algorithm"):

    # Create simple grid
    grid = np.zeros((10, 10))

    # Add sample obstacle
    grid[3, :] = 1
    grid[3, 5] = 0  # gap

    start = (0, 0)
    goal = (9, 9)

    path, explored = a_star(grid, start, goal)

    if path:
        st.success("Path found!")
        st.write("Path:", path)
        st.write("Path length:", len(path) - 1)
        st.write("Explored nodes:", len(explored))
    else:
        st.error("No path found!")