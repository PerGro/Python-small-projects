import pandas as pd
import tkinter as tk
from tkinter import filedialog
import os
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import showerror
import re

"""本脚本所有输入数字均为真实数字，无需考虑因下标带来的差异"""

LONG_ENTRY = 80
MID_ENTRY_POS = 100
BUTTON_RIGHT_MID_LONG_ENTRY = 680
SHORT_ENTRY = 10
RUN_BUTTON = 350
QUIT_BUTTON = 450
RETURN_BUTTON = 10
TO_OTHER = 100

class Frame:
    def __init__(self):
        """
        框架初始化，变量初始化，Entry初始化，Label初始化，Button初始化，item初始化，loop()
        """
        self.root = tk.Tk()
        self.frame_init()
        self.var_init()
        self.txt_create()
        self.label_create()
        self.button_create()
        self.item_create()

        self.txt_register()
        self.label_register()
        self.button_register()
        self.item_register()
        self.loop()

    def frame_init(self):
        """整体框架的构造函数，主要用于负责tk.Frame的初始化"""
        pass

    def var_init(self):
        """负责变量类的初始化，主要负责tk.IntVar(), tk.StringVar()等"""
        pass

    def txt_create(self):
        """负责文本框类的创建，包括tk.Entry(), tk.scrooledtxt.ScroolledText()"""
        pass

    def txt_register(self):
        """注册（渲染）tk.Entry(), tk.scroolledtext.ScroolledText()类Widget"""
        pass

    def label_create(self):
        """负责Label类的创建，主要为tk.Label()"""
        pass

    def item_create(self):
        """负责除tk.Label(), tk.Button(), tk.Entry(), tk.scroolledtext.ScroolledText()的其他部件如tk.Scroollbar()的创建"""
        pass

    def item_register(self):
        """负责注册item_create中的部件"""
        pass

    def button_create(self):
        """负责创建按钮类部件，为tk.Button()"""
        pass

    def label_register(self):
        """负责注册label_create中的部件"""
        pass

    def button_register(self):
        """负责注册button_create中的部件"""
        pass

    def loop(self):
        self.root.mainloop()

    def return_to_menu(self):
        """用于返回主菜单"""
        self.root.destroy()
        MainMenu()

    def to_other(self):
        """用于调出选项菜单"""
        self.root.destroy()
        SmallWindow()

    def quit(self):
        """用于退出"""
        self.root.destroy()


class MainMenu(Frame):
    """主界面"""

    def __init__(self):
        super(MainMenu, self).__init__()

    def frame_init(self):
        self.root.title('Excel快速处理器')
        self.root.geometry('825x720')
        self.root.minsize(width=825, height=720)
        self.root.maxsize(width=825, height=720)

    def button_create(self):
        self.button1 = tk.Button(self.root, text='查找模式', width=25, height=5, command=self.to_find)
        self.button2 = tk.Button(self.root, text='筛选模式', width=25, height=5, command=self.filter)

    def button_register(self):
        self.button1.place(x=65, y=310)
        self.button2.place(x=590, y=310)

    def loop(self):
        self.root.mainloop()

    def to_find(self):
        self.root.destroy()
        FindFunction()

    def filter(self):
        self.root.destroy()
        Filter()


