from flask import Flask, jsonify, request, url_for


app = Flask(__name__)

wordcounts = [
    {
        'id': 1,
        'keyword': u"Microfocus",
        'value': 45
    },
    {
        'id': 2,
        'keyword': u"Programador",
        'value': 33
    },
    {
        'id': 34,
        'keyword': u"Cobol",
        'value': 3
    },
]


@app.route("/search/wordcounts", methods=['GET'])
def search():
    return jsonify ( { 'wordcounts': wordcounts } )

@app.route("/search/wordcounts/<int:id>", methods=['GET'])
def search_id(id):
    return jsonify ( { 'wordcounts': wordcounts[id] } )

@app.route("/search/wordcounts/<keyword>", methods=['GET'])
def search_keyword():
    query = request.args.get('query', '')
    for item in wordcounts:
        if item['keyword'] == query:
            return jsonify({'wordcounts' : [item]})
    return jsonify ({})



if __name__ == "__main__":
    app.run(debug=True)
