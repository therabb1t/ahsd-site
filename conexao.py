from flask import Flask, render_template
import subprocess

app = Flask(__name__)
@app.route('/')
def index():

    return render_template('index.html')

@app.route('/run_quiz1')
def run_quiz1():
    subprocess.Popen(['python', 'quiz1.py'])
    return "O quiz para Jovens foi iniciado."

@app.route('/run_quiz2')
def run_quiz2():
    subprocess.Popen(['python', 'quiz2.py'])
    return "O quiz para Responsáveis foi iniciado."

@app.route('/run_quiz3')
def run_quiz3():
    subprocess.Popen(['python', 'quiz3.py'])
    return "O quiz para Professores foi iniciado."

if __name__ == "__main__":
    app.run(debug=True)
