student_scores = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

scores = [x[1] for x in student_scores]
secMinScore = sorted(scores)[1]

result = []
for lst in student_scores:
    if lst[1]==sec_minScore:
        result.append(lst[0])
result
