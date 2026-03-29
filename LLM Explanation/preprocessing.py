def preprocess(astar_df, quantum_df):

    quantum_df = quantum_df.rename(columns={
        "quantum_success": "success",
        "quantum_path_length": "path_length",
        "quantum_explored_nodes": "explored_nodes"
    })

    astar_df['path_length'] = astar_df['path_length'].fillna(0)
    quantum_df['path_length'] = quantum_df['path_length'].fillna(0)

    astar_df['explored_nodes'] = astar_df['explored_nodes'].fillna(0)
    quantum_df['explored_nodes'] = quantum_df['explored_nodes'].fillna(0)

    astar_df['success'] = astar_df['success'].astype(int)
    quantum_df['success'] = quantum_df['success'].astype(int)

    return astar_df, quantum_df