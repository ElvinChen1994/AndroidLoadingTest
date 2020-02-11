# -*- coding:utf-8 -*-
# Author : chen
# Data : 2020/2/11 11:50 下午
import csv
import  os

import time
class jwApp():
    def __init__(self):
        self.jwcontent=''
    #启动app
    def startApp(self):
        #获取冷启动时间
        jwcmd='adb shell am start  -W  -n com.android.browser/.BrowserActivity'

        # 在命令行中发现这是一个多行的结果
        #每隔1秒中执行次命令
        time.sleep(1)
        self.jwcontent=os.popen(jwcmd)
    #停止app
    def stopApp(self):
        #以冷启动方式关闭
        jwcmd='adb shell am  force-stop com.android.browser'

        #以热启动时间关闭
        #jwcmd = 'adb shell   input  keyevent 3'
        os.popen(jwcmd)
    #获取app启动时间
    def GetStartTime(self):
        # 遍历每一行
        #readlines() ====>这个没有提示
# 注意readlines 不能使用两次，因为第一次用了  指针会指向最后

        for line in self.jwcontent.readlines():
            if "ThisTime" in line:
                #strip去除每一行最后一个字母
			#split默认以数字0 分割
                self.satrtTimes=line.split(":")[1].strip("\n")
                break
        return  self.satrtTimes

#控制过程(如何启动app+如何关闭app)
class Controller():
    def __init__(self,count):
        self.app=jwApp()
        self.count=count
        # 启动时间，消耗时间
        self.alldata=[("currentTime","elpasedtime")]
    #单次测试过程 ====》收集数据
    def testprocess(self):
        self.app.startApp()
        # 获取app消耗时间
        jwelpasedtime=self.app.GetStartTime()
        self.app.stopApp()
        # 获取当前时间
        jwcurrenttime=self.getCurrentTime()
        print(jwcurrenttime)
        print(jwelpasedtime)
        self.alldata.append((jwcurrenttime,jwelpasedtime))
    #多次执行测试过程
    def run(self):
        while self.count>0:
            self.testprocess()
            self.count=self.count-1

    #获取当前时间
    def  getCurrentTime(self):
        # 指定时间格式
        # import time
        currentTime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        return  currentTime

    # 保存测试结果===》存放到CSV文件中去
    def saveDatatoCSV(self):
        csvfile=open('startTime.csv','w+')
        writer=csv.writer(csvfile)
        print(self.alldata)
        writer.writerows(self.alldata)
        csvfile.close()

if __name__=='__main__':
    #10次打开关闭app
    controller=Controller(10)
    controller.run()
    controller.saveDatatoCSV()