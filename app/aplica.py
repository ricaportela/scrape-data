from flask import Flask, jsonify, request, url_for


app = Flask(__name__)

wordcounts = [
    {
        'keyword': u"Microfocus",
        'value': 45
    },
    {
        'keyword': u"Programador",
        'value': 33
    },
    {
        'keyword': u"Cobol",
        'value': 3
    },
]


@app.route("/search", methods=['GET'])
def search_keyword():
    query = request.args.get('query', '')
    for item in wordcounts:
        if item['keyword'] == query:
            return jsonify({'wordcounts': [item]})
    return jsonify({})

if __name__ == "__main__":
    app.run(debug=True)
