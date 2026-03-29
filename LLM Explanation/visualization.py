import matplotlib.pyplot as plt
import seaborn as sns

def visualize(astar_df, quantum_df, metrics_df):

    # Path Length Distribution
    plt.figure()
    sns.histplot(astar_df['path_length'], kde=True, label="A*", bins=10)
    sns.histplot(quantum_df['path_length'], kde=True, label="Quantum", bins=10)
    plt.legend()
    plt.title("Path Length Distribution")
    plt.show()

    # Explored Nodes Distribution
    plt.figure()
    sns.boxplot(data=[astar_df['explored_nodes'], quantum_df['explored_nodes']])
    plt.xticks([0,1], ["A*", "Quantum"])
    plt.title("Explored Nodes Comparison (Boxplot)")
    plt.show()

    # Success Rate per Run
    plt.figure()
    plt.plot(astar_df['success'], label="A*", marker='o')
    plt.plot(quantum_df['success'], label="Quantum", marker='x')
    plt.legend()
    plt.title("Run-wise Success Comparison")
    plt.show()

    sns.set(style="whitegrid")

    # Success Rate
    plt.figure()
    sns.barplot(x="Algorithm", y="Success Rate", data=metrics_df)
    plt.title("Success Rate Comparison")
    plt.show()

    # Path Length
    plt.figure()
    sns.barplot(x="Algorithm", y="Avg Path Length", data=metrics_df)
    plt.title("Average Path Length")
    plt.show()

    # Explored Nodes
    plt.figure()
    sns.barplot(x="Algorithm", y="Avg Explored Nodes", data=metrics_df)
    plt.title("Explored Nodes Comparison")
    plt.show()