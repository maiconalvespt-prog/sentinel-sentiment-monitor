# Coleta de dados (API ou Scraping)import feedparser

import feedparser
import logging
from datetime import datetime

# Configuração de logs para rastrear erros de conexão
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NewsFetcher:
    def __init__(self, topic: str):
        self.topic = topic
        # URL do Google News RSS
        self.url = f"https://news.google.com/rss/search?q={topic}&hl=pt-BR&gl=BR&ceid=BR:pt-419"

    def collect_news(self, limit: int = 10) -> list:
        """Coleta as notícias mais recentes sobre o tema."""
        logger.info(f"Iniciando coleta de notícias sobre: {self.topic}")
        
        try:
            feed = feedparser.parse(self.url)
            results = []

            for entry in feed.entries[:limit]:
                item = {
                    "title": entry.title,
                    "link": entry.link,
                    "published": entry.published,
                    "source": entry.source.title if 'source' in entry else "Desconhecido"
                }
                results.append(item)
                
            logger.info(f"{len(results)} notícias coletadas com sucesso.")
            return results
        except Exception as e:
            logger.error(f"Erro ao acessar o feed RSS: {e}")
            return []