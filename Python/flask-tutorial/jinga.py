# JINJA 2 ENGINE

# {{ }} - EXPRESSION TO PRINT
# {{%  %}} - IF/ FOR
# {{# #}} - COMMENTS 



from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")
    
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == "POST":
        name = request.form['name']
        return f'Hello, {name}'
    return render_template("form.html")

# @app.route('/submit', methods=['GET', 'POST'])
# def submit():
#     if request.method == "POST":
#         name = request.form['name']
#         return f'Hello, {name}'
#     return render_template("form.html")

@app.route("/success/<int:score>")
def success(score):
    # return f"The marks i scored is {score}"
    res = ""
    if score> 45:
        res = "PASSed"
    else:
        res = "FAILed"
    exp = {"res": res, "score":score}
    return render_template("result.html", result=exp)


@app.route('/submit', methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        sql = float(request.form['sql'])
        total_marks = (maths + c + sql)/3

        return redirect(url_for('success', score=total_marks))  # Pass as keyword arg

    return render_template('form.html')  # Or whatever your input form page is




if __name__ == "__main__":
    app.run(debug=True)