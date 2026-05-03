import fitz
import glob
import re
import json

# 1. Read existing questions to avoid duplicates
existing_questions = set()
with open("src/data/data.ts", "r") as f:
    content = f.read()
    # basic regex to find question: "..."
    import re
    matches = re.findall(r'question:\s*"([^"]+)"', content)
    for m in matches:
        # normalize
        norm = re.sub(r'\s+', '', m)
        existing_questions.add(norm)

def normalize(text):
    return re.sub(r'\s+', '', text)

all_new_1 = []
all_new_2 = []

for filepath in glob.glob("pdfs/*.pdf"):
    if "1차" in filepath or "1차" in filepath:
        category = "1차평가"
    elif "2차" in filepath or "2차" in filepath:
        category = "2차평가"
    else:
        continue

    doc = fitz.open(filepath)
    text = ""
    for page in doc:
        text += page.get_text()
    
    # Extract questions
    # Format usually: 1. [진위형] ... \n 정답 : 1 \n 문제해설 : ... \n 출제원 : ...
    # Wait, the number could be "1." or "1..". "정답 : 1" or "정답.:.1"
    
    # We can split by something that always appears, e.g. "정답 :" or "정답.:."
    # Let's find all questions using regex.
    # Pattern: (?P<num>\d+)\.\.?(?P<type>\[[^\]]+\])\.?\s*(?P<qtext>.*?)(?=채점/득점)
    q_pattern = re.compile(r'(\d+)\.\.?\s*(\[[^\]]+\])\.?\s*(.*?)(?=\n채점/득점|\r\n채점/득점)', re.DOTALL)
    
    # Pattern for answer: 정답\s*\.?\s*:\s*\.?\s*(\d+)
    a_pattern = re.compile(r'정답\s*\.?\s*:\s*\.?\s*(\d+)')
    
    # Pattern for explanation: 문제해설\s*\.?\s*:\s*\.?\s*(.*?)(?=\n출제원|\r\n출제원)', re.DOTALL)
    e_pattern = re.compile(r'문제해설\s*\.?\s*:\s*\.?\s*(.*?)(?=\n출제원|\r\n출제원)', re.DOTALL)
    
    # Pattern for page: 출제원\s*\.?\s*:\s*\.?\s*(.*?)(?=\n\d+\.\.?\s*\[|\n닫기|\nO\s|\nO\*|\n기수명)', re.DOTALL)
    p_pattern = re.compile(r'출제원\s*\.?\s*:\s*\.?\s*(.*?)(?=\n\d+\.\.?\s*\[|\n닫기|\nKB|\nO\s|\nO\*|\n기수명)', re.DOTALL)

    questions = []
    
    # Split text by questions roughly
    parts = re.split(r'\n(?=\d+\.\.?\s*\[)', text)
    if len(parts) == 1:
        parts = re.split(r'\n(?=\d+\.\s*\[)', text)

    for part in parts:
        q_match = re.search(r'^(\d+)\.\.?\s*(\[[^\]]+\])\.?\s*(.*?)(?=\n채점/득점|\nO\*/|\nX\*/|\nO /|\nX /)', part, re.DOTALL)
        if not q_match:
            continue
            
        q_num = q_match.group(1)
        q_type = q_match.group(2).replace('.', '')
        q_text = q_match.group(3).replace('\n', '').strip()
        
        a_match = re.search(r'정답\s*\.?\s*:\s*\.?\s*(\d+)', part)
        ans = a_match.group(1) if a_match else "1"
        
        e_match = re.search(r'문제해설\s*\.?\s*:\s*\.?\s*(.*?)(?=\n출제원)', part, re.DOTALL)
        exp = e_match.group(1).replace('\n', ' ').strip() if e_match else ""
        
        p_match = re.search(r'출제원\s*\.?\s*:\s*\.?\s*(.*?)$', part, re.DOTALL)
        pg = p_match.group(1).replace('\n', '').strip() if p_match else ""
        
        questions.append({
            "type": q_type,
            "question": q_text,
            "answer": int(ans) - 1, # 0-indexed
            "explanation": exp,
            "page": pg
        })
        
    # Now extract options
    # The options are at the very end of the text, after "닫기" or similar, or just a long list of lines.
    # Let's find the block of text after the last "출제원 : ...".
    last_idx = text.rfind('출제원')
    if last_idx != -1:
        # find the end of that line
        end_of_line = text.find('\n', last_idx)
        options_text = text[end_of_line:]
        # Remove "닫기", "KB직무필수", "1차평가", names, "기수명", "기수", "평가명", "이름"
        clean_lines = []
        for line in options_text.split('\n'):
            line = line.strip()
            if not line: continue
            if line in ['닫기', '기수명', '기수', '평가명', '이름']: continue
            if 'KB직무필수' in line: continue
            if '1차평가' in line or '2차평가' in line: continue
            if line in ['신소은', '심태영', '이소진', '조윤행', '임현']: continue
            
            clean_lines.append(line)
            
        # Distribute clean_lines to questions
        opt_idx = 0
        for q in questions:
            num_opts = 2 if '진위형' in q['type'] else 4
            q['options'] = clean_lines[opt_idx : opt_idx + num_opts]
            opt_idx += num_opts
            
            # If options are O, X normalize them
            if '진위형' in q['type']:
                q['options'] = ['O', 'X']

            # Clean question text if it starts with [진위형] etc
            if q['question'].startswith('['):
                q['question'] = re.sub(r'^\[.*?\]\s*', '', q['question'])
                
            # Filter duplicates
            norm_q = normalize(q['question'])
            if norm_q not in existing_questions:
                existing_questions.add(norm_q)
                if category == "1차평가":
                    all_new_1.append(q)
                else:
                    all_new_2.append(q)

print(json.dumps({"1": all_new_1, "2": all_new_2}, ensure_ascii=False))

