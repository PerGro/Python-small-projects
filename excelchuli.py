import pandas as pd
import tkinter as tk
from tkinter import filedialog
import os
from tkinter.scrolledtext import ScrolledText


class Frame:
    def __init__(self):
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
        pass

    def var_init(self):
        pass

    def txt_create(self):
        pass

    def txt_register(self):
        pass

    def label_create(self):
        pass

    def item_create(self):
        pass

    def item_register(self):
        pass

    def button_create(self):
        pass

    def label_register(self):
        pass

    def button_register(self):
        pass

    def loop(self):
        self.root.mainloop()


class MainMenu(Frame):
    def __init__(self):
        super(MainMenu, self).__init__()

    def frame_init(self):
        self.root.title('Excel快速处理器')
        self.root.geometry('825x720')
        self.root.minsize(width=825, height=720)
        self.root.maxsize(width=825, height=720)

    def button_create(self):
        self.button1 = tk.Button(self.root, text='查找模式', width=25, height=5, command=self.to_find)
        self.button2 = tk.Button(self.root, text='批处理模式', width=25, height=5)

    def button_register(self):
        self.button1.place(x=65, y=310)
        self.button2.place(x=590, y=310)

    def loop(self):
        self.root.mainloop()

    def to_find(self):
        self.root.destroy()
        FindFunction()


class FindFunction(Frame):
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
        self.frame_file_choose_orgin_entry_string = tk.StringVar()
        self.frame_file_choose_orgin_config_sheet_entry_string = tk.StringVar()
        self.frame_file_choose_compare_entry_string = tk.StringVar()
        self.frame_file_compare_config_entry1_int = tk.StringVar()
        self.frame_file_compare_config_entry2_int = tk.StringVar()
        self.frame_file_compare_config_entry3_int = tk.StringVar()
        self.frame_file_orgin_config_entry_int = tk.StringVar()
        self.frame_file_orgin_config_entry2_int = tk.StringVar()

        self.frame_file_choose_orgin_entry_string.set('')
        self.frame_file_choose_compare_entry_string.set('')

    def txt_create(self):
        self.frame_file_choose_orgin_entry = tk.Entry(self.frame_file, textvariable=self.frame_file_choose_orgin_entry_string, width=80)
        self.frame_file_choose_compare_entry = tk.Entry(self.frame_file, textvariable=self.frame_file_choose_compare_entry_string, width=80)
        self.frame_file_choose_orgin_config_sheet_entry = tk.Entry(self.frame_file, width=10, textvariable=self.frame_file_choose_orgin_config_sheet_entry_string)
        self.frame_file_orgin_config_entry = tk.Entry(self.frame_file, width=3, textvariable=self.frame_file_orgin_config_entry_int)
        self.frame_file_orgin_config_entry2 = tk.Entry(self.frame_file, width=3, textvariable=self.frame_file_orgin_config_entry2_int)
        self.frame_file_compare_config_entry1 = tk.Entry(self.frame_file, width=3, textvariable=self.frame_file_compare_config_entry1_int)
        self.frame_file_compare_config_entry2 = tk.Entry(self.frame_file, width=3, textvariable=self.frame_file_compare_config_entry2_int)
        self.frame_file_compare_config_entry3 = tk.Entry(self.frame_file, width=3, textvariable=self.frame_file_compare_config_entry3_int)
        self.frame_result_text = ScrolledText(self.frame_result, height=28, width=100, undo=True)


    def txt_register(self):
        self.frame_file_choose_orgin_entry.place(x=100, y=5)
        self.frame_file_choose_compare_entry.place(x=100, y=100)
        self.frame_file_choose_orgin_config_sheet_entry.place(x=120, y=50)
        self.frame_file_orgin_config_entry.place(x=650, y=50)
        self.frame_file_orgin_config_entry2.place(x=675, y=50)
        self.frame_file_compare_config_entry1.place(x=620, y=150)   # name
        self.frame_file_compare_config_entry2.place(x=645, y=150)   # id
        self.frame_file_compare_config_entry3.place(x=670, y=150)   # phone number
        self.frame_result_text.place(x=50, y=10)

    def label_create(self):
        self.frame_head_title = tk.Label(self.frame_head, text='快速查找器', font=('黑体', 20, 'bold'))
        self.frame_file_choose_orgin = tk.Label(self.frame_file, text='选择目标文件')  # 要对比的文件
        self.frame_file_choose_orgin_config_sheet = tk.Label(self.frame_file, text='请输入工作薄名称')
        self.frame_file_choose_compare = tk.Label(self.frame_file, text='选择花名册')   # 花名册
        self.frame_file_orgin_config = tk.Label(self.frame_file, text='姓名读取行与列')
        self.frame_file_compare_config = tk.Label(self.frame_file, text='姓名、id、电话号码读取列')

    def button_create(self):
        self.frame_file_brower1 = tk.Button(self.frame_file, text='浏览', height=1, command=self.cat_excel1)
        self.frame_file_brower2 = tk.Button(self.frame_file, text='浏览', height=1, command=self.cat_excel2)
        self.frame_end_button1 = tk.Button(self.frame_end, text='查询', font=('黑体', 20, 'bold'), command=self.run)
        self.frame_end_button2 = tk.Button(self.frame_end, text='退出', font=('黑体', 20, 'bold'), command=self.quit)
        self.frame_end_button_return = tk.Button(self.frame_end, text='返回主页面', font=('黑体', 10, 'bold'), command=self.return_to_menu)
        self.frame_end_button_choose_other = tk.Button(self.frame_end, text='进入其他功能区', font=('黑体', 10, 'bold'), command=self.to_other)

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

    def loop(self):
        self.root.mainloop()

    def quit(self):
        self.root.destroy()

    def cat_excel1(self):
        self.file_orgin = filedialog.askopenfilename()
        self.frame_file_choose_orgin_entry_string.set(self.file_orgin)
        self.frame_file_choose_orgin_config_sheet_entry_string.set('Sheet1')

    def cat_excel2(self):
        self.file_compare = filedialog.askopenfilename()
        self.frame_file_choose_compare_entry_string.set(self.file_compare)
        file = pd.read_excel(self.file_compare, header=None)
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
                if index == '姓名':
                    self.frame_file_compare_config_entry1_int.set(str(count))
                elif index == '学号':
                    self.frame_file_compare_config_entry2_int.set(str(count))
                elif index == '电话':
                    self.frame_file_compare_config_entry3_int.set(str(count))
                count += 1

    def run(self):
        self.frame_result_text.delete('1.0', tk.END)
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

    def return_to_menu(self):
        self.root.destroy()
        MainMenu()

    def to_other(self):
        self.root.destroy()
        s = SmallWindow()



