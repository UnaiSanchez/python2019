import requests
def generator():
    api_url = "https://random.dog/woof.json"  
    while True:
        result = requests.get(api_url)
        if result.status_code == 200:
            yield result.json()
        else:
            yield "failed"
dog_generator = generator()