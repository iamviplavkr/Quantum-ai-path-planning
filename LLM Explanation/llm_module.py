from google import genai

client = genai.Client(api_key="AIzaSyBGmO_47TdwrsW-aC7hLqNS2F_R6fjOwss")

def generate_explanation(metrics_df):
    try:
        failure_info = ""
        try:
            failures = metrics_df[metrics_df["Success Rate"] < 1]
            if len(failures) > 0:
                failure_info = failures.to_string(index=False)
            else:
                failure_info = "No major failures observed."
        except:
            failure_info = "Failure analysis not available."

        prompt = f"""
        You are an advanced AI research assistant.

        Analyze the following experimental results from a Hybrid Classical–Quantum Path Planning system:

        {metrics_df.to_string(index=False)}

        Perform a COMPLETE analysis with the following sections:

        1. Beginner Explanation:
        - Explain results in very simple terms

        2. Technical Analysis:
        - Compare A* vs Quantum approach
        - Discuss determinism vs probabilistic behavior

        3. Key Observations:
        - Highlight important patterns

        4. Failure Analysis:
        - Analyze why failures occur
        - Data:
        {failure_info}

        5. Decision-Making Insight:
        - When should we use A* vs Quantum?

        6. Strength of Quantum Approach:

        7. Future Improvements:

        8. Table Comparison:
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        if hasattr(response, "text") and response.text:
            return response.text
        elif hasattr(response, "candidates") and response.candidates:
            return response.candidates[0].content.parts[0].text
        else:
            return "No response from Gemini."

    except Exception as e:
        return f"Error: {e}"


def ai_decision_system(obstacle_density):
    try:
        prompt = f"""
        You are an AI system selecting path planning algorithms.

        Given obstacle density = {obstacle_density},

        Choose:
        - A* OR Quantum

        Explain:
        - Why this choice
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return getattr(response, "text", "No response")

    except Exception as e:
        return str(e)


def analyze_specific_run(astar_df, quantum_df, i):
    try:
        a = astar_df.iloc[i]
        q = quantum_df.iloc[i]

        prompt = f"""
        Compare these runs:

        A*:
        Success: {a['success']}
        Path Length: {a['path_length']}
        Explored: {a['explored_nodes']}

        Quantum:
        Success: {q['success']}
        Path Length: {q['path_length']}
        Explored: {q['explored_nodes']}

        Explain:
        - Why results differ
        - Which is better here
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return getattr(response, "text", "No response")

    except Exception as e:
        return str(e)