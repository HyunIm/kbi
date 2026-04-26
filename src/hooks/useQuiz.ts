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
    if (state.wrongAnswers.length > 0) {
      const existing = localStorage.getItem(WRONG_ANSWERS_KEY);
      const existingArray: Question[] = existing ? JSON.parse(existing) : [];
      
      // Deduplicate
      const newArray = [...existingArray, ...state.wrongAnswers];
      const unique = newArray.filter((v, i, a) => a.findIndex(t => (t.id === v.id)) === i);
      
      localStorage.setItem(WRONG_ANSWERS_KEY, JSON.stringify(unique));
    }
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
