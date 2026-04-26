export interface Question {
  id: string;
  category: "주차평가" | "1차평가" | "2차평가";
  source: string;
  question: string;
  options: string[];
  answer: number;
  explanation: string;
  page: string;
}

export type QuizMode = "WEEKLY" | "EVAL1" | "EVAL2" | "RANDOM" | "WRONG_NOTES" | null;
export type QuizType = "LEARNING" | "EXAM";

export interface QuizState {
  questions: Question[];
  currentQuestionIndex: number;
  score: number;
  wrongAnswers: Question[];
  isFinished: boolean;
  userAnswers: Record<string, number>;
}
