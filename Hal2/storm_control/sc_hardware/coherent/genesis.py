import ctypes
import time
import threading
from ctypes import wintypes

class Genesis():
    def __init__(self, laser_handle_index, power_mW):
        self.laser_handle_index = laser_handle_index
        self.power_mW = power_mW

        # print('coherent turn on')
        # cohr_dll = ctypes.cdll.LoadLibrary(
        #     "C:/Users/Light-saver/Documents/LabVIEW/Lasers/Coherent Genesis/Win64/CohrHOPS.dll")
        # v0 = ctypes.create_string_buffer(16)
        # cohr_dll.CohrHOPS_GetDLLVersion(v0)
        # # print(str(v0.value))
        # v1 = (ctypes.c_ulonglong * 2)()
        # v2 = ctypes.c_ushort()
        # v2p = ctypes.pointer(v2)
        # v3 = ctypes.c_ushort()
        # v3p = ctypes.pointer(v3)
        # v4 = ctypes.c_ushort()
        # v4p = ctypes.pointer(v4)
        # v5 = ctypes.c_ushort()
        # v5p = ctypes.pointer(v5)
        # v6 = ctypes.c_ushort()
        # v6p = ctypes.pointer(v6)
        # # cohr_dll.CohrHOPS_CheckForDevices(v1, v2p, v3p, v4p, v5p, v6p)

        # self.handle = v1

    def threadingon(self):
        print(threading)

        print('hello')
        print('coherent turn on')
        cohr_dll = ctypes.windll.LoadLibrary(
            "C:/Users/Light-saver/Documents/LabVIEW/Lasers/Coherent Genesis/Win64/CohrHOPS.dll")
        v0 = ctypes.create_string_buffer(16)
        ret = cohr_dll.CohrHOPS_GetDLLVersion(v0)
        # print(str(v0.value))
        v1 = ctypes.create_string_buffer(64)#(ctypes.c_ulonglong * 2)()
        v2 = ctypes.c_ushort()
        v2p = ctypes.pointer(v2)
        v3 = ctypes.c_ushort()
        v3p = ctypes.pointer(v3)
        v4 = ctypes.c_ushort()
        v4p = ctypes.pointer(v4)
        v5 = ctypes.c_ushort()
        v5p = ctypes.pointer(v5)
        v6 = ctypes.c_ushort()
        v6p = ctypes.pointer(v6)
        v2p = ctypes.create_string_buffer(64) #wintypes.LPDWORD()
        v3p = ctypes.create_string_buffer(64)# wintypes.LPDWORD()
        v4p = ctypes.create_string_buffer(64)# wintypes.LPDWORD()
        v5p = ctypes.create_string_buffer(64)# wintypes.LPDWORD()
        v6p = ctypes.create_string_buffer(64) #wintypes.LPDWORD()
        ret = cohr_dll.CohrHOPS_CheckForDevices(v1, v2p, v3p, v4p, v5p, v6p)

        ret = cohr_dll.CohrHOPS_InitializeHandle.argtypes = [ctypes.c_ulonglong, ctypes.c_void_p]
        v7 = ctypes.create_string_buffer(16)
        ret = cohr_dll.CohrHOPS_InitializeHandle(v1[self.laser_handle_index], v7)
        ret = cohr_dll.CohrHOPS_SendCommand.argtypes = [ctypes.c_ulonglong, ctypes.c_void_p, ctypes.c_void_p]
        v8p = ctypes.create_string_buffer(16)
        v11p = ctypes.c_char_p(b'PCMD=50')
        ret = cohr_dll.CohrHOPS_SendCommand(v1[self.laser_handle_index], v11p, v8p)
        # time.sleep(3)
        v10p = ctypes.c_char_p(b'KSWCMD=1')
        v12p = ctypes.create_string_buffer(16)
        ret = cohr_dll.CohrHOPS_SendCommand(v1[self.laser_handle_index], v10p, v12p)
        ret = cohr_dll.CohrHOPS_Close(v1[self.laser_handle_index])


    def turnOn(self, fake_arg):

            # t1 = threading.Thread(target=self.threadingon)
            # # Start the thread. The main function continues immediately.
            # t1.start()
            # print('hello')
            # print('hello2')
            # return
            cohr_dll = ctypes.cdll.LoadLibrary(
                "C:/Users/Light-saver/Documents/LabVIEW/Lasers/Coherent Genesis/Win64/CohrHOPS.dll")
            v0 = ctypes.create_string_buffer(16)
            ret = cohr_dll.CohrHOPS_GetDLLVersion(v0)
            # print(str(v0.value))
            v1 = (ctypes.c_ulonglong * 2)()  # (ctypes.c_ulonglong * 2)()
            v2 = ctypes.c_ushort()
            v2p = ctypes.pointer(v2)
            v3 = ctypes.c_ushort()
            v3p = ctypes.pointer(v3)
            v4 = ctypes.c_ushort()
            v4p = ctypes.pointer(v4)
            v5 = ctypes.c_ushort()
            v5p = ctypes.pointer(v5)
            v6 = ctypes.c_ushort()
            v6p = ctypes.pointer(v6)
            v2p = ctypes.create_string_buffer(64)  # wintypes.LPDWORD()
            v3p = ctypes.create_string_buffer(64)  # wintypes.LPDWORD()
            v4p = ctypes.create_string_buffer(64)  # wintypes.LPDWORD()
            v5p = ctypes.create_string_buffer(64)  # wintypes.LPDWORD()
            v6p = ctypes.create_string_buffer(64)  # wintypes.LPDWORD()
            ret = cohr_dll.CohrHOPS_CheckForDevices(v1, v2p, v3p, v4p, v5p, v6p)

            ret = cohr_dll.CohrHOPS_InitializeHandle.argtypes = [ctypes.c_ulonglong, ctypes.c_void_p]
            v7 = ctypes.create_string_buffer(16)
            ret = cohr_dll.CohrHOPS_InitializeHandle(v1[self.laser_handle_index], v7)
            # ret = cohr_dll.CohrHOPS_SendCommand.argtypes = [ctypes.c_ulonglong, ctypes.c_void_p, ctypes.c_void_p]
            # v8p = ctypes.create_string_buffer(16)
            # v11p = ctypes.c_char_p(b'PCMD=50')
            # ret = cohr_dll.CohrHOPS_SendCommand(v1[self.laser_handle_index], v11p, v8p)
            # # time.sleep(3)
            # v10p = ctypes.c_char_p(b'KSWCMD=1')
            # v12p = ctypes.create_string_buffer(16)
            # ret = cohr_dll.CohrHOPS_SendCommand(v1[self.laser_handle_index], v10p, v12p)
            cohr_dll.CohrHOPS_Close.argtypes = [ctypes.c_ulonglong]
            ret = cohr_dll.CohrHOPS_Close(v1[self.laser_handle_index])
            print('closed')
            print(ret)

    def turnOff(self, fake_arg):

        print('turn off ')
        cohr_dll = ctypes.windll.LoadLibrary("C:/Users/Light-saver/Documents/LabVIEW/Lasers/Coherent Genesis/Win64/CohrHOPS.dll")
        v0 = ctypes.create_string_buffer(16)
        ret = cohr_dll.CohrHOPS_GetDLLVersion(v0)
        print(str(v0.value))
        v1 = (ctypes.c_ulonglong * 2)()
        v1 = ctypes.create_string_buffer(16)
        v2 = ctypes.c_ulonglong()
        v2p = ctypes.pointer(v2)
        v2p = ctypes.create_string_buffer(16)
        # v2p = (ctypes.c_ulonglong * 2)()
        v3 = ctypes.c_ulonglong()
        v3p = ctypes.pointer(v3)
        v3p = ctypes.create_string_buffer(16)
        # v3p = (ctypes.c_ulonglong * 2)()
        v4 = ctypes.c_ulonglong()
        v4p = ctypes.pointer(v4)
        v4p = ctypes.create_string_buffer(16)
        # v4p = (ctypes.c_ulonglong * 2)()
        v5 = ctypes.c_ulonglong()
        v5p = ctypes.pointer(v5)
        v5p = ctypes.create_string_buffer(16)
        # v5p = (ctypes.c_ulonglong * 2)()
        v6 = ctypes.c_ulonglong()
        v6p = ctypes.pointer(v6)
        v6p = ctypes.create_string_buffer(16)
        # v6p = (ctypes.c_ulonglong * 2)()
        # ret = cohr_dll.CohrHOPS_CheckForDevices.argtypes = [ctypes.c_ulonglong, ctypes.c_ulonglong, ctypes.c_ulonglong, ctypes.c_ulonglong, ctypes.c_ulonglong, ctypes.c_ulonglong]
        ret = ctypes.c_int32()
        v1  = (ctypes.c_ulonglong * 2)()
        v2p = ctypes.create_string_buffer(32) #wintypes.LPDWORD()
        v3p = ctypes.create_string_buffer(32)# wintypes.LPDWORD()
        v4p = ctypes.create_string_buffer(32)# wintypes.LPDWORD()
        v5p = ctypes.create_string_buffer(32)# wintypes.LPDWORD()
        v6p = ctypes.create_string_buffer(32) #wintypes.LPDWORD()
        # cohr_dll.CohrHOPS_CheckForDevices.argtypes = [ctypes.c_ulonglong, wintypes.LPDWORD, wintypes.LPDWORD, wintypes.LPDWORD, wintypes.LPDWORD, wintypes.LPDWORD]
        ret = cohr_dll.CohrHOPS_CheckForDevices(v1, v2p, v3p, v4p, v5p, v6p)
        # print(v1.value)
        ret = cohr_dll.CohrHOPS_InitializeHandle.argtypes = [ctypes.c_ulonglong, ctypes.c_void_p]
        v7 = ctypes.create_string_buffer(16)
        ret = cohr_dll.CohrHOPS_InitializeHandle(v1[self.laser_handle_index], v7)
        # ret = cohr_dll.CohrHOPS_SendCommand.argtypes = [ctypes.c_ulonglong, ctypes.c_void_p, ctypes.c_void_p]
        # v8p = ctypes.create_string_buffer(16)
        # v10p = ctypes.c_char_p(b'KSWCMD=0')
        # ret = cohr_dll.CohrHOPS_SendCommand(v1[self.laser_handle_index], v10p, v8p)
        cohr_dll.CohrHOPS_Close.argtypes = [ctypes.c_ulonglong]
        ret = cohr_dll.CohrHOPS_Close(v1[self.laser_handle_index])
        print('closed')
        print(ret)



if __name__ == "__main__":

    lsr2 = Genesis(0, 50)
    # lsr2.turnOn(0)
    # time.sleep(15)
    lsr2.turnOff(0)
