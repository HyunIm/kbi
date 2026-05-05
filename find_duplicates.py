import re
from collections import defaultdict
import json

with open('src/data/data.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract all questions
# This regex looks for `question: "something",` or `question: 'something',`
# It might be tricky if questions have escaped quotes. 
# Better: Since it's valid JS/TS, let's use a simpler approach.
# Let's extract blocks representing objects.

questions_seen = defaultdict(list)

# We can find all lines starting with "question:" or '"question":'
lines = content.split('\n')
current_id = "UNKNOWN"
current_category = "UNKNOWN"

for line in lines:
    line_stripped = line.strip()
    if line_stripped.startswith('id:') or line_stripped.startswith('"id":'):
        current_id = line_stripped.split(':')[1].strip().strip('",').strip("',")
    if line_stripped.startswith('category:') or line_stripped.startswith('"category":'):
        current_category = line_stripped.split(':')[1].strip().strip('",').strip("',")
        
    if line_stripped.startswith('question:') or line_stripped.startswith('"question":'):
        # Extract the question text
        # It's between the first quote and the last quote before comma
        first_quote_idx = line.find('"')
        if first_quote_idx == -1:
            first_quote_idx = line.find("'")
            
        last_quote_idx = line.rfind('"')
        if last_quote_idx == first_quote_idx or last_quote_idx == -1:
            last_quote_idx = line.rfind("'")
            
        if first_quote_idx != -1 and last_quote_idx != -1 and first_quote_idx != last_quote_idx:
            q_text = line[first_quote_idx+1:last_quote_idx].strip()
            
            # Normalize for better matching (remove spaces)
            q_norm = re.sub(r'\s+', '', q_text)
            
            questions_seen[q_norm].append({
                "id": current_id,
                "category": current_category,
                "text": q_text
            })

duplicates = {k: v for k, v in questions_seen.items() if len(v) > 1}

print(f"Total unique questions: {len(questions_seen)}")
if len(duplicates) == 0:
    print("No duplicates found!")
else:
    print(f"Found {len(duplicates)} duplicate questions:")
    for k, v in duplicates.items():
        print("-" * 40)
        print(f"Normalized text: {k[:50]}...")
        for item in v:
            print(f"  ID: {item['id']}, Category: {item['category']}")
            print(f"  Text: {item['text']}")
