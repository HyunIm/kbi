import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Dashboard } from './pages/Dashboard';
import { QuizEngine } from './pages/QuizEngine';

function App() {
  return (
    <Router basename="/kbi">
      <div className="font-sans antialiased text-slate-900 bg-slate-50 min-h-screen selection:bg-blue-200">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/quiz" element={<QuizEngine />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
