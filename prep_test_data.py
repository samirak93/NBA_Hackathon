import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar as calendar

#prepare columns for test data

df=pd.read_csv('test_set.csv')

data=pd.DataFrame(df)
mapping = {'CLE': 1, 'POR': 2,'GSW': 3,'ORL': 4,'IND': 5,'BOS': 6,'TOR': 7,'MIL': 8,'MEM': 9,
           'PHI': 10,'PHX': 11,'LAL': 12,'ATL': 13,'CHI': 14,'SAC': 15,'BKN': 16,'DET': 17,'OKC': 18,
           'MIA': 19,'UTA': 20,'NOP': 21,'NYK': 22,'SAS': 23,'DEN': 24,'LAC': 25,'HOU': 26,'MIN': 27,'WAS': 28,'CHA': 29,'DAL': 30}
updated=data.replace({'Home_Team': mapping,'Away_Team':mapping})
updated['home_team_score']=0
updated['away_team_score']=0
updated['wins_home']=0
updated['wins_away']=0
updated['loss_home']=0
updated['loss_away']=0
updated['largest_lead_home']=0
updated['largest_lead_away']=0
updated['result_win']=0
updated['ASG_Count']=0
updated['day']= pd.to_datetime(updated['Game_Date']).dt.dayofweek

array=[]
for x,y in zip(updated.Home_Team,updated.Away_Team):
    if ((x==1)&(y==3)) | ((x==3)&(y==1)):
        (array.append(int('1')))
    elif ((x==6)&(y==12)) | ((x==12)&(y==6)):
        array.append(int('1'))
    elif ((x == 17) & (y == 12)) | ((x == 12) & (y == 17)):
        array.append(int('1'))
    elif ((x == 10) & (y == 6)) | ((x == 6) & (y == 10)):
        array.append(int('2'))
    elif ((x == 6) & (y == 22)) | ((x == 22) & (y == 6)):
        array.append(int('2'))
    elif ((x == 16) & (y == 22)) | ((x == 22) & (y == 16)):
        array.append(int('2'))
    elif ((x == 17) & (y == 14)) | ((x == 14) & (y == 17)):
        array.append(int('2'))
    elif ((x == 1) & (y == 14)) | ((x == 14) & (y == 1)):
        array.append(int('2'))
    elif ((x == 19) & (y == 14)) | ((x == 14) & (y == 19)):
        array.append(int('2'))
    elif ((x == 22) & (y == 14)) | ((x == 14) & (y == 22)):
        array.append(int('2'))
    elif ((x == 6) & (y == 17)) | ((x == 17) & (y == 6)):
        array.append(int('2'))
    elif ((x == 22) & (y == 19)) | ((x == 19) & (y == 22)):
        array.append(int('2'))
    elif ((x == 22) & (y == 5)) | ((x == 5) & (y == 22)):
        array.append(int('2'))
    elif ((x == 12) & (y == 25)) | ((x == 25) & (y == 12)):
        array.append(int('3'))
    elif ((x == 30) & (y == 26)) | ((x == 26) & (y == 30)):
        array.append(int('3'))
    elif ((x == 23) & (y == 26)) | ((x == 26) & (y == 23)):
        array.append(int('3'))
    elif ((x == 20) & (y == 26)) | ((x == 26) & (y == 20)):
        array.append(int('3'))
    elif ((x == 12) & (y == 23)) | ((x == 23) & (y == 12)):
        array.append(int('3'))
    elif ((x == 11) & (y == 23)) | ((x == 23) & (y == 11)):
        array.append(int('3'))
    else:
        array.append(int(0))
updated["rivalry"]=array

home_team_rank=[]
twitter_followers_home=[]

for x in (updated.Home_Team):
    if ((x==1)):
        home_team_rank.append(int(11))
        twitter_followers_home.append(int(2100000))
    elif (x==2):
        home_team_rank.append(int(17))
        twitter_followers_home.append(int(823000))
    elif (x==3):
        home_team_rank.append(int(3))
        twitter_followers_home.append(int(3500000))
    elif (x==4):
        home_team_rank.append(int(19))
        twitter_followers_home.append(int(1500000))
    elif (x==5):
        home_team_rank.append(int(24))
        twitter_followers_home.append(int(930000))
    elif (x==6):
        home_team_rank.append(int(5))
        twitter_followers_home.append(int(2300000))
    elif (x==7):
        home_team_rank.append(int(13))
        twitter_followers_home.append(int(1400000))
    elif (x==8):
        home_team_rank.append(int(27))
        twitter_followers_home.append(int(695000))
    elif (x==9):
        home_team_rank.append(int(26))
        twitter_followers_home.append(int(766000))
    elif (x==10):
        home_team_rank.append(int(25))
        twitter_followers_home.append(int(925000))
    elif (x==11):
        home_team_rank.append(int(14))
        twitter_followers_home.append(int(753000))
    elif (x==12):
        home_team_rank.append(int(2))
        twitter_followers_home.append(int(6170000))
    elif (x==13):
        home_team_rank.append(int(23))
        twitter_followers_home.append(int(991000))
    elif (x==14):
        home_team_rank.append(int(4))
        twitter_followers_home.append(int(3600000))
    elif (x==15):
        home_team_rank.append(int(15))
        twitter_followers_home.append(int(714000))
    elif (x==16):
        home_team_rank.append(int(7))
        twitter_followers_home.append(int(755000))
    elif (x==17):
        home_team_rank.append(int(21))
        twitter_followers_home.append(int(710000))
    elif (x==18):
        home_team_rank.append(int(16))
        twitter_followers_home.append(int(1800000))
    elif (x==19):
        home_team_rank.append(int(10))
        twitter_followers_home.append(int(4090000))
    elif (x==20):
        home_team_rank.append(int(20))
        twitter_followers_home.append(int(632000))
    elif (x==21):
        home_team_rank.append(int(30))
        twitter_followers_home.append(int(659000))
    elif (x==22):
        home_team_rank.append(int(1))
        twitter_followers_home.append(int(1780000))
    elif (x==23):
        home_team_rank.append(int(12))
        twitter_followers_home.append(int(2300000))
    elif (x==24):
        home_team_rank.append(int(22))
        twitter_followers_home.append(int(634000))
    elif (x==25):
        home_team_rank.append(int(6))
        twitter_followers_home.append(int(1100000))
    elif (x==26):
        home_team_rank.append(int(8))
        twitter_followers_home.append(int(1710000))
    elif (x==27):
        home_team_rank.append(int(29))
        twitter_followers_home.append(int(645000))
    elif (x == 28):
        home_team_rank.append(int(18))
        twitter_followers_home.append(int(662000))
    elif (x==29):
        home_team_rank.append(int(28))
        twitter_followers_home.append(int(726000))
    elif (x==30):
        twitter_followers_home.append(int(1200000))
        home_team_rank.append(int(9))


