# 🤖 IA Insights - Cobdesk

Sistema interativo de geração de infográficos dinâmicos alimentado por Inteligência Artificial.

---

## 🚀 Acesso Rápido

### 🌐 **Landing Page IA Insights**
👉 **https://anderson-cmyk.github.io/apresentacao-cobdesk/ia-insights.html**

### 🎬 **Apresentação Completa Cobdesk**
👉 **https://anderson-cmyk.github.io/apresentacao-cobdesk/apresentacao.html**

### 🔗 **API Backend**
👉 **https://5000-ij1s3ognzyyj9eepk3p6b-29c30d4d.manusvm.computer/api/generate**

---

## 📖 O que é?

O **IA Insights** é uma ferramenta web que permite fazer perguntas sobre comunicação, call centers e preferências de clientes, e receber respostas estruturadas em formato de infográfico profissional, geradas em tempo real por Inteligência Artificial (OpenAI GPT-4.1-mini).

---

## ✨ Funcionalidades

### 🎯 Três Cards Especializados

1. **💬 WhatsApp: O Canal Ideal**
   - Por que o WhatsApp é a melhor ferramenta de comunicação
   - Dados sobre uso no Brasil (165+ milhões de usuários)
   - Vantagens da comunicação assíncrona

2. **📞 Desafios de Call Center**
   - Problemas estruturais do setor
   - Baixos salários e alta rotatividade
   - Impacto na experiência do cliente

3. **👤 Preferência do Cliente**
   - Por que clientes preferem WhatsApp ao telefone
   - Dados comportamentais (93% preferem WhatsApp)
   - Tendências de comunicação

### 🎨 Recursos

- ✅ **Geração em tempo real** (3-8 segundos)
- ✅ **Infográficos profissionais** com design moderno
- ✅ **Histórico de até 10 infográficos** por sessão
- ✅ **Design responsivo** (mobile, tablet, desktop)
- ✅ **Interface intuitiva** estilo iOS 26 Light Theme
- ✅ **Respostas estruturadas** com título, pontos, estatísticas e conclusão

---

## 🎯 Como Usar

### Passo a Passo

1. **Acesse a página:** https://anderson-cmyk.github.io/apresentacao-cobdesk/ia-insights.html

2. **Selecione um card:** Clique em um dos 3 cards temáticos
   - 💬 WhatsApp
   - 📞 Call Center
   - 👤 Preferência do Cliente

3. **Digite sua pergunta:** No campo de texto, escreva uma pergunta relacionada ao tema
   - Exemplo: "Por que empresas devem usar WhatsApp?"

4. **Gere o infográfico:** Clique em "Gerar Infográfico" ou pressione Enter

5. **Aguarde:** A IA levará alguns segundos para processar

6. **Visualize:** Clique em "Ver Infográfico" na lista de histórico

7. **Explore:** Teste outros cards e perguntas!

---

## 🏗️ Tecnologias

### Frontend
- **HTML5** - Estrutura semântica
- **CSS3** - Design moderno com gradientes e animações
- **JavaScript ES6+** - Lógica interativa e chamadas à API
- **GitHub Pages** - Hospedagem gratuita

### Backend
- **Flask 3.1.1** - Framework web Python
- **OpenAI API** - GPT-4.1-mini para geração de conteúdo
- **Flask-CORS** - Suporte a requisições cross-origin
- **Python 3.11** - Linguagem de programação

---

## 📊 Exemplos de Perguntas

### Para o Card "WhatsApp"
- "Por que o WhatsApp é melhor que telefone?"
- "Quais as vantagens do WhatsApp para empresas?"
- "Como o WhatsApp melhora a experiência do cliente?"

### Para o Card "Call Center"
- "Quais os principais problemas dos call centers?"
- "Por que há tanta rotatividade em call centers?"
- "Como melhorar a qualidade do atendimento em call centers?"

### Para o Card "Preferência do Cliente"
- "Por que clientes não gostam de ligações telefônicas?"
- "Quais canais de comunicação os clientes preferem?"
- "Como a comunicação assíncrona beneficia o cliente?"

---

## 📚 Documentação

### Arquivos Disponíveis

- **[IA-INSIGHTS-DOCUMENTACAO.md](IA-INSIGHTS-DOCUMENTACAO.md)** - Documentação técnica completa (13.500+ palavras)
  - Arquitetura do sistema
  - Configuração técnica
  - Exemplos de uso
  - Troubleshooting
  - Roadmap futuro

