import numpy as np

def mask_and_classify_scores(arr):

    if type(arr) != np.ndarray:
        return None
    if len(arr.shape) != 2 or arr.shape[0] != arr.shape[1]:
        return None
    if arr.shape[0] < 4:
        return None
    
    fixed_scores = arr.copy()
    fixed_scores[fixed_scores < 0] = 0
    fixed_scores[fixed_scores > 100] = 100
    
    levels = np.zeros_like(fixed_scores, dtype=int)
    levels[(fixed_scores < 40)] = 0
    levels[(fixed_scores >=40) & (fixed_scores < 70)] = 1
    levels[(fixed_scores >= 70)] = 2
    n = fixed_scores.shape[0]
    pass_counts = np.zeros(n, dtype=int)
    for i in range(n):
        passed = 0
        for mark in fixed_scores[i]:
            if mark >= 50:
                passed += 1
        pass_counts[i] = passed
        
    return (fixed_scores, levels, pass_counts)

arr = np.array([
    [105, -5, 55, 40],
    [70, 10, 90, 120],
    [30, 50, 60, 80],
    [0, 100, 45, -20]
])

result = mask_and_classify_scores(arr)

print("Cleaned:\n", result[0])
print("Levels:\n", result[1])
print("Passing per row:", result[2])
