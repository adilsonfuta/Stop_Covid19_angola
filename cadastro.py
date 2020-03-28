import json
url="http://StopCovid19/angola_api/encontrar/Luanda"

api=json.encode(url)

api={
 "Luanda":{
     "id":1,
     "cidade":"Luanda",
     "casos":3,
     "suspeito":2,
     "descartados":0,
     "mortes":0
 }   
}

print(api)

