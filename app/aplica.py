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

@app.route("/search/wordcounts/<str:keyword>", methods=['GET'])
def search_word(keyword):
    
    return jsonify ( { 'wordcounts': wordcount[0] } )


if __name__ == "__main__":
    app.run(debug=True)
