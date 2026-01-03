// src/services/api.ts

const API_BASE_URL = 'http://localhost:8000/api'; // Substitua pela URL da sua API

/**
 * Realiza o login do usuário.
 * Por enquanto, é uma função mockada.
 * @param {string} username - O nome de usuário.
 * @param {string} password - A senha.
 * @returns {Promise<{token: string}>} - Uma promessa que resolve com um token de autenticação.
 */
export async function loginUser(username: string, password: string): Promise<{ token: string }> {
  // Simula uma chamada de API para o backend
  console.log('Tentando login com:', username, password);

  // Em uma implementação real, você faria uma chamada `fetch` para o seu endpoint de login
  // const response = await fetch(`${API_BASE_URL}/token/`, {
  //   method: 'POST',
  //   headers: {
  //     'Content-Type': 'application/json',
  //   },
  //   body: JSON.stringify({ username, password }),
  // });

  // if (!response.ok) {
  //   throw new Error('Falha no login');
  // }

  // const data = await response.json();
  // return { token: data.access }; // Supondo que a API retorna um token de acesso

  // --- Mock da resposta ---
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve({ token: 'fake-jwt-token' });
    }, 1000);
  });
}
