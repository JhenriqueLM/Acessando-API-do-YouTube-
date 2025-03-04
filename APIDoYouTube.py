import requests
import json
import pandas as pd 
from googleapiclient.discovery import build
from datetime import datetime

YouTubeChaveAPI = "AIzaSyCLFgAW5cA_VHzS_gosfzDnXykMa5LdEZY"
YouTube = build('YouTube','V3',developerKey= YouTubeChaveAPI)
playlistDoCanal = 'Arusu' # Canal M4rkim Blxck
conparandoDatas = 20120604
listaDeDatas = {}

def transformadoDeDatas (dataNoFormatoISO):
    dataIso = datetime.strptime(dataNoFormatoISO, "%Y-%m-%dT%H:%M:%SZ")
    dataTransformada =  dataIso.strftime("%d/%m/%Y ")
    #print(dataTransformada)
    return dataTransformada


Tokens =""

for x in range(5):
    print("primeiro loop")
    numeradoRDoVideoASerAnalizado = 0
    while True:
        responseCanal = YouTube.channels().list(part = "snippet,contentDetails,status ",  forUsername  = playlistDoCanal ).execute()
        print (responseCanal)
        idDaPlaylist = responseCanal ['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        print(idDaPlaylist)
        responsePlaylist = YouTube.playlistItems().list(part = "snippet,contentDetails,status", playlistId = idDaPlaylist, maxResults= 50, pageToken = Tokens  ).execute() 
        #print(responsePlaylist)
        datas = responsePlaylist['items'][numeradoRDoVideoASerAnalizado]['snippet']['publishedAt']
        datas = transformadoDeDatas(datas)
        print (datas)
        print(numeradoRDoVideoASerAnalizado)
        # Tokens = responsePlaylist.get("nextPageToken")
        # print(Tokens)
        listaDeDatas["DatasDeLancamento"] = datas
        Tokens = responsePlaylist.get("nextPageToken")
        print(Tokens)

        if Tokens == None:
            print(Tokens)
            print("Saindo do loop")
            break
        if numeradoRDoVideoASerAnalizado == 49:
            numeradoRDoVideoASerAnalizado = 0

        numeradoRDoVideoASerAnalizado = numeradoRDoVideoASerAnalizado + 1
    print("continuando coidigo")
    # x = True
# numeradoRDoVideoASerAnalizado = 0
# while True :
#     responseCanal = YouTube.channels().list(part = "snippet,contentDetails,status ",  forUsername  = playlistDoCanal ).execute()
#     #res = ( response['items'][1]['snippet']['publishedAt'])
#     #rint (responseCanal['items'][0]['id'])
#     idDaPlaylist = responseCanal ['items'][0]['contentDetails']['relatedPlaylists']['uploads']
#     #print(idDaPlaylist)
#     responsePlaylist = YouTube.playlistItems().list(part = "snippet,contentDetails,status", playlistId = idDaPlaylist, maxResults= 50 , pageToken = Tokens ).execute() 
#     datas =  responsePlaylist['items'][numeradoRDoVideoASerAnalizado]['snippet']['publishedAt']
#     datas = transformadoDeDatas(datas)
#     print(datas)
#     Tokens = responsePlaylist.get("nextPageToken")
#     listaDeDatas["DatasDeLancamento"] = datas
#     if Tokens == None:
#         print(Tokens)
#         print("Saindo do loop")
#         break

#     numeradoRDoVideoASerAnalizado = numeradoRDoVideoASerAnalizado + 1
    