# inova-acao-afro
Projeto Desenvolvido durante o curso Inova Ação Afro - CESAR / SHARE RH

Curriculo: https://inovacaoafro.pythonanywhere.com

Git: https://github.com/blogdomarcio/inova-acao-afro

## Cartorios

    Base Cartorios_utf8.csv
    
    passo 1 : pyhton manage.py load_estados
    passo 2 : pyhton manage.py load_cidades
    passo 3 : pyhton manage.py load_bairros
    passo 4 : pyhton manage.py load_cartorios

  - https://inovacaoafro.pythonanywhere.com/cartorios/dashboard/
    
    <img src='https://marcioweb.s3.amazonaws.com/screen.PNG'>
    
    #### API's com Django Restframework
    
    | Endpoint  |  Método  |  Ação  |
    | ------------------- | ------------------- | ------------------- |
    |  https://inovacaoafro.pythonanywhere.com/cartorios |  GET |  Retorna lista de cartórios paginadas de 50 em 50 |
    |  https://inovacaoafro.pythonanywhere.com/cartorios/BA |  GET |  Retorna a lista de cartórios da UF paginadas de 50 em 50 |
    |  https://inovacaoafro.pythonanywhere.com/cartorios/2578  |  GET |  Retorna os detalhes de um cartório |
    |  https://inovacaoafro.pythonanywhere.com/cartorios |  POST |  Adiciona um novo cartório à base de dados |
    |  https://inovacaoafro.pythonanywhere.com/cartorios/2578 |  PUT |  Atualização completa de um cartório |
    |  https://inovacaoafro.pythonanywhere.com/cartorios/2578 |  PATCH |  Atualização Parcial de um cartório |
    |  https://inovacaoafro.pythonanywhere.com/cartorios/2578 |  DELETE |  Remove um cartório da base de dados |

    
    
    - https://inovacaoafro.pythonanywhere.com/cartorios/api-rest/
    - https://inovacaoafro.pythonanywhere.com/cartorios/api/lista-estados
    - https://inovacaoafro.pythonanywhere.com/cartorios/api/lista-cidades-estado/SP
    - https://inovacaoafro.pythonanywhere.com/cartorios/api/lista-cartorios-cidade/388
     
   ###### Lista Cartorios por Cidade: Itapetinga/BA - ID CIDADE: 388
   <img src='https://marcioweb.s3.amazonaws.com/api_cidades.PNG'>
   <img src='https://marcioweb.s3.amazonaws.com/itapetinga_full.PNG'>
    
## Cadastro de Pessoas

    Base people_data.csv
    
    passo 1 : pyhton manage.py load_people_data

   - https://inovacaoafro.pythonanywhere.com/pessoas
   - https://inovacaoafro.pythonanywhere.com/pessoas/api/maisnovas/json
   - https://inovacaoafro.pythonanywhere.com/pessoas/api/maisvelhas/json