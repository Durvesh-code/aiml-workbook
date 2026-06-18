from flask import Flask, flash, render_template, url_for, request, jsonify
# url_for generate the dynamic url for us
# using this static_folder we can change the flask default files finding path old => static new => assests
app = Flask(__name__)  # static_folder= "assests", static_url_path="/assests"

app.secret_key("dsjfklsdjklfjsdlfjlkfjsdkljfjdsk")

@app.route("/")
def hello_world():
    # static file => dynamically generate url
    # print(url_for("static", filename= "style.css"))
    return render_template("index.html")

@app.route("/contact")
def contact():
    flash("support timings are from 9-5")
    return render_template("contact.html")


# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         name = request.form["username"]
#         password = request.form["password"]

#         # send it to database & verify
#         return render_template("welcome.html", name=name, password=password)
#         # return "<p> This route is to handle login </p>"
#     else:
#         return render_template("login.html")
    

    # if request.method == "GET":
    #     return "<p> GET Method"

if __name__ == "__main__":
    app.run(debug=True)
