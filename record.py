import requests
import json

API_KEY = "0daf50d6c4caa5f7ae3513bc52162612a78fd43fe65d6ea8842bb8cd8a26e914"
BASE_URL = "https://apiv3.apifootball.com"

def getPaisesDisponiveis():
    responseGetCountries = requests.get(f'{BASE_URL}/?action=get_countries&APIkey={API_KEY}')
    ListaFiltradaSemLogoPais = []

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

def getJogos():
    responsegetJogos = requests.get(f'{BASE_URL}?action=get_events&timezone=+07:00&APIkey={API_KEY}')
    responsegetJogosPretty = json.dumps(responsegetJogos.json(), indent=5)
    return responsegetJogosPretty

def getStatus():
    responsegetStatus = requests.get(f'{BASE_URL}?action=get_statistics&match_id=86392&APIkye={API_KEY}')
    responsegetStatusPretty = json.dumps(responsegetStatus.json(), indent=6)
    return responsegetStatusPretty

def getH2H():
    responsegetH2H = requests.get(f'{BASE_URL}?action=get_H2H&firstTeamId=7275&secondTeamId=151&APIkey={API_KEY}')
    responsegetH2HPretty = json.dumps(responsegetH2H.json(), indent=5)
    responsegetH2HPretty
    
#print(getLigasDisponiveis())
#print(getTimes(153))
#print(getTabela(153))
#print(getJogos(153))