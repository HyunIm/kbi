import json

new_1cha = [
    {
        "id": "1차평가_new_25",
        "category": "1차평가",
        "source": "1차평가",
        "question": "단체해외연수경비 지급에 대한 설명 중 옳지 못한 것은?",
        "options": ["연수자 개인별 대리환전도 가능하다.", "필요외화소요경비확인서가 필요하다.", "송금 또는 휴대수출도 가능하다.", "거래외국환은행 지정대상이 아니다."],
        "answer": 0,
        "explanation": "개별환전은 금지되어 있음",
        "page": "1권 99-100, 22p"
    },
    {
        "id": "1차평가_new_26",
        "category": "1차평가",
        "source": "1차평가",
        "question": "현지금융신고 절차에 대한 설명 중 바른 내용인 것은?",
        "options": ["보증한도는 제한이 없다.", "계열사는 보증할 수 없다.", "해외사무소도 수혜 대상이다.", "한국은행 신고대상이다."],
        "answer": 0,
        "explanation": "현지금융의 보증한도는 제한이 없다.",
        "page": "1권 198-201p"
    },
    {
        "id": "1차평가_new_27",
        "category": "1차평가",
        "source": "1차평가",
        "question": "거주자인 일반기업의 채권 또는 채무를 비거주자의 채무 또는 채권과 상계하는 경우 실무상 신고등의 절차와 관련이 없는 사항인 것은?",
        "options": ["신고예외", "외국환은행신고", "한국은행신고", "관세청신고"],
        "answer": 3,
        "explanation": "상계업무는 위탁규정에서 관세청 신고대상은 없다.",
        "page": "1권 116-117p"
    },
    {
        "id": "1차평가_new_28",
        "category": "1차평가",
        "source": "1차평가",
        "question": "외국기업 국내지사의 영업기금 도입으로 인정할 수 있는 자금은?",
        "options": ["외국환신고(확인)필증을 교부받은 휴대수입된 자금", "본사에서 송금한 외화자금", "본사소속 외국지점에서 송금한 외화자금", "본사가 국내 예치한 원화자금"],
        "answer": 1,
        "explanation": "영업기금으로 인정되기 위해서는 반드시 본사로부터 지정거래은행앞 직접 송금한 외화자금에 한한다.",
        "page": "1권 252p"
    },
    {
        "id": "1차평가_new_29",
        "category": "1차평가",
        "source": "1차평가",
        "question": "정유회사의 단기외화자금 차입시 신고등의 절차로 틀린 내용인 것은?",
        "options": ["1년이하의 차입시 적용한다.", "외국환은행 신고대상이다.", "차입용도는 수입결제대금이다.", "중계무역인 경우도 허용된다."],
        "answer": 3,
        "explanation": "중계무역은 제외함",
        "page": "1권 158p"
    },
    {
        "id": "1차평가_new_30",
        "category": "1차평가",
        "source": "1차평가",
        "question": "지급등의 방법 규정에서 제3자 지급 시 신고예외에 해당하는 기준 금액은?",
        "options": ["미화 2천 불 이하", "미화 3천 불 이하", "미화 5천 불 이하", "미화 1만 불 이하"],
        "answer": 2,
        "explanation": "제3자지급등의 신고예외 금액은 미화5천불 이하이다.(2019.5.3개정)",
        "page": "1권 122p"
    },
    {
        "id": "1차평가_new_31",
        "category": "1차평가",
        "source": "1차평가",
        "question": "예금계정에서 다음 중 거주자계정 개설대상자인 자는?",
        "options": ["국민인 비거주자", "외국인 거주자 개인", "대한민국 재외공관직원", "외국영주권자인 거주자"],
        "answer": 3,
        "explanation": "외국영주권자는 국민이므로 국민인거주자는 거주자계정 개설 대상자이다.",
        "page": "1권 144, 15p"
    },
    {
        "id": "1차평가_new_32",
        "category": "1차평가",
        "source": "1차평가",
        "question": "외국환 매각실적이 없는 비거주자에게 재환전할 수 있는 한도는?",
        "options": ["미화 3천 불 이내", "미화 5천 불 이내", "미화 1만 불 이내", "미화 2만 불 이내"],
        "answer": 2,
        "explanation": "미화 1만 불까지 재환전이 가능하고 여권에 기재하여야 한다.",
        "page": "1권 83p"
    }
]

new_2cha = [
    {
        "id": "2차평가_new_27",
        "category": "2차평가",
        "source": "2차평가",
        "question": "외화수표 전면에 'non negotiable', 'Only payee's account', 'not Transferable' 등의 문구가 있으면 지시금지식으로 발행된 것으로 반드시 수취인으로부터 매입하도록 한다.",
        "options": ["O", "X"],
        "answer": 0,
        "explanation": "이런 문구가 수표면에 있다면 수취인인 본인만이 매입요청하는 것을 원칙으로 한다.",
        "page": "2권 123p"
    },
    {
        "id": "2차평가_new_28",
        "category": "2차평가",
        "source": "2차평가",
        "question": "외화수표 부도반환 사유 중 '불법수표' 항목에 해당하지 않는 것은?",
        "options": ["Forgery", "Counterfeit", "Mutilated", "Fraudulent"],
        "answer": 2,
        "explanation": "Mutilated' 는 훼손이나 오손된 수표를 말한다.",
        "page": "2권 183p"
    },
    {
        "id": "2차평가_new_29",
        "category": "2차평가",
        "source": "2차평가",
        "question": "타발송금 매입업무에서 외국환은행의 확인절차 제외대상인 경우로 옳지 못한 것은?",
        "options": ["미화 5만 불 이하인 경우", "환전영업자(환전상)인 경우", "지방자치단체인 경우", "주한외교관인 경우"],
        "answer": 0,
        "explanation": "미화 2만불 이하인 경우 제외 대상이다.",
        "page": "2권 62-63p"
    }
]

def add_items(content, marker, items):
    lines = content.split('\n')
    # find the end of the specified category
    insert_idx = -1
    in_category = False
    for i, line in enumerate(lines):
        if f'category: "{marker}"' in line:
            in_category = True
        if in_category and 'category: "' in line and f'category: "{marker}"' not in line:
            # We hit the next category, insert before the opening brace of this object
            for j in range(i-1, -1, -1):
                if lines[j].strip() == '},':
                    insert_idx = j + 1
                    break
            if insert_idx != -1:
                break
                
    # If we didn't find the next category, maybe it's the last one
    if insert_idx == -1 and in_category:
        for j in range(len(lines)-1, -1, -1):
            if lines[j].strip() == '];':
                insert_idx = j
                break

    if insert_idx != -1:
        # Build string to insert
        to_insert = []
        for item in items:
            item_str = json.dumps(item, ensure_ascii=False, indent=4)
            # fix indentation
            item_str = "  {\n" + "\n".join("    " + l for l in item_str.split('\n')[1:-1]) + "\n  },"
            to_insert.append(item_str)
        
        # fix the missing comma issue from before on the line before insertion
        if lines[insert_idx - 1].strip() == "}":
            lines[insert_idx - 1] += ","
            
        lines = lines[:insert_idx] + to_insert + lines[insert_idx:]
    
    return '\n'.join(lines)

with open('src/data/data.ts', 'r') as f:
    content = f.read()

content = add_items(content, "1차평가", new_1cha)
content = add_items(content, "2차평가", new_2cha)

# strip trailing comma of the very last item in the whole file
if content.rstrip().endswith("},\n];"):
    content = content.rstrip()[:-4] + "\n  }\n];\n"

with open('src/data/data.ts', 'w') as f:
    f.write(content)

