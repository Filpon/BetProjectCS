import pandas as pd
pastmatchs = pd.read_csv('C:\Projects_Learnpython\BetProjectCS\past_CSmatchs.csv', sep=';') 
presentmatchs = pd.read_csv('C:\Projects_Learnpython\BetProjectCS\present_CSmatchs.csv', sep=';')

# Проверка победы первой команды в прошлых матчах
lpastmatchs = pastmatchs[['Left_team_title', 'Right_team_title', 'Winning_team_match_result',\
            'Hypothesis']].loc[pastmatchs['Hypothesis'] == "Гипотеза верна"].\
          loc[pastmatchs['Winning_team_match_result'] == "Первая команда"]

# Проверка победы второй команды в прошлых матчах
rpastmatchs = pastmatchs[['Left_team_title', 'Right_team_title', 'Winning_team_match_result',\
            'Hypothesis']].loc[pastmatchs['Hypothesis'] == "Гипотеза верна"].\
          loc[pastmatchs['Winning_team_match_result'] == "Вторая команда"]

# Проверка первой команды в текущих матчах
lpresentmatchs = presentmatchs[['Left_team_title', 'Right_team_title',\
               'Moneybet_for_left_team', 'Moneybet_for_right_team']].\
             loc[presentmatchs['Moneybet_for_left_team'] > presentmatchs['Moneybet_for_right_team']]

# Проверка второй команды в текущих матчах
rpresentmatchs = presentmatchs[['Left_team_title', 'Right_team_title',\
               'Moneybet_for_left_team', 'Moneybet_for_right_team']].\
             loc[presentmatchs['Moneybet_for_left_team'] < presentmatchs['Moneybet_for_right_team']]

lipresentmatchs = lpresentmatchs['Left_team_title']
ripresentmatchs = rpresentmatchs['Right_team_title']

top_teams_left = []
top_teams_right = []

for lprmatch in list(lipresentmatchs):
    if (lprmatch in list(lpastmatchs['Left_team_title'])) and ((list(lpastmatchs['Hypothesis']).count('Гипотеза верна')) >=7)\
    or lprmatch in list(rpastmatchs['Right_team_title']) and ((list(lpastmatchs['Hypothesis']).count('Гипотеза верна')) >=7):
        top_teams_left.append(lprmatch)

for rprmatch in list(ripresentmatchs):
    if (rprmatch in list(lpastmatchs['Left_team_title'])) and ((list(lpastmatchs['Hypothesis']).count('Гипотеза верна')) >=7)\
    or rprmatch in list(rpastmatchs['Right_team_title']) and ((list(lpastmatchs['Hypothesis']).count('Гипотеза верна')) >=7):
        print(rprmatch)
        top_teams_right.append(rprmatch)


print(top_teams_left)
print(top_teams_right)