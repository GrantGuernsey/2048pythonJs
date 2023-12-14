# app.py
import json
from flask import Flask, render_template, jsonify
from twentyFourtyEightNonVisual import GamePlayer

app = Flask(__name__)

# Initialize the game player
game_player = GamePlayer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_game_state')
def get_game_state():
    game_state = game_player.get_board().tolist()
    total_score = game_player.get_total_score()
    game_status = game_player.is_game_over()
    return jsonify({'game_state': game_state, 'score': total_score, 'game_over' : game_status})

@app.route('/move/<direction>')
def move(direction):
    if direction in ['w', 's', 'a', 'd']:
        game_player.move(direction)
        game_state = game_player.get_board().tolist()
        total_score = game_player.get_total_score()
        game_status = game_player.is_game_over()
        return jsonify({'game_state': game_state, 'score': total_score, 'game_over' : game_status})
    else:
        return jsonify({'error': 'Invalid move'})

@app.route('/restart_game')
def restart_game():
    global game_player
    game_player = GamePlayer()
    game_state = game_player.get_board().tolist()
    total_score = game_player.get_total_score()
    game_status = game_player.is_game_over()
    return jsonify({'game_state': game_state, 'score': total_score, 'game_over' : game_status})
    
if __name__ == '__main__':
    app.run(debug=True)
