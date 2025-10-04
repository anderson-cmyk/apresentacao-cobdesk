# 🤖 IA Insights - Cobdesk
## Sistema de Geração de Infográficos Dinâmicos com IA

---

## 📋 Visão Geral

O **IA Insights** é um sistema interativo de geração de infográficos alimentado por Inteligência Artificial (OpenAI GPT-4.1-mini) que permite aos usuários fazer perguntas sobre três áreas especializadas e receber respostas estruturadas em formato de infográfico profissional.

### 🎯 Objetivo

Fornecer insights baseados em IA sobre:
1. **WhatsApp como canal ideal de comunicação**
2. **Desafios da indústria de call centers**
3. **Preferências dos clientes em comunicação**

---

## 🏗️ Arquitetura do Sistema

### Frontend
- **Tecnologia:** HTML5, CSS3, JavaScript Vanilla
- **Design:** iOS 26 Light Theme inspirado
- **Responsividade:** Mobile-first, adaptável a todos os dispositivos
- **Hospedagem:** GitHub Pages
- **URL:** https://anderson-cmyk.github.io/apresentacao-cobdesk/ia-insights.html

### Backend
- **Framework:** Flask (Python 3.11)
- **API:** OpenAI GPT-4.1-mini
- **CORS:** Habilitado para requisições do GitHub Pages
- **Hospedagem:** Servidor público temporário
- **URL da API:** https://5000-ij1s3ognzyyj9eepk3p6b-29c30d4d.manusvm.computer/api/generate

### Integração
- **Protocolo:** REST API (JSON)
- **Método:** POST
- **Endpoint:** `/api/generate`
- **Autenticação:** API Key OpenAI (configurada no servidor)

---

## 🎨 Funcionalidades

### 1. Seleção de Cards Especializados

Três cards temáticos com contextos específicos:

#### 💬 Card 1: WhatsApp - O Canal Ideal
- **Foco:** Defender o WhatsApp como ferramenta de comunicação não invasiva
- **Contexto:** 165+ milhões de usuários no Brasil, zero franquia de dados, comunicação assíncrona
- **Tipo de resposta:** Vantagens competitivas, dados de mercado, benefícios para empresas

#### 📞 Card 2: Desafios de Call Center
- **Foco:** Análise crítica dos problemas estruturais do setor
- **Contexto:** Baixos salários (R$ 1.500-2.000), alta rotatividade (60-80%), instalações precárias
- **Tipo de resposta:** Problemas identificados, impactos, sugestões de melhoria

#### 👤 Card 3: Preferência do Cliente
- **Foco:** Perspectiva do consumidor sobre canais de comunicação
- **Contexto:** 93% preferem WhatsApp, telefone é invasivo, comunicação assíncrona
- **Tipo de resposta:** Razões da preferência, dados comportamentais, tendências

### 2. Geração de Infográficos com IA

**Fluxo de funcionamento:**

1. Usuário seleciona um card temático
2. Digita uma pergunta ou contexto
3. Sistema envia requisição para backend Flask
4. Backend processa com prompt especializado
5. OpenAI GPT-4.1-mini gera resposta estruturada em JSON
6. Frontend renderiza infográfico HTML dinâmico
7. Infográfico é exibido em nova aba (blob URL)

**Estrutura da resposta da IA:**

```json
{
  "title": "Título impactante",
  "points": [
    "Ponto principal 1",
    "Ponto principal 2",
    "Ponto principal 3",
    "Ponto principal 4",
    "Ponto principal 5"
  ],
  "stats": [
    "Estatística 1 com dados concretos",
    "Estatística 2 com dados concretos"
  ],
  "conclusion": "Conclusão clara e objetiva",
  "cardId": "whatsapp|callcenter|preferencia",
  "question": "Pergunta original do usuário",
  "timestamp": "2025-10-04T23:06:29.220196"
}
```

### 3. Histórico de Infográficos

- **Capacidade:** Até 10 infográficos por sessão
- **Comportamento:** FIFO (First In, First Out) - remove o mais antigo quando excede 10
- **Armazenamento:** Memória local (JavaScript) - limpa ao recarregar página
- **Visualização:** Lista com card, pergunta, timestamp e link para visualização

### 4. Design Profissional

**Características visuais:**

