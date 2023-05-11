import requests
import json
import pytz

API_KEY = "0daf50d6c4caa5f7ae3513bc52162612a78fd43fe65d6ea8842bb8cd8a26e914"
BASE_URL = "https://apiv3.apifootball.com"
print("funciona")
def getPaisesDisponiveis():
    responseGetCountries = requests.get(f'{BASE_URL}/?action=get_countries&APIkey={API_KEY}')
    ListaFiltradaSemLogoPais = []
    print(responseGetCountries)
    for country in responseGetCountries.json():
        country.pop('country_logo', None)
        ListaFiltradaSemLogoPais.append(country)
    
    return ListaFiltradaSemLogoPais

def getLigasDisponiveis(country_id):
    responseGetLigasDisponiveis = requests.get(f'{BASE_URL}/?action=get_leagues&country_id={country_id}&APIkey={API_KEY}')
    ListaFiltradaSemLogoPaiseLiga = []

    for ligas in responseGetLigasDisponiveis.json():
        ligas.pop('league_logo',None)
        ligas.pop('country_logo',None)
        ListaFiltradaSemLogoPaiseLiga.append(ligas)

    return ListaFiltradaSemLogoPaiseLiga

def getTimes(league_id):
    responseGetTimes = requests.get(f'{BASE_URL}/?action=get_teams&league_id={league_id}&APIkey={API_KEY}')
    responseGetTimesPretty = json.dumps(responseGetTimes.json(), indent=4)
    return responseGetTimesPretty

def getTabela(league_id):
    responseGetTabela = requests.get(f'{BASE_URL}/?action=get_standings&league_id={league_id}&APIkey={API_KEY}')
    responseGetTabelaPretty = json.dumps(responseGetTabela.json(), indent=4)
    return responseGetTabelaPretty

def getJogos(league_id):
    tz = pytz.timezone('America/Sao_Paulo')
    responsegetJogos = requests.get(f'{BASE_URL}?action=get_events&from=2023-07-12&to=2023-12-31&league_id={league_id}&APIkey={API_KEY}')
    responsegetJogosPretty = json.dumps(responsegetJogos.json(), indent=5)
    print(responsegetJogos)
    return responsegetJogosPretty

#print(getLigasDisponiveis())
#print(getTimes(153))
#print(getTabela(153))
print(getJogos(153))