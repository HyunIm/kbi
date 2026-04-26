import React from 'react';
import { useNavigate } from 'react-router-dom';
import { QuizState } from '../types';

interface QuizResultProps {
  state: QuizState;
}

export const QuizResult: React.FC<QuizResultProps> = ({ state }) => {
  const navigate = useNavigate();
  const totalQuestions = state.questions.length;
  const score = Math.round((state.score / totalQuestions) * 100);

  return (
    <div className="w-full max-w-3xl mx-auto bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden">
      <div className="p-8 text-center bg-gradient-to-b from-blue-50 to-white">
        <h2 className="text-3xl font-bold text-slate-800 mb-2">퀴즈 결과</h2>
        <div className="text-6xl font-extrabold text-blue-600 my-6">
          {score}점
        </div>
        <p className="text-slate-600 text-lg">
          총 {totalQuestions}문제 중 {state.score}문제를 맞혔습니다.
        </p>
      </div>

      {state.wrongAnswers.length > 0 && (
        <div className="p-6 md:p-8 border-t border-slate-100">
          <h3 className="text-xl font-bold text-slate-800 mb-4 flex items-center">
            <span className="mr-2">📝</span> 오답 노트
          </h3>
          <div className="space-y-6">
            {state.wrongAnswers.map((question, idx) => {
              const userAnswerIdx = state.userAnswers[question.id];
              return (
                <div key={idx} className="p-4 bg-slate-50 rounded-lg border border-slate-200">
                  <div className="mb-2 flex justify-between items-start">
                    <span className="text-xs font-semibold px-2 py-1 bg-slate-200 text-slate-700 rounded">
                      {question.category}
                    </span>
                    <span className="text-xs text-slate-500">{question.page}</span>
                  </div>
                  <p className="font-semibold text-slate-800 mb-3">{question.question}</p>
                  
                  <div className="text-sm space-y-1 mb-4">
                    <p className="text-red-600">
                      <span className="font-medium">나의 답:</span> {userAnswerIdx !== undefined ? question.options[userAnswerIdx] : '미선택'}
                    </p>
                    <p className="text-green-600">
                      <span className="font-medium">정답:</span> {question.options[question.answer]}
                    </p>
                  </div>

                  <div className="p-3 bg-blue-50/50 rounded border border-blue-100 text-sm text-slate-700">
                    <span className="font-semibold text-blue-800 mr-2">해설:</span>
                    {question.explanation}
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      )}

      <div className="p-6 bg-slate-50 flex gap-4">
        <button
          onClick={() => navigate('/')}
          className="flex-1 py-3 px-4 bg-white border border-slate-300 text-slate-700 font-bold rounded-lg hover:bg-slate-50 transition-colors"
        >
          대시보드로 돌아가기
        </button>
      </div>
    </div>
  );
};
