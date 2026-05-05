import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { BookOpen, Target, Shuffle, BookX, Trash2 } from 'lucide-react';
import { getWrongAnswersFromStorage, clearWrongAnswers } from '../hooks/useQuiz';

export const Dashboard: React.FC = () => {
  const navigate = useNavigate();
  const [wrongAnswersCount, setWrongAnswersCount] = useState(0);

  useEffect(() => {
    setWrongAnswersCount(getWrongAnswersFromStorage().length);
  }, []);

  const handleStartQuiz = (mode: string) => {
    navigate(`/quiz?mode=${mode}`);
  };

  const handleClearWrongAnswers = (e: React.MouseEvent) => {
    e.stopPropagation();
    if (window.confirm('정말 오답 노트를 초기화하시겠습니까?')) {
      clearWrongAnswers();
      setWrongAnswersCount(0);
    }
  };

  return (
    <div className="min-h-screen bg-slate-50 pb-12">
      {/* Header */}
      <header className="bg-blue-600 text-white pt-12 pb-20 px-6 rounded-b-[40px] shadow-md">
        <div className="max-w-4xl mx-auto">
          <h1 className="text-3xl md:text-4xl font-extrabold tracking-tight mb-2">
            직무필수 연수 퀴즈
          </h1>
          <p className="text-blue-100 text-lg">
            이동 중에도 간편하게 핵심 직무 지식을 학습하세요.
          </p>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-4xl mx-auto px-6 -mt-10">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

          {/* Card 1 */}
          <button
            onClick={() => handleStartQuiz('WEEKLY')}
            className="group flex flex-col text-left bg-white p-6 rounded-2xl shadow-sm border border-slate-200 hover:shadow-md hover:border-blue-300 transition-all"
          >
            <div className="w-12 h-12 bg-blue-100 text-blue-600 rounded-full flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
              <BookOpen size={24} />
            </div>
            <h3 className="text-xl font-bold text-slate-800 mb-2">주차별 풀이</h3>
            <p className="text-slate-500 text-sm">1주차부터 12주차까지 원하는 주차를 선택하여 꼼꼼하게 학습합니다. (학습형)</p>
          </button>

          {/* Card 2 */}
          <button
            onClick={() => handleStartQuiz('EVAL1')}
            className="group flex flex-col text-left bg-white p-6 rounded-2xl shadow-sm border border-slate-200 hover:shadow-md hover:border-blue-300 transition-all"
          >
            <div className="w-12 h-12 bg-indigo-100 text-indigo-600 rounded-full flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
              <Target size={24} />
            </div>
            <h3 className="text-xl font-bold text-slate-800 mb-2">평가별 모의고사</h3>
            <p className="text-slate-500 text-sm">1차 또는 2차 평가 대비 실전 모의고사를 진행합니다. (학습형)</p>
          </button>

          {/* Card 3 */}
          <button
            onClick={() => handleStartQuiz('RANDOM')}
            className="group flex flex-col text-left bg-white p-6 rounded-2xl shadow-sm border border-slate-200 hover:shadow-md hover:border-blue-300 transition-all"
          >
            <div className="w-12 h-12 bg-emerald-100 text-emerald-600 rounded-full flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
              <Shuffle size={24} />
            </div>
            <h3 className="text-xl font-bold text-slate-800 mb-2">랜덤 모의고사</h3>
            <p className="text-slate-500 text-sm">전체 문항 중 20문제를 무작위로 추출하여 실력을 테스트합니다. (시험형)</p>
          </button>

          {/* Card 4 - Wrong Answers */}
          <div className="relative group bg-white p-6 rounded-2xl shadow-sm border border-slate-200 hover:shadow-md hover:border-red-300 transition-all flex flex-col text-left">
            <button
              onClick={() => handleStartQuiz('WRONG_NOTES')}
              disabled={wrongAnswersCount === 0}
              className="flex-1 w-full text-left focus:outline-none disabled:opacity-60"
            >
              <div className="w-12 h-12 bg-red-100 text-red-600 rounded-full flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
                <BookX size={24} />
              </div>
              <h3 className="text-xl font-bold text-slate-800 mb-2">오답 노트 풀이</h3>
              <p className="text-slate-500 text-sm">틀렸던 문제를 다시 풀어보며 약점을 보완합니다. 현재 {wrongAnswersCount}문제가 저장되어 있습니다. (학습형)</p>
            </button>

            {wrongAnswersCount > 0 && (
              <button
                onClick={handleClearWrongAnswers}
                className="absolute top-6 right-6 p-2 text-slate-400 hover:text-red-500 hover:bg-red-50 rounded-full transition-colors"
                title="오답 노트 초기화"
              >
                <Trash2 size={20} />
              </button>
            )}
          </div>

        </div>
      </main>
    </div>
  );
};
