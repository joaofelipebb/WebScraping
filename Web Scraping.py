#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup

def fazer_solicitacao(url):
    """Realiza uma solicitação GET para a URL e retorna o conteúdo da página."""
    try:
        response = requests.get(url)
        response.raise_for_status()  #Lança uma exceção se a solicitação não for bem-sucedida
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a solicitação: {e}")
        return None

def extrair_noticias(html_content):
    """Extrai informações de títulos, links e resumos de notícias a partir do conteúdo HTML."""
    noticias = []
    soup = BeautifulSoup(html_content, 'html.parser')
    
    #Encontra os elementos HTML que contêm as notícias
    news_elements = soup.find_all('div', class_='news-item')
    
    for news_element in news_elements:
        #Extrai o título da notícia
        title = news_element.find('h2', class_='news-title').text
        
        #Extrai o link da notícia
        link = news_element.find('a', href=True)['href']
        
        #Extrai o resumo da notícia (se disponível)
        summary_element = news_element.find('p', class_='news-summary')
        summary = summary_element.text if summary_element else "Resumo não disponível"
        
        noticias.append({'titulo': title, 'link': link, 'resumo': summary})
    
    return noticias

def exibir_noticias(noticias):
    """Exibe as notícias no console."""
    for idx, noticia in enumerate(noticias, start=1):
        print(f"Notícia {idx}:")
        print(f"Título: {noticia['titulo']}")
        print(f"Link: {noticia['link']}")
        print(f"Resumo: {noticia['resumo']}")
        print("----")

def main():
    url = 'https://example.com/news'
    
    #Faz a solicitação à página da web
    html_content = fazer_solicitacao(url)
    
    if html_content:
        #Extrai as notícias
        noticias = extrair_noticias(html_content)
        
        #Exibe as notícias
        exibir_noticias(noticias)
    else:
        print("Não foi possível obter o conteúdo da página.")

if __name__ == '__main__':
    main()


# In[ ]:




