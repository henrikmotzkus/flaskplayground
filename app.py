from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        return render_template_string('''
            <!doctype html>
            <title>Flask Input</title>
            <h1>You entered: {{ user_input }}</h1>
            <form method="post">
                <input type="text" name="user_input" placeholder="Enter something">
                <button type="submit">Submit</button>
            </form>
        ''', user_input=user_input)
    return render_template_string('''
        <!doctype html>
        <title>Flask Input</title>
        <h1>Enter something below:</h1>
        <form method="post">
            <input type="text" name="user_input" placeholder="Enter something">
            <button type="submit">Submit</button>
        </form>
    ''')

if __name__ == "__main__":
    app.run(debug=True)