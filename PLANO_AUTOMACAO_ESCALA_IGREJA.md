# Plano de Automação de Escala de Cultos da Igreja

## Progresso
- [x] Documento .md criado
- [x] Preparar ambiente
- [x] Modelar o banco
- [x] Construir APIs
- [ ] Construir o Frontend
- [ ] Implementar Copiar Escala do Mês
- [ ] Garantias de seleção segura
- [ ] Validação e Testes
- [ ] Exportação e Impressão

## Tecnologias
- Backend: Django + Django REST Framework
- Banco: PostgreSQL
- Frontend: React
- UI: Tailwind CSS + daisyUI
- Marcação/Estilos: HTML e CSS

## Objetivo
- Automatizar a escala mensal de cultos: cadastro de obreiros, locais, tipos de culto (Nat Culto), datas e atribuições.
- Permitir copiar a escala de um mês inteiro para outro e editá-la, sempre escolhendo apenas entre obreiros/locais/Nat Culto já cadastrados.

## Escopo Funcional
- Cadastro: Obreiro (nome, cargo, ativo), Local (nome, ativo), Nat Culto (tipo/descrição, ativo).
- Agenda de cultos: data e hora, local, Nat Culto.
- Escala mensal: itens que associam obreiros aos cultos.
- Copiar escala: duplicar a configuração de um mês para outro com regras de mapeamento de datas.
- Edição segura: selecionar apenas registros previamente cadastrados (drop-downs).
- Busca/filtragem por mês, local, Nat Culto e obreiro.
- Auditoria simples: quem criou/alterou e quando.
- Exportação/Impressão: PDF ou planilha (opcional).

## Modelo de Dados (MVP)
- obreiro: id, nome, cargo, ativo
- local: id, nome, ativo
- nat_culto: id, nome (ou descrição), ativo
- culto: id, data_hora, local_id, nat_culto_id
- escala: id, mes (1–12), ano, status
- escala_item: id, escala_id, culto_id, obreiro_id
- Observações:
  - escala_item pode usar diretamente o cargo do obreiro; se o papel variar por culto, adicionar campo papel.
  - Chaves estrangeiras com cascata restrita para preservar integridade.

## Regras de Negócio
- Não permitir cadastro de itens de escala com obreiros/locais/Nat Culto inativos.
- Impedir conflito: um obreiro não pode estar em dois cultos com horários sobrepostos.
- **Contador de Escala Mensal:** O sistema deve calcular e exibir quantas vezes um obreiro foi escalado dentro de um determinado mês. (Concluído no backend)
- Copiar escala deve respeitar:
  - Apenas obreiros/locais/Nat Culto existentes e ativos; se um obreiro não existir/estiver inativo, o item fica pendente para revisão.
  - Datas de destino calculadas por “mesma semana e dia da semana” ou “mesmo dia do mês”.
- Edição sempre via seleção de listas provenientes do banco (sem texto livre para chaves).

## Fluxos Principais
- Cadastrar base: obreiros, locais, Nat Culto.
- Criar cultos: datas, horários, vínculo a local e Nat Culto.
- Criar escala do mês: gerar escala e adicionar escala_item.
- Copiar escala: escolher mês origem e mês destino; aplicar mapeamento; revisar pendências; salvar.
- Gerenciar: ativar/inativar registros; filtrar e imprimir.

## Telas (MVP)
- Dashboard: seletor de mes/ano, resumo da escala.
- Obreiros: lista, criar/editar, ativar/inativar.
- Locais: lista, criar/editar, ativar/inativar.
- Nat Culto: lista, criar/editar, ativar/inativar.
- Cultos: calendário/lista com data/hora, local, Nat Culto.
- Escala mensal: grade por culto com obreiros atribuídos, ação Copiar mês.
- Revisão de cópia: pendências e conflitos a resolver.
- Exportação/Impressão (opcional): gerar PDF/CSV.

## Arquitetura Sugerida
- Aplicação web simples:
  - Backend: Django (5.x) com Django REST Framework (DRF).
  - Banco: PostgreSQL.
  - Frontend: React com Vite.
  - UI: Tailwind CSS + daisyUI para componentes e temas.
  - Integrações: CORS configurado entre frontend e backend; autenticação JWT opcional para perfis de acesso.
 - Alternativa mínima: planilha + Apps Script para protótipo rápido; migração posterior para web.

## Passo a Passo de Implementação
1) Preparar ambiente
- Instalar Python 3.12+ e PostgreSQL.
- Criar venv e instalar dependências: Django, djangorestframework, psycopg2, django-cors-headers.
- Criar repositório e pastas: backend/ e frontend/.
- Backend:
  - `django-admin startproject backend` e `python manage.py startapp escala`.
  - Configurar `settings.py` para PostgreSQL e CORS.
  - Registrar app `escala` e DRF.
- Frontend:
  - `npm create vite@latest frontend -- --template react`.
  - Instalar Tailwind CSS + daisyUI e configurar tema básico.

