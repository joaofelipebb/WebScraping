# WebScraping
O código em questão realiza a extração de informações de um site fictício de notícias e as exibe no console.
Ele pode ser personalizado para raspar dados de sites reais, desde que respeite os termos de uso e as políticas do site em questão.
Resumidamente, vou apresentar as funcionalidades deste código:
fazer_solicitacao(url): Realiza uma solicitação HTTP GET para uma URL especificada e retorna o conteúdo da página. Lida com erros de solicitação.
extrair_noticias(html_content): Analisa o conteúdo HTML da página web e extrai informações de títulos, links e resumos de notícias. Retorna uma lista de dicionários com essas informações.
exibir_noticias(noticias): Exibe as informações das notícias (título, link e resumo) no console.
main(): Ponto de entrada do programa. Define a URL da página, faz a solicitação, extrai e exibe as notícias.
Execução Principal: Verifica se o script está sendo executado como programa principal e inicia o web scraping.
