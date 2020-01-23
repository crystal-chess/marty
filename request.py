
import requests
import backoff

"""
The request handler.
"""
class Request:

    """
    Construct a new request handler.
    """
    def __init__(self, url, token):
        self.url = url;
        self.token = token;
        self.endpoints = [
            url + '/bot?token=' + token + '&arrows={}',
            url + '/bot?token=' + token + '&chat={}',
            url + '/bot?token=' + token + '&arrows=clear',
            url + '/bot?token=' + token + '&play={}',
            url + '/bot?token=' + token + '&play=R',
            url + '/bot?token=' + token + '&stream={}'
        ]

    """
    Make an arrow on the board.
    """
    def arrow(squareone, squaretwo):
        response = requests.get(self.endpoints[0] + squareone + squaretwo)
        return response.json
        
        

    """
    Send a message to the chat.
    """
    def chat(message):
        response = requests.get(self.endpoints[1] + message)
        return response.json

    """
    Clear the arrows on a board.
    """
    def clear():
        response = requests.get(self.endpoints[2])
        return response.json

    """
    Play a move.
    """
    def arrow(squareone, squaretwo, promotion):
        response = requests.get(self.endpoints[0] + squareone + squaretwo + promotion)
        return response.json

    """
    Resign a game.
    """
    def resign():
        response = requests.get(self.endpoints[4])
        return response.json

    
