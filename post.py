from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/method_post", methods=["GET", "POST"])
def method_post():
    return render_template("post_led.html")

@app.route('/method_post_act', methods=["GET",  "POST"])
def method_post_act():
    if request.method == "POST":
        NumLed = request.form["NumLed"]
        return render_template("post_led.html", NumLed=NumLed)
    
if __name__ == '__main__':
    app.run(debug=True, port=88, host='0.0.0.0')    
