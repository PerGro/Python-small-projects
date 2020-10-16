import tkinter as tk
import interfaces
from interfaces import *
from tkinter.messagebox import *
from tkinter import ttk


class BigWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.minsize(width=600, height=400)
        self.frame_create()
        self.frame_register()
        self.label_create()
        self.button_create()
        self.var_create()
        self.entry_create()
        self.entry_register()
        self.label_register()
        self.button_register()

    def _name_set(self, name):
        self.root.title(name)

    def _resize(self, width, height):
        self.root.minsize(width=width, height=height)

    def frame_create(self):
        pass

    def label_create(self):
        pass

    def button_create(self):
        pass

    def entry_create(self):
        pass

    def var_create(self):
        pass

    def frame_register(self):
        pass

    def label_register(self):
        pass

    def button_register(self):
        pass

    def entry_register(self):
        pass

    def var_register(self):
        pass

    def run(self):
        self.root.mainloop()

class SmallWindow(BigWindow):
    def __init__(self, title):
        self.root = tk.Tk()
        self.root.title(title)
        self.frame_create()
        self.frame_register()
        self.label_create()
        self.label_register()
        self.button_create()
        self.button_register()
        self.var_create()
        self.var_register()
        self.entry_create()
        self.entry_register()
        self.run()

class SmallWindowCreator:
    def __init__(self, title:str, function, inputtype:str, outputnames:list, *args):
        self.root = tk.Tk()
        self.root.title(title)
        self.widgets_name = args
        if isinstance(args[0], list):
            self.widgets_name = args[0]
        self.function = function
        self.inputtype = inputtype
        self.labels = []
        self.entrys = []
        self.outputnames = outputnames
        self.row = 0
        self.col = 0
        self.__widget_creator()
        button = tk.Button(self.root, text='查找', command=self.__getfun).grid(row=self.row, columnspan=2)
        self.root.mainloop()

    def __widget_creator(self):
        for i, widgets in enumerate(self.widgets_name):
            self.labels.append(tk.Label(self.root, text=self.widgets_name[i]))
            self.entrys.append(tk.Entry(self.root, width=30))
        for i in range(len(self.labels)):
            self.labels[i].grid(row=self.row, column=self.col)
            self.col = 1
            self.entrys[i].grid(row=self.row, column=self.col)
            self.row += 1
            self.col = 0

    def __getfun(self):
        res = {}
        input = [self.entrys[i].get() for i in range(len(self.entrys))]
        if self.inputtype == 'int':
            for i in input:
                i = int(i)
        elif self.inputtype == 'double' or self.inputtype == 'float':
            for i in input:
                i = float(i)
        results = []
        # results.extend((list(self.function(input))))
        try:
            results.extend(self.function(input))
        except TypeError:
            results.extend([self.function(input)])
        temp = []
        for i in results:
            if isinstance(i, list):
                for _ in i:
                    temp.append(_)
            else:
                temp.append(i)
        for i, name in enumerate(self.outputnames):
            res[name] = str(temp[i])
        strings = ''
        res_key = list(res.keys())
        res_val = list(res.values())
        for i in range(len(res_key)):
            strings += res_key[i] + ': ' + res_val[i]
        ReasultWindow(strings)


class ReasultWindow:
    def __init__(self, result:str):
        self.root = tk.Tk()
        self.root.title('结果')
        self.root.minsize(width=200, height=50)
        self.res = tk.Label(self.root, text=result)
        self.res.pack()
        self.run()

    def run(self):
        self.root.mainloop()

