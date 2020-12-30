import selenium
import ast
import win32clipboard as wc
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import re
import time
import tkinter as tk

def copy_to_clipboard():
    wc.OpenClipboard()
    wc.EmptyClipboard()
    wc.SetClipboardData(wc.CF_UNICODETEXT, download_url_entry.get())
    wc.CloseClipboard()

def init_get(settings):
    wait_time = settings['wait_time']
    tag_name = settings['tag_name']
    iframes = settings['iframes']
    tag_index = settings['tag_index']
    phone_id = custom_phone_entry.get()
    pwd_input = custom_pwd_entry.get()
    url = url_get_entry.get()
    patten = custom_patten_entry.get()

    browser = webdriver.Chrome()
    browser.get(url)
    phone = browser.find_element_by_id('phone')
    phone.send_keys(phone_id)
    pwd = browser.find_element_by_id('pwd')
    pwd.send_keys(pwd_input)
    pwd.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, wait_time)
    time.sleep(wait_time)

    frame = browser.find_elements_by_tag_name('iframe')[0]
    browser.switch_to.frame(frame)
    i = 0
    while iframes - 1:
        frame = browser.find_elements_by_tag_name('iframe')[tag_index[i]]
        browser.switch_to.frame(frame)
    objectid = re.findall(patten, browser.page_source)

    download_url_str.set('d0.ananas.chaoxing.com/download/' + objectid[tag_index[i]])

def run():
    init_get(ast.literal_eval(custom_pro_entry.get()))

def quit():
    root.destroy()

root = tk.Tk()
root.title('学习通菜鸟下载pdf工具1.0.0')
root.minsize(width=825, height=540)
root.maxsize(width=825, height=540)
title_frame = tk.Frame(root)
url_get_frame = tk.Frame(root)
custom_info = tk.Frame(root)
custom_patten_frame = tk.Frame(root)
download_url_frame = tk.Frame(root)
custom_pro_frame = tk.Frame(root)
button_frame = tk.Frame(root)
title_frame.pack(pady=20)
url_get_frame.pack(pady=20)
custom_info.pack(pady=20)
custom_patten_frame.pack(pady=20)
custom_pro_frame.pack(pady=20)
download_url_frame.pack(pady=20)
button_frame.pack(pady=20)

title_label = tk.Label(title_frame, text='学习通下载pdf简易工具', font=('黑体', 20, 'bold'))
title_label.pack()

url_get_label = tk.Label(url_get_frame, text='请输入页面url：')
url_get_label.grid(row=0, column=0)
url_str = tk.StringVar()
url_get_entry = tk.Entry(url_get_frame, textvariable=url_str, width=80)
url_get_entry.grid(row=0, column=1)

custom_phone_label = tk.Label(custom_info, text='账号：')
custom_phone_label.grid(row=0, column=0)
custom_phone_entry = tk.Entry(custom_info, width=40)
custom_phone_entry.grid(row=0, column=1)
custom_pwd_label = tk.Label(custom_info, text=' 密码：')
custom_pwd_label.grid(row=0, column=2)
custom_pwd_entry = tk.Entry(custom_info, width=40, show='*')
custom_pwd_entry.grid(row=0, column=3)


custom_patten_label = tk.Label(custom_patten_frame, text='用户自定义筛选条件（默认无需调整）：')
custom_patten_label.grid(row=0, column=0)
custom_patten_str = tk.StringVar()
custom_patten_str.set('objectid=\"([\\S]*)\"')
custom_patten_entry = tk.Entry(custom_patten_frame, textvariable=custom_patten_str, width=62)
custom_patten_entry.grid(row=0, column=1)

download_url_label = tk.Label(download_url_frame, text='下载链接：')
download_url_label.grid(row=0, column=0)
download_url_str = tk.StringVar()
download_url_entry = tk.Entry(download_url_frame, textvariable=download_url_str, state=tk.DISABLED, width=80)
download_url_entry.grid(row=0, column=1)
download_url_btn = tk.Button(download_url_frame, text='复制', command=copy_to_clipboard)
download_url_btn.grid(row=0, column=2)

custom_pro_label = tk.Label(custom_pro_frame, text='高级用户自定义：')
custom_pro_label.grid(row=0, column=0)
custom_pro_str = tk.StringVar()
custom_pro_str.set("{'iframes': 1, 'wait_time': 10, 'tag_name': 'iframe', 'tag_index': [0]}")
custom_pro_entry = tk.Entry(custom_pro_frame, width=75, textvariable=custom_pro_str)
custom_pro_entry.grid(row=0, column=1)

button_run = tk.Button(button_frame, text='运行', font=('黑体', 20, 'bold'), command=run)
button_run.grid(row=0, column=0)
button_quit = tk.Button(button_frame, text='退出', font=('黑体', 20, 'bold'), command=quit)
button_quit.grid(row=0, column=1)
tk.mainloop()


