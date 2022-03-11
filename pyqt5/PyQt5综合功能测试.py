import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from random import randint

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon("1.png"))
        self.setWindowTitle("我的程序窗口")
        self.statusBar().showMessage('准备就绪')#首次运行提示状态
        self.centern()
        self.InitUI()

    def InitUI(self):
        #菜单栏相关
        GuessNumberAct = QAction(QIcon('1.png'),"猜数字", self)
        GuessNumberAct.setStatusTip("猜数字的游戏")
        GuessNumberAct.triggered.connect(self.GuessNumber)
        LCDAct=QAction(QIcon('1.png'),"信号槽", self)
        LCDAct.setStatusTip("信号槽模块，包括拖拽和旋转")
        LCDAct.triggered.connect(self.LCD)
        GuessFingerAct=QAction(QIcon('1.png'),"猜拳", self)
        GuessFingerAct.setStatusTip("来一局猜拳游戏")
        GuessFingerAct.triggered.connect(self.GuessFinger)
        CaculateAct=QAction(QIcon('1.png'),"计算器", self)
        CaculateAct.setStatusTip("计算器")
        CaculateAct.triggered.connect(self.Caculate)
        ProcessBarAct=QAction(QIcon('1.png'),"进度条", self)
        ProcessBarAct.setStatusTip("进度条功能")
        ProcessBarAct.triggered.connect(self.ProcessBar)
        exitAct = QAction(QIcon('1.png'), '退出(&Q)', self)#设置选项图标和名称
        exitAct.setShortcut('Ctrl+Q')#设置快捷键
        exitAct.setStatusTip('退出程序')#鼠标指上去后提示
        exitAct.triggered.connect(qApp.quit)#设置点击动作连接

        saveMenu = QMenu("二级目录", self)        #菜单栏二级目录
        saveAct = QAction(QIcon('1.png'), "保存(&S)", self)
        saveasAct = QAction(QIcon('1.png'), '另存为(&O)', self)
        saveMenu.addAction(saveAct)        #菜单二级目录加入进去
        saveMenu.addAction(saveasAct)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('文件(&F)')
        fileMenu.addAction(GuessNumberAct)
        fileMenu.addAction(LCDAct)
        fileMenu.addAction(GuessFingerAct)
        fileMenu.addAction(CaculateAct)
        fileMenu.addAction(ProcessBarAct)
        fileMenu.addMenu(saveMenu)
        fileMenu.addSeparator()     #添加分割线
        fileMenu.addAction(exitAct)     #按该顺序排列菜单

        toolbar = self.addToolBar("工具栏")
        toolbar.addAction(GuessNumberAct)
        toolbar.addAction(exitAct)
        # toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon) #是否使工具栏有下标名称

        self.show()

    def closeEvent(self, event):
        reply=QMessageBox.question(self,"退出窗口确认","确认退出吗",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        # reply=QMessageBox.critical(self,"退出窗口确认","确认退出吗",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        # reply=QMessageBox.warning(self,"退出窗口确认","确认退出吗",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        # reply=QMessageBox.information(self,"退出窗口确认","确认退出吗",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        #第三个参数指定出现在对话框中的按钮的组合。最后一个参数是默认按钮。它是初始键盘焦点的按钮。
        #QMessageBox对话框包含类型只是图标不同其他无太大差别
        if reply==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


    #上下文菜单，右键后的选项
    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
        newAct = cmenu.addAction("新建")
        opnAct = cmenu.addAction("保存")
        quitAct = cmenu.addAction("退出")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        if action == quitAct:
            qApp.quit()


    def centern(self):
        qr=self.frameGeometry()
        cp=QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def GuessNumber(self):
        self.form1 = QWidget()
        self.form1.resize(300,300)
        self.bt1 = QPushButton("我猜", self.form1)
        self.num = randint(1, 100)
        self.bt1.setGeometry(100, 100, 50, 50)
        self.bt1.setToolTip("点击这里猜数字")  # 工具提示
        self.setToolTip("这里什么都没有哦")
        self.bt1.clicked.connect(self.showMessage)
        self.text = QLineEdit("在这里输入数字", self.form1)
        self.text.selectAll()  # 将文本框全选，方便输入数字，否则你还得手动全选删除默认字符
        self.text.setFocus()  # 让焦点置于文本栏中，方便用户输入，不然还得手动在文本栏中单击一下
        self.text.setGeometry(50, 50, 100, 50)
        self.form1.show()

    def showMessage(self):
        guessnumber=int(self.text.text())
        print(self.num)

        if guessnumber>self.num:
            QMessageBox.about(self.form1,"看结果","猜大了")
            self.text.setFocus()
            self.text.selectAll()
        elif guessnumber<self.num:
            QMessageBox.about(self.form1,"看结果","猜小了")
            self.text.setFocus()
            self.text.selectAll()
        else:
            QMessageBox.about(self.form1,"看结果","答对了")
            self.num=randint(1,100)
            self.text.clear()
            self.text.setFocus()

    def LCD(self):
        self.form2 = QWidget()
        self.form2.resize(1024, 768)
        lcd1 = QLCDNumber(self.form2)
        lcd2 = QLCDNumber(self.form2)
        dial = QDial(self.form2)
        slider = QSlider(self.form2)
        lcd1.setGeometry(200, 50, 100, 50)
        dial.setGeometry(200, 100, 100, 100)
        lcd2.setGeometry(400, 50, 100, 50)
        slider.setGeometry(400, 100, 100, 100)
        dial.valueChanged.connect(lcd1.display)
        slider.valueChanged.connect(lcd2.display)
        self.form2.show()

    def GuessFinger(self):
        self.form3 = QWidget()
        self.form3.resize(300, 300)
        cqbt1 = QPushButton('剪刀', self.form3)
        cqbt1.setGeometry(30, 50, 40, 20)
        cqbt2 = QPushButton('石头', self.form3)
        cqbt2.setGeometry(130, 50, 40, 20)
        cqbt3 = QPushButton('布', self.form3)
        cqbt3.setGeometry(230, 50, 40, 20)
        cqbt1.clicked.connect(self.buttonclicked)
        cqbt2.clicked.connect(self.buttonclicked)
        cqbt3.clicked.connect(self.buttonclicked)
        self.form3.show()

    def buttonclicked(self):
        computer=randint(1,3)
        player=0
        sender=self.sender()
        if sender.text() == '剪刀':
            player = 1
        elif sender.text() == '石头':
            player = 2
        else:
            player = 3

        if player == computer:
            QMessageBox.about(self.form3, '结果', '平手')
        elif player == 1 and computer == 2:
            QMessageBox.about(self.form3, '结果', '电脑：石头，电脑赢了！')
        elif player == 2 and computer == 3:
            QMessageBox.about(self.form3, '结果', '电脑：布，电脑赢了！')
        elif player == 3 and computer == 1:
            QMessageBox.about(self.form3, '结果', '电脑：剪刀，电脑赢了！')
        elif computer == 1 and player == 2:
            QMessageBox.about(self.form3, '结果', '电脑：剪刀，玩家赢了！')
        elif computer == 2 and player == 3:
            QMessageBox.about(self.form3, '结果', '电脑：石头，玩家赢了！')
        elif computer == 3 and player == 1:
            QMessageBox.about(self.form3, '结果', '电脑：布，玩家赢了！')

    def Caculate(self):
        self.form4=QWidget()
        grid = QGridLayout()
        self.form4.setLayout(grid)
        self.form4.setGeometry(300, 300, 400, 300)
        self.form4.setWindowTitle("计算器")
        self.form4.lcd = QLCDNumber()
        grid.addWidget(self.form4.lcd, 0, 0, 3, 0)
        grid.setSpacing(10)

        names = ['cls', 'bc', '', 'close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(4, 9) for j in range(4, 8)]

        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)
            button.clicked.connect(self.Cli)
        self.form4.show()

    def Cli(self):
        sender = self.form4.sender().text()
        ls = ['/', '*', '-', '=', '+']
        if sender in ls:
            self.form4.lcd.display('A')
        else:
            self.form4.lcd.display(sender)

    def ProcessBar(self):
        self.form5=QWidget()
        self.form5.pbar = QProgressBar(self)
        self.form5.pbar.setGeometry(30, 40, 200, 25)

        self.form5.btn = QPushButton('Start', self)
        self.form5.btn.move(40, 80)
        self.form5.btn.clicked.connect(self.doAction)

        self.form5.timer = QBasicTimer()
        self.form5.step = 0

        self.form5.setGeometry(300, 300, 280, 170)
        self.form5.setWindowTitle('QProgressBar')
        self.form5.show()

    def timerEvent(self, e):

        if self.form5.step >= 100:
            self.form5.timer.stop()
            self.form5.btn.setText('Finished')
            return

        self.form5.step = self.step + 1
        self.form5.pbar.setValue(self.step)

    def doAction(self):

        if self.form5.timer.isActive():
            self.form5.timer.stop()
            self.form5.btn.setText('Start')
        else:
            self.form5.timer.start(100, self)
            self.form5.btn.setText('Stop')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())