class WindowFindJmmj(SmallWindow):
    def __init__(self, title):
        super(WindowFindJmmj, self).__init__(title)

    def frame_create(self):
        self.frame_body = tk.Frame(self.root)

    def frame_register(self):
        self.frame_body.pack()

    def label_create(self):
        self.label_body_n = tk.Label(self.frame_body, text='钢筋根数')
        self.label_body_d = tk.Label(self.frame_body, text='钢筋公称直径')

    def entry_create(self):
        self.entry_body_n = tk.Entry(self.frame_body, width=50, textvariable=self.entry_body_n_intvar)
        self.entry_body_d = tk.Entry(self.frame_body, width=50, textvariable=self.entry_body_d_intvar)

    def var_create(self):
        self.entry_body_n_intvar = tk.IntVar()
        self.entry_body_d_intvar = tk.IntVar()

    def label_register(self):
        self.label_body_n.grid(row=0, column=0, padx=1, pady=1, sticky=tk.E)
        self.label_body_d.grid(row=1, column=0, padx=1, pady=1, sticky=tk.E)

    def entry_register(self):
        self.entry_body_n.grid(row=0, column=1)
        self.entry_body_d.grid(row=1, column=1)

    def button_create(self):
        self.button_body_find = tk.Button(self.frame_body, text='查找', command=self.find)

    def button_register(self):
        self.button_body_find.grid(row=3, columnspan=2)

    def find(self):
        res = get_jmspace(int(self.entry_body_n.get()), int(self.entry_body_d.get()))
        ReasultWindow('公称钢筋截面面积为： ' + str(res))


