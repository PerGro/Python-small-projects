import datasets
from datasets import *
import numpy as np


def get_pjl(a, b, h):
    """
    计算配筋率
    :param a: 为钢筋截面面积
    :param b: 为截面尺寸
    :param h: 为有效高度或箍筋间距
    :return: 配筋率
    """
    return a / b / h


def find_gj(b, h, As, nums=1, e=0.05):
    pjl = As / b / h
    jmmatrix = np.load('as.npy')
    bestd = [-10000, 0, 0]
    bestu = [100000, 0, 0]
    rows_len = len(jmmatrix) - 1
    col_len = len(jmmatrix[0]) - 1
    row = 0
    col = col_len
    res = []
    while 1 and col > 0 and row < 15:
        temp = jmmatrix[row][col]
        if temp < As * (1 - e):
            row += 1
            continue
        while 1 and col >= 0 and row < 15:
            if temp > As * (1 + e) and temp > As * (1 - e):
                col -= 1
                temp = jmmatrix[row][col]
                continue
            else:
                break
        if col < 0 or row >= 16:
            break
        elif temp > As * (1 + e) or temp < As * (1 - e):
            continue
        else:
            res.append([temp, row, col])
            rou = get_dif(As, temp)
            if rou < 0 and rou > bestd[0]:
                bestd[0] = rou
                bestd[1] = row
                bestd[2] = col
            elif rou > 0 and rou < bestu[0]:
                bestu[0] = rou
                bestu[1] = row
                bestu[2] = col
        col -= 1
    for i in res:
        print(i)
    if nums != 1:
        pass



def get_dif(a, b):
    return (a - b) / a

if __name__ == '__main__':
    find_gj(250, 460, 1425, e=0.05)
