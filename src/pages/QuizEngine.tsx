import React, { useMemo, useState } from 'react';
import { useSearchParams, useNavigate } from 'react-router-dom';
import { ChevronLeft } from 'lucide-react';
import { dummyData } from '../data/data';
import { getWrongAnswersFromStorage, useQuiz } from '../hooks/useQuiz';
import { QuestionCard } from '../components/QuestionCard';
import { QuizResult } from '../components/QuizResult';
import { Question, QuizType } from '../types';

export const QuizEngine: React.FC = () => {
  const [searchParams] = useSearchParams();
  const navigate = useNavigate();
  const mode = searchParams.get('mode') || 'RANDOM';

  // State for sub-options
  const [selectedSubOption, setSelectedSubOption] = useState<string | null>(null);

  // Initialize questions based on mode
  const initialQuestions = useMemo(() => {
    let questions: Question[] = [];

    switch (mode) {
      case 'WEEKLY':
        if (selectedSubOption) {
          if (selectedSubOption === 'ALL') {
            questions = dummyData.filter(q => q.category === '주차평가');
          } else {
            // selectedSubOption is like "1주차"
            questions = dummyData.filter(q => q.category === '주차평가' && q.source === `${selectedSubOption} 진행평가`);
          }
        }
        break;
      case 'EVAL1':
        if (selectedSubOption) {
          questions = dummyData.filter(q => q.category === selectedSubOption);
        }
        break;
      case 'RANDOM':
        // Shuffle and pick 20 (or max available)
        questions = [...dummyData].sort(() => 0.5 - Math.random()).slice(0, 20);
        break;
      case 'WRONG_NOTES':
        questions = getWrongAnswersFromStorage();
        break;
    }
    return questions;
  }, [mode, selectedSubOption]);

  const quizType: QuizType = (mode === 'RANDOM') ? 'EXAM' : 'LEARNING';

  const { state, handleAnswer, nextQuestion } = useQuiz(initialQuestions);

  // Render Sub-option Selector
  if ((mode === 'WEEKLY' || mode === 'EVAL1') && !selectedSubOption) {
    return (
      <div className="min-h-screen bg-slate-50 flex flex-col">
        <header className="bg-white border-b border-slate-200 p-4 sticky top-0 z-10 flex items-center">
          <button onClick={() => navigate('/')} className="p-2 mr-2 text-slate-500 hover:text-slate-800 rounded-full hover:bg-slate-100">
            <ChevronLeft size={24} />
          </button>
          <h1 className="text-lg font-bold text-slate-800">
            {mode === 'WEEKLY' ? '주차 선택' : '평가 선택'}
          </h1>
        </header>
        <main className="flex-1 p-6 max-w-2xl mx-auto w-full">
          <div className="space-y-3">
            {mode === 'WEEKLY' && (
              <>
                <button 
                  onClick={() => setSelectedSubOption('ALL')}
                  className="w-full text-left p-4 bg-white rounded-xl shadow-sm border border-blue-300 hover:border-blue-500 hover:bg-blue-50 text-blue-700 font-bold mb-4"
                >
                  1~12주차 전체 학습하기
                </button>
                <div className="grid grid-cols-2 gap-3">
                  {[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12].map(week => (
                    <button 
                      key={week}
                      onClick={() => setSelectedSubOption(`${week}주차`)}
                      className="w-full text-left p-4 bg-white rounded-xl shadow-sm border border-slate-200 hover:border-blue-500 hover:bg-blue-50 text-slate-700 font-semibold"
                    >
                      {week}주차
                    </button>
                  ))}
                </div>
              </>
            )}
            {mode === 'EVAL1' && ['1차평가', '2차평가'].map(evalMode => (
              <button 
                key={evalMode}
                onClick={() => setSelectedSubOption(evalMode)}
                className="w-full text-left p-4 bg-white rounded-xl shadow-sm border border-slate-200 hover:border-blue-500 hover:bg-blue-50 text-slate-700 font-semibold"
              >
                {evalMode} 대비 모의고사
              </button>
            ))}
          </div>
        </main>
      </div>
    );
  }

  if (initialQuestions.length === 0) {
    return (
      <div className="min-h-screen bg-slate-50 flex items-center justify-center p-6">
        <div className="text-center">
          <p className="text-xl text-slate-600 mb-4">선택한 조건에 해당하는 문제가 없습니다.</p>
          <button onClick={() => navigate('/')} className="px-6 py-2 bg-blue-600 text-white rounded-lg font-medium">
            돌아가기
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-50 flex flex-col">
      <header className="bg-white border-b border-slate-200 p-4 sticky top-0 z-10 flex items-center justify-between">
        <div className="flex items-center">
          <button onClick={() => navigate('/')} className="p-2 mr-2 text-slate-500 hover:text-slate-800 rounded-full hover:bg-slate-100">
            <ChevronLeft size={24} />
          </button>
          <h1 className="text-lg font-bold text-slate-800">
            {quizType === 'EXAM' ? '실전 모의고사' : '학습 모드'}
          </h1>
        </div>
        {!state.isFinished && (
          <div className="bg-blue-100 text-blue-800 text-sm font-bold px-3 py-1 rounded-full">
            {state.currentQuestionIndex + 1} / {initialQuestions.length}
          </div>
        )}
      </header>

      <main className="flex-1 p-4 md:p-8 flex flex-col items-center">
        {!state.isFinished && state.questions[state.currentQuestionIndex] ? (
          <QuestionCard
            key={state.questions[state.currentQuestionIndex].id}
            question={state.questions[state.currentQuestionIndex]}
            quizType={quizType}
            onAnswer={(idx) => handleAnswer(state.questions[state.currentQuestionIndex].id, idx)}
            onNext={nextQuestion}
            currentIndex={state.currentQuestionIndex}
            totalQuestions={state.questions.length}
          />
        ) : state.isFinished ? (
          <QuizResult state={state} />
        ) : (
          <div className="text-slate-500">문제 데이터를 불러오는 중입니다...</div>
        )}
      </main>
    </div>
  );
};
