import pyautogui as gui
import time
import re


if __name__ == '__main__':
    html_gui = gui.getWindowsWithTitle('阳间插件-巧克力与香子兰')
    html_gui = re.sub('\D', "", str(html_gui))
    html_gui = int(html_gui[2:])

    gui.Window(html_gui).activate()
    # 改变电压值为1786 485
    # run is on 1589 186
    # shut down is on 1661 185
    # time.sleep(4)
    # print(gui.position())

    value_list = [0.5, 1, 2, 3, 4, 5, 6, 7, 8]

    for i, value in enumerate(value_list):
        gui.moveTo(x=1786, y=609)   # 点击需要改变的单元框位置
        gui.click()
        for _ in range(10):
            gui.press('backspace')
            time.sleep(0.1)
        gui.typewrite(str(value_list[i]))
        gui.moveTo(x=1786, y=709)  # 单击其他一处确定
        gui.click()
        gui.moveTo(1589, 238)  # 运行
        gui.click()
        time.sleep(8)
        im1 = gui.screenshot(r'D:\python脚本\shiyanjiaoben\temp\{}.jpg'.format(i))
        gui.moveTo(1661, 234)   # 停止
        gui.click()