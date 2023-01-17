from flask import Flask
from flask import render_template
import json


app = Flask(__name__, template_folder = 'template')

@app.route('/')
def home() :
  f = open('media/data.json')
  data = json.load(f)
  f.close()
  return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
