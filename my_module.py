import pandas_datareader as data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from cProfile import label


def donwload_data(data_source = 'yahoo', start_date = '2000-01-01', end_date = '2021-12-31', 
                tickers = ['^IXIC','^DJI','^GSPC','^FCHI', '^GDAXI', '^N225', '^HSI', '^VIX']):
    """
    Fonction de récupération des indices dans un dictionnaire conentant tous les DataFrames
    INPUTS :
        data_source (string) : api utilisée pour récupérer les données
        start_date (string) : format date aaaa-mm-jj déterminant le début de la période
        end_date (string) : format date aaaa-mm-jj déterminant la fin de la période
        tickers (liste) : liste de ticker en type string à récupérer
    RETURN
        dictionnaire contenant tous les DataFrames
    """
    dict_df = {}
    for i in tickers:
        dict_df[i] = data.DataReader(i, data_source, start_date, end_date)

    return dict_df


def visualize(indice1, indice2, colonne, dict_df):
    """
    Fonction de visualisation des indices.
    INPUTS :
        indice1 (string) : premier indice
        indice2 (string) : deuxième indice
        colonne (string) : colonne retenue (open, close, high, low, etc)
        dict_df (dictionnaire) : dictionnaire contenant tous les DataFrames
    RETURN
        None
    """
    plt.figure(figsize = (15,15))
    plt.subplot(2,1,1)
    plt.plot(dict_df[indice1][colonne])
    plt.subplot(2,1,2)
    plt.plot(dict_df[indice2][colonne])
    plt.show()



def plot_ma(dict_df, indice1, colonne, list_of_windows = [7, 20, 200]):
    """
    Fonction de visualisation des indices.
    INPUTS :
        dict_df (dictionnaire) : dictionnaire contenant tous les DataFrames
        indice1 (string) : premier indice
        colonne (string) : colonne retenue (open, close, high, low, etc)
        list_of_windows (list of int) : fenêtre de moyenne mobile à déterminer
    RETURN
        None
    """
    plt.figure(figsize = (15,15))
    plt.subplot(2,1,1)
    plt.plot(dict_df[indice1][colonne])
    for window in list_of_windows:
        plt.plot(dict_df[indice1][colonne].rolling(window = window).mean(), label = f'Moving average {window}')
        plt.legend()
    plt.subplot(2,1,2)
    for window in list_of_windows:
        plt.plot(dict_df[indice1][colonne].rolling(window = window).std(), label = f'Variance {window}')
        # plt.yscale('log')
        # plt.ylim(0, 1e4)
    plt.show()


def plot_corr(indice1, indice2, colonne, dict_df):
    """
    Fonction de visualisation des correlations entre indice.
    INPUTS :
        indice1 (string) : premier indice
        indice2 (string) : deuxième indice
        colonne (string) : colonne retenue (open, close, high, low, etc)
        dict_df (dictionnaire) : dictionnaire contenant tous les DataFrames
    RETURN
        None
    """
    plt.figure(figsize = (15,15))
    plt.subplot(2,1,1)
    plt.plot(dict_df[indice1][colonne])
    plt.plot(dict_df[indice2][colonne])
    plt.subplot(2,1,2)
    plt.plot(dict_df[indice1][colonne].rolling(200).corr(dict_df[indice2][colonne]))
    plt.show()


# def graph_interactif2(ticker):
    
#     fig = go.Figure(data = [go.Candlestick(
#                             x = df1.index,
#                             open = dict_df['^IXIC']['Open'],
#                             high = dict_df['^IXIC']['High'],
#                             low = dict_df['^IXIC']['Low'],
#                             close = dict_df['^IXIC']['Close'])])

#     fig.add_trace(go.Scatter(
#                             x = df1.index,
#                             y = dict_df['^IXIC']['Close'].rolling(7).mean(),
#                             line = dict(color = '#FF8C00', width = 1, dash = 'dot'),
#                             name = '7 MA'))
#     fig.add_trace(go.Scatter(
#                             x = df1.index,
#                             y = dict_df['^IXIC']['Close'].rolling(20).mean(),
#                             line = dict(color = '#AFEEEE', width = 1, dash = 'dot'),
#                             name = '20 MA'))
#     fig.add_trace(go.Scatter(
#                             x = df1.index,
#                             y = dict_df['^IXIC']['Close'].rolling(200).mean(),
#                             line = dict(color = '#8B008B', width = 1, dash = 'dot'),
#                             name = '200 MA'))

#     fig.update_layout(xaxis_rangeslider_visible = False, template = 'plotly_dark')
    
#     for tick in ticker:
#         if ticker == '^IXIC':
#             tick = 'Nasdaq'
#             fig.update_layout(yaxis_title = f'{tick}', xaxis_title = 'Date')
#         elif ticker == '^DJI':
#             tick = 'Dow Jones'
#             fig.update_layout(yaxis_title = f'{tick}', xaxis_title = 'Date')
#         elif ticker == '^GSPC':
#             tick = 'SP500'
#             fig.update_layout(yaxis_title = f'{tick}', xaxis_title = 'Date')
#         elif ticker == '^FCHI':
#             tick = 'CAC 40'
#             fig.update_layout(yaxis_title = f'{tick}', xaxis_title = 'Date')
#         elif ticker == '^GDAXI':
#             tick = 'DAX 40'
#             fig.update_layout(yaxis_title = f'{tick}', xaxis_title = 'Date')
#         elif ticker == '^N225':
#             tick = 'Nikkei'
#             fig.update_layout(yaxis_title = f'{tick}', xaxis_title = 'Date')
#         elif ticker == '^HSI':
#             tick = 'Hangseng'
#             fig.update_layout(yaxis_title = f'{tick}', xaxis_title = 'Date')
#         elif ticker == '^VIX':
#             tick = 'VIX'
#             fig.update_layout(yaxis_title = f'{tick}', xaxis_title = 'Date')    
#     fig.show()


    