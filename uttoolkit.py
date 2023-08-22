# -*- coding: UTF-8 -*-
import RSlib
import tkinter as tk
import shutil
from random import randint
from  tkinter import messagebox
from  tkinter import filedialog
from tkinter import  ttk
import webbrowser
import os
import pathlib
icon = "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAADAFBMVEUBAACAAAAAgACAgAAAAICAAIAAgICAgIDAwMD/AAAA/wD//wAAAP//AP8A//////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABMJ8z+AAAAAXRSTlMAQObYZgAAADpJREFUeNq1zDsKADAMAlCz9v5ndS7GfiEd66I8SAJoAKHkCJXFI7IkYzxh5Q8AJ7GETfRJASbOpzd0CFEMYeFyJNMAAAAASUVORK5CYII="
RSlib.doadmin()
a = os.path.join(os.path.expanduser("~"), 'AppData')
window = tk.Tk()
window.title("传说之下存档管理工具")
label = tk.Label(window, text="UT-toolkit", fg="black", font=("微软雅黑", 24, "bold"))
label.pack(side="top", pady=20)
label2 = tk.Label(window, text="作者:凌琳", fg="black", font=("微软雅黑", 10))
label2.pack(side="top", pady=1)
button1 = tk.Button(window, text="导出/备份存档", width=15, font=("微软雅黑", 14), command=lambda: click_button_1_actions())
button1.pack(pady=10)
button2 = tk.Button(window, text="导入/恢复存档", width=15, font=("微软雅黑", 14), command=lambda: click_button_2_actions())
button2.pack(pady=10)
button3 = tk.Button(window, text="为坠落的人类命名", width=15, font=("微软雅黑", 14), command=lambda: click_button_4_actions())
button3.pack(pady=10)
button4 = tk.Button(window, text="真正的重置", width=15, font=("微软雅黑", 14), command=lambda: click_button_3_actions())
button4.pack(pady=10)
button5 = tk.Button(window, text="其他", width=15, font=("微软雅黑", 14), command=lambda: click_button_5_actions())
button5.pack(pady=10)
window.geometry("300x430")
icon_image = tk.PhotoImage(data=icon)
window.iconphoto(True, icon_image)
window.resizable(0, 0)
def click_button_1_actions():
    utfliepath = a + "/Local/UNDERTALE"
    try:
        RSlib.dozipfile(utfliepath)
        zipedutfliename = str(randint(1,10000))
        os.rename(a + "/Local/UNDERTALE.zip",a + "/Local/"+zipedutfliename+".utfile")
        shutil.move(a + "/Local/"+zipedutfliename+".utfile",tk.filedialog.askdirectory(title="选择一个保存位置"))
        messagebox.showinfo("提示","存档备份成功\n保存的文件名："+zipedutfliename+".utfile")
    except FileNotFoundError:
        messagebox.showwarning("提示","您似乎没有存档")
def click_button_2_actions():
    flag2 = False
    if RSlib.checktask("UNDERTALE.exe"):
        if tk.messagebox.askokcancel("提示","游戏似乎正在运行，要继续吗？"):
            flag2 = True
            uttaskpath = RSlib.gettaskpath("UNDERTALE.exe")
            RSlib.dokilltask("UNDERTALE.exe")
        else:
            return None
    tk.messagebox.showwarning("警告","此操作会覆盖你的存档")
    if os.path.exists("./cache"):
        shutil.rmtree("./cache")
    utfliepath = a + "/Local/UNDERTALE"
    os.makedirs("./cache")
    if not os.path.exists(utfliepath):
        os.makedirs(utfliepath)
    doloadedutflie = tk.filedialog.askopenfilename(title="选择你的存档文件",filetypes=[('UT存档备份', '*.utfile'), ('UT存档zip备份', '*.zip')])
    loadedutflie = os.path.splitext(doloadedutflie)
    utflie = loadedutflie[0] + ".zip"
    os.rename(doloadedutflie,utflie)
    iszipfile = RSlib.unzip_file(utflie,"./cache")
    os.rename(utflie, doloadedutflie)
    if  iszipfile :
        flag = True
    else:
        flag = False
    checkfile1 = pathlib.Path("./cache/file0")
    checkfile2 = pathlib.Path("./cache/file9")
    if checkfile1.is_file() and checkfile2.is_file() and os.path.exists("./cache/undertale.ini"):
        flag1 = True
    else:
        flag1 = False
    if  flag and flag1:
        shutil.rmtree(utfliepath)
        shutil.copytree("./cache",utfliepath)
        shutil.rmtree("./cache")
        tk.messagebox.showinfo("提示","存档已覆盖")
    else:
        tk.messagebox.showwarning("提示","不是有效的存档文件")
    if flag2 :
        os.startfile(uttaskpath)
