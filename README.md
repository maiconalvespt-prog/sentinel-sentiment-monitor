# 🛡️ Sentinel: Monitor de Reputação em Tempo Real

Este projeto nasceu da minha curiosidade em entender como transformar dados brutos da web em informações visuais úteis. O **Sentinel** é um monitor que "sente o pulso" da mídia sobre qualquer tema, utilizando Python e Processamento de Linguagem Natural (NLP).

## 🧠 Por que construí este projeto?
Muitas ferramentas de monitoramento são complexas ou pagas. Eu queria criar algo acessível que mostrasse o ciclo completo do dado: desde a extração (Scraping), passando pela sanitização (Data Cleaning) e inteligência (NLP), até a entrega visual para o usuário final.

## 🛠️ Minhas Escolhas Técnicas
Durante o desenvolvimento, tomei decisões específicas para garantir a qualidade do software:

* **Arquitetura Modular:** Em vez de um script único, separei a lógica em `processor` (coleta e análise) e `utils` (limpeza). Isso facilita muito a manutenção e a escala do código.
* **Limpeza de Dados (Helpers):** Percebi que os títulos das notícias vinham com muitos caracteres especiais que "sujavam" a análise de sentimento. Criei um módulo específico de limpeza para normalizar os textos antes de processá-los.
* **Interface com Streamlit:** Escolhi o Streamlit pela rapidez em transformar scripts Python em dashboards profissionais e interativos, focando na experiência do usuário.

## 📂 Estrutura do Repositório
* `app.py`: O "maestro" que une todas as partes e renderiza o painel.
* `processor/scraper.py`: Motor de busca via RSS (Google News).
* `processor/analyzer.py`: Onde a mágica do NLP acontece usando TextBlob.
* `utils/helpers.py`: Funções para garantir que o dado chegue limpo e legível.

## 📈 Aprendizados e Desafios
O maior desafio foi lidar com o idioma e a ironia em textos curtos, o que me ensinou muito sobre os limites das bibliotecas de NLP atuais. Também aprimorei meu fluxo de trabalho com ambientes virtuais (`.venv`) e controle de versão com Git.

---
**Projeto desenvolvido por Maicon Alves**
*Focado em demonstrar habilidades em Engenharia de Dados, Clean Code e Python.*