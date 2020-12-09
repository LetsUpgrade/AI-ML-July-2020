from flask import Flask

# Instantiate the Flask app
app = Flask(__name__)

@app.route('/') # Home directory
def hello():
    return "<h1>Hello AI-ML Batch 1 Students. Congratulations to all of you.</h1>"

# If you want to run this app, you must call the run()
if __name__== '__main__':
    app.run(debug=True)

