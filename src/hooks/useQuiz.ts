import { useState, useEffect } from 'react';
import { Question, QuizState } from '../types';

const WRONG_ANSWERS_KEY = 'kbi_wrong_answers';

export const useQuiz = (initialQuestions: Question[]) => {
  const [state, setState] = useState<QuizState>({
    questions: initialQuestions,
    currentQuestionIndex: 0,
    score: 0,
    wrongAnswers: [],
    isFinished: false,
    userAnswers: {},
  });

  useEffect(() => {
    setState({
      questions: initialQuestions,
      currentQuestionIndex: 0,
      score: 0,
      wrongAnswers: [],
      isFinished: false,
      userAnswers: {},
    });
  }, [initialQuestions]);

  const handleAnswer = (questionId: string, selectedOptionIndex: number) => {
    const currentQuestion = state.questions[state.currentQuestionIndex];
    const isCorrect = currentQuestion.answer === selectedOptionIndex;

    setState(prev => {
      const newWrongAnswers = isCorrect 
        ? prev.wrongAnswers 
        : [...prev.wrongAnswers, currentQuestion];

      return {
        ...prev,
        score: isCorrect ? prev.score + 1 : prev.score,
        wrongAnswers: newWrongAnswers,
        userAnswers: { ...prev.userAnswers, [questionId]: selectedOptionIndex },
      };
    });
  };

  const nextQuestion = () => {
    setState(prev => {
      if (prev.currentQuestionIndex >= prev.questions.length - 1) {
        return { ...prev, isFinished: true };
      }
      return { ...prev, currentQuestionIndex: prev.currentQuestionIndex + 1 };
    });
  };

  const saveWrongAnswersToStorage = () => {
    const existing = localStorage.getItem(WRONG_ANSWERS_KEY);
    const existingArray: Question[] = existing ? JSON.parse(existing) : [];
    
    // 이번 세션에서 푼 문제들의 ID
    const answeredQuestionIds = Object.keys(state.userAnswers);
    
    // 이번 세션에서 맞춘 문제 ID (푼 문제 중 틀린 문제에 없는 ID)
    const correctlyAnsweredIds = answeredQuestionIds.filter(
      id => !state.wrongAnswers.some(q => q.id === id)
    );

    // 기존 오답 목록에서 이번에 맞춘 문제 제거
    let newArray = existingArray.filter(q => !correctlyAnsweredIds.includes(q.id));
    
    // 이번에 틀린 문제 추가
    newArray = [...newArray, ...state.wrongAnswers];
    
    // 중복 제거
    const unique = newArray.filter((v, i, a) => a.findIndex(t => (t.id === v.id)) === i);
    
    localStorage.setItem(WRONG_ANSWERS_KEY, JSON.stringify(unique));
  };

  // Save when finished
  useEffect(() => {
    if (state.isFinished) {
      saveWrongAnswersToStorage();
    }
  }, [state.isFinished]);

  return {
    state,
    handleAnswer,
    nextQuestion,
  };
};

export const getWrongAnswersFromStorage = (): Question[] => {
  const existing = localStorage.getItem(WRONG_ANSWERS_KEY);
  return existing ? JSON.parse(existing) : [];
};

export const clearWrongAnswers = () => {
  localStorage.removeItem(WRONG_ANSWERS_KEY);
};
