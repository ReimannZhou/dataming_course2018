from data_analysis import *

csv_path = './input/NFL Play by Play 2009-2017 (v4).csv'
dataFrame = read_csv(csv_path,None)
name = 'NPBP'

#标称属性
name_category = ['Drive', 'qtr', 'down', 'SideofField', 'ydstogo', 'GoalToGo', 'FirstDown', 'posteam',
                 'DefensiveTeam', 'PlayAttempted', 'sp', 'Touchdown', 'ExPointResult', 'TwoPointConv', 
                 'DefTwoPoint', 'Safety', 'Onsidekick', 'PuntResult', 'PlayType', 'Passer', 'Passer_ID', 
                 'PassAttempt', 'PassOutcome', 'PassLength', 'QBHit', 'PassLocation', 'InterceptionThrown',
                 'Interceptor', 'Rusher', 'Rusher_ID', 'RushAttempt', 'RunLocation', 'RunGap', 'Receiver', 
                 'Receiver_ID', 'Reception', 'ReturnResult', 'Returner', 'BlockingPlayer', 'Tackler1', 'Tackler2', 
                 'FieldGoalResult', 'Fumble', 'RecFumbTeam', 'RecFumbPlayer', 'Sack', 'Challenge.Replay', 
                 'ChalReplayResult', 'Accepted.Penalty', 'PenalizedTeam', 'PenaltyType', 'PenalizedPlayer', 
                 'HomeTeam', 'AwayTeam', 'Timeout_Indicator', 'Timeout_Team', 'Season']
#数值属性
name_value = ['TimeUnder', 'TimeSecs', 'PlayTimeDiff', 'yrdln', 'yrdline100', 'ydsnet', 'Yards.Gained', 
              'AirYards', 'YardsAfterCatch', 'FieldGoalDistance', 'Penalty.Yards', 'PosTeamScore', 'DefTeamScore', 
              'ScoreDiff', 'AbsScoreDiff', 'posteam_timeouts_pre', 'HomeTimeouts_Remaining_Pre', 'AwayTimeouts_Remaining_Pre', 
              'HomeTimeouts_Remaining_Post', 'AwayTimeouts_Remaining_Post', 'No_Score_Prob', 'Opp_Field_Goal_Prob', 
              'Opp_Safety_Prob', 'Opp_Touchdown_Prob', 'Field_Goal_Prob', 'Safety_Prob', 'Touchdown_Prob', 'ExPoint_Prob', 
              'TwoPoint_Prob', 'ExpPts', 'EPA', 'airEPA', 'yacEPA', 'Home_WP_pre', 'Away_WP_pre', 'Home_WP_post', 
              'Away_WP_post', 'Win_Prob', 'WPA', 'airWPA', 'yacWPA']

#标称属性统计频数
count(dataFrame, name_category, name)

#数值属性统计最小、最大、均值、中位数、四分位数及缺失值个数
describe(dataFrame, name_value, name)

#绘制直方图
histogram(dataFrame, name_value, name)

#绘制qq图
qqplot(dataFrame, name_value, name)

#绘制盒图
boxplot(dataFrame, name_value, name)

#存在na的属性
cols = ['No_Score_Prob', 'Opp_Field_Goal_Prob', 'Opp_Safety_Prob', 'Opp_Touchdown_Prob', 'Field_Goal_Prob', 
        'Safety_Prob', 'Touchdown_Prob', 'ExpPts', 'EPA', 'airEPA', 'yacEPA', 'Home_WP_pre', 'Away_WP_pre', 
        'Home_WP_post', 'Away_WP_post', 'Win_Prob', 'WPA', 'airWPA', 'yacWPA']

#将缺失值剔除,若出现na，则按行删除数据
df_dropna = dataFrame.copy()
df_dropna = df_dropna.dropna(axis = 0, how = 'any')
compare(dataFrame, df_dropna, cols, name + 'dropna')

#用最高频率值来填补缺失值
df_filled = dataFrame.copy()
for col in cols:
    # 计算最高频率的值
    most_frequent_value = df_filled[col].value_counts(dropna = True).idxmax()
    # 替换缺失值
    df_filled[col].fillna(value = most_frequent_value, inplace = True)
compare(dataFrame, df_filled, cols, name + 'filled_frequent')

# 通过属性的相关关系来填补缺失值
df_filled_inter = dataFrame.copy()
# 对每一列数据，分别进行处理
for col in cols:
    df_filled_inter[col].interpolate(inplace = True)
compare(dataFrame, df_filled_inter, cols, name + 'filled_inter')
