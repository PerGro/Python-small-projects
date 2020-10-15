import tk

GJ_KLQD = {'300': 270, '335': 300, '400': 360, '500': 435}
b = tk.DataFind()
def function(strings:list):
    return GJ_KLQD[strings[0]]
b.custom_set1('WTF', 'wtf', function, 'str', ['抗拉强度为'], ['钢筋强度等级'])
b.run()