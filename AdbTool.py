# -*- coding: cp936 -*-
import os,subprocess
import time

#用于获取手机是否连接电脑
def connectDevice():
    '''检查设备是否连接成功，如果成功返回True，否则返回False'''
    try:
        '''获取设备列表信息'''
        deviceInfoTemp= subprocess.check_output('adb devices')
        deviceInfo = deviceInfoTemp.decode()
        
        '''如果链接设备成功返回true，否则返回false'''
        if "	device" in deviceInfo:
            return True
        else:
            return False
    except Exception as err:
        print("Device Connect Fail:" + err)


#用于将lua_log文件导出到电脑
def copyLuaLogFile():
    date = input("请输入lua_log日期（例如：4月19日的log输入 0419）：")
    
    path = "/sdcard/jjlog_lua_" + str(date) + ".log"
    pullsheel = "adb pull " + str(path) + " f:"

    print("正在导出，请稍等...")

    os.system(pullsheel)

    object_file = "f:\\jjlog_lua_" + str(date) + ".log" 
    if os.path.exists(object_file):
        print("导出成功！")
    else:
        print("导出失败！")


#用于将android_log文件导出到电脑
def copyAndroidLogFile():
    date = input("请输入android_log日期（例如：4月19日的log输入 0419）：")
    
    path = "/sdcard/jjlog_android_" + str(date) + ".log"
    pullsheel = "adb pull " + str(path) + " f:\\"

    print("正在导出，请稍等...")

    os.system(pullsheel)

    object_file = "f:\\jjlog_android_" + str(date) + ".log" 
    if os.path.exists(object_file):
        print("导出成功！")
    else:
        print("导出失败！")
    
	
#函数入口
"""判断手机是否连接成功，如果连接失败让用户选择是否重新尝试连接"""
while not connectDevice():
    print("连接手机失败，请确保手机打开USB调试！")
    result = input("输入 1 重新尝试，输入 2 退出程序：")
    if result == 1:
        continue
    else:     
        break

        
if connectDevice():
    print("成功连接手机！")
    logType = input("请输入导出log类型（导出 lua_log 请输入 1 ，导出 android_log 请输入 2）：")
    if logType == 1:
        copyLuaLogFile()
    else:
        copyAndroidLogFile()
    
    time.sleep(3)
else:
    print("即将退出本程序...")
    
    time.sleep(3)



