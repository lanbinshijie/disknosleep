
# Disk No Sleep <img alt="Static Badge" src="https://img.shields.io/badge/License-MIT-blue"> <img alt="Static Badge" src="https://img.shields.io/badge/Version-v1.0-green">
Disk No Sleep (DNS)，一个机械硬盘唤醒小程序

![pCcrd00.png](https://s1.ax1x.com/2023/07/07/pCcsU8e.png)


## 原理
最近买了一个硬盘柜和四块机械硬盘，但是在使用的时候发现机械硬盘一不小心就偷偷进入休眠状态。导致有些时候需要使用时还要激活硬盘，速度很慢有时甚至会卡死。在辛苦的Google之后，从网上搜集到了这样一个方法：只要往硬盘里写入东西就可以维持机械硬盘运作，这个小程序就是按照这样的原理编写而成的。

程序很简洁，就是每隔十秒钟向磁盘中写入一份数据，使磁盘始终处于活动状态。

## 使用方法

> 请确保您的电脑已经安装Python环境

1. 下载`nosleep.py`
2. 修改`write_to_disk`函数中写入磁盘的代码调整至您的需求（具体可看下方说明））
```python
def write_to_disk():
    i = 1
    while True:
        # 写入数据到硬盘（可以修改打印信息）
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
```
3. 双击运行程序，或修改后缀成为pyw在后台运行（可用任务管理器杀死进程）

### 修改原则
1. 请将`with open() as f`的数量更改成您拥有的磁盘数量。比如我有4块硬盘，我就复制了四份。
2. 请修改文件地址最前方的盘符，使其变成您所挂在的磁盘
3. 原则上，您可以修改文件写入的路径和内容，但是我们不建议这么做，因为没有必要
4. 请遵循开源协议MIT协议

## 使用提醒
1. 程序可以通过修改后缀名为pyw在后台运行
2. 在程序运行时可以按下`Ctrl + C`键中断程序
   - 接下来程序会进入暂停状态
   - 您可以通过输入`y`来继续运行程序
   - 也可以通过输入任意字符（甚至直接回车）来中断程序使程序退出

