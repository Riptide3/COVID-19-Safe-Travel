def __init__(self):
    self.sim = simulator.Simulator()
    self.sim.forever()


# my
self.daySpin.setEnabled(False)
self.hourSpin.setEnabled(False)
self.strategyRadioButton1.setChecked(True)
self.strategyRadioButton2.toggled.connect(self.daySpin.setEnabled)
self.strategyRadioButton2.toggled.connect(self.hourSpin.setEnabled)
self.startButton.clicked.connect(self.startButton_clicked)
# my



def show_route(self, name, ID):
    d_date, risk, route = self.sim.get_plan(ID)
    text = ''
    E2C = {'BUS': '汽车', 'TRAIN': '火车', 'AIRPLANE': '飞机'}
    prev = int(d_date.strftime('%H'))  # TODO:测试
    one_day = datetime.timedelta(days=1)
    if len(route) > 0:
        text += name + '，您好\n\n' + '为您规划的路线如下：\n\n'
        for part in route:
            if part['origin'] == part['destination']:
                continue
            else:
                if part['departure_time'] < prev:
                    d_date += one_day
                text += f"{d_date.strftime('%m-%d')} {part['departure_time']:02} - "
                if part['arrival_time'] < part['departure_time']:
                    d_date += one_day
                text += f"{d_date.strftime('%m-%d')} {part['arrival_time']:02}  "
                text += f"{part['origin']} --> {part['destination']}  {E2C[part['type']]}\n"
                prev = part['arrival_time']
        text += f'\n该路线的风险值为：{str(risk)}\n'
    else:
        text = f'抱歉，没有满足您要求的路线\n'

    font = QtGui.QFont()
    font.setFamily("新宋体")
    # font.setPointSize(10)
    self.routeTextBrowser.setFont(font)
    self.routeTextBrowser.setText(text)


def startButton_clicked(self):
    name = self.nameLineEdit.text()
    ID = self.idLineEdit1.text()
    if name == '' or ID == '':
        QtWidgets.QMessageBox.warning(self.centralwidget, '注意', '姓名和身份证号不能为空！',
                                      QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
    elif self.originCombo.currentText() == self.destinationCombo.currentText():
        QtWidgets.QMessageBox.warning(self.centralwidget, '注意', '出发地和目的地不能相同！',
                                      QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
    else:
        origin = self.originCombo.currentText()
        destination = self.destinationCombo.currentText()
        limit = self.strategyRadioButton2.isChecked()
        print(limit)
        if limit:
            print(self.daySpin.text())
            print(self.hourSpin.text())
            time_limit = int(self.daySpin.text()[:-1]) * 24 + int(self.hourSpin.text()[:-1])
        else:
            time_limit = 4 * 24  # TODO: 修改此处
        traveler = {'name': name, 'ID': ID, 'origin': origin, 'destination': destination, 'time_limit': time_limit}
        print(traveler)
        self.nameLineEdit.clear()
        self.idLineEdit1.clear()
        self.sim.new_traveler(traveler)
        self.show_route(name, ID)


def fa(self):
    self.startSearchButton