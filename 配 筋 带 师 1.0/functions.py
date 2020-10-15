import datasets
from datasets import *

def get_pjl(a, b, h):
    """
    计算配筋率
    :param a: 为钢筋截面面积
    :param b: 为截面尺寸
    :param h: 为有效高度或箍筋间距
    :return: 配筋率
    """
    return a / b / h