class DataFind(BigWindow):
    def __init__(self):
        super(DataFind, self).__init__()
        self._name_set('找参带师')

    def frame_create(self):
        self.frame_begin = tk.Frame(self.root, width=600, height=100)
        self.frame_body = tk.Frame(self.root, width=600, height=300)

    def label_create(self):
        self.label_begin_title = tk.Label(self.frame_begin, text='重生之我是配筋带师之找参专家')

    def button_create(self):
        self.button_body_jmmj = tk.Button(self.frame_body, text='公称截面面积', command=self.find_jmmj)
        self.button_body_envl = tk.Button(self.frame_body, text='根据环境求梁保护层厚度', command=self.find_envl)
        self.button_body_envb = tk.Button(self.frame_body, text='根据环境求板保护层厚度', command=self.find_envb)
        self.button_body_xdsyqgd = tk.Button(self.frame_body, text='相对受压区高度和最大抵抗矩系数', command=self.find_xdsyqgd)
        self.button_body_kyqd = tk.Button(self.frame_body, text='混凝土抗压强度', command=self.find_kyqd)
        self.button_body_klqd = tk.Button(self.frame_body, text='混凝土抗拉强度', command=self.find_klqd)
        self.button_body_gj_kyqd = tk.Button(self.frame_body, text='普通钢筋抗压强度', command=self.find_gj_kyqd)
        self.button_body_gj_klqd = tk.Button(self.frame_body, text='普通钢筋抗拉强度', command=self.find_gj_klqd)
        self.button_body_syqylxs = tk.Button(self.frame_body, text='混凝土受压区等效应力系数', command=self.find_syqylxs)
        self.button_body_all = tk.Button(self.frame_body, text='我全都要', command=self.find_all)
        self.button_body_custom1 = tk.Button(self.frame_body, text='自定义1')
        self.button_body_custom2 = tk.Button(self.frame_body, text='自定义2')
        self.button_body_custom3 = tk.Button(self.frame_body, text='自定义3')
        self.button_body_custom4 = tk.Button(self.frame_body, text='自定义4')

    def frame_register(self):
        self.frame_begin.pack()
        self.frame_body.pack()

    def label_register(self):
        self.label_begin_title.pack()

    def button_register(self):
        self.button_body_jmmj.grid(row=0, column=0, padx=5, pady=5)
        self.button_body_envl.grid(row=0, column=1, padx=5, pady=5)
        self.button_body_envb.grid(row=0, column=2, padx=5, pady=5)
        self.button_body_xdsyqgd.grid(row=0, column=3, padx=5, pady=5)
        self.button_body_kyqd.grid(row=1, column=0, padx=5, pady=5)
        self.button_body_klqd.grid(row=1, column=1, padx=5, pady=5)
        self.button_body_gj_kyqd.grid(row=1, column=2, padx=5, pady=5)
        self.button_body_gj_klqd.grid(row=1, column=3, padx=5, pady=5)
        self.button_body_syqylxs.grid(row=2, column=0, padx=5, pady=5)
        self.button_body_all.grid(row=3, columnspan=4)
        self.button_body_custom1.grid(row=6, column=0, padx=5, pady=5)
        self.button_body_custom2.grid(row=6, column=1, padx=5, pady=5)
        self.button_body_custom3.grid(row=6, column=2, padx=5, pady=5)
        self.button_body_custom4.grid(row=6, column=3, padx=5, pady=5)

    def find_jmmj(self):
        WindowFindJmmj('查找公称截面面积')

    def find_envl(self):
        SmallWindowCreator('根据环境查找梁保护层厚度', interfaces.get_envl_l, 'str', ['最低保护层厚度'], '环境等级')

    def find_envb(self):
        SmallWindowCreator('根据环境求板保护层厚度', interfaces.get_envb_l, 'str', ['最低保护层厚度'], '环境等级')

    def find_xdsyqgd(self):
        SmallWindowCreator('相对受压区高度和最大抵抗矩系数', interfaces.get_xdsygd_l, 'str', ['相对受压区高度', '\n界面最大抵抗矩系数'],
                           '混凝土强度等级', '钢筋强度等级')

    def find_kyqd(self):
        SmallWindowCreator('混凝土抗压强度', interfaces.get_kyqd_l, 'str', ['混凝土抗压强度'], '混凝土强度等级')

    def find_klqd(self):
        SmallWindowCreator('混凝土抗拉强度', interfaces.get_klqd_l, 'str', ['混凝土抗拉强度'], '混凝土强度等级')

    def find_gj_kyqd(self):
        SmallWindowCreator('普通钢筋抗压强度', interfaces.get_gj_kyqd_l, 'str', ['抗压强度为'], '钢筋强度等级')

    def find_gj_klqd(self):
        SmallWindowCreator('普通钢筋抗拉强度', interfaces.get_gj_klqd_l, 'str', ['抗拉强度为'], '钢筋强度等级')

    def find_syqylxs(self):
        SmallWindowCreator('混凝土受压区等效矩形应力系数', interfaces.get_syqylxs_l, 'str', ['α1', '\nβ1'], '混凝土强度等级')

    def find_all(self):
        SmallWindowCreator('我全都要', interfaces.get_all, 'str',
                           ['相对受压区高度', '\n界面最大抵抗矩系数',
                            '\n混凝土抗压强度',
                            '\n混凝土抗拉强度',
                            '\n普通钢筋抗压强度为',
                            '\n普通钢筋抗拉强度为',
                            '\nα1', '\nβ1'],
                           '混凝土强度等级', '钢筋强度等级')

    def custom_set1(self, title:str, windowsname, func, inputtype, outputs, inputname):
        """
        用户接口
        :param title: 控件名称
        :param windowsname: 子窗口标题
        :param func: 用户操作函数
        :param inputtype: 输入数据类型，只支持单一类型
        :param outputs: 输出结果的结果名称
        :param inputname: 输入参数的参数名称
        :return:
        """
        self.button_body_custom1.config(text=title)
        if title == 'peijin':
            showerror('哦豁，恭喜你发现彩蛋！', 'JOJO, 我不配筋了！')
            return 0
        def getfuc():
            SmallWindowCreator(windowsname, func, inputtype, outputs, inputname)
        self.button_body_custom1.config(command=getfuc)

    def custom_set2(self, title:str, windowsname, func, inputtype, outputs, inputname):
        self.button_body_custom2.config(text=title)
        def getfuc():
            SmallWindowCreator(windowsname, func, inputtype, outputs, inputname)
        self.button_body_custom2.config(command=getfuc)

    def custom_set3(self, title:str, windowsname, func, inputtype, outputs, inputname):
        self.button_body_custom3.config(text=title)
        def getfuc():
            SmallWindowCreator(windowsname, func, inputtype, outputs, inputname)
        self.button_body_custom3.config(command=getfuc)

    def custom_set4(self, title:str, windowsname, func, inputtype, outputs, inputname):
        self.button_body_custom4.config(text=title)
        def getfuc():
            SmallWindowCreator(windowsname, func, inputtype, outputs, inputname)
        self.button_body_custom4.config(command=getfuc)

    def custom_set(self, title, windowsname, func, inputtype, outputs, inputname, index):
        if index == 1:
            self.custom_set1(title, windowsname, func, inputtype, outputs, inputname)
        elif index == 2:
            self.custom_set2(title, windowsname, func, inputtype, outputs, inputname)
        elif index == 3:
            self.custom_set3(title, windowsname, func, inputtype, outputs, inputname)
        elif index == 4:
            self.custom_set4(title, windowsname, func, inputtype, outputs, inputname)


