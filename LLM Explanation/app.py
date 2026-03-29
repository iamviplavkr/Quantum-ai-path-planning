from data_loader import load_data
from preprocessing import preprocess
from metrics import get_metrics
from visualization import visualize
from llm_module import generate_explanation, ai_decision_system, analyze_specific_run
from pdf_report import generate_pdf

def main():
    astar_df, quantum_df = load_data()

    astar_df, quantum_df = preprocess(astar_df, quantum_df)

    metrics_df = get_metrics(astar_df, quantum_df)

    visualize(astar_df, quantum_df, metrics_df)

    explanation = generate_explanation(metrics_df)
    decision = ai_decision_system(0.25)
    run_analysis = analyze_specific_run(astar_df, quantum_df, 0)

    generate_pdf(metrics_df, explanation, decision, run_analysis)

    print("Done")

if __name__ == "__main__":
    main()