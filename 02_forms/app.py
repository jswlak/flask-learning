from flask import Flask, render_template, request

app = Flask(__name__) 

@app.route('/')  
def home():
    return render_template('index.html')


@app.route('/greet', methods=['POST'])
def greet():
    username = request.form['username']  # Get data from form
    return render_template('greet.html', name=username)

if __name__ == '__main__':
    app.run(debug=True)  