class FindFunction(Frame):  # 快速查找模块
    """命名规则：self.frame_name_widgetfunction_widgetname(_datatype)"""

    def __init__(self):
        super(FindFunction, self).__init__()

    def frame_init(self):
        self.root.title('让我看看是哪个龟孙')
        self.root.geometry('825x720')
        self.root.minsize(width=825, height=720)
        self.root.maxsize(width=825, height=720)

        self.frame_head = tk.Frame(self.root, height=40, width=825)
        self.frame_file = tk.Frame(self.root, height=180, width=825)
        self.frame_result = tk.Frame(self.root, height=400, width=825)
        self.frame_end = tk.Frame(self.root, height=100, width=825)

        self.frame_head.pack()
        self.frame_file.pack()
        self.frame_result.pack()
        self.frame_end.pack()

    def var_init(self):
        """
        self.frame_file_choose_orgin_entry_string  与目标文件文本框连接
        self.frame_file_choose_orgin_config_sheet_entry_string  与sheet选择框相连接
        self.frame_file_choose_compare_entry_string 与花名册选择框相连接
        self.frame_file_compare_config_entry1_int   与选择姓名列相连接
        self.frame_file_compare_config_entry2_int   与选择id列相连接
        self.frame_file_compare_config_entry3_int   与选择电话相连接
        self.frame_file_orgin_config_entry_int  与选择检测开始行连解
        self.frame_file_orgin_config_entry2_int  与选择开始列连接
        """
        self.frame_file_choose_orgin_entry_string = tk.StringVar()
        self.frame_file_choose_orgin_config_sheet_entry_string = tk.StringVar()
        self.frame_file_choose_compare_entry_string = tk.StringVar()
        self.frame_file_compare_config_entry1_int = tk.StringVar()
        self.frame_file_compare_config_entry2_int = tk.StringVar()
        self.frame_file_compare_config_entry3_int = tk.StringVar()
        self.frame_file_orgin_config_entry_int = tk.StringVar()
        self.frame_file_orgin_config_entry2_int = tk.StringVar()
        self.frame_file_custom_name_string = tk.StringVar()
        self.frame_file_custom_id_string = tk.StringVar()
        self.frame_file_custom_phone_string = tk.StringVar()

        self.frame_file_choose_orgin_entry_string.set('请输入/选择目标文件')
        self.frame_file_choose_compare_entry_string.set('请输入/选择花名册文件')
        self.frame_file_custom_name_string.set('姓名')
        self.frame_file_custom_id_string.set('学号')
        self.frame_file_custom_phone_string.set('电话')

    def txt_create(self):
        self.frame_file_choose_orgin_entry = tk.Entry(self.frame_file, textvariable=self.frame_file_choose_orgin_entry_string, width=80)
        self.frame_file_choose_compare_entry = tk.Entry(self.frame_file, textvariable=self.frame_file_choose_compare_entry_string, width=80)
        self.frame_file_choose_orgin_config_sheet_entry = tk.Entry(self.frame_file, width=10, textvariable=self.frame_file_choose_orgin_config_sheet_entry_string)
        self.frame_file_orgin_config_entry = tk.Entry(self.frame_file, width=3, textvariable=self.frame_file_orgin_config_entry_int)
        self.frame_file_orgin_config_entry2 = tk.Entry(self.frame_file, width=3, textvariable=self.frame_file_orgin_config_entry2_int)
        self.frame_file_compare_config_entry1 = tk.Entry(self.frame_file, width=3, textvariable=self.frame_file_compare_config_entry1_int)
        self.frame_file_compare_config_entry2 = tk.Entry(self.frame_file, width=3, textvariable=self.frame_file_compare_config_entry2_int)
        self.frame_file_compare_config_entry3 = tk.Entry(self.frame_file, width=3, textvariable=self.frame_file_compare_config_entry3_int)
        self.frame_result_text = ScrolledText(self.frame_result, height=28, width=100, undo=True, state=tk.DISABLED)
        s = tk.Text()

    def txt_register(self):
        self.frame_file_choose_orgin_entry.place(x=100, y=5)
        self.frame_file_choose_compare_entry.place(x=100, y=100)
        self.frame_file_choose_orgin_config_sheet_entry.place(x=120, y=50)
        self.frame_file_orgin_config_entry.place(x=650, y=50)
        self.frame_file_orgin_config_entry2.place(x=675, y=50)
        self.frame_file_compare_config_entry1.place(x=620, y=150)  # name
        self.frame_file_compare_config_entry2.place(x=645, y=150)  # id
        self.frame_file_compare_config_entry3.place(x=670, y=150)  # phone number
        self.frame_result_text.place(x=50, y=10)

    def label_create(self):
        self.frame_head_title = tk.Label(self.frame_head, text='快速查找器', font=('黑体', 20, 'bold'))
        self.frame_file_choose_orgin = tk.Label(self.frame_file, text='选择目标文件')  # 要对比的文件
        self.frame_file_choose_orgin_config_sheet = tk.Label(self.frame_file, text='请输入工作薄名称')
        self.frame_file_choose_compare = tk.Label(self.frame_file, text='选择花名册')  # 花名册
        self.frame_file_orgin_config = tk.Label(self.frame_file, text='姓名读取行与列')
        self.frame_file_compare_config = tk.Label(self.frame_file, text='姓名、id、电话号码读取列')

    def button_create(self):
        self.frame_file_brower1 = tk.Button(self.frame_file, text='浏览', height=1, command=self.cat_excel1)
        self.frame_file_brower2 = tk.Button(self.frame_file, text='浏览', height=1, command=self.cat_excel2)
        self.frame_end_button1 = tk.Button(self.frame_end, text='查询', font=('黑体', 20, 'bold'), command=self.run)
        self.frame_end_button2 = tk.Button(self.frame_end, text='退出', font=('黑体', 20, 'bold'), command=self.quit)
        self.frame_end_button_return = tk.Button(self.frame_end, text='返回主页面', font=('黑体', 10, 'bold'), command=self.return_to_menu)
        self.frame_end_button_choose_other = tk.Button(self.frame_end, text='进入其他功能区', font=('黑体', 10, 'bold'), command=self.to_other)
        self.frame_file_custom = tk.Button(self.frame_file, text='自定义', command=self.custom)

    def label_register(self):
        self.frame_head_title.place(x=350, y=5)
        self.frame_file_choose_orgin.place(x=5, y=5)
        self.frame_file_choose_orgin_config_sheet.place(x=5, y=50)
        self.frame_file_choose_compare.place(x=10, y=100)
        self.frame_file_orgin_config.place(x=550, y=50)
        self.frame_file_compare_config.place(x=470, y=150)

    def button_register(self):
        self.frame_file_brower1.place(x=680, y=5)
        self.frame_file_brower2.place(x=680, y=100)
        self.frame_end_button1.place(x=350, y=10)
        self.frame_end_button2.place(x=450, y=10)
        self.frame_end_button_return.place(x=10, y=10)
        self.frame_end_button_choose_other.place(x=100, y=10)
        self.frame_file_custom.place(x=710, y=150)

    def loop(self):
        self.root.mainloop()

    def quit(self):
        self.root.destroy()

    def cat_excel1(self):
        """控制目标文件的输入读取"""
        self.file_orgin = filedialog.askopenfilename()
        self.frame_file_choose_orgin_entry_string.set(self.file_orgin)
        self.frame_file_choose_orgin_config_sheet_entry_string.set('Sheet1')

    def cat_excel2(self):
        """控制花名册的输入读取"""
        self.file_compare = filedialog.askopenfilename()
        try:
            file = pd.read_excel(self.file_compare, header=None)
        except FileNotFoundError:
            return 0
        # 保证在不选择任何文件情况下仍不会报错
        self.frame_file_choose_compare_entry_string.set(self.file_compare)
        length = 0
        index_list = []
        try:
            while True:
                file.iloc[0, length]
                index_list.append(file.iloc[0, length])
                length += 1
        except IndexError:
            count = 1
            for index in index_list:
                if index == self.frame_file_custom_name_string.get():
                    self.frame_file_compare_config_entry1_int.set(str(count))
                elif index == self.frame_file_custom_id_string.get():
                    self.frame_file_compare_config_entry2_int.set(str(count))
                elif index == self.frame_file_custom_phone_string.get():
                    self.frame_file_compare_config_entry3_int.set(str(count))
                count += 1

    def run(self):
        """点击“查询”后会执行的方法"""
        self.frame_result_text.config(state=tk.NORMAL)
        self.frame_result_text.delete('1.0', tk.END)
        # 所有需要输入的数字均为真实数字，无需再考虑下标问题
        try:
            FindGuiSun(self,
                       self.frame_file_choose_compare_entry.get(),
                       int(self.frame_file_compare_config_entry1.get()) - 1,
                       int(self.frame_file_compare_config_entry2.get()) - 1,
                       int(self.frame_file_compare_config_entry3.get()) - 1,
                       int(self.frame_file_orgin_config_entry.get()),
                       int(self.frame_file_orgin_config_entry2.get()),
                       self.frame_file_choose_orgin_entry.get(),
                       self.frame_file_choose_orgin_config_sheet_entry.get(),
                       name=True,
                       id=True,
                       phone=True
                       )
        except ValueError:
            #   阴阳对话框
            showerror(title='用这个程序还能出错，不会吧，不会吧', message='看看文件有没有加载好，以及检查一下文件的目录有没有问题，注意如果是手动输入，请把所有\\改为/')
        self.frame_result_text.config(state=tk.DISABLED)

    def return_to_menu(self):
        """返回主菜单的方法"""
        self.root.destroy()
        MainMenu()

    def to_other(self):
        """
        跳转到其他工作区的方法，2020/9/2：目前只完善了龟孙查找器
        """
        self.root.destroy()
        SmallWindow()

    def custom(self):
        class ChooseWindow:
            """为控制“自定义”组件的windows"""

            def __init__(self, windows, name, id, phone):
                """
                大杂烩
                :param windows: 父窗口
                :param name: 父窗口的frame_file_custom_name_string
                :param id: 父窗口的frame_file_custom_id_string
                :param phone: 父窗口的frame_file_custom_phone_string
                """
                self.windows = windows
                self.root = tk.Tk()
                self.root.minsize(width=400, height=150)
                self.root.maxsize(width=400, height=150)
                self.root.title('自定义筛选')
                self.name_string = tk.StringVar()
                self.id_string = tk.StringVar()
                self.phone_string = tk.StringVar()
                self.frame_file_custom_name_string = ''
                self.frame_file_custom_id_string = ''
                self.frame_file_custom_phone_string = ''
                self.set_up()
                self.name_label = tk.Label(self.root, text='name')
                self.name_label.place(x=70, y=20)
                self.id_label = tk.Label(self.root, text='id')
                self.id_label.place(x=170, y=20)
                self.phone_label = tk.Label(self.root, text='phone number')
                self.phone_label.place(x=270, y=20)
                self.tips_label = tk.Label(self.root, text='请输入新值')
                self.tips_label.place(x=5, y=50)
                self.button1 = tk.Button(self.root, text='确定', command=self.sure)
                self.button1.place(x=120, y=110)
                self.button2 = tk.Button(self.root, text='取消', command=self.quit)
                self.button2.place(x=220, y=110)
                self.name_entry = tk.Entry(self.root, width=8, textvariable=self.name_string)
                self.name_entry.insert(0, name)
                self.name_entry.place(x=70, y=50)
                self.id_entry = tk.Entry(self.root, width=8, textvariable=self.id_string)
                self.id_entry.insert(0, id)
                self.id_entry.place(x=170, y=50)
                self.phone_entry = tk.Entry(self.root, width=8, textvariable=self.phone_string)
                self.phone_entry.insert(0, phone)
                self.phone_entry.place(x=270, y=50)
                self.loop()

            def loop(self):
                self.root.mainloop()

            def set_up(self):
                # 默认为这些，可通过更改来改变默认参数
                self.name_string.set('姓名')
                self.id_string.set('学号')
                self.phone_string.set('电话号码')

            def sure(self):
                self.frame_file_custom_name_string = self.name_entry.get()
                self.frame_file_custom_id_string = self.id_entry.get()
                self.frame_file_custom_phone_string = self.phone_entry.get()
                self.windows.frame_file_custom_name_string.set(self.frame_file_custom_name_string)
                self.windows.frame_file_custom_id_string.set(self.frame_file_custom_id_string)
                self.windows.frame_file_custom_phone_string.set(self.frame_file_custom_phone_string)
                length = 0
                index_list = []
                try:
                    file = pd.read_excel(self.windows.file_compare, header=None)
                    while True:
                        file.iloc[0, length]
                        index_list.append(file.iloc[0, length])
                        length += 1
                except IndexError:
                    count = 1
                    for index in index_list:
                        if index == self.windows.frame_file_custom_name_string.get():
                            self.windows.frame_file_compare_config_entry1_int.set(str(count))
                        elif index == self.windows.frame_file_custom_id_string.get():
                            self.windows.frame_file_compare_config_entry2_int.set(str(count))
                        elif index == self.windows.frame_file_custom_phone_string.get():
                            self.windows.frame_file_compare_config_entry3_int.set(str(count))
                        count += 1
                except FileNotFoundError:
                    """此错误会在当自定义筛选找不到对应的文件时被调用"""
                    showerror(title='用这个程序还能出错，不会吧，不会吧', message='看看文件有没有加载好，以及检查一下文件的目录有没有问题，注意如果是手动输入，请把所有\\改为/')
                except AttributeError:
                    showerror(title='用这个程序还能出错，不会吧，不会吧', message='看看文件有没有加载好，以及检查一下文件的目录有没有问题，注意如果是手动输入，请把所有\\改为/')
                self.root.destroy()

            def quit(self):
                self.root.destroy()

        c = ChooseWindow(self, self.frame_file_custom_name_string.get(), self.frame_file_custom_id_string.get(), self.frame_file_custom_phone_string.get())


