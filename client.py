import requests
file_path= input.next("enter the filepath to the file you want to check")
APIkey= '631396087b7bdcd13074d93bccf5a69c8b5462ee5cc9018ddc4e1354e0df8137'

def scanFile(APIkey, file_path):
    url= 'https://www.virustotal.com/vtapi/v2/url/scan'
    request = requests.post(url, file_path, APIkey)
    result = request.json()

    if 'scan_id' in result:
        return result['scan_id']