import React, { useState } from 'react';
import { Question, QuizType } from '../types';

interface QuestionCardProps {
  question: Question;
  quizType: QuizType;
  onAnswer: (selectedOption: number) => void;
  onNext: () => void;
  currentIndex: number;
  totalQuestions: number;
}

export const QuestionCard: React.FC<QuestionCardProps> = ({
  question,
  quizType,
  onAnswer,
  onNext,
  currentIndex,
  totalQuestions,
}) => {
  const [selectedIdx, setSelectedIdx] = useState<number | null>(null);
  const [showExplanation, setShowExplanation] = useState<boolean>(false);

  const handleOptionClick = (idx: number) => {
    if (selectedIdx !== null) return; // Prevent multiple clicks
    setSelectedIdx(idx);
    
    if (quizType === 'LEARNING') {
      setShowExplanation(true);
    }
    
    onAnswer(idx);
    
    // In exam mode, automatically go to next question after a short delay
    // Wait, typically Exam mode might not show explanations and just proceed
    if (quizType === 'EXAM') {
      setTimeout(() => {
        onNext();
      }, 300);
    }
  };

  const handleNextClick = () => {
    setSelectedIdx(null);
    setShowExplanation(false);
    onNext();
  };

  return (
    <div className="w-full max-w-2xl mx-auto bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden">
      <div className="p-6">
        <div className="flex justify-between items-center mb-4">
          <span className="bg-blue-100 text-blue-800 text-xs font-semibold px-2.5 py-0.5 rounded">
            {question.category}
          </span>
          <span className="text-sm text-slate-500 font-medium">
            {currentIndex + 1} / {totalQuestions}
          </span>
        </div>
        
        <h2 className="text-xl md:text-2xl font-bold text-slate-800 mb-6 leading-tight">
          {question.question}
        </h2>

        <div className="space-y-3">
          {question.options.map((option, idx) => {
            let btnClass = "w-full text-left p-4 rounded-lg border-2 transition-all duration-200 text-base md:text-lg ";
            
            if (selectedIdx === null) {
              btnClass += "border-slate-200 hover:border-blue-400 hover:bg-blue-50 text-slate-700";
            } else if (quizType === 'LEARNING') {
              if (idx === question.answer) {
                btnClass += "border-green-500 bg-green-50 text-green-800 font-medium";
              } else if (idx === selectedIdx) {
                btnClass += "border-red-500 bg-red-50 text-red-800";
              } else {
                btnClass += "border-slate-200 text-slate-400 opacity-60";
              }
            } else if (quizType === 'EXAM') {
              if (idx === selectedIdx) {
                btnClass += "border-blue-500 bg-blue-50 text-blue-800 font-medium";
              } else {
                btnClass += "border-slate-200 text-slate-400 opacity-60";
              }
            }

            return (
              <button
                key={idx}
                disabled={selectedIdx !== null}
                className={btnClass}
                onClick={() => handleOptionClick(idx)}
              >
                <div className="flex items-start">
                  <span className="mr-3 font-semibold">{idx + 1}.</span>
                  <span>{option}</span>
                </div>
              </button>
            );
          })}
        </div>

        {showExplanation && quizType === 'LEARNING' && (
          <div className="mt-6 p-4 bg-blue-50 border border-blue-100 rounded-lg animate-fade-in">
            <div className="flex items-center justify-between mb-2">
              <h3 className="font-bold text-blue-900 flex items-center">
                {selectedIdx === question.answer ? '✅ 정답입니다!' : '❌ 오답입니다'}
              </h3>
              <span className="text-xs text-blue-600 font-medium">{question.page} ({question.source})</span>
            </div>
            <p className="text-slate-700 leading-relaxed text-sm md:text-base">
              {question.explanation}
            </p>
          </div>
        )}

        {quizType === 'LEARNING' && selectedIdx !== null && (
          <button
            onClick={handleNextClick}
            className="mt-6 w-full py-4 bg-blue-600 hover:bg-blue-700 text-white font-bold rounded-lg transition-colors text-lg"
          >
            {currentIndex === totalQuestions - 1 ? '결과 보기' : '다음 문제'}
          </button>
        )}
      </div>
    </div>
  );
};
