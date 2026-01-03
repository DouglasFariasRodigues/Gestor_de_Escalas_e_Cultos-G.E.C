// src/contexts/AuthContext.tsx
import React, { createContext, useState, useContext, ReactNode } from 'react';

// Define o formato do contexto de autenticação
interface AuthContextType {
  isAuthenticated: boolean;
  login: (token: string) => void;
  logout: () => void;
}

// Cria o contexto com um valor padrão
const AuthContext = createContext<AuthContextType | undefined>(undefined);

// Hook customizado para usar o contexto de autenticação
export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
}

// Provedor de autenticação que envolve a aplicação
export function AuthProvider({ children }: { children: ReactNode }) {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  // Função de login (simulada)
  const login = (token: string) => {
    // Em uma aplicação real, você armazenaria o token (ex: no localStorage)
    console.log('Token de acesso:', token);
    localStorage.setItem('authToken', token);
    setIsAuthenticated(true);
  };

  // Função de logout
  const logout = () => {
    localStorage.removeItem('authToken');
    setIsAuthenticated(false);
  };

  const value = {
    isAuthenticated,
    login,
    logout,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}
