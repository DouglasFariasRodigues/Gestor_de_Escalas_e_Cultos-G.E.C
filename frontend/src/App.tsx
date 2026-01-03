// src/App.tsx
import { Routes, Route } from 'react-router-dom';
import DashboardPage from './pages/DashboardPage.tsx';
import LoginPage from './pages/LoginPage.tsx';
import ObreirosPage from './pages/ObreirosPage.tsx';
import ProtectedRoute from './components/ProtectedRoute.tsx';

function App() {
  return (
    <div className="min-h-screen bg-gray-900 text-white">
      <Routes>
        <Route 
          path="/" 
          element={
            <ProtectedRoute>
              <DashboardPage />
            </ProtectedRoute>
          } 
        />
        <Route 
          path="/obreiros" 
          element={
            <ProtectedRoute>
              <ObreirosPage />
            </ProtectedRoute>
          } 
        />
        <Route path="/login" element={<LoginPage />} />
      </Routes>
    </div>
  )
}

export default App;