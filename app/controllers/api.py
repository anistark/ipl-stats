import sys
import traceback
import json
from flask import Blueprint, jsonify, request, make_response
from app import app, db
from app import models, helpers

@app.route('/api/stat', methods=['GET'])
def get_stat():
    response_data = {}
    try:
        season = request.args.get('season')
        # print('season:', season)
        winner_teams = helpers.get_winner_teams(season=season)
        response_data = {
                'winner_teams': winner_teams,
                'most_toss': helpers.get_most_toss_team(season=season),
                'most_player_of_match': helpers.get_most_player_of_match(season=season),
                'most_match_winning_team': winner_teams[0]['winner'],
                'most_winning_team_city': helpers.get_most_winning_team_city(season=season, team=winner_teams[0]['winner']),
                'toss_bat_percent': helpers.get_toss_bat_percent(season=season),
                'city_based': helpers.get_city_based(season=season),
                'largest_run_winners': helpers.get_largest_run_winners(season=season),
                'highest_wicket_winners': helpers.get_highest_wicket_winners(season=season),
                'team_win_toss_match': helpers.get_team_win_toss_match(season=season)
            }
    except Exception as e:
        ex_type, ex, tb = sys.exc_info()
        print('traceback:', traceback.print_tb(tb))
    return jsonify({'success': True, 'data': response_data})
