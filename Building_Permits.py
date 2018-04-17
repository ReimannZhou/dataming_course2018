from data_analysis import *

csv_path = './input/Building_Permits.csv'
dataFrame = read_csv(csv_path,None)
name = 'BD'

#标称属性
name_category = ['Permit Type', 'Block', 'Lot', 'Street Number', 'Street Number Suffix', 'Street Name', 'Street Suffix',
                 'Current Status', 'Structural Notification', 'Voluntary Soft-Story Retrofit', 'Fire Only Permit',
                 'Existing Use', 'Proposed Use', 'Plansets', 'TIDF Compliance', 'Existing Construction Type', 
                 'Proposed Construction Type', 'Site Permit', 'Supervisor District', 'Neighborhoods - Analysis Boundaries']
#数值属性
name_value = ['Number of Existing Stories', 'Number of Proposed Stories', 'Estimated Cost', 'Revised Cost', 'Existing Units', 'Proposed Units']

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
cols = ['Structural Notification', 'Voluntary Soft-Story Retrofit', 'Fire Only Permit', 'TIDF Compliance']

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

# 通过属性的相关关系来填补缺失值并进行直方图比较
df_filled_inter = dataFrame.copy()
# 对每一列数据，分别进行处理
for col in cols:
    df_filled_inter[col].interpolate(inplace = True)
compare(dataFrame, df_filled_inter, cols, name + 'filled_inter')