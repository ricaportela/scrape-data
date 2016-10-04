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


@app.route("/search/<keyword>", methods=['GET'])
def search_keyword(keyword):
    for item in wordcounts:
        if item['keyword'] == keyword:
            return jsonify({'wordcounts': [item]})
        else:
            print("deu erro !!")

    return jsonify({})

if __name__ == "__main__":
    app.run(debug=True)