'''
此为查找的主程序
'''


class FindGuiSun:
    def __init__(self, textbox, file, name_col, id_col, phone_col, find_row=None, find_col=None, file_name=None, sheet_name='0', **kwargs):  # file_name为目标文件的路径
        """
        :param textbox: 父窗口
        :param file: 花名册
        :param name_col: 查找花名册所在列
        :param id_col: 查找id所在列
        :param phone_col: 查找电话所在列
        :param find_row: 目标文件查找行
        :param find_col: 目标文件查找列
        :param file_name: 目标文件路径
        :param sheet_name: 目标文件sheet名
        :param kwargs: name id phone三个选项，分别控制是否打印姓名、id、电话信息（可自定义）
        """
        self.textbox = textbox
        self.file = pd.read_excel(file)
        length = self.getlength(self.file, name_col)
        name_list = self.file.iloc[:length, name_col]
        id_list = self.file.iloc[:length, id_col]
        phone_number_list = self.file.iloc[:length, phone_col]
        id_and_phone = []
        for i in range(len(id_list)):
            id_and_phone.append([id_list[i], phone_number_list[i]])
        persons = dict(zip(name_list, id_and_phone))
        self.name = name_list
        self.phone_info = persons
        self.find_col = find_col
        self.find_row = find_row
        self.file_name = file_name
        self.find_nums = length
        self.sheet_name = sheet_name
        self.option = kwargs
        self.length = length
        self.find_length = 0
        self.compared()

    def getlength(self, file, col, row=0):
        openfile = file
        namecol = col
        length = 0
        try:
            while True:
                openfile.iloc[length + row, namecol]
                length += 1
        except IndexError:
            return length

    def __print_info(self, info=None, excel_info=None, name=False, ids=False, phone_number=False):
        self.textbox.frame_result_text.insert(tk.END, "查找excel：" + excel_info[0], '查找列位置：' + str(excel_info[1]), '查找行位置：' + str(excel_info[2]) + '\n')
        self.textbox.frame_result_text.insert(tk.END, '花名册中有 ' + str(self.length) + '\n')
        self.textbox.frame_result_text.insert(tk.END, '找到(包括重复项) ' + str(self.find_length) + '\n')
        self.textbox.frame_result_text.insert(tk.END, '还有这些龟孙没有交：' + '\n')
        self.textbox.frame_result_text.insert(tk.END, '————————————————————————————' + '\n')
        for i in range(len(info)):
            if name:
                self.textbox.frame_result_text.insert(tk.END, self.textbox.frame_file_custom_name_string.get() + ': ' + str(info[i][0]) + '\n')
            if ids:
                self.textbox.frame_result_text.insert(tk.END, self.textbox.frame_file_custom_id_string.get() + ': ' + str(info[i][1]) + '\n')
            if phone_number:
                self.textbox.frame_result_text.insert(tk.END, self.textbox.frame_file_custom_phone_string.get() + ': ' + str(info[i][2]) + '\n')
            self.textbox.frame_result_text.insert(tk.END, '————————————————————————————' + '\n')
        self.textbox.frame_result_text.insert(tk.END, '共{}个龟孙没交'.format(len(info)) + '\n')

    def compared(self):
        find_file = pd.read_excel(r'{}'.format(self.file_name), sheet_name=self.sheet_name, header=None)
        names = []
        name_length = self.getlength(find_file, self.find_col, row=self.find_row)
        if self.find_col:
            names = find_file.iloc[:name_length, self.find_col - 1]
        if self.find_row:
            names = find_file.iloc[self.find_row - 1: name_length + self.find_row - 2, self.find_col - 1]
        if self.find_col is None and self.find_row is None:
            return 0
        names = list(names)
        for i in range(len(names)):
            names[i] = str(names[i])
        while 'nan' in names:
            names.remove('nan')
        temp = list(self.name)
        self.find_length = len(names)
        for name_num in range(len(names)):
            if names[name_num] in temp:
                temp.remove(names[name_num])
        print_info = self.option
        info = []
        for i in range(len(temp)):
            info.append([temp[i], self.phone_info[temp[i]][0], self.phone_info[temp[i]][1]])
        self.__print_info(info=info, excel_info=[self.file_name, self.find_col, self.find_row], name=print_info['name'], ids=print_info['id'], phone_number=print_info['phone'])


