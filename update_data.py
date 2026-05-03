import json

new_1cha = [
    {
        "id": "1차평가_new_1",
        "category": "1차평가",
        "source": "1차평가",
        "question": "외국기업 국내지사의 영업기금은 반드시 본사로부터 직접 지정거래외국환은행앞으로 송금되어야 하므로 타행으로 송금되어 온 경우 인정할 수 없다.",
        "options": ["O", "X"],
        "answer": 0,
        "explanation": "외국기업 국내지사의 영업기금은 반드시 본사로부터 지정거래은행으로 송금되어야 한다.",
        "page": "1권 252p"
    },
    {
        "id": "1차평가_new_2",
        "category": "1차평가",
        "source": "1차평가",
        "question": "거주자 또는 비거주자가 지급수단을 휴대입국할 경우 입국세관장에게 신고하여야 하는 기준금액으로 옳은 것은?",
        "options": ["미화 2천 불 초과", "미화 5천 불 초과", "미화 1만 불 초과", "미화 2만 불 초과"],
        "answer": 2,
        "explanation": "출입국세관에 신고하여야 하는 기준은 미화 1만 불 초과이다.",
        "page": "1권 130p"
    },
    {
        "id": "1차평가_new_3",
        "category": "1차평가",
        "source": "1차평가",
        "question": "다음 중 대외송금에 전혀 제한을 받지 않는 예금계정은 어느 것인가?",
        "options": ["비거주자 자유원계정", "비거주자원화계정", "거주자계정", "해외이주자계정"],
        "answer": 0,
        "explanation": "비거주자 자유원계정은 대외처분에 전혀 제한이 없다.",
        "page": "1권 144, 147p"
    },
    {
        "id": "1차평가_new_4",
        "category": "1차평가",
        "source": "1차평가",
        "question": "다음 중 경상거래에 해당하는 것은?",
        "options": ["임대차계약", "증권취득", "상표권사용료", "부동산매매"],
        "answer": 2,
        "explanation": "상표권사용료는 경상거래에 속한다.",
        "page": "1권 17p"
    },
    {
        "id": "1차평가_new_5",
        "category": "1차평가",
        "source": "1차평가",
        "question": "자본거래의 대금결제 시 외국환은행을 통하지 아니하고 지급 또는 수령이 허용된 금액 기준으로 옳은 것은?",
        "options": ["건당 1천 불 이하", "건당 2천 불 이하", "건당 3천 불 이하", "건당 5천 불 이하"],
        "answer": 3,
        "explanation": "건당 5천불 이하는 외국환은행을 통하지 않고 직접 결제가 가능함",
        "page": "1권 142p"
    },
    {
        "id": "1차평가_new_6",
        "category": "1차평가",
        "source": "1차평가",
        "question": "외국환거래규정상의 '신고등'의 절차에 해당하지 않는 것은?",
        "options": ["확인", "신고", "인가", "허가"],
        "answer": 2,
        "explanation": "인가는 신고등의 범주에 속하지 않는다.",
        "page": "1권 18-20p"
    },
    {
        "id": "1차평가_new_7",
        "category": "1차평가",
        "source": "1차평가",
        "question": "다음 중 입찰보증등에 해당하지 않는 것은?",
        "options": ["물품환매보증", "이행보증", "입찰보증", "선수금환급보증"],
        "answer": 0,
        "explanation": "물품환매보증은 입찰보증등의 대상이 아니다.",
        "page": "1권 59p"
    },
    {
        "id": "1차평가_new_8",
        "category": "1차평가",
        "source": "1차평가",
        "question": "교포등에 대한 여신에서 외국환은행 신고대상에 해당하는 거주자의 담보제공 한도금액으로 옳은 것은?",
        "options": ["동일인 미화 10만 불", "동일인 미화 20만 불", "동일인 미화 30만 불", "동일인 미화 50만 불"],
        "answer": 3,
        "explanation": "50만 불까지는 외국환은행 신고이고 초과 시에는 한국은행앞 신고사항이다.",
        "page": "1권 165-167p"
    },
    {
        "id": "1차평가_new_9",
        "category": "1차평가",
        "source": "1차평가",
        "question": "해외여행경비 지급대상자인 국외연수생은 수학기간 기준이 언제까지인가?",
        "options": ["2개월 미만", "3개월 미만", "5개월 미만", "6개월 미만"],
        "answer": 3,
        "explanation": "수학기간이 6개월 미만은 국외연수생이며, 6개월 이상이 되면 해외유학생이 된다.",
        "page": "1권 94p"
    },
    {
        "id": "1차평가_new_10",
        "category": "1차평가",
        "source": "1차평가",
        "question": "외국인 비거주자가 국내부동산 취득 시 신고하여야 하는 경우는?",
        "options": ["거주용 임차", "상속취득", "증여취득", "유증취득"],
        "answer": 2,
        "explanation": "상속이나 유증은 신고예외이나 증여취득은 한국은행 신고대상이다.",
        "page": "1권 182p"
    },
    {
        "id": "1차평가_new_11",
        "category": "1차평가",
        "source": "1차평가",
        "question": "외국환은행을 통하지 아니하는 지급등의 방법에서 신고예외 지급대상에 포함되지 않는 경우인 것은?",
        "options": ["해외이주비", "수입대금 휴대반출", "신용카드지급", "재외동포 재산반출"],
        "answer": 1,
        "explanation": "수입대금 휴대반출은 한국은행신고 대상임",
        "page": "1권 123-124p"
    },
    {
        "id": "1차평가_new_12",
        "category": "1차평가",
        "source": "1차평가",
        "question": "비거주자의 국내부동산 취득 규정에서 외국인비거주자가 상속 또는 유증으로 인하여 취득하는 경우에는 신고하지 않아도 된다.",
        "options": ["O", "X"],
        "answer": 0,
        "explanation": "외국인비거주자가 상속 또는 유증으로 인하여 국내에 있는 부동산을 취득하는 경우, 신고예외 대상이다.",
        "page": "1권 182p"
    },
    {
        "id": "1차평가_new_13",
        "category": "1차평가",
        "source": "1차평가",
        "question": "외국환은행이 비거주자(국민제외)에게 원화 대출 시 전 금융기관 동일인 한도 20억원까지는 신고예외 대상으로 규제사항이 아니다.",
        "options": ["O", "X"],
        "answer": 1,
        "explanation": "비거주자는 국내에서 10억원 까지는 신고없이 대출받을 수 있다.",
        "page": "1권 56p"
    },
    {
        "id": "1차평가_new_14",
        "category": "1차평가",
        "source": "1차평가",
        "question": "현지법인의 현지금융 담보용도로 주로 사용되는 지급보증서에 해당하는 것은?",
        "options": ["Standby L/C", "Letter of Guarantee", "Clean L/C", "Demand Guarantee"],
        "answer": 0,
        "explanation": "Standby L/C : 현지법인의 현지금융 담보용으로 주로 사용된다.",
        "page": "1권 58-59, 200p"
    },
    {
        "id": "1차평가_new_15",
        "category": "1차평가",
        "source": "1차평가",
        "question": "외국인거주자가 해외유학경비 지급 시 원칙상 국민인 거주자로 간주되어 동일한 규정을 적용받을 수 있는 국내 최소 거주기간은?",
        "options": ["1년 이상", "2년 이상", "3년 이상", "5년 이상"],
        "answer": 3,
        "explanation": "외국인거주자는 적어도 국내에서 5년을 체류하여야 유학경비를 지급한다.",
        "page": "1권 93-94p"
    },
    {
        "id": "1차평가_new_16",
        "category": "1차평가",
        "source": "1차평가",
        "question": "국내 법인의 해외예금 거래내역이 국세청 및 관세청에 통보되는 기준은?",
        "options": ["연간입금액 또는 연말잔액 미화 5만 불 초과", "연간입금액 또는 연말잔액 미화 10만 불 초과", "연간입금액 또는 연말잔액 미화 30만 불 초과", "연간입금액 또는 연말잔액 미화 50만 불 초과"],
        "answer": 3,
        "explanation": "법인의 해외예금이 50만 불 초과 시 한국은행을 경유하여 국세청과 관세청에 통보된다.",
        "page": "1권 152p"
    },
    {
        "id": "1차평가_new_17",
        "category": "1차평가",
        "source": "1차평가",
        "question": "외국인 국내직접투자 시 수탁은행으로 지정되어 있는 본점 또는 지정 영업점이 아닌 외국환은행의 일반영업점에서 취급이 가능한 업무는?",
        "options": ["투자배당금 송금", "외국인투자기업 등록신청업무", "신규 외국인투자 신고 업무", "지분의 양도나 청산 업무"],
        "answer": 0,
        "explanation": "투자배당금이나 과실송금은 외국환은행의 일반영업점에서 취급이 가능하다.",
        "page": "1권 256p"
    },
    {
        "id": "1차평가_new_18",
        "category": "1차평가",
        "source": "1차평가",
        "question": "해외지점의 영업활동 제한 대상이 아닌 것은?",
        "options": ["부동산취득", "경상거래", "증권거래", "금전대여"],
        "answer": 1,
        "explanation": "해외지점의 경상거래는 제한대상이 아니다.",
        "page": "1권 224p"
    },
    {
        "id": "1차평가_new_19",
        "category": "1차평가",
        "source": "1차평가",
        "question": "비거주자 원화예금 계정에서 비거주자 자유원계정은 비거주자가 개설할 수 있는 계정으로 예치에 제한이 없는 대신 대외송금 시에 제한을 두고 있다.",
        "options": ["O", "X"],
        "answer": 1,
        "explanation": "비거주자원화계정은 예치에 제한이 없고 대외송금에 제한을 두고 있다.",
        "page": "1권 145~148p"
    },
    {
        "id": "1차평가_new_20",
        "category": "1차평가",
        "source": "1차평가",
        "question": "해외예금거래 신고한 일반거주자가 추가로 해외에서 건당 5천 불을 초과하여 직접 입금한 경우에는 입금일로부터 15일 이내에 해외입금보고서를 지정거래 외국환은행에 제출하여야 한다.",
        "options": ["O", "X"],
        "answer": 1,
        "explanation": "해외입금보고는 기준은 1만불 초과시 30일이내로 이행하여야 함",
        "page": "1권 151p"
    },
    {
        "id": "1차평가_new_21",
        "category": "1차평가",
        "source": "1차평가",
        "question": "외국환은행은 영수확인서를 몇 년간 보존하여야 하는가?",
        "options": ["1년", "2년", "3년", "5년"],
        "answer": 3,
        "explanation": "신고서는 2년이지만, 영수확인서는 5년간 보관하여야 한다.",
        "page": "1권 32p"
    },
    {
        "id": "1차평가_new_22",
        "category": "1차평가",
        "source": "1차평가",
        "question": "외국환 매입 시 영수확인서 징구와 관련이 없는 사항인 것은?",
        "options": ["거주자인 국내법인", "외국인거주자", "취득증빙서류 미제출 시", "타발송금"],
        "answer": 1,
        "explanation": "외국인거주자는 해당되지 않는다.",
        "page": "1권 50p"
    },
    {
        "id": "1차평가_new_23",
        "category": "1차평가",
        "source": "1차평가",
        "question": "거주자가 비거주자로부터 외화가 아닌 원화로 차입 시 재정경제부 앞 신고대상인 경우는?",
        "options": ["10억 원 초과 차입 시", "20억 원 초과 차입 시", "30억 원 초과 차입 시", "50억 원 초과 차입 시"],
        "answer": 0,
        "explanation": "해외 원화차입은 10억 원 초과 시 재정경제부 신고대상이다.",
        "page": "1권 161p"
    },
    {
        "id": "1차평가_new_24",
        "category": "1차평가",
        "source": "1차평가",
        "question": "외국인거주자의 국내 보수 또는 소득 지급 시 증빙서류를 제출하지 못하는 경우 연간 송금액 최고한도는 얼마까지인가?",
        "options": ["연간 지급누계 1만 불", "연간 지급누계 2만 불", "연간 지급누계 3만 불", "연간 지급누계 5만 불"],
        "answer": 3,
        "explanation": "외국인근로자는 급여명세표 없이도 연간 5만 불까지 송금을 허용하고 있다.",
        "page": "1권 81-82p"
    }
]

