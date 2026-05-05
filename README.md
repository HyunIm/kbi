# 직무필수 연수 퀴즈 (KBI Training Quiz App)

이동 중에도 간편하게 핵심 직무 지식을 학습하고 평가를 대비할 수 있도록 제작된 **직무필수 연수 퀴즈 애플리케이션**입니다. 

## 🚀 기능 소개 (Features)

사용자의 학습 목적에 따라 다양한 모드를 지원합니다.

- **주차별 풀이 (학습형)**
  - 1주차부터 12주차까지 원하는 주차를 선택하여 꼼꼼하게 학습할 수 있습니다.
  - "1~12주차 전체 학습하기" 옵션을 통해 전체 주차평가 문제를 한 번에 풀어볼 수도 있습니다.
- **평가별 모의고사 (학습형)**
  - 1차 평가 및 2차 평가를 대비하기 위한 실전 모의고사 모드입니다.
- **랜덤 모의고사 (시험형)**
  - 전체 문항 중 20문제를 무작위로 추출하여 실력을 테스트합니다.
- **오답 노트 풀이 (학습형)**
  - 퀴즈를 풀면서 틀렸던 문제들만 따로 모아 다시 풀어보며 취약점을 보완할 수 있습니다.
  - 기기에 저장된 오답 기록을 언제든 초기화할 수 있습니다.

## 🛠️ 기술 스택 (Tech Stack)

- **Frontend Framework**: React 18, Vite
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **Icons**: Lucide React
- **Routing**: React Router DOM
- **Deployment**: GitHub Pages (`gh-pages`)

## 📂 프로젝트 구조 (Project Structure)

```
kbi/
├── src/
│   ├── components/      # QuestionCard, QuizResult 등 재사용 가능한 UI 컴포넌트
│   ├── data/            # 퀴즈 문항 데이터베이스 (data.ts)
│   ├── hooks/           # 퀴즈 상태 관리 및 오답 노트 로컬 스토리지 연동 (useQuiz.ts)
│   ├── pages/           # 메인 대시보드(Dashboard) 및 퀴즈 엔진(QuizEngine) 페이지
│   ├── types/           # TypeScript 인터페이스 및 타입 정의
│   ├── App.tsx          # 메인 애플리케이션 컴포넌트 및 라우팅 설정
│   └── index.css        # Tailwind CSS 엔트리 포인트
├── pdfs/                # 문제 추출에 사용된 원본 PDF 파일들
└── package.json
```

## ⚙️ 로컬 실행 및 배포 (Installation & Deployment)

### 필수 조건 (Prerequisites)
- Node.js (v16 이상 권장)
- npm

### 로컬 환경 실행
1. 저장소를 클론하고 프로젝트 폴더로 이동합니다.
2. 종속성을 설치합니다.
   ```bash
   npm install
   ```
3. 개발 서버를 실행합니다.
   ```bash
   npm run dev
   ```
4. 브라우저에서 `http://localhost:5173/kbi/` 에 접속하여 확인합니다.

### GitHub Pages 배포
이 프로젝트는 `gh-pages` 패키지를 통해 손쉽게 배포할 수 있도록 설정되어 있습니다.
```bash
npm run deploy
```
- 위 명령어를 실행하면 자동으로 TypeScript 컴파일과 Vite 빌드(`npm run build`)가 진행되며, 결과물인 `dist` 폴더가 `gh-pages` 브랜치로 푸시되어 배포가 완료됩니다.

## 💡 오답 노트 초기화 방법
메인 대시보드에서 "오답 노트 풀이" 카드의 우측 상단에 있는 휴지통 아이콘을 클릭하면 저장된 오답 데이터를 모두 초기화할 수 있습니다. (브라우저의 `localStorage`를 사용합니다.)
