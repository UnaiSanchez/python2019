import requests
file=requests.get("https://pythonavanzado.techtalents.cloud/file.txt")
texto= file.text
position=texto.find("python",0,-1)
print(position)
my_data={
    "position":position
}
requests.get("http://192.168.20.144:8000",params=my_data)