import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from pandas import DataFrame, Series


def set_display():
    '''显示设置'''
    pd.set_option('display.max_columns', 2000)
    pd.set_option('display.max_rows', 2000)
    pd.set_option('display.width', 2000)


def read_csv(path, na_values = None):
    '''读取csv数据集'''
    return pd.read_csv(path, na_values=na_values, low_memory = False)


def count(dataFrame, columns, outname = '', dropna = False, format_width = 30):
    '''标称属性，给出每个可能取值的频数'''
    file = open('./output/out_' + outname + '.txt', 'a')
    format_text = '{{:<{0}}}{{:<{0}}}'.format(format_width)
    for col in columns:
        print('标称属性 <{}> 频数统计'.format(col), file = file)
        print(format_text.format('value', 'count'), file = file)
        print('--' * format_width, file = file)
        
        counts = pd.value_counts(dataFrame[col].values, dropna = dropna)
        for i, index in enumerate(counts.index):
            #计算NaN的数目
            if pd.isnull(index):
                print(format_text.format('-NaN-', counts.values[i]), file = file)
            else:
                print(format_text.format(index, counts[index]), file = file)
        print('--' * format_width, file = file)
        print('\n', file = file)
    file.close()


def describe(dataFrame, columns, outname = ''):
    '''数值属性，给出最大、最小、均值、中位数、四分位数及缺失值的个数'''
    file = open('./output/out_' + outname + '.txt', 'a')
    desc = dataFrame[columns].describe()
    statistic = DataFrame()
    statistic['max'] = desc.loc['max']
    statistic['min'] = desc.loc['min']
    statistic['mean'] = desc.loc['mean']
    statistic['50%'] = desc.loc['50%']
    statistic['25%'] = desc.loc['25%']
    statistic['75%'] = desc.loc['75%']
    statistic['NaN'] = dataFrame[columns].isnull().sum()
    print(statistic, file = file)
    file.close()


# 绘图配置
row_size = 2
col_size = 3
cell_size = row_size * col_size


def histogram(dataFrame, columns, name):
    '''直方图'''
    counts = 0
    for i, col in enumerate(columns):
        if i % cell_size == 0:
            fig = plt.figure()
        ax = fig.add_subplot(col_size, row_size, (i % cell_size) + 1)
        dataFrame[col].hist(ax = ax, grid = False, figsize = (15, 15), bins = 50)
        plt.title(col)
        if (i + 1) % cell_size == 0 or i + 1 == len(columns):
            counts += 1
            plt.subplots_adjust(wspace=0.3, hspace=0.3)
            plt.savefig('./output/' + name + '_histogram' + str(counts) + '.png')
            plt.show()


def qqplot(dataFrame, columns, name):
    '''qq图'''
    counts = 0
    for i, col in enumerate(columns):
        if i % cell_size == 0:
            fig = plt.figure(figsize=(15, 15))
        ax = fig.add_subplot(col_size, row_size, (i % cell_size) + 1)
        sm.qqplot(dataFrame[col], ax = ax)
        ax.set_title(col)
        if (i + 1) % cell_size == 0 or i + 1 == len(columns):
            counts += 1
            plt.subplots_adjust(wspace = 0.3, hspace = 0.3)
            plt.savefig('./output/' + name + '_qqplot' + str(counts) + '.png')
            plt.show()


def boxplot(dataFrame, columns, name):
    '''盒图'''
    counts = 0
    for i, col in enumerate(columns):
        if i % cell_size == 0:
            fig = plt.figure()
        ax = fig.add_subplot(col_size, row_size, (i % cell_size) + 1)
        dataFrame[col].plot.box(ax = ax, figsize = (15, 15))
        if (i + 1) % cell_size == 0 or i + 1 == len(columns):
            counts += 1
            plt.subplots_adjust(wspace = 0.3, hspace = 0.3)
            plt.savefig('./output/' + name + '_boxplot' + str(counts) + '.png')
            plt.show()


def compare(df1, df2, columns, name, bins=50):
    '''直方图比较'''
    counts = 0
    for col in columns:
        counts += 1

        fig = plt.figure()
        ax1 = fig.add_subplot(121)
        df1[col].hist(ax=ax1, grid=False, figsize=(15, 5), bins=bins)
        plt.title('origin\n{}\n'.format(col))
        ax2 = fig.add_subplot(122)
        df2[col].hist(ax=ax2, grid=False, figsize=(15, 5), bins=bins)
        plt.title('filled\n{}\n'.format(col))
        plt.subplots_adjust(wspace=0.3, hspace=10)
        plt.savefig('./output/' + name + '_compare' + str(counts) + '.png')
        plt.show()