class MainWindow(BigWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self._name_set('主页面')

    def button_create(self):
        self.root_zj_button = tk.Button(self.root, text='配筋带师', command=self.pj)
        self.root_zc_button = tk.Button(self.root, text='找参带师', command=self.zc)

    def button_register(self):
        self.root_zj_button.place(x=50, y=100)
        self.root_zc_button.place(x=150, y=100)

    def zc(self):
        d = DataFind()
        d.run()

    def pj(self):
        g = GetGangJin()
        g.run()


class GetGangJin(BigWindow):
    def __init__(self):
        super(GetGangJin, self).__init__()
        self._name_set('配筋带师')
        self._resize(1, 1)

    def frame_create(self):
        self.begin = tk.Frame(self.root, width=400)
        self.body = tk.Frame(self.root, width=400)

    def label_create(self):
        self.label_begin_title = tk.Label(self.begin, text='配筋带师')
        self.label_body_as = tk.Label(self.body, text='所需钢筋截面面积')
        self.label_body_pc = tk.Label(self.body, text='容许偏差(%)')
        self.label_body_nums = tk.Label(self.body, text='最大查找种类')
        self.label_body_b = tk.Label(self.body, text='等效截面尺寸b')
        self.label_body_h = tk.Label(self.body, text='等效界面尺寸h')

    def var_create(self):
        self.entry_body_as_int = tk.IntVar()

    def entry_create(self):
        self.entry_body_as = tk.Entry(self.body, width=40, textvariable=self.entry_body_as_int)
        self.entry_body_pc = tk.Entry(self.body, width=5)
        self.entry_body_nums = tk.Entry(self.body, width=40)
        self.entry_body_b = tk.Entry(self.body, width=40)
        self.entry_body_h = tk.Entry(self.body, width=40)

    def button_create(self):
        self.button_body_find = tk.Button(self.body, text='查询', command=self.find)

    def frame_register(self):
        self.begin.pack()
        self.body.pack()

    def label_register(self):
        self.label_begin_title.pack()
        self.label_body_as.grid(row=0, column=0, sticky=tk.E, padx=1, pady=1)
        self.label_body_pc.grid(row=1, column=0, sticky=tk.E, padx=1, pady=1)
        self.label_body_nums.grid(row=2, column=0, sticky=tk.E, padx=1, pady=1)
        self.label_body_b.grid(row=3, column=0, sticky=tk.E, padx=1, pady=1)
        self.label_body_h.grid(row=4, column=0, sticky=tk.E, padx=1, pady=1)

    def button_register(self):
        self.button_body_find.grid(row=100, columnspan=2)

    def entry_register(self):
        self.entry_body_as.grid(row=0, column=1)
        self.entry_body_pc.grid(row=1, column=1)
        self.entry_body_nums.grid(row=2, column=1)
        self.entry_body_b.grid(row=3, column=1)
        self.entry_body_h.grid(row=4, column=1)

    def find(self):
        pass


if __name__ == '__main__':
    d = MainWindow()
    d.run()
