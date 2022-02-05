# Desafio_CNPJ_ReceitaFederal

Pequeno desafio para um possível estágio, feito em 28/12/2021

## Guia

*Objetivo:* Construir um data pipeline desde a extração, até o processamento e exibição. (a linguagem pode ser da sua escolha, se for RUBY ganha BONUS POINTS)

*Processo:* Seguir os requisitos abaixo e ver minha explicação em video aqui

*Entrega:* Enviar zip para ***.com.br [se desejar colocar o codigo em um repositório tem que ser PRIVADO no gitlab ou github, me enviar a URL e compartilhar o acesso com meu email ;)]

*Projeto:* Obter dados de empresas da Receita Federal, limpar e formatar os dados, realizar cruzamentos simples e gerar CSV com os dados

## Etapas

1. Código ler um dos arquivos em CSVs [Dados Abertos CNPJ ESTABELECIMENTO XX da receita](https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj)  (BONUS POINTS: ler todos os arquivos ESTABELECIMENTO)

2. Organizar os dados num hash/dicionario

3. Salvar no mongodb localmente ou em cloud MongoAtlas (gratuito)
Eu escolheria o caminho mais simples aqui

4. Ler os dados do db e obter as seguintes informações:

    *a*. a qual % das empresas estão ativas (SITUAÇÃO CADASTRAL)

    *b.* Quantas empresas do setor de restaurantes foram abertas em cada ano ? (prefixo do CNAE PRINCIPAL e DATA DE INÍCIO ATIVIDADE)(prefixo de restaurantes 56.1xxxxx, ex: 5611-2/03 é restaurante)

    *c.* BONUS POINTS: quantas empresas num raio de 5km do cep 01422000

    *d.* BONUS POINTS: tabela de correlação de CNAE FISCAL PRINCIPAL com os CNAE FISCAL SECUNDÁRIA

5. Exportar os dados do ponto 4 para um CSV (BONUS POINTS: exportar para formato excel)

### Arquivos

- desafio_respostas.ipynb - Onde se encontram as respostas
- distance_locator.py - Código criado para usar a API do Google e verificar distâncias
- encoders.txt - Lista de encoders, em linhas, que servem para o csv
- index.txt - Lista de indexes, em linhas, para os campos dos dados
- txt_row_to_list.py - Transforma os arquivos de lista em linha, para lista em formato Python - encoders.txt - index.txt

### Arquivos gerados pelo 'desafio_respostas.ipynb'

- CNPJ_ativo.csv
- CNPJ_ativo.xlsx
- CNPJ_Setor_Restaurantes.csv
- CNP_Setor_Restaurantes.xlsx

### Anotações

- 'data situacao cadastral': '20161110'           <==== mudar tipo para data
- 'pais': '03'                                    <==== mudar tipo para int
- 'data de inicio atividade': '20050429'          <==== mudar tipo para data
- 'ddd 1': '11'                                   <==== mudar tipo para int
- 'telefone 1': '36491000'                        <==== mudar tipo para int
- 'ddd 2': '31.0'                                 <==== mudar tipo para int
- 'telefone 2': '33880436'                        <==== mudar tipo para int
- 'ddd do fax': '82.0'                            <==== mudar tipo para int
- 'fax': '33118379'                               <==== mudar tipo para int
- 'data da situacao especial': 'nan'              <==== mudar tipo para data
