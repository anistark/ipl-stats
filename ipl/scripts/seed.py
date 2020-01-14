import sys, os
import psycopg2, csv
import config

os.system('clear')

conn = psycopg2.connect(host=config.DB_CONFIG.host, dbname=config.DB_CONFIG.db_name, user=config.DB_CONFIG.username, password=config.DB_CONFIG.password)

print('-- init --')

cur = conn.cursor()
cur.execute('''create table matches(id int,season int,city text,date date,team1 text,team2 text,toss_winner text,toss_decision text,result text,dl_applied boolean,winner text,win_by_runs int,win_by_wickets int,player_of_match text,venue text,umpire1 text,umpire2 text,umpire3 text);''')
file1 = '/Users/Anirudha/Documents/practice/gale/ipl/matches.csv'
with open(file1) as csvfile:
    i = 0
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if row[0].isdigit():
            i = i+1
            print('Processing for matches id: #', i, end="\r")
            cur.execute("INSERT INTO matches (id,season,city,date,team1,team2,toss_winner,toss_decision,result,dl_applied,winner,win_by_runs,win_by_wickets,player_of_match,venue,umpire1,umpire2,umpire3) VALUES ("+row[0]+","+row[1]+",'"+row[2].replace("'",'\\"')+"','"+row[3].replace("'",'\\"')+"','"+row[4].replace("'",'\\"')+"','"+row[5].replace("'",'\\"')+"','"+row[6].replace("'",'\\"')+"','"+row[7].replace("'",'\\"')+"','"+row[8].replace("'",'\\"')+"','"+row[9].replace("'",'\\"')+"','"+row[10].replace("'",'\\"')+"',"+row[11]+","+row[12]+",'"+row[13].replace("'",'\\"')+"','"+row[14].replace("'",'\\"')+"','"+row[15].replace("'",'\\"')+"','"+row[16].replace("'",'\\"')+"','"+row[17].replace("'",'\\"')+"')")

cur.close()

cur2 = conn.cursor()
cur2.execute('''create table deliveries(id int, match_id int, inning int, batting_team text, bowling_team text, over int, ball int, batsman text, non_striker text, bowler text, is_super_over int, wide_runs int, bye_runs int, legbye_runs int, noball_runs int, penalty_runs int, batsman_runs int, extra_runs int, total_runs int, player_dismissed text, dismissal_kind text, fielder text);''')
file2 = '/Users/Anirudha/Documents/practice/gale/ipl/deliveries.csv'
with open(file2) as csvfile:
    i = 0
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if row[0].isdigit():
            i = i+1
            print('Processing for deliveries id: #', i, end="\r")
            cur2.execute("INSERT INTO deliveries (id, match_id, inning, batting_team, bowling_team, over, ball, batsman, non_striker, bowler, is_super_over, wide_runs, bye_runs, legbye_runs, noball_runs, penalty_runs, batsman_runs, extra_runs, total_runs, player_dismissed, dismissal_kind, fielder) VALUES ("+str(i)+","+row[0]+","+row[1]+",'"+row[2].replace("'",'\\"')+"','"+row[3].replace("'",'\\"')+"','"+row[4].replace("'",'\\"')+"',"+row[5]+",'"+row[6].replace("'",'\\"')+"','"+row[7].replace("'",'\\"')+"','"+row[8].replace("'",'\\"')+"',"+row[9]+","+row[10]+","+row[11]+","+row[12]+","+row[13]+","+row[14]+","+row[15]+","+row[16]+","+row[17]+",'"+row[18].replace("'",'\\"')+"','"+row[19].replace("'",'\\"')+"','"+row[20].replace("'",'\\"')+"')")
cur2.close()

conn.commit()

print('-- All Done --')
