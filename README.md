# Grid-Based Path Planning using A* Algorithm (Classical Approach)

## 📌 Project Overview
This project focuses on solving a grid-based path planning problem using the classical A* (A-star) algorithm.

The environment consists of a 2D grid with randomly placed obstacles, where the objective is to find the shortest path from a start point to a goal point.

This is the first phase of a larger system that will later integrate quantum-inspired optimization and AI-based explanation modules.

---

## 🎯 Objectives
- To understand and implement the A* path planning algorithm
- To simulate a grid-based environment with obstacles
- To evaluate algorithm performance using multiple runs
- To visualize path planning and explored nodes

---

## 🧠 A* Algorithm Overview

A* is a best-first search algorithm that finds the shortest path using:

- **g(n):** Cost from start node to current node  
- **h(n):** Heuristic estimate (Manhattan distance)  
- **f(n) = g(n) + h(n)**  

The algorithm always selects the node with the lowest f(n), ensuring optimal pathfinding when a solution exists.

---

## ⚙️ Features Implemented

- Grid-based environment (size configurable)
- Random obstacle generation
- A* shortest path planning
- Tracking explored nodes
- Multiple experiment runs
- JSON-based logging of results
- Visualization of path and search process

---

## 📊 Experimentation

The algorithm is executed over multiple runs with different obstacle configurations.

### Metrics Collected:
- Success rate (whether path was found)
- Path length (number of steps)
- Number of explored nodes

Logs are stored in:  
`astar_logs.json`

---

## 📈 Visualization

The output includes a graphical representation of:

- Black cells → Obstacles  
- Light blue cells → Explored nodes  
- Red line → Final path  
- S → Start  
- G → Goal  

---

## 📁 Project Structure

    classical/
        astar.py        # A* implementation with experiments and visualization

---

## ▶️ How to Run

    pip install numpy matplotlib
    python classical/astar.py

---

## 📌 Current Status

- ✅ Classical A* path planning implemented  
- ⬜ Quantum-inspired optimization (upcoming)  
- ⬜ LLM-based explanation module (planned)  
- ⬜ Docker containerization (planned)  

---

## 🚀 Future Work

- Integrate quantum-inspired decision module using Qiskit  
- Compare classical vs quantum approaches  
- Add AI-based explanation of results  
- Containerize the system using Docker  

---

## 👨‍💻 Author

Anant Jain
Viplav Kumar
Ehsaas Bhalla