new_2cha = [
    {
        "id": "2차평가_new_1",
        "category": "2차평가",
        "source": "2차평가",
        "question": "수표의 유효기간에서 통상 은행발행 수표는 3개월 이내 이고 개인수표는 6개월 이내이다.",
        "options": ["O", "X"],
        "answer": 1,
        "explanation": "수표의 유효기간 중 개인수표는 3개월 이내이다.",
        "page": "2권 178p"
    },
    {
        "id": "2차평가_new_2",
        "category": "2차평가",
        "source": "2차평가",
        "question": "외국인거주자로부터의 외국통화 매입 시 자금의 원천인 외국환신고(확인)필증으로 본인명의의 자금임을 확인하여야 하는 기준 금액은 동일자 동일인 기준 미화 5천 불 초과인 경우이다.",
        "options": ["O", "X"],
        "answer": 1,
        "explanation": "외국인거주자로부터 외국통화 매입 시 본인명의의 자금확인에 관한 설명으로 2만불 초과이다.",
        "page": "2권 75p"
    },
    {
        "id": "2차평가_new_3",
        "category": "2차평가",
        "source": "2차평가",
        "question": "미국의 수표법상 수표전면의 위변조 시 부도시효지급일로부터 언제까지 수표가 부도반환되는가?",
        "options": ["6개월 이내", "1년 이내", "2년 이내", "3년 이내"],
        "answer": 1,
        "explanation": "수표전면은 1년 이내 부도반환된다.",
        "page": "2권 128p"
    },
    {
        "id": "2차평가_new_4",
        "category": "2차평가",
        "source": "2차평가",
        "question": "장기 미지급송금은 송금대전이 상대은행에서 지급되지 않고 얼마동안 남아 있는 경우를 말하는가?",
        "options": ["3개월 이상", "6개월 이상", "1년 이상", "5년 이상"],
        "answer": 1,
        "explanation": "해외송금을 취결하였으나 6개월 이상 지급되지 않는 송금을 말한다.",
        "page": "2권 47p"
    },
    {
        "id": "2차평가_new_5",
        "category": "2차평가",
        "source": "2차평가",
        "question": "외국법인의 대리인이 통장개설 시 실명확인 방법 중 바르지 못한 내용은?",
        "options": ["해당 법인이 당해 국가에 설립되어 있음을 증명하는 서류가 있어야 한다.", "외국인투자신고서가 있는 경우에는 위임장 겸용이 가능하다.", "대리인의 실명확인증표가 있어야 한다.", "증권거래를 위한 투자등록증을 제시하는 경우 위임장에 공증을 받을 필요가 없다."],
        "answer": 3,
        "explanation": "증권거래를 위한 투자등록증을 제시하는 경우 위임장에 공증이 필요하다.",
        "page": "2권 98p"
    },
    {
        "id": "2차평가_new_6",
        "category": "2차평가",
        "source": "2차평가",
        "question": "당발송금 퇴결절자에 대한 내용 중 옳지 않은 것은?",
        "options": ["지급은행에 지급지시취소 통지", "결제은행에 대기지시취소 통지", "취소승락 회신전문 확인", "퇴결대금은 전신환매입률 적용"],
        "answer": 1,
        "explanation": "결제은행에 차기지시(출금)취소 통지하여야 함",
        "page": "2권 43~44p"
    },
    {
        "id": "2차평가_new_7",
        "category": "2차평가",
        "source": "2차평가",
        "question": "외국환은행의 확인의무와 거리가 먼 경우는?",
        "options": ["신고대상 확인의무", "사후관리의무", "실명확인의무", "제재사항 통지의무"],
        "answer": 3,
        "explanation": "제재사항 통지의무는 제재기관의 업무이다.",
        "page": "2권 219-221p"
    },
    {
        "id": "2차평가_new_8",
        "category": "2차평가",
        "source": "2차평가",
        "question": "다음 중 호주지역 은행의 Local Code에 해당하는 것은?",
        "options": ["IBAN NO.", "ABA NO.", "TRANSIT NO.", "BSB NO."],
        "answer": 3,
        "explanation": "BSB NO.는 호주지역이다.",
        "page": "2권 36-38P"
    },
    {
        "id": "2차평가_new_9",
        "category": "2차평가",
        "source": "2차평가",
        "question": "다음 중 정기적금이 허용된 예금계정은 어느 것인가?",
        "options": ["비거주자원화계정", "대외계정", "해외이주자계정", "비거주자자유원계정"],
        "answer": 1,
        "explanation": "대외계정과 거주자계정만 정기적금 과목이 있다.",
        "page": "2권 167p"
    },
    {
        "id": "2차평가_new_10",
        "category": "2차평가",
        "source": "2차평가",
        "question": "다음 외화당좌예금에 대한 설명 중 가장 옳지 못한 것은?",
        "options": ["외화당좌예금 거래장이 아닌 통장만을 교부한다.", "일반적으로 외화당좌는 수표 및 어음 지급이 없다.", "보증료나 수수료의 채무변제 충당 시 지급청구서가 필요없다.", "통상적으로 적정 이자를 지급하지 않는다."],
        "answer": 0,
        "explanation": "외화당좌예금은 통장이 아닌 거래장을 교부한다.",
        "page": "2권 144p"
    },
    {
        "id": "2차평가_new_11",
        "category": "2차평가",
        "source": "2차평가",
        "question": "외국환거래법규 위반으로 인한 과태료 처분 시 최고 부과금액은 얼마까지인가?",
        "options": ["1천만 원 이하", "3천만 원 이하", "5천만 원 이하", "1억 원 이하"],
        "answer": 3,
        "explanation": "과태료부과는 1억 원 이하로서 위반규모나 사유에 따라 차등적용한다.",
        "page": "2권 229p"
    },
    {
        "id": "2차평가_new_12",
        "category": "2차평가",
        "source": "2차평가",
        "question": "타발송금 지급 시 영수확인서 제출대상과 관계 없는 사항인 것은?",
        "options": ["비거주자", "취득경위서류 미제출", "동일자, 동일인 기준 일정한도 초과시", "이전거래 간주"],
        "answer": 0,
        "explanation": "영수확인서는 비거주자는 제출대상자가 아니다.",
        "page": "2권 54p"
    },
    {
        "id": "2차평가_new_13",
        "category": "2차평가",
        "source": "2차평가",
        "question": "다음 중 외국환은행의 외국환신고(확인)필증 발행교부 대상이 아닌 경우는?",
        "options": ["일반해외여행경비(증빙서류가 없는 경우)", "해외유학경비", "해외이주비", "단체해외연수경비"],
        "answer": 0,
        "explanation": "일반여행경비는 출국세관이 발행한다.",
        "page": "2권 96p, 1권 96p"
    },
    {
        "id": "2차평가_new_14",
        "category": "2차평가",
        "source": "2차평가",
        "question": "거주자나 비거주자가 외국통화를 원화로 환전 시 국세청 및 관세청에 통보되는 기준금액인 것은?",
        "options": ["미화 1천 불 초과", "미화 5천 불 초과", "미화 1만 불 초과", "미화 2만 불 초과"],
        "answer": 2,
        "explanation": "거주자는 물론 외국인 및 비거주자도 1만 불 초과 환전 시 통보되고 있다.",
        "page": "2권 74-75p"
    },
    {
        "id": "2차평가_new_15",
        "category": "2차평가",
        "source": "2차평가",
        "question": "다음 예치환거래은행과 관련된 사항에 해당하는 설명과 관련이 없는 것은?",
        "options": ["코레스은행이다.", "신용장통지은행이다.", "대금추심 관련 상호계약을 한다.", "전신문을 상호교환한다."],
        "answer": 1,
        "explanation": "환거래은행 중에서 일부 예치환거래은행을 두고 있으며 신용장통지은행과는 무관하다.",
        "page": "2권 7p"
    },
    {
        "id": "2차평가_new_16",
        "category": "2차평가",
        "source": "2차평가",
        "question": "외화수표의 부도반환 사유 중 수표지급인의 계좌에 결제자금이 없거나 부족한 경우의 사유인 것은?",
        "options": ["Mutilated", "Maker Signature", "Endorsement", "NSF"],
        "answer": 3,
        "explanation": "NSF는 잔고부족 부도반환사유이다.",
        "page": "2권 183p"
    },
    {
        "id": "2차평가_new_17",
        "category": "2차평가",
        "source": "2차평가",
        "question": "외화수표 추심업무에 대한 내용 중 옳지 못한 것은?",
        "options": ["당행이 추심의뢰은행이 되는 경우에는 타발추심이다.", "추심전매입은 여신행위이다.", "신용도가 낮은 개인수표는 추심후 매입을 권장한다.", "추심대전 지급시 전신환매입률을 적용한다."],
        "answer": 0,
        "explanation": "당행이 추심의뢰은행이 되는 경우에는 당발추심이다.",
        "page": "2권 110~117p"
    },
    {
        "id": "2차평가_new_18",
        "category": "2차평가",
        "source": "2차평가",
        "question": "외국통화 매도 시 환전 한도에 대한 설명 중 틀린 것은?",
        "options": ["외국인거주자의 일반여행경비는 5만 불 범위내", "비거주자는 최근 입국일 이후 매각실적 범위내", "국민인 거주자의 소지목적환전은 금액제한 없음", "비거주자로서 매각실적이 없는 경우 1만 불 범위내"],
        "answer": 0,
        "explanation": "외국인거주자의 일반여행경비는 1만불 이내임",
        "page": "2권 89p"
    },
    {
        "id": "2차평가_new_19",
        "category": "2차평가",
        "source": "2차평가",
        "question": "외국환은행의 거래내역 통보기관이 아닌 것은?",
        "options": ["국세청장", "관세청장", "무역협회장", "금융감독원장"],
        "answer": 2,
        "explanation": "무역협회장에게 통보의무는 없음",
        "page": "2권 220p"
    },
    {
        "id": "2차평가_new_20",
        "category": "2차평가",
        "source": "2차평가",
        "question": "외국환신고(확인)필증은 외국인거주자 또는 비거주가 외화현찰을 얼마 이상 매입요청 시 징구하여야 하나?",
        "options": ["동일자 미화 2천 불 초과", "동일자 미화 5천 불 초과", "동일자 미화 1만 불 초과", "동일자 미화 2만 불 초과"],
        "answer": 3,
        "explanation": "동일자 미화 2만 불 초과의 경우 반드시 외국환신고(확인)필증을 제출하여야 한다.",
        "page": "2권 62p"
    },
    {
        "id": "2차평가_new_21",
        "category": "2차평가",
        "source": "2차평가",
        "question": "외국환은행의 고액현금보고(CTR)의무 대상인 금액 기준은?",
        "options": ["1천만 원 이상", "2천만 원 이상", "3천만 원 이상", "5천만 원 이상"],
        "answer": 0,
        "explanation": "고액현금거래보고 대상은 1천만 원이상이다.",
        "page": "2권 221p"
    },
    {
        "id": "2차평가_new_22",
        "category": "2차평가",
        "source": "2차평가",
        "question": "거주자 또는 비거주자로부터 외국통화 매입 시 실명확인을 생략할 수 있는 금액기준은 얼마인가?",
        "options": ["건당 1백만 원 이하 상당액", "건당 2백만 원 이하 상당액", "건당 3백만 원 이하 상당액", "건당 5백만 원 이하 상당액"],
        "answer": 0,
        "explanation": "1백만 원 상당의 외국통화 매매 시 실명생략이 가능하다.",
        "page": "2권 73p"
    },
    {
        "id": "2차평가_new_23",
        "category": "2차평가",
        "source": "2차평가",
        "question": "외화수표 추심업무에서 추심의뢰장 작성 항목에 해당하지 않는 것은?",
        "options": ["취급부점표시", "참조번호기재", "제시은행명칭", "추심의뢰인의 신용도"],
        "answer": 3,
        "explanation": "추심의뢰인의 신용도는 작성대상이 아님",
        "page": "2권 182p"
    },
    {
        "id": "2차평가_new_24",
        "category": "2차평가",
        "source": "2차평가",
        "question": "다음 외화수표 중에서 은행의 예금보유에 관계 없이 발행회사 또는 은행에 수표금액에 해당하는 금액을 입금하면 이에 해당하는 수표를 의뢰인에게 교부하는 것으로서 은행, 개인 또는 우체국에서도 발행할 수 있는 것은?",
        "options": ["Personal Check", "Cashier's Check", "Money order", "Banker's Check"],
        "answer": 2,
        "explanation": "Money Order에 대한 설명이다.",
        "page": "2권 113p"
    },
    {
        "id": "2차평가_new_25",
        "category": "2차평가",
        "source": "2차평가",
        "question": "타발송금 매입내역이 국세청 및 관세청에 통보되는 기준에 해당하는 것은?",
        "options": ["미화 1천 불 초과", "미화 2천 불 초과", "미화 1만 불 초과", "미화 2만 불 초과"],
        "answer": 2,
        "explanation": "미화 1만 불 초과 시 매 익월 통보된다.",
        "page": "2권 62p"
    },
    {
        "id": "2차평가_new_26",
        "category": "2차평가",
        "source": "2차평가",
        "question": "거래당사자의 외국환거래법규 위반시 형사처벌의 최고형량 기준은?",
        "options": ["1년이하의 징역 또는 1억원이하의 벌금", "2년이하의 징역 또는 2억원이하의 벌금", "3년이하의 징역 또는 3억원이하의 벌금", "5년이하의 징역 또는 5억원이하의 벌금"],
        "answer": 3,
        "explanation": "외국환법규위반시 최고 5년이하의 징역 또는 5억원이하의 벌금에 처한다.",
        "page": "2권 230p"
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
        
        lines = lines[:insert_idx] + to_insert + lines[insert_idx:]
    
    return '\n'.join(lines)

with open('src/data/data.ts', 'r') as f:
    content = f.read()

content = add_items(content, "1차평가", new_1cha)
content = add_items(content, "2차평가", new_2cha)

# Ensure the last item before ]; doesn't have a trailing comma, though typescript allows it.
# Actually, the original file had `},` for all except the last.

with open('src/data/data.ts', 'w') as f:
    f.write(content)

