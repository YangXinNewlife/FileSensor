# -*- coding:utf -*-
import pexpect
class Transfer(object):
    def __init__(self):
        print "Transfer Working"

    def file_transfer(self,ip, user, passwd, dst_path, filename):
        passwd_key = '.*assword.*'
        cmdline = 'scp %s %s@%s:%s' % (filename, user, ip, dst_path)
        try:
            child = pexpect.spawn(cmdline)
            child.expect(passwd_key)
            child.sendline(passwd)
            child.expect(pexpect.EOF)
            print "Transfer Work Finish!"
        except:
            print "upload faild!"

if __name__ == '__main__':
    triger = Transfer()
    triger.file_transfer('192.168.1.241', 'root', '123456', '/data/sftp/mysftp/rec_data/', 'a.txt')