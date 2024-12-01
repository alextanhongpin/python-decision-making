import itertools
import numpy as np

# Step 1: Define alternatives and criteria
alternatives = ["Alternative 1", "Alternative 2", "Alternative 3"]
criteria = ["Criterion 1", "Criterion 2", "Criterion 3"]

# Step 2: Generate pairwise comparisons
pairwise_comparisons = list(itertools.combinations(alternatives, 2))

# Step 3: Simulate ranking preferences for comparisons (e.g., user input or predefined)
# Here, we assume a user ranks Alternative 1 > Alternative 2, Alternative 2 > Alternative 3, etc.
# For simplicity, we use a dictionary to store these preferences
rankings = {
    ("Alternative 1", "Alternative 2"): 1,
    ("Alternative 1", "Alternative 3"): 1,
    ("Alternative 2", "Alternative 3"): 1,
    ("Alternative 2", "Alternative 1"): -1,
    ("Alternative 3", "Alternative 1"): -1,
    ("Alternative 3", "Alternative 2"): -1,
}

# Step 4: Calculate scores for each alternative
scores = {alternative: 0 for alternative in alternatives}
for (alt1, alt2), rank in rankings.items():
    scores[alt1] += rank
    scores[alt2] -= rank

# Step 5: Normalize scores to get final ranking
total_score = sum(scores.values())
normalized_scores = {alt: score / total_score for alt, score in scores.items()}

# Rank alternatives based on normalized scores
ranked_alternatives = sorted(
    normalized_scores, key=normalized_scores.__getitem__, reverse=True
)

print("Ranked Alternatives:", ranked_alternatives)