class PiChuLi(Frame):
    def __init__(self):
        super(PiChuLi, self).__init__()

    def frame_init(self):
        super(PiChuLi, self).frame_init()


class SmallWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('请翻个牌子吧')
        self.root.geometry('270x480')
        self.root.minsize(width=270, height=480)
        self.root.maxsize(width=270, height=480)
        self.back = 0
        self.main_menu()
        self.root.mainloop()

    def main_menu(self):
        button1 = tk.Button(self.root, text='龟孙查找器', command=self.return_back1)
        button2 = tk.Button(self.root, text='高级筛选器', command=self.return_back2)

        button1.pack(fill=tk.X)
        button2.pack(fill=tk.X)

    """暂时没找到什么好方法"""

    def return_back1(self):
        self.root.destroy()
        FindFunction()

    def return_back2(self):
        self.root.destroy()
        Filter()


"""以下为筛选器"""


class Filter(Frame):
    def __init__(self):
        super().__init__()
        self.file_path = None
        self.file = None

    def frame_init(self):
        self.root.title('高级筛选器')
        self.root.geometry('825x720')
        self.root.minsize(width=825, height=720)
        self.root.maxsize(width=825, height=720)

        self.file_choose = tk.Frame(self.root, width=825, height=80)
        self.file_filter = tk.Frame(self.root, width=825, height=100)
        self.file_re = tk.Frame(self.root, width=825, height=110)
        self.file_result = tk.Frame(self.root, width=825, height=380)
        self.file_end = tk.Frame(self.root, width=825, height=50)

        self.file_choose.pack()
        self.file_re.pack()
        self.file_filter.pack()
        self.file_result.pack()
        self.file_end.pack()

        # self.show_frames()  # 用于显示各frame的位置

    def show_frames(self):
        self.file_choose.config(bg='blue')
        self.file_re.config(bg='green')
        self.file_filter.config(bg='pink')
        self.file_result.config(bg='black')
        self.file_end.config(bg='gray')

    def var_init(self):
        self.file_choose_entry_string = tk.StringVar()
        self.file_choose_sheet_entry_string = tk.StringVar()
        self.file_re_relist_entry_string = tk.StringVar()
        self.file_re_choose_pos_row_entry_int = tk.IntVar()
        self.file_re_choose_pos_col_entry_int = tk.IntVar()
        self.file_filter_quick_filter_entry_string = tk.StringVar()
        self.file_filter_quick_filter_row_entry_int = tk.IntVar()
        self.file_filter_quick_filter_col_entry_int = tk.IntVar()

    def label_create(self):
        self.file_choose_label = tk.Label(self.file_choose, text='选择文件:')
        self.file_choose_sheet_label = tk.Label(self.file_choose, text='选择工作薄:')
        self.file_re_relabel_label = tk.Label(self.file_re, text='请输入正则表达式:')
        self.file_re_choose_pos_label = tk.Label(self.file_re, text='请输入开始筛选的行与列:')
        self.file_filter_quick_filter_label = tk.Label(self.file_filter, text='快速筛选:')
        self.file_filter_quick_filter_col_label = tk.Label(self.file_filter, text='请输入筛选列:')

    def txt_create(self):
        self.file_choose_entry = tk.Entry(self.file_choose, width=LONG_ENTRY, textvariable=self.file_choose_entry_string)
        self.file_choose_sheet_entry = tk.Entry(self.file_choose, width=SHORT_ENTRY, textvariable=self.file_choose_sheet_entry_string)
        self.file_re_relist_entry = tk.Entry(self.file_re, width=LONG_ENTRY, textvariable=self.file_re_relist_entry_string)
        self.file_re_choose_pos_row_entry = tk.Entry(self.file_re, width=3, textvariable=self.file_re_choose_pos_row_entry_int)
        self.file_re_choose_pos_col_entry = tk.Entry(self.file_re, width=3, textvariable=self.file_re_choose_pos_col_entry_int)
        self.file_filter_quick_filter_entry = tk.Entry(self.file_filter, width=LONG_ENTRY, textvariable=self.file_filter_quick_filter_entry_string)
        self.file_filter_quick_filter_row_entry = tk.Entry(self.file_filter, width=3, textvariable=self.file_filter_quick_filter_row_entry_int)
        self.file_filter_quick_filter_col_entry = tk.Entry(self.file_filter, width=3, textvariable=self.file_filter_quick_filter_col_entry_int)
        self.file_result_entry = ScrolledText(self.file_result, height=28, width=100, undo=True, state=tk.DISABLED)

    def button_create(self):
        self.file_choose_button = tk.Button(self.file_choose, text='浏览', command=self.read_file)
        self.file_choose_reflash_button = tk.Button(self.file_choose, text='重新加载', command=self.reset_file)
        self.file_re_filter_button = tk.Button(self.file_re, text='筛选')
        self.file_re_filter_clear_button = tk.Button(self.file_re, text='清空', command=self.clear)
        self.file_filter_quick_filter_delete_button = tk.Button(self.file_filter, text='剔除')
        self.file_filter_quick_filter_get_button = tk.Button(self.file_filter, text='提取')
        self.file_end_run_button = tk.Button(self.file_end, text='运行', font=('黑体', 20, 'bold'))
        self.file_end_quit_button = tk.Button(self.file_end, text='退出', command=self.quit, font=('黑体', 20, 'bold'))
        self.file_end_button_return = tk.Button(self.file_end, text='返回主页面', font=('黑体', 10, 'bold'), command=self.return_to_menu)
        self.file_end_button_choose_other = tk.Button(self.file_end, text='进入其他功能区', font=('黑体', 10, 'bold'), command=self.to_other)

    def label_register(self):
        self.file_choose_label.place(x=50, y=5)
        self.file_choose_sheet_label.place(x=50, y=50)
        self.file_re_relabel_label.place(x=30, y=5)
        self.file_re_choose_pos_label.place(x=50, y=60)
        self.file_filter_quick_filter_label.place(x=50, y=5)
        self.file_filter_quick_filter_col_label.place(x=50, y=60)

    def txt_register(self):
        self.file_choose_entry.place(x=MID_ENTRY_POS+10, y=10)
        self.file_choose_sheet_entry.place(x=130, y=55)
        self.file_re_relist_entry.place(x=MID_ENTRY_POS, y=30)
        self.file_re_choose_pos_row_entry.place(x=200, y=60)
        self.file_re_choose_pos_col_entry.place(x=230, y=60)
        self.file_filter_quick_filter_entry.place(x=MID_ENTRY_POS, y=30)
        self.file_filter_quick_filter_row_entry.place(x=150, y=60)
        self.file_filter_quick_filter_col_entry.place(x=180, y=60)
        self.file_result_entry.place(x=50)

    def button_register(self):
        self.file_choose_button.place(x=BUTTON_RIGHT_MID_LONG_ENTRY, y=10)
        self.file_choose_reflash_button.place(x=BUTTON_RIGHT_MID_LONG_ENTRY+40, y=10)
        self.file_re_filter_button.place(x=BUTTON_RIGHT_MID_LONG_ENTRY, y=30)
        self.file_re_filter_clear_button.place(x=BUTTON_RIGHT_MID_LONG_ENTRY+40, y=30)
        self.file_filter_quick_filter_delete_button.place(x=BUTTON_RIGHT_MID_LONG_ENTRY, y=30)
        self.file_filter_quick_filter_get_button.place(x=BUTTON_RIGHT_MID_LONG_ENTRY+40, y=30)
        self.file_end_run_button.place(x=RUN_BUTTON)
        self.file_end_quit_button.place(x=QUIT_BUTTON)
        self.file_end_button_choose_other.place(x=TO_OTHER, y=10)
        self.file_end_button_return.place(x=RETURN_BUTTON, y=10)

    def read_file(self):
        self.file_path = filedialog.askopenfilename()
        self.file_choose_entry_string.set(self.file_path)
        self.file_choose_sheet_entry_string.set('Sheet1')

    def reset_file(self):
        self.file = pd.read_excel(self.file_path)

    def clear(self):
        self.file_re_relist_entry_string.set('')


if __name__ == '__main__':
    MainMenu()