2) Modelar o banco
- Tabelas e chaves:
  - obreiro(id PK, nome UNIQUE, cargo, ativo BOOL)
  - local(id PK, nome UNIQUE, ativo BOOL)
  - nat_culto(id PK, nome UNIQUE, ativo BOOL)
  - culto(id PK, data_hora DATETIME, local_id FK, nat_culto_id FK)
  - escala(id PK, mes INT, ano INT, status TEXT)
  - escala_item(id PK, escala_id FK, culto_id FK, obreiro_id FK)
- Índices:
  - culto(local_id, data_hora), escala(mes, ano), escala_item(escala_id, culto_id), escala_item(obreiro_id).
- Integridade:
  - CHECK para mes 1–12, ativo como boolean.
  - UNIQUE (mes, ano) se desejar uma escala por mês.
 - Implementação:
   - Definir `models.py` no app `escala` com relacionamentos e `choices` quando aplicável.
   - Criar migrações e aplicar com `python manage.py makemigrations` e `migrate`.

3) Construir APIs
- Configuração:
  - Instalar e habilitar DRF; definir `DEFAULT_RENDERER_CLASSES` e `DEFAULT_PARSER_CLASSES`.
  - Configurar `django-cors-headers` para permitir requisições do frontend.
- Endpoints (DRF ViewSets/Generic Views):
  - Obreiros:
    - POST /api/obreiro criar
    - GET /api/obreiro listar
    - PATCH /api/obreiro/:id editar/ativar/inativar
  - Locais e Nat Culto: CRUD similar.
  - Cultos:
    - POST /api/culto criar
    - GET /api/culto?mes=..&ano=.. listar por mês
    - Validar sobreposições e FK ativas.
  - Escala:
    - POST /api/escala criar (mes, ano)
    - GET /api/escala?mes=..&ano=.. obter
    - POST /api/escala/:id/itens adicionar/remover itens
    - POST /api/escala/:id/copiar copiar para {mesDestino, anoDestino}
- Regras na API:
  - Recusar vínculos com registros inativos.
  - Checar conflitos de horários por obreiro.
  - Serializers com validações de integridade.

4) Construir o Frontend
Esta etapa será dividida em sub-tarefas para facilitar o acompanhamento.

**Fase 1: Configuração e Estrutura Base**
- [x] Criar projeto com Vite + React + TypeScript.
- [x] Instalar e configurar Tailwind CSS para estilização.
- [x] Opcional: Instalar daisyUI para componentes de UI pré-prontos.
- [x] Criar estrutura de pastas do projeto (`pages`, `components`, `services`, `hooks`, `contexts`).
- [x] Instalar `react-router-dom` para gerenciar as rotas da aplicação.
- [ ] Configurar o `BrowserRouter` em `main.tsx` para habilitar o roteamento.
- [ ] Configurar as rotas iniciais em `App.tsx` (ex: redirecionar para `/login`).

**Fase 2: Autenticação e Layout Principal**
- [ ] Criar a página de Login (`pages/LoginPage.tsx`).
- [ ] Desenvolver o formulário de login (UI).
- [ ] Criar um componente de Layout Principal (`components/layout/MainLayout.tsx`) com Header e Sidebar.
- [ ] Criar a página de Dashboard (`pages/DashboardPage.tsx`) como página principal pós-login.
- [ ] Configurar rotas protegidas que só podem ser acessadas após o login.
- [ ] Criar um Contexto de Autenticação (`contexts/AuthContext.tsx`) para gerenciar o estado do usuário.
- [ ] Criar o serviço de API (`services/api.ts`) e a função de login para conectar ao backend.
- [ ] Implementar a lógica de login e logout.

**Fase 3: Cadastros Base (CRUDs)**
- [ ] **Obreiros:**
    - [ ] Criar a página de Obreiros (`pages/WorkersPage.tsx`).
    - [ ] Criar o serviço de API para Obreiros (listar, criar, editar).
    - [ ] Desenvolver a tabela para listar os obreiros.
    - [ ] Desenvolver o modal/formulário para criar/editar um obreiro.
- [ ] **Locais:**
    - [ ] Criar a página de Locais (`pages/LocationsPage.tsx`).
    - [ ] Implementar o CRUD completo para Locais (similar a Obreiros).
- [ ] **Tipos de Culto (Nat Culto):**
    - [ ] Criar a página de Tipos de Culto (`pages/ServiceTypesPage.tsx`).
    - [ ] Implementar o CRUD completo para Tipos de Culto.

**Fase 4: Funcionalidade Principal (Escalas)**
- [ ] Criar a página de Escalas (`pages/SchedulesPage.tsx`).
- [ ] Desenvolver o seletor de Mês/Ano.
- [ ] Criar a visualização da escala em formato de tabela/calendário.
- [ ] Implementar a funcionalidade para atribuir obreiros a um culto.
- [ ] Criar o serviço de API para gerenciar a escala.
- [ ] Implementar a funcionalidade "Copiar Escala do Mês" em um modal.
- [ ] Desenvolver a tela de revisão da cópia para resolver pendências.

