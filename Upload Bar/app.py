from flask import render_template, request, make_response, jsonify, Flask

app = Flask(__name__)

@app.route("/upload-video", methods=["GET", "POST"])
def upload_video():

    if request.method == "POST":

        file = request.files["file"]

        print("File uploaded")
        print(file)

        res = make_response(jsonify({"message": "File uploaded"}), 200)

        return res

    return render_template("public/upload_video.html")

if __name__ == '__main__':
    app.run(debug=True)