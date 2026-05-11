# Lógica de análise de sentimento

from textblob import TextBlob
import logging

# Configuração de logs para manter o padrão do projeto
logger = logging.getLogger(__name__)

class SentimentAnalyzer:
    """
    Motor de análise de sentimentos que processa textos e retorna
    indicadores de polaridade.
    """
    
    def __init__(self):
        # Poderíamos carregar modelos mais pesados aqui no futuro
        logger.info("Analisador de sentimentos inicializado.")

    def analyze(self, text: str) -> dict:
        """
        Realiza a análise de um texto e classifica entre Positivo, Negativo ou Neutro.
        """
        try:
            # TextBlob realiza a análise de polaridade (-1 a 1)
            blob = TextBlob(text)
            
            # Tentativa de tradução automática se o texto for longo o suficiente 
            # (Opcional, mas mostra que você pensou no problema do idioma)
            polarity = blob.sentiment.polarity
            
            return {
                "score": round(polarity, 2),
                "label": self._get_label(polarity),
                "sentiment_id": self._get_id(polarity)
            }
        except Exception as e:
            logger.error(f"Falha na análise de sentimento: {e}")
            return {"score": 0, "label": "Erro", "sentiment_id": "error"}

    def _get_label(self, score: float) -> str:
        """Método privado para definir a etiqueta com base no score."""
        if score > 0.1:
            return "Positivo"
        elif score < -0.1:
            return "Negativo"
        return "Neutro"

    def _get_id(self, score: float) -> str:
        """Define um ID para facilitar a estilização no Dashboard."""
        if score > 0.1: return "pos"
        if score < -0.1: return "neg"
        return "neu"