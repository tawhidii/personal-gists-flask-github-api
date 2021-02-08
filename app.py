import requests
import json
from flask import Flask 
from flask import render_template
app = Flask(__name__)


@app.route("/")
def index():
	token = 'test-key'
	user_name = 'user-name'
	url = f'https://api.github.com/users/{user_name}/gists'
	headers = {
		    'Authorization': f'token {token}',
		    'Accept': 'application/vnd.github.v3+json',
	}

	r = requests.get(url,headers=headers)
	value = json.loads(r.content.decode('utf-8'))
	url_context = []
	desc_context = []
	for data in value:
		
		url_context.append(data['html_url'])
		desc_context.append(data['description']) 
	
	data_list = []
	for data_temp in zip(desc_context,url_context):
		data_list.append(data_temp)	



	context = {
		'data': data_list,	
	}
	
	return render_template('index.html',context=context)

if __name__ == '__main__':
	app.run()
