import numpy as np

# Step 1: Define the problem and criteria
decisions = ["Decision 1", "Decision 2", "Decision 3"]
criteria = ["Criterion 1", "Criterion 2", "Criterion 3"]

# Step 2: Construct pairwise comparison matrix for criteria
criteria_comparison = np.array([[1, 3, 1 / 2], [1 / 3, 1, 1 / 4], [2, 4, 1]])

# Step 3: Calculate the weight of each criterion
criteria_sum = criteria_comparison.sum(axis=0)
normalized_comparison = criteria_comparison / criteria_sum
criteria_weights = normalized_comparison.mean(axis=1)

# Step 4: Construct pairwise comparison matrices for decisions for each criterion
# Example matrices for each criterion
decision_comparisons = [
    np.array([[1, 1 / 2, 3], [2, 1, 4], [1 / 3, 1 / 4, 1]]),
    np.array([[1, 3, 1 / 2], [1 / 3, 1, 1 / 4], [2, 4, 1]]),
    np.array([[1, 1 / 2, 1 / 3], [2, 1, 1 / 4], [3, 4, 1]]),
]

# Calculate the scores for each decision
decision_scores = []
for comparison in decision_comparisons:
    decision_sum = comparison.sum(axis=0)
    normalized_decision = comparison / decision_sum
    decision_weights = normalized_decision.mean(axis=1)
    decision_scores.append(decision_weights)

# Convert decision scores to numpy array for matrix multiplication
decision_scores = np.array(decision_scores).T

# Step 5: Calculate the final score for each decision
final_scores = decision_scores @ criteria_weights

# Rank the decisions
ranking = np.argsort(-final_scores)
ranked_decisions = [decisions[i] for i in ranking]

print("Ranked Decisions:", ranked_decisions)
