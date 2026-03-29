import pandas as pd

def compute_metrics(df, name):
    return {
        "Algorithm": name,
        "Success Rate": df['success'].mean(),
        "Avg Path Length": df[df['path_length'] > 0]['path_length'].mean(),
        "Avg Explored Nodes": df['explored_nodes'].mean()
    }

def get_metrics(astar_df, quantum_df):
    astar_metrics = compute_metrics(astar_df, "A*")
    quantum_metrics = compute_metrics(quantum_df, "Quantum")

    metrics_df = pd.DataFrame([astar_metrics, quantum_metrics])
    print(metrics_df)

    return metrics_df