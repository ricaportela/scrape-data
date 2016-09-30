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

@app.route("/search/wordcounts/<int:word_id>", methods=['GET'])
def search_id(word_id):
    wordcount = filter (lambda t: t['id'] == word_id, wordcounts)
    if len(wordcount) == 0:
        abort(404)
    return jsonify ( { 'wordcounts': wordcount[0] } )


if __name__ == "__main__":
    app.run(debug=True)
