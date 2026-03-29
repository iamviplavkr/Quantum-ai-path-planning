# 🚀 Hybrid Classical–Quantum Path Planning System

## 📌 Overview
This project implements a Hybrid Path Planning System that compares a classical algorithm (A*) with a quantum-inspired probabilistic approach in a 2D grid environment.

The system integrates:
- Data analysis and visualization  
- LLM-based reasoning using Google Gemini  
- AI-based decision making  
- Automated PDF report generation  

---

## 🎯 Objectives
- Implement and evaluate A* path planning  
- Explore quantum-inspired probabilistic navigation  
- Compare both approaches using performance metrics  
- Integrate LLM for explanation and reasoning  
- Generate a complete analytical report automatically  

---

## 🧠 System Architecture

project/
│
├── data_loader.py        # Load JSON logs  
├── preprocessing.py      # Clean and normalize data  
├── metrics.py            # Compute performance metrics  
├── visualization.py      # Generate plots and graphs  
├── llm_module.py         # Gemini-based AI reasoning  
├── pdf_report.py         # Generate PDF report  
├── app.py                # Main execution file  
├── requirements.txt      # Dependencies  
│
├── astar_logs.json  
├── quantum_path_logs.json  

---

## ⚙️ How the System Works

### 1. Data Loading
- Reads experiment logs from:
  - astar_logs.json  
  - quantum_path_logs.json  

### 2. Preprocessing
- Handles missing values  
- Standardizes column names  
- Converts data into usable format  

### 3. Metrics Computation
Calculates:
- Success Rate  
- Average Path Length  
- Average Explored Nodes  

### 4. Visualization
Generates:
- Path length distribution  
- Explored nodes comparison  
- Success rate trends  
- Bar charts for metrics  

### 5. LLM Integration
Using Google Gemini API, the system performs:
- Multi-level explanation  
- Failure analysis  
- Algorithm comparison  
- AI-based decision making  
- Per-run analysis  

### 6. PDF Report Generation
Automatically creates:

Hybrid_AI_Report.pdf containing:
- Metrics summary  
- Graphs  
- LLM-generated insights  
- Decision analysis  

---

## 🚀 How to Run the Project

### 1. Clone / Download Repository
git clone <your-repo-link>  
cd project  

### 2. Install Dependencies
pip install -r requirements.txt  

### 3. Add Your Gemini API Key
In llm_module.py, replace:
client = genai.Client(api_key="YOUR_API_KEY")

### 4. Place Input Files
Ensure these files are in the project folder:
- astar_logs.json  
- quantum_path_logs.json  

### 5. Run the Project
python app.py  

---

## 📊 Output
After execution, the system will:
- Display visualizations  
- Generate AI explanations  
- Create a PDF report  

Output file:
Hybrid_AI_Report.pdf  

---

## 🧠 Key Features
- Classical vs Quantum comparison  
- Probabilistic vs deterministic analysis  
- AI-powered explanation system  
- Automated reporting pipeline  
- Modular and scalable architecture  

---

## 💡 Technologies Used
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- ReportLab  
- Google Gemini API  

---

## 🔮 Future Improvements
- Streamlit dashboard for UI  
- Interactive visual analytics  
- LLM-based adaptive algorithm selection  
- Docker containerization  
- Real-time simulation  

---

## 👨‍💻 Authors
- Anant Jain  
- Viplav Kumar  
- Ehsaas Bhalla  

---

## 📌 Conclusion
This project demonstrates how classical algorithms, quantum-inspired methods, and modern LLMs can be combined to create an intelligent, explainable, and adaptive path planning system.