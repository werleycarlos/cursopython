from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt

# url da pagina alvo

url = 'https://www.themoviedb.org/movie'

# cabeçalho com user-agent para simular um navegador especifico
headers0 = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36' }

# fazendo a requisição com o cabeçalho e a url alvo

response = requests.get(url, headers=headers0)

#verificar se a resposta foi positiva

if response.status_code == 403:
    print(f'Erro {response.status_code}: não autorizado.')
elif response.status_code != 200:
    print(f'Erro {response.status_code}: não fpo possível acessar a página.')
# se passou daqui, tudo deu certo ao capturar a página, então vamos realizar o screapping
else: 
    # realizar o parse no conteúdo html
    soup = BeautifulSoup(response.text, 'html.parser')

    # verificar a estrutura html para ver o que está retornando
    # print(soup.prettify()[:1000])

    # selecionando os filmes da página
    movies = soup.find_all('div', class_ ='card style_1')
    print(f'Total de filmes: {len(movies)}')
    # verifica quantos filmes foram encontrados

    # listar e armazenar as informações dos filmes

    movies_list = []

    #iterando sobre os filmes para extrair as informações

    for movie in movies:
        try:
            #extração do título
            title_tag = movie.find('a', class_ = 'image')
            nome_filme = title_tag['title'] if title_tag else 'titulo não encontrado'

            date_tag = movie.find('p')
            release_date = date_tag.get_text(strip=True) if date_tag else "Data não encontrada"

            mes = release_date[6:9]


           # title = movie.find('h2', class_='card-title'.get_text(strip=True))

            tabela = {'titulo': nome_filme, 'Data': release_date}

           # if nome_filme != 'titulo não encontrado':
            movies_list.append(tabela)

        except Exception as travou:
            print(f'Erro ao processar o filme: {travou}')
    # convertendo os dados em um dataflame
    df = pd.DataFrame(movies_list)

    #exibir resultados
    if not df.empty:
        print(df)

        print("dados das datas extraidas", df['Data'].head())
        df['Data'] = pd.to_datetime(df['Data'], format='%d de %b de %Y', errors="coerce")
        


        # salvar em csv
        df.to_csv('movies.csv', index=False)
        print('Tabela salva com sucesso')
        # garantir que as datas  sejam corretamente interpretadas
        df['Data'] = pd.to_datetime(df['Data'], errors='coerce')

        # extraindo o mês do ano
        df['Mês/Ano'] = df['Data'].dt.to_period('M')
        
        # contagem de filmes por mês
        filmes_por_mes = df['Mês/Ano'].value_counts().sort_index()

        
        #plotar o gráfico de barras
        plt.figure(figsize=(10,6))
        filmes_por_mes.plot(kind='bar', color='skyblue')
        plt.title('Qtde de filmes por mês')
        plt.xlabel('Mês/Ano')
        plt.ylabel('Qtde de Filmes')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        plt.figure(figsize=(10,6))
        filmes_por_mes.plot(kind='pie', color='skyblue')
        plt.title('Qtde de filmes por mês')
        plt.tight_layout()
        plt.show()

    else:
        print("Nenhum dado encontrado.")










