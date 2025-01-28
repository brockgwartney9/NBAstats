import csv
columns = [
    ["player", "TEXT"],
    ["age", "INTEGER"],
    ["team", "TEXT"],
    ["position", "TEXT"],
    ["games", "INTEGER"],
    ["gamesStarted", "INTEGER"],
    ["mp", "INTEGER"],
    ["fieldgoals", "INTEGER"],
    ["fieldgoalsatt", "INTEGER"],
    ["fieldgoalpercent", "REAL"],
    ["threepointers", "INTEGER"],
    ["threepointersatt", "INTEGER"],
    ["threepointpercent", "REAL"],
    ["twopointers", "INTEGER"],
    ["twopointersatt", "INTEGER"],
    ["twopointerpercent", "REAL"],
    ["effectivefieldgoalpercent", "REAL"],
    ["freethrows", "INTEGER"],
    ["freethrowatt", "INTEGER"],
    ["freethroughpercent", "REAL"],
    ["offensiverebounds", "INTEGER"],
    ["defensiverebounds", "INTEGER"],
    ["rebounds", "INTEGER"],
    ["assists", "INTEGER"],
    ["steals", "INTEGER"],
    ["blocks", "INTEGER"],
    ["turnovers", "INTEGER"],
    ["fouls", "INTEGER"],
    ["points", "INTEGER"],
    ["trippledoubles", "INTEGER"],
    ["awards", "TEXT"],
    ##["playerid", "INTEGER"],
]



def print_sql_command(columms):
    s = "CREATE TABLE realstats ("
    for column in columms:
        s = f"{s} {column[0]} {column[1]}, "
    s = s + ')'
    return s
def pre_create(columns):
    command = ''
    command = command + "INSERT INTO realstats ("
    for ind in columns:
        if ind[0] == "awards":
             command = command + ind[0]
             continue
        command = command + ind[0] + ", "
    command = command + ")"
    return command

def create_sql_add_command(columns):

    #command = pre_create(columns) + "VALUES"
    commands= []

    with open('DATABASE/23-24csv.csv', mode = 'r', encoding= 'utf-8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            command = "INSERT INTO REALSTATS (player, age, team, position, games, gamesStarted, mp, fieldgoals, fieldgoalsatt, fieldgoalpercent, threepointers, threepointersatt, threepointpercent, twopointers, twopointersatt, twopointerpercent, effectivefieldgoalpercent, freethrows, freethrowatt, freethroughpercent, offensiverebounds, defensiverebounds, rebounds, assists, steals, blocks, turnovers, fouls, points, trippledoubles, awards) VALUES "
            if row[0] == '' or row[1] == "Age":
                continue
            else:
                sub_cmd = "("
                for i in range(len(row)):
                    if i == 0:
                        row[i] = row[i].replace("'", "''")
                        sub_cmd = f'{sub_cmd}"{row[i]}"'
                    elif i == (len(row) - 2):
                        break
                    else:
                        if columns[i][1] == "TEXT":
                            sub_cmd = f'{sub_cmd},"{row[i]}"'
                        elif row[i] == '':
                            sub_cmd = f'{sub_cmd},{0}'
                        else:
                            sub_cmd = f'{sub_cmd},{row[i]}'
                        
                sub_cmd = command + sub_cmd + ");"
                commands.append(sub_cmd)
    return commands



with open("sql_command.txt", mode= 'w', encoding= 'utf-8') as file:
    x = create_sql_add_command(columns)
    for y in x:
        file.write(y)