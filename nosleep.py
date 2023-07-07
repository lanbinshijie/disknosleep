import time

print('''
  _____  _     _      _   _          _____ _
 |  __ \(_)   | |    | \ | |        / ____| |
 | |  | |_ ___| | __ |  \| | ___   | (___ | | ___  ___ _ __
 | |  | | / __| |/ / | . ` |/ _ \   \___ \| |/ _ \/ _ \ '_ \\
 | |__| | \__ \   <  | |\  | (_) |  ____) | |  __/  __/ |_) |
 |_____/|_|___/_|\_\ |_| \_|\___/  |_____/|_|\___|\___| .__/
                                                      | |
                                                      |_|
===============================================================
Disk No Sleep - DNS磁盘唤醒服务       By. Lanbin      V1.0
''')


def write_to_disk():
    i = 1
    while True:
        # 写入数据到硬盘
        print("[第" + str(i) + "次]正在写入数据到A、F、I、G盘......")
        with open(r'A:\nosleep.dat', 'w') as file:
            file.write('Some data\n')
        with open(r'F:\nosleep.dat', 'w') as file:
            file.write('Some data\n')
        with open(r'I:\nosleep.dat', 'w') as file:
            file.write('Some data\n')
        with open(r'G:\nosleep.dat', 'w') as file:
            file.write('Some data\n')
        print("写入成功！十秒后再试......")
        time.sleep(10)  # 暂停10秒钟
        i += 1


def main():
    try:
        write_to_disk()
    except KeyboardInterrupt:
        com = input("磁盘休眠暂停结束，输入Y继续，其他退出: >> ")
        if com == "y":
            main()
        else:
            exit()
        pass


if __name__ == '__main__':
    main()
