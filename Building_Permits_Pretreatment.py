import csv
import pandas as pd
from math import isnan
#定义一些列表，用来存放数据
permit_type_list = []#Permit Type
current_status_list = []#Current Status
Number_of_Existing_Stories_list = []
Number_of_Proposed_Stories_list = []
Estimated_Cost_list = []
Revised_Cost_list = []
Existing_Use_list = []
Existing_Units_list = []
Proposed_Use_list = []
Proposed_Units_list = []
Plansets_list = []
Existing_Construction_Type_list = []
Proposed_Construction_Type_list = []
Supervisor_District_list = []
Zipcode_list = []
Location_list = []


#写文件
##dataframe.to_csv("test1.csv",index=False,sep=',')
def datatransfor():
    # 读文件
    dataframe = pd.read_csv('./input/Building_Permits.csv',
                            usecols=['Permit Type', 'Current Status', 'Number of Existing Stories',
                                     'Number of Proposed Stories', 'Estimated Cost', 'Revised Cost',
                                     'Existing Use', 'Existing Units', 'Proposed Use', 'Proposed Units',
                                     'Plansets', 'Existing Construction Type', 'Proposed Construction Type',
                                     'Supervisor District', 'Zipcode'])

    data_1 = dataframe["Permit Type"].values
    data_2 = dataframe["Current Status"].values
    data_3 = dataframe["Number of Existing Stories"].values
    data_4 = dataframe["Number of Proposed Stories"].values
    data_5 = dataframe["Estimated Cost"].values
    data_6 = dataframe["Revised Cost"].values
##    data_7 = dataframe["Existing Use"].values
##    data_8 = dataframe["Existing Units"].values
##    data_9 = dataframe["Proposed Use"].values
##    data_10 = dataframe["Proposed Units"].values
    data_11 = dataframe["Plansets"].values
    data_12 = dataframe["Existing Construction Type"].values
    data_13 = dataframe["Proposed Construction Type"].values
    data_14 = dataframe["Supervisor District"].values
    data_15 = dataframe["Zipcode"].values
    lenth = len(data_1)
    
    #Permit Type
    for i1 in range(0,lenth):
        string = 'PT'+str(int(data_1[i1]))
        permit_type_list.append(string)
##    print('data1  ',len(data_1))
##    print('data2  ',len(data_2))
##    print('data3  ',len(data_3))
##    print('data4  ',len(data_4))
##    print('data5  ',len(data_5))
##    print('data6  ',len(data_6))
##    print('data11  ',len(data_11))
##    print('data12  ',len(data_12))
##    print('data13  ',len(data_13))
##    print('data14  ',len(data_14))
    #Current Status
    current_status_list = list(data_2)
    
    #Number of Existing Stories
    for i3 in range(0,lenth):
        if isnan(data_3[i3]):
            tag3 = ""
        else:
            if 0<=data_3[i3]<=10:
                tag3 = 'NOES_L'
            elif 11<=data_3[i3]<=30:
                tag3 = 'NOES_M'
            elif 31<=data_3[i3]<=78:
                tag3 = 'NOES_H' 
        Number_of_Existing_Stories_list.append(tag3)
    
    #Number of Proposed Stories   
    for i4 in range(0,lenth):
        if isnan(data_4[i4]):
            tag4 = ""
        else:
            if 0<=data_4[i4]<=10:
                tag4 = 'NOPS_L'
            elif 11<=data_4[i4]<=30:
                tag4 = 'NOPS_M'
            elif 31<=data_4[i4]<=78:
                tag4 = 'NOPS_H' 
        Number_of_Proposed_Stories_list.append(tag4)
    
    #Estimated_Cost_list
    for i5 in range(0,lenth):
        if isnan(data_5[i5]):
            tag5 = ""
        else:
            if 0<=data_5[i5]<=100000:
                tag5 = 'EC_L'
            elif 100000<data_5[i5]<=1000000:
                tag5 = 'EC_M'
            elif 1000000<data_5[i5]<=537958646:
                tag5 = 'EC_H'
        Estimated_Cost_list.append(tag5)

    #Revised_Cost_list
    for i6 in range(0,lenth):
        if isnan(data_6[i6]):
            tag6 = ""
        else:
            if 0<=data_6[i6]<=100000:
                tag6 = 'RC_L'
            elif 100000<data_6[i6]<=1000000:
                tag6 = 'RC_M'
            elif 1000000<=data_6[i6]<=780500000:
                tag6 = 'RC_H'
        Revised_Cost_list.append(tag6)
    #Plansets
    for i11 in range(0,lenth):
        if isnan(data_11[i11]):
            string11 = ""
        else:
            string11 = 'P'+str(int(data_11[i11]))
        Plansets_list.append(string11)

    #Existing Construction Type
    for i12 in range(0,lenth):
        if isnan(data_12[i12]):
            string12 = ""
        else:
            string12 = 'ECT'+str(int(data_12[i12]))
        Existing_Construction_Type_list.append(string12)

    #Proposed Construction Type
    for i13 in range(0,lenth):
        if isnan(data_13[i13]):
            string13 = ""
        else:
            string13 = 'PCT'+str(int(data_13[i13]))
        Proposed_Construction_Type_list.append(string13)

    #Supervisor District
    for i14 in range(0,lenth):
        if isnan(data_14[i14]):
            string14 = ""
        else:
            string14 = 'SD'+str(int(data_14[i14]))
        Supervisor_District_list.append(string14)
    
    for i15 in range(0,lenth):
        if isnan(data_15[i15]):
            string15 = ""
        else:
            string15 = str(int(data_15[i15]))
        Zipcode_list.append(string15)
##    print(len(permit_type_list))
##    print(len(current_status_list))
##    print(len(Number_of_Existing_Stories_list))
##    print(len(Number_of_Proposed_Stories_list))
##    print(len(Estimated_Cost_list))
##    print(len(Revised_Cost_list))
##    print(len(Plansets_list))
##    print(len(Existing_Construction_Type_list))
##    print(len(Proposed_Construction_Type_list))
##    print(len(Supervisor_District_list))
##    print(len(Zipcode_list))
    dataframe = pd.DataFrame({'Permit Type':permit_type_list,'Current Status':current_status_list,'Number of Existing Stories':Number_of_Existing_Stories_list,'Number of Proposed Stories':Number_of_Proposed_Stories_list,'Estimated Cost':Estimated_Cost_list,'Revised Cost':Revised_Cost_list,'Plansets':Plansets_list,'Existing Construction Type':Existing_Construction_Type_list,'Proposed Construction Type list':Proposed_Construction_Type_list,'Supervisor District':Supervisor_District_list,'Zipcode':Zipcode_list})
##    #将DataFrame存储为csv,index表示是否显示行名，default=True
    with open('./input/test2.csv', 'w'):
        print('ok')
    dataframe.to_csv("./input/test2.csv",index=False,sep=',')
    
datatransfor()
