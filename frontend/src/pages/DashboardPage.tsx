import React from "react";
import MainLayout from "../components/layout/MainLayout";

const DashboardPage: React.FC = () => {
  return (
    <MainLayout>
      <div className="p-4">
        <h1 className="text-2xl font-bold"> Bem-vindo ao G.E.C</h1>
        <p>Sistema de Gerenciamento de Escalas de Culto.</p>
        <p>Use o menu lateral para navegar.</p>
      </div>
    </MainLayout>
  );
};

export default DashboardPage;