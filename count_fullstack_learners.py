# Practice exercise: use fictional records; the skills listed do not establish a qualification.
def count_fullstack_learners(learner_skills):
    count = 0
    for skills in learner_skills.values():
        normalized = {s.lower() for s in skills}
        if {"html", "css", "python"}.issubset(normalized):
            count += 1
    return count
