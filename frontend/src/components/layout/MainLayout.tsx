// src/components/layout/MainLayout.tsx
import React from 'react';

type MainLayoutProps = {
  children: React.ReactNode;
};

function MainLayout({ children }: MainLayoutProps) {
  return (
    <div className="drawer lg:drawer-open">
      <input id="my-drawer-2" type="checkbox" className="drawer-toggle" />
      <div className="drawer-content flex flex-col items-center justify-center">
        {/* Page content here */}
        <header className="w-full p-4 bg-base-200">
          <label htmlFor="my-drawer-2" className="btn btn-primary drawer-button lg:hidden">
            Abrir Menu
          </label>
          <h1 className="text-2xl font-bold">Dashboard</h1>
        </header>
        <main className="flex-1 w-full p-4">
          {children}
        </main>
      </div>
      <div className="drawer-side">
        <label htmlFor="my-drawer-2" aria-label="close sidebar" className="drawer-overlay"></label>
        <ul className="menu p-4 w-80 min-h-full bg-base-200 text-base-content">
          {/* Sidebar content here */}
          <li className="menu-title">G.E.C</li>
          <li><a>Dashboard</a></li>
          <li><a>Obreiros</a></li>
          <li><a>Locais</a></li>
          <li><a>Tipos de Culto</a></li>
          <li><a>Escalas</a></li>
        </ul>
      </div>
    </div>
  );
}

export default MainLayout;
