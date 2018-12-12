# -*- coding: cp936 -*-
import os,subprocess
import time

#获取手机是否连接电脑
def connectDevice():
    '''检查设备是否连接成功，如果成功返回True，否则返回False'''
    try:
        '''获取设备列表信息'''
        deviceInfoTemp = subprocess.check_output('adb devices')
        deviceInfo = deviceInfoTemp.decode()
        
        '''如果链接设备成功返回true，否则返回false'''
        if "	device" in deviceInfo:
            return True
        else:
            return False
    except Exception as err:
        print("Device Connect Fail:" + err)


#获取手机的 abilist
def getAbilist():
    
    try:
        '''获取设备 CPU 信息'''
        CPUInfoTemp = subprocess.check_output('adb shell getprop ro.product.cpu.abilist')
        CPUInfo = CPUInfoTemp.decode()   
        print("该设备支持 ABI 类型为：" + str(CPUInfo)+"------------------------------------------------------------")

        if "arm64-v8a" in CPUInfo:
            print("支持 64 位和 32 位。")
        elif "armeabi-v7a" or "armeabi"in CPUInfo:
            print("不支持 64 位，支持 32 位。")
        else:
    	    print("既不支持 64 位，也不支持 32 位。")
		
    except Exception as err:
        print("获取 CPU 信息失败：:" + err)

	
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
    print("------------------------------------------------------------")
    getAbilist();
    time.sleep(10)
else:
    print("即将退出本程序...")    
    time.sleep(10)



