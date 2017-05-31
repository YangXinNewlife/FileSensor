# -*- coding:utf-8 -*-
import os
import time
import transfer
class Sensor(object):
    def __init__(self):
        print "Sensor Start Working"

    def file_check(self, directory):
        files = os.listdir(directory)
        self.triger(files)

    def dir_check(self, directory):
        if os.path.exists(directory):
            print "Dir_Check OK"
        else:
            raise Exception("Directory Not Exists")

    def triger(self, files):
        triger = transfer.Transfer()
        for file_name in files:
            file_name = '/root/script/20170531/' + file_name
            file_size_start = os.path.getsize(file_name)
            time.sleep(3)
            file_size_finish = os.path.getsize(file_name)
            if int(file_size_start) == int(file_size_finish):
                triger.file_transfer('192.168.1.241', 'root', '123456', '/data/sftp/mysftp/rec_data/20170531/',file_name)

if __name__ == '__main__':
    sensor = Sensor()
    monitor_dir = '/root/script/20170531'
    sensor.dir_check(monitor_dir)
    sensor.file_check(monitor_dir)

