# -*- coding: UTF-8 -*-
#导入库
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
# 图标数据，这里使用base64编码的图标数据
icon = "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAADAFBMVEUBAACAAAAAgACAgAAAAICAAIAAgICAgIDAwMD/AAAA/wD//wAAAP//AP8A//////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABMJ8z+AAAAAXRSTlMAQObYZgAAADpJREFUeNq1zDsKADAMAlCz9v5ndS7GfiEd66I8SAJoAKHkCJXFI7IkYzxh5Q8AJ7GETfRJASbOpzd0CFEMYeFyJNMAAAAASUVORK5CYII="
RSlib.doadmin()# 获取管理员
a = os.path.join(os.path.expanduser("~"), 'AppData')# 获取用户的AppData文件夹路径
##################################窗口属性和按钮相关
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
button3 = tk.Button(window, text="重命名角色", width=15, font=("微软雅黑", 14), command=lambda: click_button_4_actions())
button3.pack(pady=10)
button4 = tk.Button(window, text="删除存档", width=15, font=("微软雅黑", 14), command=lambda: click_button_3_actions())
button4.pack(pady=10)
button5 = tk.Button(window, text="其他", width=15, font=("微软雅黑", 14), command=lambda: click_button_5_actions())
button5.pack(pady=10)
window.geometry("300x430")
icon_image = tk.PhotoImage(data=icon)
window.iconphoto(True, icon_image)
window.resizable(0, 0)
###################################窗口属性和按钮相关
def click_button_1_actions():
    utfliepath = a + "/Local/UNDERTALE"# 游戏存档位置
    try:
        RSlib.dozipfile(utfliepath)# 压缩存档文件夹
        zipedutfliename = str(randint(1,10000))# 生成随机存档名
        os.rename(a + "/Local/UNDERTALE.zip",a + "/Local/"+zipedutfliename+".utfile")
        shutil.move(a + "/Local/"+zipedutfliename+".utfile",tk.filedialog.askdirectory(title="选择一个保存位置"))# 获取保存位置
        messagebox.showinfo("提示","存档备份成功\n保存的文件名："+zipedutfliename+".utfile")
    except FileNotFoundError:
        messagebox.showwarning("提示","您似乎没有存档")
def click_button_2_actions():
    flag2 = False
    if RSlib.checktask("UNDERTALE.exe"): # 判断游戏是否在运行
        if tk.messagebox.askokcancel("提示","游戏似乎正在运行，要继续吗？"):
            flag2 = True
            uttaskpath = RSlib.gettaskpath("UNDERTALE.exe")# 获取进程路径
            RSlib.dokilltask("UNDERTALE.exe")# 杀死进程
        else:
            return None
    tk.messagebox.showwarning("警告","此操作会覆盖你的存档")
    if os.path.exists("./cache"):
        shutil.rmtree("./cache")
    utfliepath = a + "/Local/UNDERTALE"# 游戏存档位置
    os.makedirs("./cache") # 创建缓存文件夹
    if not os.path.exists(utfliepath):# 如果没有游戏存档文件夹，创建
        os.makedirs(utfliepath)
    # 获取存档备份位置
    doloadedutflie = tk.filedialog.askopenfilename(title="选择你的存档文件",filetypes=[('UT存档备份', '*.utfile'), ('UT存档zip备份', '*.zip')])
    ################判断是否为存档备份文件
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
    ##################判断是否为存档备份文件
    if  flag and flag1:#如果是
        #覆盖存档
        shutil.rmtree(utfliepath)
        shutil.copytree("./cache",utfliepath)
        shutil.rmtree("./cache")
        tk.messagebox.showinfo("提示","存档已覆盖")
    else:
        tk.messagebox.showwarning("提示","不是有效的存档文件")
    if flag2 :
        os.startfile(uttaskpath)# 如果关闭了游戏进程重新则开启游戏进程
