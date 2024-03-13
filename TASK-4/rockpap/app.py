# app.py
from flask import Flask, render_template, request
from game_logic import get_computer_choice, determine_winner

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.form['user_choice']
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    return render_template('result.html', user_choice=user_choice.capitalize(), computer_choice=computer_choice.capitalize(), result=result)

if __name__ == '__main__':
    app.run(debug=True)
