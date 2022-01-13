# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

#the strategy to defeat all the bots is a variation of abbey's strategy
#instead of looking at the last two moves, we consider the last three moves

ideal_response = {"P": "S", "R": "P", "S": "R"}
last_played_opponent = {}

def player(prev_play, opponent_history=[]):
    if prev_play != "":
      opponent_history.append(prev_play)

    lookup_range = 3
    guess = "S"

    if len(opponent_history) > lookup_range:
        opponent_moves = "".join(opponent_history[-lookup_range:])

        if "".join(opponent_history[-(lookup_range + 1):]) in last_played_opponent.keys():
            last_played_opponent["".join(opponent_history[-(lookup_range + 1):])] += 1
        else:
            last_played_opponent["".join(opponent_history[-(lookup_range + 1):])] = 1
      
        potential_moves = [opponent_moves + "R", opponent_moves + "P", opponent_moves + "S"]

        for i in potential_moves:
          if not i in last_played_opponent.keys():
            last_played_opponent[i] = 0

        prediction = max(potential_moves, key=lambda key: last_played_opponent[key])[-1]

        guess = ideal_response[prediction]

    return guess