def click_button_3_actions():
    flag = False
    utfliepath = a + "/Local/UNDERTALE"
    if RSlib.checktask("UNDERTALE.exe"):
        if tk.messagebox.askokcancel("提示","游戏似乎正在运行，要继续吗？"):
            uttaskpath = RSlib.gettaskpath("UNDERTALE.exe")
            RSlib.dokilltask("UNDERTALE.exe")
            flag = True
        else:
            return  None
    try:
        c = tk.messagebox.askokcancel("*","*你确定吗？你会抹除掉这个世界所有的痕迹")
        if c :
            c1 = tk.messagebox.askyesno("*","*你是否要抹除这个世界？")
            if c1:
                shutil.rmtree(utfliepath)
                tk.messagebox.showinfo("","*你扬了你的存档，这使你充满了决心")
                if flag :
                    os.startfile(uttaskpath)
    except FileNotFoundError:
        messagebox.showwarning("提示", "您似乎没有存档")
def click_button_4_actions():
    utfliepath = a + "/Local/UNDERTALE"
    try:
        tk.messagebox.showinfo("提示","修改非实时生效，需进入游戏再次存档即可")
        child_window = tk.Toplevel(window)
        child_window.title("请输入名称")
        child_window.resizable(0, 0)
        entry = tk.Entry(child_window)
        entry.pack(padx=20, pady=20, side=tk.LEFT)
        def replace_content():
            flag = False
            try:
                if RSlib.checktask("UNDERTALE.exe"):
                    if tk.messagebox.askokcancel("提示", "游戏似乎正在运行，要继续吗？"):
                        flag = True
                        uttaskpath = RSlib.gettaskpath("UNDERTALE.exe")
                        RSlib.dokilltask("UNDERTALE.exe")
                    else:
                        return None
                new_content = entry.get()
                with open(utfliepath+"/file0", "r") as file:
                    lines = file.readlines()
                lines[0] = new_content + '\n'
                with open(utfliepath+"/file0", "w") as file:
                    file.writelines(lines)
                with open(utfliepath + "/file9", "r") as file1:
                    lines = file1.readlines()
                lines[0] = new_content + '\n'
                with open(utfliepath + "/file9", "w") as file1:
                    file1.writelines(lines)
                checkfile = pathlib.Path(utfliepath + "/file8")
                if checkfile.is_file():
                    with open(utfliepath + "/file8", "r") as file2:
                        lines = file2.readlines()
                    lines[0] = new_content + '\n'
                    with open(utfliepath + "/file8", "w") as file2:
                        file2.writelines(lines)
                file.close()
                file1.close()
                if checkfile.is_file():
                    file2.close()
                if flag:
                    os.startfile(uttaskpath)
                child_window.destroy()
                tk.messagebox.showinfo("提示","修改成功")
            except FileNotFoundError:
                messagebox.showwarning("提示", "您似乎没有存档")
                return  None
        button = tk.Button(child_window, text="确定", command=replace_content)
        button.pack(padx=20, pady=20, side=tk.LEFT)
    except FileNotFoundError:
        messagebox.showwarning("提示", "您似乎没有存档")
