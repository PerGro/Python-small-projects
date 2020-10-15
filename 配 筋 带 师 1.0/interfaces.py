import numpy as np
import datasets
from datasets import ENV_B, ENV_L, XDSYGD_JMZDDKJXS, KLQD, KYQD
from datasets import *

def get_envb(env:str):
    """
    获得环境因素下板的最低保护层厚度
    :param env:
    :return:
    """
    return ENV_B[env]

def get_envl(env:str):
    """
    获得环境因素下梁的最低保护层厚度
    :param env:
    :return:
    """
    return ENV_L[env]

def get_envl_l(env:list):
    return get_envl(env[0])

def get_envb_l(env:list):
    return get_envb(env[0])

def get_jmspace(n:int, d:int):
    """
    用来获得公称截面面积
    :param n: 为钢筋数量
    :param d: 为钢筋直径
    :return: 公称直径
    """
    a = np.load('as.npy')
    index = [6, 8, 10, 12, 14, 16, 18, 20, 22, 25, 28, 32, 36, 40, 50]
    _ = 0
    for i, ind in enumerate(index):
        if ind == d:
            break
        _ += 1
    return a[_][n - 1]

def get_xdsygd(h:str, g:str):
    return XDSYGD_JMZDDKJXS[h][g]

def get_xdsygd_l(strings:list):
    if int(strings[0][1:]) < 50:
        strings[0] = 'C50'
    return get_xdsygd(strings[0], strings[1])

def get_kyqd(h:str):
    return KYQD[h]

def get_kyqd_l(strings:list):
    return get_kyqd(strings[0])

def get_klqd(h:str):
    return KLQD[h]

def get_klqd_l(strings:list):
    return get_klqd(strings[0])

def get_gj_kyqd(g:str):
    return datasets.GJ_KYQD[g]

def get_gj_kyqd_l(strings:list):
    return get_gj_kyqd(strings[0])

def get_gj_klqd(g:str):
    return datasets.GJ_KLQD[g]

def get_gj_klqd_l(strings:list):
    return get_gj_klqd(strings[0])

def get_syqylxs(c:str):
    return SYQYLXS[c]

def get_syqylxs_l(strings:list):
    if int(strings[0][1:]) < 50:
        strings[0] = 'C50'
    return get_syqylxs(strings[0])
