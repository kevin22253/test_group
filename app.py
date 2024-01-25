from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play/<choice>')
def play(choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    result = determine_winner(choice, computer_choice)

    return jsonify({'player_choice': choice, 'computer_choice': computer_choice, 'result': result})

def determine_winner(player, computer):
    if player == computer:
        return 'It\'s a tie!'
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        return 'You win!'
    else:
        return 'Computer wins!'

if __name__ == '__main__':
    app.run(debug=True)
