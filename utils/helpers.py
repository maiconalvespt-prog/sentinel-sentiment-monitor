# Limpeza de texto e formatação

import re
import string

def clean_text(text: str) -> str:
    """
    Remove URLs, caracteres especiais e excesso de espaços.
    Isso ajuda o analisador de sentimento a ser mais preciso.
    """
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # Remove pontuação (opcional, dependendo da análise)
    # text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Remove espaços duplos e quebras de linha
    text = " ".join(text.split())
    
    return text.strip()

def format_date(raw_date: str) -> str:
    """
    Normaliza as datas vindas de diferentes fontes para um padrão legível.
    """
    # Aqui você pode usar bibliotecas como 'dateutil' se as fontes forem variadas
    return raw_date.replace("+0000", "").strip()

def truncate_text(text: str, limit: int = 100) -> str:
    """
    Corta o texto para exibição no dashboard sem quebrar palavras ao meio.
    """
    if len(text) <= limit:
        return text
    return text[:limit].rsplit(' ', 1)[0] + "..."