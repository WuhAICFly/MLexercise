# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 按两次 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


import time
import random
import pyautogui
while 1:
    # 125秒钟移动一次鼠标(移动鼠标时间与位置，可以根据自己需要设定)，微颤一下然后回到原位置
    time.sleep(1)
    x, y = pyautogui.position()
    pyautogui.moveTo(x=3600,y=random.randint(1500,1600))
    pyautogui.moveRel(1,0,duration=2)
    pyautogui.moveTo(x,y,duration=2)
    pyautogui.moveRel()  #函数相对于当前的位置移动鼠标
#for i in range(10):
#   pyautogui.moveRel(100, 0, duration=0.25)
#   pyautogui.moveRel(0, 100, duration=0.25)
#   pyautogui.moveRel(-100, 0, duration=0.25)
#   pyautogui.moveRel(0, -100, duration=0.25)

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
