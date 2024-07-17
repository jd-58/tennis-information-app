import requests
import json

"""response = requests.get('https://tennis-live-data.p.rapidapi.com/players/ATP',
                        headers={
                            'x-rapidapi-host': 'tennis-live-data.p.rapidapi.com',
                            'x-rapidapi-key': '6bc8820a94msh69bfa3d71bd2ca9p1b0278jsne09e75704c76'})
players = response.json()
player2 = response.json()['results']
players = json.loads(players)
print(players)
"""


class User:
    def __init__(self, username, player, tournament, year, player_ranking, player_ranking_points, player_country):
        self._player = player
        self._tournament = tournament
        self._year = year
        self._player_ranking = player_ranking
        self._player_ranking_points = player_ranking_points
        self._player_country = player_country
        self._username = username

    def get_player(self):
        """Returns the player name"""
        return self._player

    def get_username(self):
        """Returns the username"""
        return self._username

    def get_tournament(self):
        """Returns the tournament name"""
        return self._tournament

    def get_year(self):
        """Returns the year"""
        return self._year

    def get_player_ranking(self):
        """Returns the player ranking"""
        return self._player_ranking

    def get_player_ranking_points(self):
        """Returns the player ranking points"""
        return self._player_ranking_points

    def get_player_country(self):
        """Returns the player country"""
        return self._player_country

    def set_player(self, player):
        """Sets the player name"""
        self._player = player
        return self._player

    def set_tournament(self, tournament):
        """Sets the tournament name"""
        self._tournament = tournament
        return self._tournament

    def set_year(self, year):
        """Sets the year"""
        self._year = year
        return self._year

    def set_username(self, username):
        """Sets the username"""
        self._username = username
        return self._username

    def set_player_ranking(self, player_ranking):
        """Sets the player ranking"""
        self._player_ranking = player_ranking
        return self._player_ranking

    def set_player_ranking_points(self, player_ranking_points):
        """Sets the player ranking points"""
        self._player_ranking_points = player_ranking_points
        return self._player_ranking_points

    def set_player_country(self, player_country):
        """Sets the player country"""
        self._player_country = player_country
        return self._player_country


jacob = User('jacob', 'Roger Federer', 'Wimbledon', 2021,
             None, None, 'Switzerland')


