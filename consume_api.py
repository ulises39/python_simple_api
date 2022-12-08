import requests
import json

base_url = 'https://api.chucknorris.io/jokes/random'

def idIsNotInArray(api_data, id_to_check):
    for data in api_data:
        if(data['id'] == id_to_check):
            print('Ids iguales: ' + id_to_check + ', ' + data['id'])
            return False
    
    return True

def consume_api(times=1):
    api_data = []
    
    i = 0
    while i < times: #iteramos hasta que se cumplan las n peticiones 
        data = requests.get(base_url)
        if( data.status_code == 200 ):
            data = data.json()
            #Validamos que no exista el id en el arreglo/lista
            if( idIsNotInArray(api_data, data['id'])):
                data['item'] = i
                api_data.append(data)
                i+=1
            # print(json.dumps(api_data, indent=4))
    return api_data

# results = consume_api(5)
# print(json.dumps(results, indent=4))