- **[RELATORIO_FINAL_IA_INSIGHTS.md](RELATORIO_FINAL_IA_INSIGHTS.md)** - Relatório final do projeto
  - Resumo executivo
  - Componentes entregues
  - Testes realizados
  - Métricas de performance
  - Próximos passos

- **[GUIA_COMPLETO_APRESENTADOR.md](GUIA_COMPLETO_APRESENTADOR.md)** - Guia para apresentação
  - Roteiro completo
  - Dicas de apresentação
  - Perguntas frequentes

---

## 🎨 Screenshots

### Landing Page
![Landing Page](https://via.placeholder.com/800x400/667eea/ffffff?text=IA+Insights+-+Landing+Page)

*Interface principal com os 3 cards especializados*

### Infográfico Gerado
![Infográfico](https://via.placeholder.com/800x600/f5f7fa/333333?text=Infográfico+Gerado+por+IA)

*Exemplo de infográfico profissional gerado pela IA*

---

## 🔧 Para Desenvolvedores

### Executar Backend Localmente

```bash
# Navegar para o diretório da API
cd ia-insights-api

# Ativar ambiente virtual
source venv/bin/activate

# Instalar dependências (se necessário)
pip install -r requirements.txt

# Executar servidor Flask
python3 src/main.py
```

### Testar API com cURL

```bash
curl -X POST http://localhost:5000/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "cardId": "whatsapp",
    "question": "Por que o WhatsApp é melhor que telefone?"
  }'
```

### Estrutura do Projeto

```
apresentacao-cobdesk/
├── ia-insights.html              # Landing page principal
├── ia-insights-api/              # Backend Flask
│   ├── src/
│   │   ├── main.py              # App Flask
│   │   └── routes/
│   │       └── generate.py      # Endpoint de geração
│   ├── requirements.txt
│   └── venv/
├── apresentacao.html             # Apresentação completa
├── IA-INSIGHTS-DOCUMENTACAO.md   # Documentação técnica
└── RELATORIO_FINAL_IA_INSIGHTS.md # Relatório final
```

---

## 🚀 Roadmap Futuro

### Curto Prazo
- [ ] Deploy permanente do backend (Render/Railway)
- [ ] Persistência com LocalStorage
- [ ] Exportação de infográficos em PDF

### Médio Prazo
- [ ] Analytics e métricas de uso
- [ ] Novos cards especializados
- [ ] Sugestões de perguntas

### Longo Prazo
- [ ] Upload de dados para análise personalizada
- [ ] Geração de gráficos reais
- [ ] Integração com CRM

---

## 📞 Suporte

### Repositório
- **GitHub:** https://github.com/anderson-cmyk/apresentacao-cobdesk
- **Issues:** Reporte bugs e sugira melhorias

### Contato
- **Email:** [seu-email@cobdesk.com]
- **Website:** [www.cobdesk.com]

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

## 🎯 Status do Projeto

✅ **CONCLUÍDO E FUNCIONANDO**

- ✅ Frontend publicado e acessível
- ✅ Backend integrado com OpenAI
- ✅ Sistema testado e validado
- ✅ Documentação completa
- ✅ Pronto para uso em produção

---

**Desenvolvido com ❤️ para transformar atendimento ao cliente através de IA**

*Última atualização: 04/10/2025*

---

## 🔗 Links Rápidos

| Recurso | Link |
|---------|------|
| 🌐 **Landing Page** | https://anderson-cmyk.github.io/apresentacao-cobdesk/ia-insights.html |
| 🎬 **Apresentação** | https://anderson-cmyk.github.io/apresentacao-cobdesk/apresentacao.html |
| 📖 **Documentação** | [IA-INSIGHTS-DOCUMENTACAO.md](IA-INSIGHTS-DOCUMENTACAO.md) |
| 📊 **Relatório** | [RELATORIO_FINAL_IA_INSIGHTS.md](RELATORIO_FINAL_IA_INSIGHTS.md) |
| 💻 **Repositório** | https://github.com/anderson-cmyk/apresentacao-cobdesk |

---

**🚀 Experimente agora: https://anderson-cmyk.github.io/apresentacao-cobdesk/ia-insights.html**