def click_button_3_actions():
    flag = False
    utfliepath = a + "/Local/UNDERTALE"# 游戏存档位置
    if RSlib.checktask("UNDERTALE.exe"):# 判断游戏是否在运行
        if tk.messagebox.askokcancel("提示","游戏似乎正在运行，要继续吗？"):
            uttaskpath = RSlib.gettaskpath("UNDERTALE.exe")# 获取进程路径
            RSlib.dokilltask("UNDERTALE.exe")# 杀死进程
            flag = True
        else:
            return  None
    try:
        if tk.messagebox.askyesno("询问","是否要删除存档？"):
            shutil.rmtree(utfliepath)# 删除存档文件夹
            tk.messagebox.showinfo("","*你扬了你的存档，这使你充满了决心")
            if flag :
                os.startfile(uttaskpath)# 如果关闭了游戏进程重新则开启游戏进程
    except FileNotFoundError:
        messagebox.showwarning("提示", "你似乎没有存档")
def click_button_4_actions():
    utfliepath = a + "/Local/UNDERTALE"
    try:
        tk.messagebox.showinfo("提示","修改非实时生效，需进入游戏再次存档即可")
        #################################子窗口
        child_window = tk.Toplevel(window)
        child_window.title("请输入名称")
        child_window.resizable(0, 0)
        #################################子窗口
        entry = tk.Entry(child_window)# 输入框
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
                    file.writelines(lines)# 覆盖 “file0”第一行
                with open(utfliepath + "/file9", "r") as file1:
                    lines = file1.readlines()
                lines[0] = new_content + '\n'
                with open(utfliepath + "/file9", "w") as file1:
                    file1.writelines(lines)# 覆盖 “file9”第一行
                checkfile = pathlib.Path(utfliepath + "/file8")
                if checkfile.is_file():#如果有file8
                    with open(utfliepath + "/file8", "r") as file2:
                        lines = file2.readlines()
                    lines[0] = new_content + '\n'
                    with open(utfliepath + "/file8", "w") as file2:
                        file2.writelines(lines)# 覆盖 “file8”第一行
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
        messagebox.showwarning("提示", "你似乎没有存档")
