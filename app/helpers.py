from app import *
from app.models import *
from sqlalchemy.orm import aliased

def special_to_dict(data):
    result_dict = {}
    for x in data.keys():
        result_dict[x] = getattr(data, x)
    return result_dict

def special_parse_object(req_arr, key, value):
    res_object = {}
    for i in range(len(req_arr)):
        # print(i, req_arr[i])
        res_object[req_arr[i][key]] = req_arr[i][value]
    return res_object

def get_seasons():
    response_data = []
    try:
        match_query = list(map(lambda x: special_to_dict(x), Match.query.with_entities(Match.season).distinct(Match.season).all()))
        # print('match_query:', match_query)
        match_query = sorted(match_query, key=lambda k: k.get('season', 0), reverse=False)
        # print('match_query:', match_query)
        for i in range(len(match_query)):
            response_data.append(match_query[i]['season'])
    except Exception as e:
        print('Exception caught in getting member data => '+str(e))
        ex_type, ex, tb = sys.exc_info()
        print('traceback:', traceback.print_tb(tb))
    return response_data

def get_winner_teams(season):
    response_data = {}
    try:
        match_query = list(map(lambda x: special_to_dict(x), Match.query.with_entities(Match.winner, db.func.count(Match.id).label('winnings')).filter_by(season=season).group_by(Match.winner).all()))
        # print('match_query:', match_query)
        match_query = sorted(match_query, key=lambda k: k.get('winnings', 0), reverse=True)
        for i in range(len(match_query)):
            if(i == 5):
                break
            response_data[i] = match_query[i]
    except Exception as e:
        print('Exception caught in getting member data => '+str(e))
        ex_type, ex, tb = sys.exc_info()
        print('traceback:', traceback.print_tb(tb))
    return response_data

def get_most_toss_team(season):
    response_data = None
    try:
        match_query = list(map(lambda x: special_to_dict(x), Match.query.with_entities(Match.toss_winner, db.func.count(Match.id).label('most_toss')).filter_by(season=season).group_by(Match.toss_winner).all()))
        # print('match_query:', match_query)
        match_query = sorted(match_query, key=lambda k: k.get('most_toss', 0), reverse=True)
        # print('match_query:', match_query)
        response_data = match_query[0]['toss_winner']
    except Exception as e:
        print('Exception caught in getting member data => '+str(e))
        ex_type, ex, tb = sys.exc_info()
        print('traceback:', traceback.print_tb(tb))
    return response_data

def get_most_player_of_match(season):
    response_data = None
    try:
        match_query = list(map(lambda x: special_to_dict(x), Match.query.with_entities(Match.player_of_match, db.func.count(Match.id).label('most_pom')).filter_by(season=season).group_by(Match.player_of_match).all()))
        # print('match_query:', match_query)
        match_query = sorted(match_query, key=lambda k: k.get('most_toss', 0), reverse=True)
        # print('match_query:', match_query)
        response_data = match_query[0]['player_of_match']
    except Exception as e:
        print('Exception caught in getting member data => '+str(e))
        ex_type, ex, tb = sys.exc_info()
        print('traceback:', traceback.print_tb(tb))
    return response_data

def get_most_winning_team_city(season, team):
    response_data = None
    try:
        match_query = list(map(lambda x: special_to_dict(x), Match.query.with_entities(Match.city, db.func.count(Match.id).label('lucky_city')).filter_by(season=season).filter_by(winner=team).group_by(Match.city).all()))
        # print('match_query:', match_query)
        match_query = sorted(match_query, key=lambda k: k.get('lucky_city', 0), reverse=True)
        # print('match_query:', match_query)
        response_data = match_query[0]['city']
    except Exception as e:
        print('Exception caught in getting member data => '+str(e))
        ex_type, ex, tb = sys.exc_info()
        print('traceback:', traceback.print_tb(tb))
    return response_data