**Fase 5: Finalização e Polimento**
- [ ] Criar componentes genéricos e reutilizáveis (ex: `Button`, `Input`, `Card`, `Modal`).
- [ ] Adicionar indicadores de carregamento (`loading spinners`) durante as chamadas de API.
- [ ] Adicionar feedback para o usuário (toasts/notificações) para sucesso e erro.
- [ ] Revisar a responsividade para diferentes tamanhos de tela.
- [ ] Implementar a funcionalidade de Exportação/Impressão (se aplicável).

5) Implementar Copiar Escala do Mês
- Entrada: mesOrigem, anoOrigem, mesDestino, anoDestino.
- Estratégia de data (escolher e documentar no sistema):
  - Semana/dia: para cada culto de origem, achar no destino a mesma semana do mês e mesmo dia da semana.
  - Dia do mês: usar o mesmo dia; se não existir (ex.: 31 em mês curto), mover para o último dia válido ou pedir confirmação.
- Processo:
  - Criar escala destino (ou usar existente).
  - Mapear cultos destino: se não existirem, criar com o mesmo local e nat_culto.
  - Para cada escala_item de origem:
    - Verificar se obreiro está ativo; se sim, vincular; se não, marcar pendência (obreiro_id = NULL e status pendente).
  - Registrar log de cópia (opcional) para auditoria.
- Revisão:
  - Tela lista pendências e conflitos; permitir resolver com dropdowns de obreiros ativos.

6) Garantias de seleção segura
- UI: todos os campos que referenciam FK são select contra listas da API.
- API: valida IDs contra entidades ativas; retornar erro claro.
- DB: FKs obrigatórias e ON DELETE RESTRICT.

7) Validação e Testes
- Casos:
  - Copiar de mês com 31 para mês com 30/28.
  - Obreiros inativados entre origem e destino.
  - Conflitos de horário ao copiar.
  - Performance com muitos cultos.
- Testes de unidade:
  - Função de mapeamento de datas.
  - Regras de integridade na API.
- Testes de integração:
  - Fluxo completo de cópia e revisão.

8) Exportação e Impressão (opcional)
- GET /api/escala/:id/export?format=pdf|csv.
- Tela com botão Imprimir usando estilos de impressão.

## Critérios de Aceitação
- Cadastro e listagem de obreiros/locais/Nat Culto funcionam e filtram apenas ativos.
- Agenda de cultos por mês com local e Nat Culto correta.
- Escala mensal exibe e permite atribuir obreiros via seleção.
- Copiar escala cria destino com mapeamento de datas escolhido, preserva local/Nat Culto e atribui obreiros ativos; pendências aparecem para revisão.
- Sistema impede conflitos de horário para um mesmo obreiro.
- Exportação/Impressão gera documento legível (se implementado).

## Boas Práticas
- Documentar claramente qual regra de mapeamento de datas foi adotada e deixar configurável.
- Manter logs de alterações de escala para rastreabilidade.
- Usar migrações de banco para evoluir o schema com segurança.
- Controle de acesso: perfis Pastor/Administrador para editar e Leitor para visualizar.

## Próximas Extensões
- Papéis diferentes por culto (leituras, música etc.) via campo papel em escala_item.
- Disponibilidade de obreiros (dias que podem servir) para sugerir atribuições.
- Notificações (email/WhatsApp) ao publicar escala.
- Multi-igreja (paróquias/campi) com segregação de dados.

## Instruções Obrigatórias para o Assistente de Código (Gemini)
1.  **Análise Obrigatória:** Ao receber este arquivo, você **deve** lê-lo por completo e entender todo o escopo, as regras e o passo a passo definidos. Este documento é a sua única fonte de verdade para este projeto.
2.  **Seguir o Plano:** Você **deve** seguir o "Passo a Passo de Implementação" na ordem definida. Não pule etapas e não espere que eu repita as instruções. Sua tarefa é me guiar através do plano.
3.  **Modo de Operação (Mentor):** Sua função é ser um mentor. Explique os conceitos, mostre exemplos de código para ilustrar, e me ajude a entender o "porquê" das coisas. Você **não deve** escrever o código final ou aplicá-lo nos arquivos por mim. Eu sou o programador; você é o guia.
4.  **Lembrete de Contexto:** Lembre-se de que você não tem memória entre chats. Você pode, e deve, me lembrar que eu preciso fornecer este arquivo de plano a cada nova conversa para garantir a continuidade.
5.  **Idioma:** Todas as suas respostas e explicações **devem** ser em português do Brasil.

## Como Exportar o Plano para PDF
- Pré-requisito: Node.js instalado.
- Comando: `npm run export:pdf`
- Saída: `PLANO_AUTOMACAO_ESCALA_IGREJA.pdf` gerado na raiz do projeto.
