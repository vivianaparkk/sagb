import csv
filename = 'Lenn-4-6-7-6-1-6_-2025-10-01-at-18.48.36.xlsx-Shots.csv'
thresh = 6
approaches = []
lenn_rows = []

# Load CSV and filter for Lenn's shots
with open(filename, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        player = row['Player'].strip().lower()
        if 'lenn' in player:
            try:
                row['Hit (y)'] = float(row['Hit (y)'])
            except:
                row['Hit (y)'] = None
            lenn_rows.append(row)

# Track differences in Hit (y) for approach moves
for i in range(1, len(lenn_rows)):
    prev = lenn_rows[i - 1]
    curr = lenn_rows[i]
    if curr['Hit (y)'] is None or prev['Hit (y)'] is None:
        continue
    y_diff = abs(curr['Hit (y)'] - prev['Hit (y)'])
    if y_diff > thresh:
        approaches.append({'index': i, 'Shot': curr['Type'],
                          'y_diff': y_diff, 'current_y': curr['Hit (y)'],
                          'prev_y': prev['Hit (y)'], 'Direction': curr['Direction']})

# Approach type breakdown
approach_types = {}
for a in approaches:
    t = a['Shot']
    approach_types[t] = approach_types.get(t, 0) + 1

# Sample output
approach_summary = {
    'total_approaches': len(approaches),
    'approach_types': approach_types,
    'sample_approaches': approaches[:5]
}

print(approach_summary)