def get_toss_bat_percent(season):
    response_data = {}
    try:
        match_query1= list(map(lambda x: special_to_dict(x), Match.query.with_entities(Match.toss_winner, db.func.count(Match.id).label('toss_win')).filter_by(season=season).group_by(Match.toss_winner).all()))
        # print('match_query:', match_query)
        match_query1 = special_parse_object(sorted(match_query1, key=lambda k: k.get('toss_win', 0), reverse=True), 'toss_winner', 'toss_win')
        # print('match_query1:', match_query1)

        match_query2= list(map(lambda x: special_to_dict(x), Match.query.with_entities(Match.toss_winner, db.func.count(Match.id).label('batted')).filter_by(season=season).filter_by(toss_decision='bat').group_by(Match.toss_winner).all()))
        # print('match_query:', match_query)
        match_query2 = special_parse_object(sorted(match_query2, key=lambda k: k.get('batted', 0), reverse=True), 'toss_winner', 'batted')
        # print('match_query2:', match_query2)

        # Find Percentage
        percent_team_wise = {}
        for key in match_query1:
            # print(key, match_query1[key])
            if(key in match_query2):
                percent_team_wise[key] = round(int(match_query2[key])/int(match_query1[key])*100, 2)
            else:
                percent_team_wise[key] = 0;
        # print('percent_team_wise:', percent_team_wise)

        total_teams = 0
        total_batted = 0
        for team in percent_team_wise:
            total_teams = total_teams+1
            total_batted = total_batted+percent_team_wise[key]
        response_data = round(total_batted/total_teams, 2)
    except Exception as e:
        print('Exception caught in getting member data => '+str(e))
        ex_type, ex, tb = sys.exc_info()
        print('traceback:', traceback.print_tb(tb))
    return response_data

def get_city_based(season):
    response_data = {}
    try:
        match_query = list(map(lambda x: special_to_dict(x), Match.query.with_entities(Match.city, db.func.count(Match.id).label('total_games')).filter_by(season=season).group_by(Match.city).all()))
        # print('match_query:', match_query)
        match_query = sorted(match_query, key=lambda k: k.get('total_games', 0), reverse=True)
        # print('match_query:', match_query)

        response_data = {
                'total_games': match_query
            }
    except Exception as e:
        print('Exception caught in getting member data => '+str(e))
        ex_type, ex, tb = sys.exc_info()
        print('traceback:', traceback.print_tb(tb))
    return response_data

def get_largest_run_winners(season):
    response_data = {}
    try:
        match_query = list(map(lambda x: special_to_dict(x), Match.query.with_entities(Match.id, Match.winner, Match.win_by_runs).filter_by(season=season).all()))
        match_query = sorted(match_query, key=lambda k: k.get('win_by_runs', 0), reverse=True)
        response_data = match_query[0]['winner']
    except Exception as e:
        print('Exception caught in getting member data => '+str(e))
        ex_type, ex, tb = sys.exc_info()
        print('traceback:', traceback.print_tb(tb))
    return response_data

def get_highest_wicket_winners(season):
    response_data = {}
    try:
        match_query = list(map(lambda x: special_to_dict(x), Match.query.with_entities(Match.id, Match.winner, Match.win_by_wickets).filter_by(season=season).all()))
        match_query = sorted(match_query, key=lambda k: k.get('win_by_wickets', 0), reverse=True)
        response_data = match_query[0]['winner']
    except Exception as e:
        print('Exception caught in getting member data => '+str(e))
        ex_type, ex, tb = sys.exc_info()
        print('traceback:', traceback.print_tb(tb))
    return response_data

def get_team_win_toss_match(season):
    response_data = {}
    try:
        response_data['total_teams'] = 0
        response_data['teams'] = []
        match1 = aliased(Match)
        match2 = aliased(Match)
        match_query = (db.session.query(match1, match2)
                                .join(match2, match1.id == match2.id)
                                .with_entities(match1.winner)
                                .distinct()
                                .filter(match1.winner == match2.toss_winner)
                                .all()
                                )
        match_result = list(map(lambda x: special_to_dict(x), match_query))
        print('match_result:', match_result, len(match_result))
        for i in range(len(match_result)):
            response_data['total_teams'] = response_data['total_teams']+1
            response_data['teams'].append(match_result[i]['winner'])
        print('response_data:', response_data)
    except Exception as e:
        print('Exception caught in getting member data => '+str(e))
        ex_type, ex, tb = sys.exc_info()
        print('traceback:', traceback.print_tb(tb))
    return response_data