class FindGuiSun:
    def __init__(self, textbox, file, name_col, id_col, phone_col, find_row=None, find_col=None, file_name=None, sheet_name='0', **kwargs):  # file_name为目标文件的路径
        self.textbox = textbox
        self.file = pd.read_excel(file)
        length = self.getlength(self.file, name_col)
        name_list = self.file.iloc[:length, name_col]  # 这里要改
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
        self.compared()

    def getlength(self, file, col):
        openfile = file
        namecol = col
        length = 0
        try:
            while True:
                openfile.iloc[length, namecol]
                length += 1
        except IndexError:
            return length


    def __print_info(self, info=None, excel_info=None, name=False, ids=False, phone_number=False):
        self.textbox.frame_result_text.insert(tk.END, "查找excel：" + excel_info[0], '查找列位置：' + str(excel_info[1]), '查找行位置：' + str(excel_info[2]) + '\n')
        self.textbox.frame_result_text.insert(tk.END, '一共查找 ' + str(self.length) + '\n')
        self.textbox.frame_result_text.insert(tk.END, '还有这些龟孙没有交：' + '\n')
        self.textbox.frame_result_text.insert(tk.END, '————————————————————————————' + '\n')
        for i in range(len(info)):
            if name:
                self.textbox.frame_result_text.insert(tk.END, '姓名: ' + str(info[i][0]) + '\n')
            if ids:
                self.textbox.frame_result_text.insert(tk.END, '学号: ' + str(info[i][1]) + '\n')
            if phone_number:
                self.textbox.frame_result_text.insert(tk.END, '电话: ' + str(info[i][2]) + '\n')
            self.textbox.frame_result_text.insert(tk.END, '————————————————————————————' + '\n')
        self.textbox.frame_result_text.insert(tk.END, '共{}个龟孙没交'.format(len(info)) + '\n')

    def compared(self):
        find_file = pd.read_excel(r'{}'.format(self.file_name), sheet_name=self.sheet_name, header=None)
        names = []
        if self.find_col:
            names = find_file.iloc[:self.find_nums, self.find_col - 1]
        if self.find_row:
            names = find_file.iloc[self.find_row - 1:, self.find_col - 1]
        if self.find_col is None and self.find_row is None:
            return 0
        names = list(names)
        temp = list(self.name)
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
        button2 = tk.Button(self.root, text='批处理器', command=self.return_back2)

        button1.pack(fill=tk.X)
        button2.pack(fill=tk.X)

    def return_back1(self):
        self.root.destroy()
        FindFunction()

    def return_back2(self):
        self.root.destroy()
        PiChuLi()


if __name__ == '__main__':
    MainMenu()