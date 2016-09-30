from flask import Flask, jsonify, request, url_for
from pydojo.core import core_blueprint
from pydojo.core.utils import id_generator
from pydojo.core.forms import CodeEditorForm
from scrapy import scrapy_function
import validators


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/pesquisa", methods=['GET'])
def pesquisa(haskey):
    if form.validate_on_submit():
        form.save()
    return jsonify{'contagem': contagem}

def uri_validator(url_pesquisa):
    try:
        return True if validators.url(url_pesquisa) else False
    except:
        return False

if __name__ == "__main__":
    app.run(debug=True)
