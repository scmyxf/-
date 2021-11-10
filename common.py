import wx

RATE_GOODS = {6202500:[350,0],	# 货物招标
	1000000:[141.9,0.00004],
	500000:[111.9,0.00006],
	100000:[79.9,0.00008],
	50000:[62.4,0.00035],
	10000:[42.4,0.000500],
	5000:[29.9,0.002500],
	1000:[9.9,0.005000],
	500:[5.9,0.008000],
	100:[1.5,0.011000],
	0:[0,0.015000]
	}

RATE_SERVICE = {5463750:[300,0],	# 服务招标
	1000000:[121.45,0.00004],
	500000:[91.45,0.00006],
	100000:[59.45,0.00008],
	50000:[41.95,0.00035],
	10000:[21.95,0.00050],
	5000:[16.95,0.00100],
	1000:[6.95,0.00250],
	500:[4.7,0.00450],
	100:[1.5,0.00800],
	0:[0,0.01500]
	}

RATE_ENGINEERING = {8998750:[450,0],	# 工程招标
	1000000:[130.05,0.00004],
	500000:[100.05,0.00006],
	100000:[68.05,0.00008],
	50000:[50.55,0.00035],
	10000:[30.55,0.00050],
	5000:[20.55,0.00200],
	1000:[6.55,0.00350],
	500:[3.8,0.00550],
	100:[1,0.00700],
	0:[0,0.01000]
	}
    
class calRecord():
    def __init__(self, index, name, type, floGoal, floCharge, dis_rate, discount):
        self.index = index  # 项目编号
        self.name = name    # 项目名称
        self.type = type    # 项目类型
        self.floGoal = floGoal  # 中标金额
        self.floCharge = floCharge    # 标准收费
        self.dis_rate = dis_rate    # 折扣
        self.discount = discount    # 折扣后收费
        
    def getIndex(self):
        return self.index
        
    def getDiscount(self):
        return self.discount
        
    def getWord(self):
        return '项目名称：%s\n项目类型：%s\n项目造价：%s万元\n标准收费：%s元\n单项折扣：%s%%\n折扣后收费：%s元\n==================\n' % (self.name, self.type, self.floGoal, self.floCharge, self.dis_rate, self.discount)

class Validator_0_100(wx.Validator):# 创建验证器子类，控制0-100以内数字
    def __init__(self):
        wx.Validator.__init__(self)
        self.ValidInput = ['.','0','1','2','3','4','5','6','7','8','9']
        self.StringLength = 0
        self.numstr = ''
        self.Bind(wx.EVT_CHAR,self.OnCharChanged)  #  绑定字符输入事件

    def OnCharChanged(self, event):
        keycode = event.GetKeyCode()    # 得到输入字符的 ASCII 码
        if keycode == 8:    # 退格（ASCII 码 为8），删除一个字符。
            if self.StringLength>0:
                self.StringLength -= 1
            self.numstr = self.numstr[:self.StringLength]
            event.Skip()    # 事件继续传递
            return
        
        InputChar = chr(keycode)    # 把 ASII 码 转成字符
        if InputChar in self.ValidInput:
            # 第一个字符为 .,非法，拦截该事件，不会成功输入
            if InputChar == '.' and self.StringLength == 0:
                return False
            else:
                self.numstr = self.numstr + InputChar
                try:
                    if float(self.numstr)>100:
                        self.numstr = self.numstr[:self.StringLength]
                        return False
                    else:
                    # 在允许输入的范围，继续传递该事件。
                        event.Skip()
                        self.StringLength += 1
                        return True
                except:
                    self.numstr = self.numstr[:self.StringLength]
                    return False
        return False

    def Clone(self):
        return Validator_0_100()

    def Validate(self):#1 使用验证器方法
        textCtrl = self.GetWindow()
        text = textCtrl.GetValue()
        try:
            if float(text)<100 and float(text)>0:
                return True
        except:
            pass
        textCtrl.SetValue('')
        self.StringLength = 0
        self.numstr = ''
        return False

    def TransferToWindow(self):
        return True

    def TransferFromWindow(self):
        return True

class NumberValidator(wx.Validator):# 创建验证器子类      
    def __init__(self):
        wx.Validator.__init__(self)
        self.ValidInput = ['.','0','1','2','3','4','5','6','7','8','9']
        self.StringLength = 0
        self.numstr = ''
        self.Bind(wx.EVT_CHAR,self.OnCharChanged)  #  绑定字符输入事件

    def OnCharChanged(self, event):
        keycode = event.GetKeyCode()    # 得到输入字符的 ASCII 码
        if keycode == 8:    # 退格（ASCII 码 为8），删除一个字符。
            if self.StringLength>0:
                self.StringLength -= 1
            self.numstr = self.numstr[:self.StringLength]
            event.Skip()    # 事件继续传递
            return
        
        InputChar = chr(keycode)    # 把 ASII 码 转成字符
        if InputChar in self.ValidInput:
            # 第一个字符为 .,非法，拦截该事件，不会成功输入
            if InputChar == '.' and self.StringLength == 0:
                return False
            else:
                self.numstr = self.numstr + InputChar
                try:
                    # 在允许输入的范围，继续传递该事件。
                    float(self.numstr)  # 通过float是否报错判断
                    event.Skip()
                    self.StringLength += 1
                    return True
                except:
                    self.numstr = self.numstr[:self.StringLength]
                    return False
        return False

    def Clone(self):
        return NumberValidator()

    def Validate(self):#1 使用验证器方法
        textCtrl = self.GetWindow()
        text = textCtrl.GetValue()
        try:
            float(text)
            return True
        except:
            textCtrl.SetValue('')
            self.StringLength = 0
            self.numstr = ''
            return False

    def TransferToWindow(self):
        return True

    def TransferFromWindow(self):
        return True