- **Paleta de cores:** Gradiente roxo (#667eea → #764ba2)
- **Tipografia:** SF Pro Display, system fonts
- **Ícones:** Emojis nativos para acessibilidade
- **Animações:** Hover states, transições suaves
- **Cards:** Bordas arredondadas, sombras sutis, efeito de elevação
- **Responsividade:** Breakpoints para mobile, tablet e desktop

**Layout dos infográficos:**

- Header com ícone e título
- Badge "✨ Gerado por IA"
- Seções com títulos coloridos
- Lista de pontos com checkmarks
- Caixas de destaque para estatísticas
- Footer com timestamp e branding

---

## 🔧 Configuração Técnica

### Backend Flask

**Estrutura de diretórios:**

```
ia-insights-api/
├── src/
│   ├── __init__.py
│   ├── main.py                 # Aplicação Flask principal
│   ├── routes/
│   │   ├── generate.py         # Rota de geração de infográficos
│   │   └── user.py             # Rotas de usuário (template)
│   ├── models/
│   │   └── user.py             # Modelos de dados (template)
│   ├── database/
│   │   └── app.db              # SQLite database
│   └── static/
│       ├── favicon.ico
│       └── index.html
├── requirements.txt            # Dependências Python
└── venv/                       # Ambiente virtual
```

**Dependências principais:**

```
Flask==3.1.1
flask-cors==6.0.0
openai==2.1.0
Flask-SQLAlchemy==3.1.1
```

**Prompts especializados:**

Cada card possui um prompt otimizado que:
- Define o papel da IA (especialista em X)
- Fornece contexto específico com dados
- Instrui sobre formato de resposta JSON
- Solicita título, pontos, estatísticas e conclusão

### Frontend

**Tecnologias utilizadas:**

- **HTML5:** Estrutura semântica
- **CSS3:** Gradientes, flexbox, grid, animações
- **JavaScript ES6+:** Async/await, fetch API, template literals
- **Blob URLs:** Para renderização de infográficos em memória

**Funções principais:**

```javascript
selectCard(cardType)              // Seleciona card temático
generateInfographic()             // Inicia geração
callBackendAPI(question)          // Chama API Flask
generateInfographicHTMLFromAPI()  // Renderiza com dados da IA
generateInfographicHTML()         // Fallback estático
renderInfographics()              // Atualiza lista de histórico
```

**Detecção de ambiente:**

```javascript
const API_URL = window.location.hostname === 'localhost' 
    ? 'http://localhost:5000/api/generate'
    : 'https://5000-ij1s3ognzyyj9eepk3p6b-29c30d4d.manusvm.computer/api/generate';
```

---

## 🚀 Como Usar

### Para Usuários Finais

1. **Acesse a página:** https://anderson-cmyk.github.io/apresentacao-cobdesk/ia-insights.html
2. **Selecione um card:** Clique em um dos 3 cards temáticos
3. **Digite sua pergunta:** No campo de texto, escreva uma pergunta relacionada ao tema
4. **Gere o infográfico:** Clique em "Gerar Infográfico" ou pressione Enter
5. **Aguarde processamento:** A IA levará 3-8 segundos para gerar a resposta
6. **Visualize o resultado:** Clique em "Ver Infográfico" na lista de histórico
7. **Explore outros temas:** Selecione outro card e repita o processo

### Para Desenvolvedores

**Executar backend localmente:**

```bash
cd ia-insights-api
source venv/bin/activate
python3 src/main.py
```

**Testar API com curl:**

```bash
curl -X POST http://localhost:5000/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "cardId": "whatsapp",
    "question": "Por que o WhatsApp é melhor que telefone?"
  }'
```

**Modificar prompts:**

Edite o arquivo `src/routes/generate.py` e ajuste os dicionários em `PROMPTS`.

**Atualizar frontend:**

1. Edite `ia-insights.html`
2. Commit e push para GitHub
3. GitHub Pages atualiza automaticamente

---

## 📊 Exemplos de Uso

### Exemplo 1: WhatsApp

**Pergunta:** "Por que empresas devem usar WhatsApp para atendimento ao cliente?"

**Resposta gerada:**

- **Título:** "WhatsApp: Comunicação Saudável e Eficiente"
- **Pontos:**
  - Comunicação assíncrona permite responder no próprio ritmo
  - Não invasivo, ao contrário de ligações telefônicas
  - Zero franquia de dados pelas operadoras
  - Histórico escrito de todas as conversas
  - 165+ milhões de usuários ativos no Brasil
- **Estatísticas:**
  - Mais de 165 milhões de usuários ativos
  - Canal líder em volume de transações no país
- **Conclusão:** "Por ser acessível, não invasivo e amplamente utilizado, o WhatsApp supera o telefone tradicional"

### Exemplo 2: Call Center

**Pergunta:** "Quais os principais problemas dos call centers?"

**Resposta gerada:**

- **Título:** "Desafios estruturais crônicos dos call centers no Brasil"
- **Pontos:**
  - Baixos salários (R$ 1.500-2.000) geram desmotivação
  - Rotatividade de 60-80% ao ano
  - Infraestrutura inadequada e instalações precárias
  - Pressão por metas agressivas reduz qualidade
  - Falta de investimento em treinamento
- **Estatísticas:**
  - Turnover anual entre 60-80%
  - Salários médios de R$ 1.500-2.000
- **Conclusão:** "Esses desafios impactam diretamente a experiência do cliente"

### Exemplo 3: Preferência do Cliente

**Pergunta:** "Por que clientes preferem WhatsApp ao telefone?"

**Resposta gerada:**

- **Título:** "Cliente no Controle: A Revolução da Comunicação Assíncrona"
- **Pontos:**
  - Telefone é invasivo e interrompe atividades
  - Difícil acesso - nem sempre é possível atender
  - WhatsApp permite responder no melhor momento
  - Conforto de comunicar-se por texto
  - Histórico sempre disponível
- **Estatísticas:**
  - 93% dos brasileiros preferem WhatsApp
  - 87% consideram ligações "inconvenientes"
- **Conclusão:** "O futuro da comunicação é assíncrono e centrado no cliente"

---

## 🔐 Segurança e Privacidade

### Dados do Usuário

- **Não armazenamos:** Perguntas, respostas ou dados pessoais
- **Sessão:** Dados mantidos apenas em memória do navegador
- **Limpeza:** Histórico é perdido ao fechar/recarregar página

### API OpenAI

- **API Key:** Armazenada apenas no servidor backend
- **Não exposta:** Frontend não tem acesso direto à chave
- **Rate limiting:** Controlado pelo servidor Flask

### CORS

- **Configuração:** Permite requisições apenas de domínios autorizados
- **Headers:** Content-Type: application/json
- **Métodos:** POST apenas

---

## 📈 Métricas e Performance

### Tempos de Resposta

- **Frontend → Backend:** ~100-300ms
- **Backend → OpenAI:** ~2-6 segundos
- **Renderização:** ~50-100ms
- **Total:** ~3-8 segundos por infográfico

### Custos

- **OpenAI API:** ~$0.001-0.003 por requisição (GPT-4.1-mini)
- **GitHub Pages:** Gratuito
- **Servidor backend:** Variável conforme hospedagem

### Capacidade

- **Requisições simultâneas:** Limitado pelo servidor Flask
- **Infográficos por sessão:** 10 (limite configurável)
- **Tamanho da resposta:** ~500-1500 tokens

---

## 🛠️ Manutenção e Atualizações

### Atualizar Prompts

1. Edite `ia-insights-api/src/routes/generate.py`
2. Modifique os dicionários em `PROMPTS`
3. Reinicie o servidor Flask
4. Teste com diferentes perguntas

### Adicionar Novo Card

1. **Frontend:** Adicione novo card HTML em `ia-insights.html`
2. **JavaScript:** Adicione entrada em `cardPrompts`
3. **Backend:** Adicione prompt em `PROMPTS` do `generate.py`
4. **Teste:** Verifique integração completa

### Mudar Modelo de IA

No arquivo `generate.py`, altere:

```python
response = client.chat.completions.create(
    model="gpt-4.1-mini",  # Altere aqui
    ...
)
```

Modelos disponíveis: `gpt-4.1-mini`, `gpt-4.1-nano`, `gemini-2.5-flash`

---

## 🐛 Troubleshooting

### Problema: Infográfico não é gerado

**Possíveis causas:**
- Backend offline
- API OpenAI com erro
- CORS bloqueado
- Timeout de rede

**Solução:**
1. Verifique console do navegador (F12)
2. Teste endpoint da API diretamente
3. Verifique logs do Flask
4. Confirme API key OpenAI válida

### Problema: Resposta vazia ou erro

**Possíveis causas:**
- Prompt mal formatado
- Resposta não é JSON válido
- Timeout da API OpenAI

**Solução:**
1. Verifique formato do prompt
2. Adicione `response_format={"type": "json_object"}`
3. Aumente timeout da requisição

### Problema: Design quebrado

**Possíveis causas:**
- CSS não carregado
- JavaScript com erro
- Navegador incompatível

**Solução:**
1. Limpe cache do navegador
2. Verifique console de erros
3. Teste em navegador moderno (Chrome, Firefox, Safari)

---

## 🔮 Roadmap Futuro

### Melhorias Planejadas

1. **Persistência de dados:**
   - LocalStorage para manter histórico entre sessões
   - Opção de exportar infográficos em PDF

2. **Compartilhamento:**
   - Gerar URLs públicas para infográficos
   - Botões de compartilhamento social

3. **Personalização:**
   - Escolha de temas de cores
   - Customização de fontes e tamanhos

4. **Analytics:**
   - Rastreamento de perguntas mais comuns
   - Métricas de uso por card

5. **Novos cards:**
   - Automação de atendimento
   - ROI de tecnologia
   - Casos de sucesso

6. **Recursos avançados:**
   - Upload de dados para análise
   - Geração de gráficos reais
   - Comparação entre infográficos

---

## 📞 Suporte e Contato

### Repositório GitHub

- **Frontend:** https://github.com/anderson-cmyk/apresentacao-cobdesk
- **Issues:** Reporte bugs e sugira melhorias

### Documentação Adicional

- **Guia do Apresentador:** `GUIA_COMPLETO_APRESENTADOR.md`
- **README:** `README.md`
- **Relatório de Correções:** `RELATORIO_CORRECOES.md`

---

## 📄 Licença

Este projeto foi desenvolvido para **Cobdesk** como parte de uma apresentação interativa sobre soluções de atendimento ao cliente.

---

## 🙏 Agradecimentos

- **OpenAI** pela API GPT-4.1-mini
- **GitHub Pages** pela hospedagem gratuita
- **Flask** pelo framework backend simples e eficiente
- **Comunidade open source** pelas ferramentas e bibliotecas

---

**Desenvolvido com ❤️ para transformar atendimento ao cliente através de IA**

*Última atualização: 04/10/2025*
