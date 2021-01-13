from rejson import Client, Path
import json

with open('books2.json', 'r') as f:
	data = json.load(f)

rj = Client(host='127.0.0.1', port=6379, decode_responses=True)

for key, val in data.items():
	rj.jsonset(str(key), Path.rootPath(), val)
	
	