def click_button_5_actions():
    # 创建子窗口
    utfliepath = a + "/Local/UNDERTALE"
    child_window = tk.Toplevel(window)
    child_window.title("其他")
    child_window.geometry("200x550")
    child_window.resizable(0, 0)
    def click_0_actions():
        utfliepath = a + "/Local/UNDERTALE"
        tk.messagebox.showinfo("提示","此功能会伪造你已完成屠杀线\n换句话说，会使真和平线变成伪善线")
        ########################################子窗口
        child_window3 = tk.Toplevel(child_window)
        child_window3.title("选择进度")
        child_window3.resizable(0, 0)
        ########################################子窗口
        combobox = ttk.Combobox(child_window3)
        combobox.pack(side=tk.LEFT)
        combobox["value"] = ("进入交易（即进入游戏与chara进行交易）","交易完成（即已同意出卖灵魂）")
        combobox.current(0)#选择框
        def actions():
            flag = False
            if RSlib.checktask("UNDERTALE.exe"):
                if tk.messagebox.askokcancel("提示", "游戏似乎正在运行，要继续吗？"):
                    flag = True
                    uttaskpath = RSlib.gettaskpath("UNDERTALE.exe")
                    RSlib.dokilltask("UNDERTALE.exe")
                else:
                    return None
            if combobox.get() == "进入交易（即进入游戏与chara进行交易）":
                if tk.messagebox.askyesno("警告","此操作会抹掉你的存档"):
                    if not os.path.exists(utfliepath):
                        os.makedirs(utfliepath)# 没存档路径创一个
                    else:
                        shutil.rmtree(utfliepath)
                        os.makedirs(utfliepath)# 有存档路径删了再创一个
                    file = open(utfliepath + "/system_information_962.tmp", 'w')# 创建文件
                    file.write("a")# 写入
                    file.close()
                    os.rename(utfliepath + "/system_information_962.tmp",utfliepath + "/system_information_962")# 重命名
                    tk.messagebox.showinfo("", "修改完成")
            else:
                if not os.path.exists(utfliepath):
                    os.makedirs(utfliepath)
                file = open(utfliepath + "/system_information_963.tmp", 'w')# 创建文件
                file.write("b")# 写入
                file.close()
                os.rename(utfliepath + "/system_information_963.tmp", utfliepath + "/system_information_963")# 重命名
                tk.messagebox.showinfo("", "修改完成")
            if flag:
                os.startfile(uttaskpath)
        button = tk.Button(child_window3, text="确定", command=actions)#一个按钮
        button.pack(padx=20, pady=20, side=tk.LEFT)
        child_window3.mainloop()
    def click_1_actions():
        flag = False
        tk.messagebox.showinfo("提示", "此功能会伪造你从未完成屠杀线\n换句话说，会使伪善线变成真和平")
        if RSlib.checktask("UNDERTALE.exe"):
            if tk.messagebox.askokcancel("提示", "游戏似乎正在运行，要继续吗？"):
                flag = True
                uttaskpath = RSlib.gettaskpath("UNDERTALE.exe")
                RSlib.dokilltask("UNDERTALE.exe")
            else:
                return None
        checkfile = pathlib.Path(utfliepath + "/system_information_962")
        checkfile1 = pathlib.Path(utfliepath + "/system_information_963")
        checkfile3 = pathlib.Path(utfliepath + "/file8")
        if checkfile3.is_file():#如果有file8
            os.remove(utfliepath + "/file8")#删file8
        if checkfile.is_file():#如果有system_information_962
            os.remove(utfliepath + "/system_information_962")
            tk.messagebox.showinfo("提示", "修改完成")#删system_information_962
        elif checkfile1.is_file():#如果有system_information_963
            os.remove(utfliepath + "/system_information_963")#删system_information_962
            tk.messagebox.showinfo("提示", "修改完成")
        else:#如果没有
            tk.messagebox.showinfo("提示","你没有完成屠杀线")
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
            tk.messagebox.showwarning("警告","游戏会在战斗时对数据进行修正\n也就是说，在不修改LOVE时不会修改血量\n但是请你放心，修改LOVE是临时的，不会使中立线变屠杀")
            if tk.messagebox.askyesno("询问","是否修改LOVE?"):
                with open(utfliepath + "/file0", "r") as file4:
                    lines = file4.readlines()
                lines[1] = "20" + '\n'# 修改LV
                lines[2] = "111" + '\n'# 修改血量
                lines[3] = "111" + '\n'# 修改血量上限
                lines[4] = "999999" + '\n'# 修改攻防
                lines[5] = "999999" + '\n'# 修改攻防
                lines[6] = "999999" + '\n'# 修改攻防
                lines[7] = "999999" + '\n'# 修改攻防
                lines[10] = "100000000000000" + '\n'# 修改金钱
                lines[28] = "52" + '\n'#修改武器和防具
                lines[29] = '53' + '\n'#修改武器和防具
                with open(utfliepath + "/file0", "w") as file4:
                    file4.writelines(lines)
                    file4.close()
                    tk.messagebox.showinfo("提示", "你已登神（bushi）")
            else:
                with open(utfliepath+"/file0", "r") as file4:
                    lines = file4.readlines()
                lines[4] = "999999" + '\n'# 修改攻防
                lines[5] = "999999" + '\n'# 修改攻防
                lines[6] = "999999" + '\n'# 修改攻防
                lines[7] = "999999" + '\n'# 修改攻防
                lines[10] = "100000000000000" + '\n'# 修改金钱
                lines[28] = "52" + '\n'#修改武器和防具
                lines[29] = '53' + '\n'#修改武器和防具
                with open(utfliepath+"/file0", "w") as file4:
                    file4.writelines(lines)
                    file4.close()
                    tk.messagebox.showinfo("提示","修改完成")
            if flag:
                os.startfile(uttaskpath)
        except FileNotFoundError:
            messagebox.showwarning("提示", "你似乎没有存档")
    def click_3_actions():
        utfliepath = a + "/Local/UNDERTALE"
        try:
            tk.messagebox.showinfo("提示", "修改非实时生效，需进入游戏再次存档即可")
            tk.messagebox.showwarning("警告","在没有关闭dogcheck的情况下，进入0-4、239-263、及265-335会进入坏档狗的界面")
            #################################子窗口
            child_window = tk.Toplevel(window)
            child_window.title("请输入room值")
            child_window.resizable(0, 0)
            #################################子窗口
            entry = tk.Entry(child_window)#输入框
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
                    lines[547] = _input + '\n'#修改548行为输入值
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
                webbrowser.open("https://pcy.ulyssis.be/undertale/rooms")# 打开网页
            #####################按钮
            button = tk.Button(child_window, text="确定", command=actions1)
            button.pack(padx=20, pady=20, side=tk.LEFT)
            button2 = tk.Button(child_window, text="房间id对照表", command=act2)
            button2.pack(padx=20, pady=20, side=tk.LEFT)
            #####################按钮
        except FileNotFoundError:
            messagebox.showwarning("提示", "您似乎没有存档")
    def click_4_actions():
        #########################################子窗口
        child_window2 = tk.Toplevel(child_window)
        child_window2.title("获取物品")
        child_window2.geometry("350x175")
        child_window2.resizable(0, 0)
        #########################################子窗口
        ##########################################标题、输入框、选择框
        label2 = tk.Label(child_window2, text="请在下方输入框键入物品id", fg="black", font=("微软雅黑", 10))
        label2.pack(side="top", pady=5)
        entry = tk.Entry(child_window2,)
        entry.pack(padx=20, pady=10, side=tk.TOP)
        combobox = ttk.Combobox(child_window2)
        entry.pack(padx=20, pady=10, side=tk.TOP)
        combobox.pack()
        combobox["value"] = ("物品栏位置一（13）", "物品栏位置二（15）", "物品栏位置三（17）","物品栏位置四（19）","物品栏位置五（21）","物品栏位置六（23）","物品栏位置七（25）","物品栏位置八（27）")
        combobox.current(0)
        ###########################################标题、输入框、选择框
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
                ################################################获取选择框里的数字
                inputstr = filter(str.isdigit, str(combobox.get()))
                inputstr2 = list(inputstr)
                finalnum =  "".join(inputstr2)
                finalnum = int(finalnum)
                ################################################获取选择框里的数字
                with open(utfliepath + "/file0", "r") as file:
                    lines = file.readlines()
                lines[finalnum-1] = str(entry.get()) + '\n'
                with open(utfliepath + "/file0", "w") as file:
                    file.writelines(lines)#写入输入框获取的数据到（选择框里的数字-1）行
                    file.close()
                    tk.messagebox.showinfo("提示", "修改完成")
                if flag:
                    os.startfile(uttaskpath)
            except FileNotFoundError:
                messagebox.showwarning("提示", "您似乎没有存档")
                return None
        def actions2():
            webbrowser.open("https://pcy.ulyssis.be/undertale/items")#打开网页
        ############################一些按钮
        button = tk.Button(child_window2, text="确定", width=15,font=("微软雅黑", 10),command=actions)
        button.pack(padx=10, pady=5, side=tk.LEFT)
        button2 = tk.Button(child_window2, text="物品id对照表", width=15, font=("微软雅黑", 10),command=actions2)
        button2.pack(padx=10, pady=5, side=tk.LEFT)
        ###########################一些按钮
        child_window2.mainloop()
    def click_5_actions():
        tk.messagebox.showinfo("提示","此功能会伪造你已到底某剧情节点\n注意：大范围剧情跨越可能导致修改失效，如：在遗迹里修改剧情至到达雪镇")
        utfliepath = a + "/Local/UNDERTALE"
        try:
            tk.messagebox.showinfo("提示", "修改非实时生效，需进入游戏再次存档即可")#提示
            ###################################
            child_window = tk.Toplevel(window)
            child_window.title("选择剧情")
            child_window.resizable(0, 0)
            ###################################子窗口
            ###################################
            combobox = ttk.Combobox(child_window)
            combobox.pack(side=tk.LEFT)
            ###################################选择框
            combobox["value"] = (#选择框里的东西（剧情节点）
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
                    ################################################获取选择框里的数字
                    inputstr = filter(str.isdigit, str(combobox.get()))
                    inputstr2 = list(inputstr)
                    finalnum = "".join(inputstr2)
                    finalnum = str(finalnum)
                    ################################################获取选择框里的数字
                    with open(utfliepath + "/file0", "r") as file:
                        lines = file.readlines()
                    lines[542] = finalnum + '\n'
                    with open(utfliepath + "/file0", "w") as file:
                        file.writelines(lines)# 写入剧情节点
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
        button = tk.Button(child_window, text="确定", command=actions1)#一个按钮
        button.pack(padx=20, pady=20, side=tk.LEFT)
    def click_6_actions():
        utfliepath = a + "/Local/UNDERTALE"
        try:
            tk.messagebox.showinfo("提示", "修改非实时生效，需进入游戏再次存档即可")
            ###################################子窗口
            child_window = tk.Toplevel(window)
            child_window.title("请输入fun")
            child_window.resizable(0, 0)
            ###################################子窗口
            entry = tk.Entry(child_window)#输入框
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
                        input_num = int(_input)# 判断是否为纯数字（整数型）
                    except ValueError:
                        tk.messagebox.showwarning("","数值非法")
                        return None
                    if 0<= input_num <= 100:# 判断大小是否在合法区间
                        text = f'fun="{_input}"'#拼接
                        with open(utfliepath+"/undertale.ini", "r", errors='ignore') as file:
                            lines = file.readlines()
                        rewirteline = [index for index, line in enumerate(lines) if "fun" in line]# 获取存档文件里要写入的位置
                        for index in rewirteline:
                            lines[index] = text + "\n"
                        with open(utfliepath+"/undertale.ini", "w", errors='ignore') as file:
                            file.writelines(lines)# 写入数据
                        file.close()
                    else:
                        tk.messagebox.showwarning("", "数值非法")
                        return None
                    if flag:
                        os.startfile(uttaskpath)
                    child_window.destroy()
                    tk.messagebox.showinfo("提示", "修改成功")
                except FileNotFoundError:
                    messagebox.showwarning("提示", "你似乎没有存档")
                    return  None
            button = tk.Button(child_window, text="确定", command=actions)
            button.pack(padx=20, pady=20, side=tk.LEFT)
        except FileNotFoundError:
            messagebox.showwarning("提示", "你似乎没有存档")
    def click_7_actions():
        os.system("notepad" + " " + utfliepath + "/undertale.ini")# 打开存档信息文件
    #########################子窗口的亿些按钮
    _button0 = tk.Button(child_window, text="创建屠杀线残留文件",width=15, command=lambda:click_0_actions(),font=("微软雅黑", 15))
    _button0.pack(pady=10)
    _button1 = tk.Button(child_window, text="删除屠杀线残留文件",width=15, command=lambda:click_1_actions(),font=("微软雅黑", 15))
    _button1.pack(pady=10)
    _button2 = tk.Button(child_window, text="一键神装",width=15, command=lambda:click_2_actions(),font=("微软雅黑", 15))
    _button2.pack(pady=10)
    _button3 = tk.Button(child_window, text="修改room", width=15,command=lambda:click_3_actions(),font=("微软雅黑", 15))
    _button3.pack(pady=10)
    _button4 = tk.Button(child_window, text="获取物品",width=15, command=lambda:click_4_actions(),font=("微软雅黑", 15))
    _button4.pack(pady=10)
    _button5 = tk.Button(child_window, text="修改剧情",width=15, command=lambda:click_5_actions(),font=("微软雅黑", 15))
    _button5.pack(pady=10)
    _button6 = tk.Button(child_window, text="修改fun",width=15, command=lambda:click_6_actions(),font=("微软雅黑", 15))
    _button6.pack(pady=10)
    _button7 = tk.Button(child_window, text="编辑存档信息文件",width=15, command=lambda:click_7_actions(),font=("微软雅黑", 15))
    _button7.pack(pady=10)
    ##########################子窗口的亿些按钮
window.mainloop()