def click_button_5_actions():
    utfliepath = a + "/Local/UNDERTALE"
    child_window = tk.Toplevel(window)
    child_window.title("其他")
    child_window.geometry("200x475")
    child_window.resizable(0, 0)
    def click_1_actions():
        flag = False

        if RSlib.checktask("UNDERTALE.exe"):
            if tk.messagebox.askokcancel("提示", "游戏似乎正在运行，要继续吗？"):
                flag = True
                uttaskpath = RSlib.gettaskpath("UNDERTALE.exe")
                RSlib.dokilltask("UNDERTALE.exe")
            else:
                return None
        if tk.messagebox.askyesno("*","*你是否想回到那个被你摧毁的世界？"):
            checkfile = pathlib.Path(utfliepath + "/system_information_962")
            checkfile1 = pathlib.Path(utfliepath + "/system_information_963")
            checkfile3 = pathlib.Path(utfliepath + "/file8")
            if checkfile3.is_file():
                os.remove(utfliepath + "/file8")
            if checkfile.is_file():
                os.remove(utfliepath + "/system_information_962")
                tk.messagebox.showinfo("*", "*修改完成")
            elif checkfile1.is_file():
                os.remove(utfliepath + "/system_information_963")
                tk.messagebox.showinfo("*", "*修改完成")
            else:
                tk.messagebox.showinfo("*","*你并没有出卖自己的灵魂")
        if flag:
             os.startfile(uttaskpath)
    def click_2_actions():
        utfliepath = a + "/Local/UNDERTALE"
        flag = False
        try:
            if RSlib.checktask("UNDERTALE.exe"):
                if tk.messagebox.askokcancel("提示", "游戏似乎正在运行，要继续吗？"):
                    flag = True
                    uttaskpath = RSlib.gettaskpath("UNDERTALE.exe")
                    RSlib.dokilltask("UNDERTALE.exe")
                else:
                    return None
            with open(utfliepath+"/file0", "r") as file4:
                lines = file4.readlines()
            lines[2] = "999999" + '\n'
            lines[3] = "999999" + '\n'
            lines[4] = "999999" + '\n'
            lines[5] = "999999" + '\n'
            lines[6] = "999999" + '\n'
            lines[7] = "999999" + '\n'
            lines[10] = "100000000000000" + '\n'
            lines[28] = "52" + '\n'
            lines[29] = '53' + '\n'
            with open(utfliepath+"/file0", "w") as file4:
                file4.writelines(lines)
                file4.close()
                tk.messagebox.showinfo("提示","你已登神（bushi）")
            if flag:
                os.startfile(uttaskpath)
        except FileNotFoundError:
            messagebox.showwarning("提示", "*您似乎没有存档")
    def click_3_actions():
        utfliepath = a + "/Local/UNDERTALE"
        try:
            tk.messagebox.showinfo("提示", "修改非实时生效，需进入游戏再次存档即可")
            tk.messagebox.showwarning("警告","在没有关闭dogcheck的情况下，进入0-4、239-263、及265-335会进入坏档狗的界面")
            child_window = tk.Toplevel(window)
            child_window.title("请输入room值")
            child_window.resizable(0, 0)
            entry = tk.Entry(child_window)
            entry.pack(padx=20, pady=20, side=tk.LEFT)
            def actions1():
                try:
                    flag = False
                    if RSlib.checktask("UNDERTALE.exe"):
                        if tk.messagebox.askokcancel("提示", "游戏似乎正在运行，要继续吗？"):
                            flag = True
                            uttaskpath = RSlib.gettaskpath("UNDERTALE.exe")
                            RSlib.dokilltask("UNDERTALE.exe")
                        else:
                            return None
                    _input = entry.get()
                    with open(utfliepath + "/file0", "r") as file:
                        lines = file.readlines()
                    lines[547] = _input + '\n'
                    with open(utfliepath + "/file0", "w") as file:
                        file.writelines(lines)
                    file.close()
                    if flag:
                        os.startfile(uttaskpath)
                    child_window.destroy()
                    tk.messagebox.showinfo("提示", "修改成功")
                except FileNotFoundError:
                    messagebox.showwarning("提示", "您似乎没有存档")
                    return  None
            def act2():
                webbrowser.open("https://pcy.ulyssis.be/undertale/rooms")
            button = tk.Button(child_window, text="确定", command=actions1)
            button.pack(padx=20, pady=20, side=tk.LEFT)
            button2 = tk.Button(child_window, text="房间id对照表", command=act2)
            button2.pack(padx=20, pady=20, side=tk.LEFT)
        except FileNotFoundError:
            messagebox.showwarning("提示", "您似乎没有存档")
    def click_4_actions():
        child_window2 = tk.Toplevel(child_window)
        child_window2.title("获取物品")
        child_window2.geometry("350x175")
        child_window2.resizable(0, 0)
        label.pack(side="top", pady=5)
        label2 = tk.Label(child_window2, text="请在下方输入框键入物品id", fg="black", font=("微软雅黑", 10))
        label2.pack(side="top", pady=5)
        entry = tk.Entry(child_window2,)
        entry.pack(padx=20, pady=10, side=tk.TOP)
        combobox = ttk.Combobox(child_window2)
        entry.pack(padx=20, pady=10, side=tk.TOP)
        combobox.pack()
        combobox["value"] = ("物品栏位置一（13）", "物品栏位置二（15）", "物品栏位置三（17）","物品栏位置四（19）","物品栏位置五（21）","物品栏位置六（23）","物品栏位置七（25）","物品栏位置八（27）")
        combobox.current(0)
        def actions():
            utfliepath = a + "/Local/UNDERTALE"
            flag = False
            try:
                if RSlib.checktask("UNDERTALE.exe"):
                    if tk.messagebox.askokcancel("提示", "游戏似乎正在运行，要继续吗？"):
                        flag = True
                        uttaskpath = RSlib.gettaskpath("UNDERTALE.exe")
                        RSlib.dokilltask("UNDERTALE.exe")
                    else:
                        return None
                inputstr = filter(str.isdigit, str(combobox.get()))
                inputstr2 = list(inputstr)
                finalnum =  "".join(inputstr2)
                finalnum = int(finalnum)
                with open(utfliepath + "/file0", "r") as file:
                    lines = file.readlines()
                lines[finalnum-1] = str(entry.get()) + '\n'
                with open(utfliepath + "/file0", "w") as file:
                    file.writelines(lines)
                    file.close()
                    tk.messagebox.showinfo("提示", "修改完成")
                if flag:
                    os.startfile(uttaskpath)
            except FileNotFoundError:
                messagebox.showwarning("提示", "*您似乎没有存档")
                return None
        def actions2():
            webbrowser.open("https://pcy.ulyssis.be/undertale/items")
        button = tk.Button(child_window2, text="确定", width=15,font=("微软雅黑", 10),command=actions)
        button.pack(padx=10, pady=5, side=tk.LEFT)
        button2 = tk.Button(child_window2, text="物品id对照表", width=15, font=("微软雅黑", 10),command=actions2)
        button2.pack(padx=10, pady=5, side=tk.LEFT)
        child_window2.mainloop()
    def click_5_actions():
        utfliepath = a + "/Local/UNDERTALE"
        try:
            tk.messagebox.showinfo("提示", "修改非实时生效，需进入游戏再次存档即可")
            child_window = tk.Toplevel(window)
            child_window.title("选择剧情")
            child_window.resizable(0, 0)
            combobox = ttk.Combobox(child_window)
            combobox.pack(side=tk.LEFT)
            combobox["value"] = (
            "初始(0)", "第一个存档点(2)", "下一个房间按钮开门后(3)", "扳下两个拉杆后(5)",
            "与人偶战斗后(7)", "牵手过桥后(8)", "刚被扔下后(9)",  "Napstablook战后(11)",
            "接到提醒背包电话后(12)", "六块掉落地板解密后(13)", "第一个三色开关解谜后(14)",
            "第二个三色开关解谜后(15)", "第三个三色开关解谜后(16)", "到家门口(17)", "进门与Toriel对话一次后(18)",
            "介绍房间后(19)" "Toriel去地下室后(21)", "地下室对话1次后(22)",
            "地下室对话2次后(23)", "拐角处第三次对话后(24)", "Toriel战后(25)", "sans握手后(36)",
            "雪镇第一次能存档时(37)", "再见过Papyrus后(40)", "过了Doggo后(42)", "电击迷宫剧情后(43)", "crossword后(47)",
            "按下隐藏开关后(49)", "遇到狗夫妇后(51)", "解决一个XOXO谜题后(53)", "解决两个后(56)", "彩砖迷题后(58)",
            "滑冰谜题后(63)", "GreaterDog战后(65)", "刚进雪镇(67)", "Papyrus战后(101)", "Undyne初过场动画结束后(106)",
            "Papyrus问过装备后(107)", "发现隐藏门后(108)", "Undyne初次追逐战后(110)", "Shyren战后(111)",
            "第二次追逐战前的存档点(113)", "追逐战后的垃圾堆存档点(115)", "MadDummy战后(116)",
            "再与Napstablook对话一次之后的存档点(117)", "behind_you后(118)", "mkid掉落剧情后(120)",
            "Undyne战前给出存档点后(121)", "Undyne战后(122)", "实验室开灯后(126)", "实验室全剧情后(127)",
            "接到马上挂的电话后(130)", "Alphys讲解蓝橙激光后(131)", "Alphys推荐三岔口解谜顺序后(132)",
            "烹饪节目结束后(135)", "Alphys打电话介绍Core后(137)", "Alphys打电话说明传送带三开关后(139)",
            "三开关谜题后(140)", "Alphys介绍七跳板谜题后(143)", "RG战后(146)", "拆弹剧情后(161)",
            "第二层最后的电话后(162)", "Alphys跳板阵前电话后(163)", "Muffet战之前(164)", "MTT音乐剧之前(165)",
            "Hotel存档点(168)", "看到Core入口敌人剪影后(176)", "接到Alphys建议走右边电话后(177)", "遇到Mj后(179)",
            "Alphys电话告知橙橙蓝顺序后(180)", "Alphys电话里道歉后(181)", "MTTex战之前(185)", "到新家后(199)",
            "审判厅剧情结束后(201)", "第一次见过Asgore后(206)", "Throne_Room外对话一次后(207)",
            "The_End存档点旁对话后(208)", "结束(999)")
            combobox.current(0)
            def actions1():
                try:
                    flag = False
                    if RSlib.checktask("UNDERTALE.exe"):
                        if tk.messagebox.askokcancel("提示", "游戏似乎正在运行，要继续吗？"):
                            flag = True
                            uttaskpath = RSlib.gettaskpath("UNDERTALE.exe")
                            RSlib.dokilltask("UNDERTALE.exe")
                        else:
                            return None
                    inputstr = filter(str.isdigit, str(combobox.get()))
                    inputstr2 = list(inputstr)
                    finalnum = "".join(inputstr2)
                    finalnum = str(finalnum)
                    print(finalnum)
                    with open(utfliepath + "/file0", "r") as file:
                        lines = file.readlines()
                    lines[542] = finalnum + '\n'
                    with open(utfliepath + "/file0", "w") as file:
                        file.writelines(lines)
                    file.close()
                    if flag:
                        os.startfile(uttaskpath)
                    child_window.destroy()
                    tk.messagebox.showinfo("提示", "修改成功")
                except FileNotFoundError:
                    messagebox.showwarning("提示", "*您似乎没有存档")
                    return  None
        except FileNotFoundError:
            messagebox.showwarning("提示", "*您似乎没有存档")
        button = tk.Button(child_window, text="确定", command=actions1)
        button.pack(padx=20, pady=20, side=tk.LEFT)
    def click_6_actions():
        utfliepath = a + "/Local/UNDERTALE"
        try:
            tk.messagebox.showinfo("提示", "修改非实时生效，需进入游戏再次存档即可")
            child_window = tk.Toplevel(window)
            child_window.title("请输入fun")
            child_window.resizable(0, 0)
            entry = tk.Entry(child_window)
            entry.pack(padx=20, pady=20, side=tk.LEFT)
            def actions():
                try:
                    flag = False
                    if RSlib.checktask("UNDERTALE.exe"):
                        if tk.messagebox.askokcancel("提示", "游戏似乎正在运行，要继续吗？"):
                            flag = True
                            uttaskpath = RSlib.gettaskpath("UNDERTALE.exe")
                            RSlib.dokilltask("UNDERTALE.exe")
                        else:
                            return None
                    _input = entry.get()
                    try:
                        input_num = int(_input)
                    except ValueError:
                        tk.messagebox.showwarning("","数值非法")
                        return None
                    if 0<= input_num <= 100:
                        text = f'fun="{_input}"'
                        with open(utfliepath+"/undertale.ini", "r", errors='ignore') as file:
                            lines = file.readlines()
                        rewirteline = [index for index, line in enumerate(lines) if "fun" in line]
                        for index in rewirteline:
                            lines[index] = text + "\n"
                        # 将修改后的内容写回文件
                        with open(utfliepath+"/undertale.ini", "w", errors='ignore') as file:
                            file.writelines(lines)
                        file.close()
                    else:
                        tk.messagebox.showwarning("", "数值非法")
                        return None
                    if flag:
                        os.startfile(uttaskpath)
                    child_window.destroy()
                    tk.messagebox.showinfo("提示", "修改成功")
                except FileNotFoundError:
                    messagebox.showwarning("提示", "*您似乎没有存档")
                    return  None
            button = tk.Button(child_window, text="确定", command=actions)
            button.pack(padx=20, pady=20, side=tk.LEFT)
        except FileNotFoundError:
            messagebox.showwarning("提示", "您似乎没有存档")
    def click_7_actions():
        os.system("notepad" + " " + utfliepath + "/undertale.ini")
    _button1 = tk.Button(child_window, text="再无交易",width=15, command=lambda:click_1_actions(),font=("微软雅黑", 15))
    _button1.pack(pady=10)
    _button2 = tk.Button(child_window, text="吸收6魂",width=15, command=lambda:click_2_actions(),font=("微软雅黑", 15))
    _button2.pack(pady=10)
    _button3 = tk.Button(child_window, text="远程折跃", width=15,command=lambda:click_3_actions(),font=("微软雅黑", 15))
    _button3.pack(pady=10)
    _button4 = tk.Button(child_window, text="获取物品",width=15, command=lambda:click_4_actions(),font=("微软雅黑", 15))
    _button4.pack(pady=10)
    _button5 = tk.Button(child_window, text="时间折跃",width=15, command=lambda:click_5_actions(),font=("微软雅黑", 15))
    _button5.pack(pady=10)
    _button6 = tk.Button(child_window, text="世界折跃",width=15, command=lambda:click_6_actions(),font=("微软雅黑", 15))
    _button6.pack(pady=10)
    _button7 = tk.Button(child_window, text="编辑存档信息文件",width=15, command=lambda:click_7_actions(),font=("微软雅黑", 15))
    _button7.pack(pady=10)
window.mainloop()