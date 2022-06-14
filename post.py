import requests
res = requests.post('http://insecure.benax.rw/iot/', data={'device': 'Elissa-pc','distance':'20pyt'})
print(res.text)