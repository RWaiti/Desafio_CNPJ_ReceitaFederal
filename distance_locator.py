import requests
import time

def distance(origem, df_destino):
    APIkey = ""
    origem = origem # "01422000"
    count = 0
    list_close = []
    list_without_result = []

    for doc in df_destino:
        destino = ""
        
        try:
            destino = destino + str(doc["bairro"])
        except:
            print("",end="")
            
        try:
            destino = destino + "%20" + str(doc["cep"])
        except:
            print("",end="")
            
        try:
            destino = destino + "%20" + str(doc["uf"])
        except:
            print("",end="")
        
        if destino == "":
            continue
        
        destino = destino.replace(" ","%20")
        
        url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins={}&destinations={}&key={}".format(origem, destino, APIkey)
        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        
        print(response.json()["rows"][0]["elements"][0]["status"], destino)
        
        # Se não achar ou não houver resultados salva a parte, para possível pesquisa diferente (com mais detalhes, ou menos)
        if response.json()["rows"][0]["elements"][0]["status"] in ["NOT_FOUND", "ZERO_RESULTS"]:
            list_without_result = list_without_result + [doc]
            continue

        dist = response.json()["rows"][0]["elements"][0]["distance"]["value"]
        
        count += 1
        if dist <= 5000:
            list_close = list_close + [doc]
            
    return list_close, list_without_result