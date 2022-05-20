from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def hello_world():
    json = request.get_json()
    user_city = json["resume"]["city"]
    user_remote = json["resume"]["remote"]
    vacancies = json["vacancies"]
    result = []
    for vacancie in vacancies:
        result.append(
            {
                "id": vacancie["id"],
                "score": 1 if vacancie["city"] == user_city or (vacancie["remote"] and user_remote) else 0,
            }
        )
    print(result, flush=True)
    return jsonify(result)


if __name__ == "__main__":
    app.run("0.0.0.0", port=5001, debug=True)
