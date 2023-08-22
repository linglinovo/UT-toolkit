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
    if os.path.exists(utfliepath):
        RSlib.dozipfile(utfliepath)
        zipedutfliename = str(randint(1,10000))
        os.rename(a + "/Local/UNDERTALE.zip",a + "/Local/"+zipedutfliename+".utfile")
        shutil.move(a + "/Local/"+zipedutfliename+".utfile",tk.filedialog.askdirectory(title="选择一个保存位置"))
        messagebox.showinfo("提示","存档备份成功\n保存的文件名："+zipedutfliename+".utfile")
    else:
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
    c = tk.messagebox.askokcancel("*","*你确定吗？你会抹除掉这个世界所有的痕迹")
    if c :
        c1 = tk.messagebox.askyesno("*","*你是否要抹除这个世界？")
        if c1:
            shutil.rmtree(utfliepath)
            tk.messagebox.showinfo("","*你扬了你的存档，这使你充满了决心")
            if flag :
                os.startfile(uttaskpath)
def click_button_4_actions():
    utfliepath = a + "/Local/UNDERTALE"
    if os.path.exists(utfliepath):
        tk.messagebox.showinfo("提示","修改非实时生效，需进入游戏再次存档即可")
        child_window = tk.Toplevel(window)
        child_window.title("请输入名称")
        child_window.resizable(0, 0)
        entry = tk.Entry(child_window)
        entry.pack(padx=20, pady=20, side=tk.LEFT)
        def replace_content():
            flag = False
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
        button = tk.Button(child_window, text="确定", command=replace_content)
        button.pack(padx=20, pady=20, side=tk.LEFT)
    else:
        messagebox.showwarning("提示", "您似乎没有存档")
def click_button_5_actions():
    utfliepath = a + "/Local/UNDERTALE"
    child_window = tk.Toplevel(window)
    child_window.title("其他")
    child_window.geometry("200x350")
    child_window.resizable(0, 0)
    def click_1_actions():
        flag = False
        if os.path.exists(utfliepath):
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
        else:
            messagebox.showwarning("提示", "*您似乎没有存档")
    def click_2_actions():
        utfliepath = a + "/Local/UNDERTALE"
        flag = False
        if os.path.exists(utfliepath):
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
        else:
            messagebox.showwarning("提示", "*您似乎没有存档")
    def click_3_actions():
        utfliepath = a + "/Local/UNDERTALE"
        if os.path.exists(utfliepath):
            tk.messagebox.showinfo("提示", "修改非实时生效，需进入游戏再次存档即可")
            tk.messagebox.showwarning("警告","在没有关闭dogcheck的情况下，进入0-4、239-263、及265-335会进入坏档狗的界面")
            child_window = tk.Toplevel(window)
            child_window.title("请输入room值")
            child_window.resizable(0, 0)
            entry = tk.Entry(child_window)
            entry.pack(padx=20, pady=20, side=tk.LEFT)

            def actions1():
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
            def act2():
                webbrowser.open("https://pcy.ulyssis.be/undertale/rooms")
            button = tk.Button(child_window, text="确定", command=actions1)
            button.pack(padx=20, pady=20, side=tk.LEFT)
            button2 = tk.Button(child_window, text="房间id对照表", command=act2)
            button2.pack(padx=20, pady=20, side=tk.LEFT)
        else:
            messagebox.showwarning("提示", "您似乎没有存档")
    def click_4_actions():
        child_window2 = tk.Toplevel(child_window)
        child_window2.title("获取物品")
        child_window2.geometry("350x200")
        child_window2.resizable(0, 0)
        label = tk.Label(child_window2, text="获取物品", fg="black", font=("微软雅黑", 20, "bold"))
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
            if os.path.exists(utfliepath):
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
                print(finalnum-1)
                print(entry.get())
                with open(utfliepath + "/file0", "r") as file:
                    lines = file.readlines()
                lines[finalnum-1] = str(entry.get()) + '\n'
                with open(utfliepath + "/file0", "w") as file:
                    file.writelines(lines)
                    file.close()
                    tk.messagebox.showinfo("提示", "修改完成")
                if flag:
                    os.startfile(uttaskpath)
            else:
                messagebox.showwarning("提示", "*您似乎没有存档")
        def actions2():
            webbrowser.open("https://pcy.ulyssis.be/undertale/items")
        button = tk.Button(child_window2, text="确定", width=15,font=("微软雅黑", 10),command=actions)
        button.pack(padx=10, pady=5, side=tk.LEFT)
        button2 = tk.Button(child_window2, text="物品id对照表", width=15, font=("微软雅黑", 10),command=actions2)
        button2.pack(padx=10, pady=5, side=tk.LEFT)
        child_window2.mainloop()
    def click_5_actions():
        if os.path.exists(utfliepath):
            os.system("notepad" + " " + utfliepath + "/undertale.ini")
        else:
            messagebox.showwarning("提示", "您似乎没有存档")
    _button1 = tk.Button(child_window, text="再无交易",width=15, command=lambda:click_1_actions(),font=("微软雅黑", 15))
    _button1.pack(pady=10)
    _button2 = tk.Button(child_window, text="吸收6魂",width=15, command=lambda:click_2_actions(),font=("微软雅黑", 15))
    _button2.pack(pady=10)
    _button3 = tk.Button(child_window, text="远程折跃", width=15,command=lambda:click_3_actions(),font=("微软雅黑", 15))
    _button3.pack(pady=10)
    _button4 = tk.Button(child_window, text="获取物品",width=15, command=lambda:click_4_actions(),font=("微软雅黑", 15))
    _button4.pack(pady=10)
    _button5 = tk.Button(child_window, text="编辑存档信息文件",width=15, command=lambda:click_5_actions(),font=("微软雅黑", 15))
    _button5.pack(pady=10)
window.mainloop()