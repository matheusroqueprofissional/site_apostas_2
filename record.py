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
    responsegetJogos = requests.get(f'{BASE_URL}?action=get_events&from=2023-05-01&to=2025-12-31&APIkey={API_KEY}')
    responsegetJogosPretty = json.dumps(responsegetJogos.json(), indent=5)
    return responsegetJogosPretty

def getStatus(match_id):
    responsegetStatus = requests.get(f'{BASE_URL}?action=get_statistics&match_id={match_id}&APIkye={API_KEY}')
    responsegetStatusPretty = json.dumps(responsegetStatus.json(), indent=6)
    return responsegetStatusPretty

    
#print(getLigasDisponiveis())
#print(getTimes(153))
#print(getTabela(3))
#print(getJogos())
#rint(getStatus(176164))

