from flask import Flask, render_template

app = Flask(__name__)  # Create app instance

@app.route('/')  # Define route
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)  # Run app with debugging