twitter_followers_away=[]
away_team_rank=[]

for x in (updated.Away_Team):
    if ((x==1)):
        away_team_rank.append(int(11))
        twitter_followers_away.append(int(2100000))
    elif (x==2):
        away_team_rank.append(int(17))
        twitter_followers_away.append(int(823000))
    elif (x==3):
        away_team_rank.append(int(3))
        twitter_followers_away.append(int(3500000))
    elif (x==4):
        away_team_rank.append(int(19))
        twitter_followers_away.append(int(1500000))
    elif (x==5):
        away_team_rank.append(int(24))
        twitter_followers_away.append(int(930000))
    elif (x==6):
        away_team_rank.append(int(5))
        twitter_followers_away.append(int(2300000))
    elif (x==7):
        away_team_rank.append(int(13))
        twitter_followers_away.append(int(1400000))
    elif (x==8):
        away_team_rank.append(int(27))
        twitter_followers_away.append(int(695000))
    elif (x==9):
        away_team_rank.append(int(26))
        twitter_followers_away.append(int(766000))
    elif (x==10):
        away_team_rank.append(int(25))
        twitter_followers_away.append(int(925000))
    elif (x==11):
        away_team_rank.append(int(14))
        twitter_followers_away.append(int(753000))
    elif (x==12):
        away_team_rank.append(int(2))
        twitter_followers_away.append(int(6170000))
    elif (x==13):
        away_team_rank.append(int(23))
        twitter_followers_away.append(int(991000))
    elif (x==14):
        away_team_rank.append(int(4))
        twitter_followers_away.append(int(3600000))
    elif (x==15):
        away_team_rank.append(int(15))
        twitter_followers_away.append(int(714000))
    elif (x==16):
        away_team_rank.append(int(7))
        twitter_followers_away.append(int(755000))
    elif (x==17):
        away_team_rank.append(int(21))
        twitter_followers_away.append(int(710000))
    elif (x==18):
        away_team_rank.append(int(16))
        twitter_followers_away.append(int(1800000))
    elif (x==19):
        away_team_rank.append(int(10))
        twitter_followers_away.append(int(4090000))
    elif (x==20):
        away_team_rank.append(int(20))
        twitter_followers_away.append(int(632000))
    elif (x==21):
        away_team_rank.append(int(30))
        twitter_followers_away.append(int(659000))
    elif (x==22):
        away_team_rank.append(int(1))
        twitter_followers_away.append(int(1780000))
    elif (x==23):
        away_team_rank.append(int(12))
        twitter_followers_away.append(int(2300000))
    elif (x==24):
        away_team_rank.append(int(22))
        twitter_followers_away.append(int(634000))
    elif (x==25):
        away_team_rank.append(int(6))
        twitter_followers_away.append(int(1100000))
    elif (x==26):
        away_team_rank.append(int(8))
        twitter_followers_away.append(int(1710000))
    elif (x==27):
        away_team_rank.append(int(29))
        twitter_followers_away.append(int(645000))
    elif (x == 28):
        away_team_rank.append(int(18))
        twitter_followers_away.append(int(662000))
    elif (x==29):
        away_team_rank.append(int(28))
        twitter_followers_away.append(int(726000))
    elif (x==30):
        twitter_followers_away.append(int(1200000))
        away_team_rank.append(int(9))


updated['Home_Team_Twitter']=twitter_followers_home
updated['Away_Team_Twitter']=twitter_followers_away

updated['Home_Team_Rank']=home_team_rank
updated['Away_Team_Rank']=away_team_rank

updated['Game_Date'] = pd.to_datetime(updated.Game_Date)
cal = calendar()
holidays = cal.holidays(start=updated.Game_Date.min(), end=updated.Game_Date.max())

updated['Holiday'] = updated['Game_Date'].isin(holidays)

holiday=[]

for holi in updated.Holiday:
    if holi==True:
        holiday.append(int(1))
    elif holi!=True:
        holiday.append(int(0))
updated['Holiday'] = holiday
df_dummy=updated.pop('Total_Viewers')

updated['Total_Viewers']=df_dummy

updated.to_csv('test_data.csv')

print updated.shape