def rock_paper_scissors(player1, player2):
    moves = ['rock', 'paper', 'scissors']
    if player1 == player2:
        return "It's a tie"
    elif (player1=='rock' and player2=='scissors') or \
         (player1=='scissors' and player2=='paper') or \
         (player1=='paper' and player2=='rock'):
        return "Player 1 wins"
    else:
        return "Player 2 wins"

