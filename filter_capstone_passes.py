# Practice exercise: 75 is an illustrative threshold, not an official pass rule.
def filter_capstone_passes(scores):
    return [s for s in scores if isinstance(s, (int, float)) and 0 <= s <= 100 and s >= 75]
