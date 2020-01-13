from app import db
from sqlalchemy.dialects.postgresql import JSON

class Match(db.Model):
    __tablename__ = 'matches'

    id = db.Column(db.Integer, primary_key=True)
    season = db.Column(db.String())
    city = db.Column(db.String())
    date = db.Column(db.Date())
    team1 = db.Column(db.String())
    team2 = db.Column(db.String())
    toss_winner = db.Column(db.String())
    toss_decision = db.Column(db.String())
    result = db.Column(db.String())
    dl_applied = db.Column(db.Boolean())
    winner = db.Column(db.String())
    win_by_runs = db.Column(db.Integer())
    win_by_wickets = db.Column(db.Integer())
    player_of_match = db.Column(db.String())
    venue = db.Column(db.String())
    umpire1 = db.Column(db.String())
    umpire2 = db.Column(db.String())
    umpire3 = db.Column(db.String())

    def __init__(self, season, city, date, team1, team2, toss_winner, toss_decision, result, dl_applied, winner, win_by_runs, win_by_wickets, player_of_match, venue, umpire1, umpire2, umpire3):
        self.season = season
        self.city = city
        self.date = date
        self.team1 = team1
        self.team2 = team2
        self.toss_winner = toss_winner
        self.toss_decision = toss_decision
        self.result = result
        self.dl_applied = dl_applied
        self.winner = winner
        self.win_by_runs = win_by_runs
        self.win_by_wickets = win_by_wickets
        self.player_of_match = player_of_match
        self.venue = venue
        self.umpire1 = umpire1
        self.umpire2 = umpire2
        self.umpire3 = umpire3

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def to_dict(self):
        return {
            'id': self.id,
            'season': self.season,
            'city': self.city,
            'date': self.date,
            'team1': self.team1,
            'team2': self.team2,
            'toss_winner': self.toss_winner,
            'toss_decision': self.toss_decision,
            'result': self.result,
            'dl_applied': self.dl_applied,
            'winner': self.winner,
            'win_by_runs': self.win_by_runs,
            'win_by_wickets': self.win_by_wickets,
            'player_of_match': self.player_of_match,
            'venue': self.venue,
            'umpire1': self.umpire1,
            'umpire2': self.umpire2,
            'umpire3': self.umpire3
        }

class Delivery(db.Model):
    __tablename__ = 'deliveries'

    id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.Integer())
    inning = db.Column(db.Integer())
    batting_team = db.Column(db.String())

    def __init__(self, match_id, inning, batting_team):
        self.match_id = match_id
        self.inning = inning
        self.batting_team = batting_team

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def to_dict(self):
        return {
            'id': self.id,
            'match_id': self.match_id,
            'inning': self.inning,
            'batting_team': self.batting_team
        }
