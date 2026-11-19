def get_top_scorers(scores):
    passed = []
    for score in scores:
        if 0 <= score <= 100 and score >= 70:
            passed.append(score)
    return passed
