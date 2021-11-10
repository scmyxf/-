# -*- coding: utf-8 -*-
###########################################################################
## Python code generated with wxFormBuilder (version 3.10.0-4761b0c)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from need.common import Validator_0_100,NumberValidator

###########################################################################
## Class CalFrame
###########################################################################

class CalFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"招标代理服务费计算", pos = wx.DefaultPosition, size = wx.Size( 528,549 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"招标代理服务费计算", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText1.Wrap( -1 )

        self.m_staticText1.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体" ) )
        self.m_staticText1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"第一步：项目属性", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        self.m_staticText2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

        bSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.EXPAND, 5 )

        gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"项目名称", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        bSizer3.Add( self.m_staticText3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
        bSizer3.Add( self.m_textCtrl1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


        gSizer1.Add( bSizer3, 1, wx.ALIGN_CENTER, 5 )

        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"项目类型", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        bSizer4.Add( self.m_staticText4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        m_comboBox1Choices = [ u"货物招标", u"服务招标", u"工程招标" ]
        self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, u"服务招标", wx.DefaultPosition, wx.Size( 90,-1 ), m_comboBox1Choices, wx.CB_READONLY )
        self.m_comboBox1.SetSelection( 1 )
        bSizer4.Add( self.m_comboBox1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.m_button7 = wx.Button( self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        bSizer4.Add( self.m_button7, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


        gSizer1.Add( bSizer4, 1, wx.ALIGN_CENTER, 5 )


        bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )

        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"第二步：数据计算", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )

        self.m_staticText6.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

        bSizer1.Add( self.m_staticText6, 0, wx.ALL|wx.EXPAND, 5 )

        fgSizer1 = wx.FlexGridSizer( 0, 3, 0, 15 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"项目造价", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        bSizer5.Add( self.m_staticText7, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, "", wx.DefaultPosition, wx.Size( 90,-1 ), style=wx.TE_PROCESS_ENTER,validator=NumberValidator())
        bSizer5.Add( self.m_textCtrl2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"万元", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )

        bSizer5.Add( self.m_staticText12, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


        fgSizer1.Add( bSizer5, 1, wx.FIXED_MINSIZE, 5 )

        self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"按标准计算：0.00元", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )

        self.m_staticText10.SetMinSize( wx.Size( 150,-1 ) )

        fgSizer1.Add( self.m_staticText10, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.m_button2 = wx.Button( self, wx.ID_ANY, u"新开项目", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.m_button2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"折扣率", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        bSizer6.Add( self.m_staticText8, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, u"90", wx.DefaultPosition, wx.Size( 35,-1 ), style=wx.TE_PROCESS_ENTER,validator=Validator_0_100())
        bSizer6.Add( self.m_textCtrl3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"%", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )

        bSizer6.Add( self.m_staticText9, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"计算", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        bSizer6.Add( self.m_button1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


        fgSizer1.Add( bSizer6, 1, wx.FIXED_MINSIZE, 5 )

        self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"折扣后收费：0.00元", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )

        self.m_staticText11.SetMinSize( wx.Size( 150,-1 ) )

        fgSizer1.Add( self.m_staticText11, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.m_button3 = wx.Button( self, wx.ID_ANY, u"保存项目", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.m_button3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


        bSizer1.Add( fgSizer1, 1, wx.EXPAND, 5 )

        self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"第三步：汇总及报表", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )

        self.m_staticText13.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

        bSizer1.Add( self.m_staticText13, 0, wx.ALL|wx.EXPAND, 5 )

        gbSizer1 = wx.GridBagSizer( 0, 5 )
        gbSizer1.SetFlexibleDirection( wx.BOTH )
        gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        bSizer9 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"计算项目表", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText14.Wrap( -1 )

        self.m_staticText14.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )

        bSizer9.Add( self.m_staticText14, 0, wx.ALL|wx.EXPAND, 5 )

        m_listBox2Choices = []
        self.m_listBox2 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 258,168 ), m_listBox2Choices, wx.LB_HSCROLL|wx.LB_MULTIPLE )
        bSizer9.Add( self.m_listBox2, 0, wx.ALL, 5 )


        gbSizer1.Add( bSizer9, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        bSizer10 = wx.BoxSizer( wx.VERTICAL )

        gSizer4 = wx.GridSizer( 0, 2, 0, 0 )

        self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"计算结果报表", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText15.Wrap( -1 )

        self.m_staticText15.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )

        gSizer4.Add( self.m_staticText15, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        bSizer111 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button6 = wx.Button( self, wx.ID_ANY, u"复制", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
        bSizer111.Add( self.m_button6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.m_button8 = wx.Button( self, wx.ID_ANY, u"清空", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
        bSizer111.Add( self.m_button8, 0, wx.ALL, 5 )


        gSizer4.Add( bSizer111, 1, wx.EXPAND, 5 )


        bSizer10.Add( gSizer4, 1, wx.EXPAND, 5 )

        self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, u"项目招标代理服务费计算表\n==================\n", wx.DefaultPosition, wx.Size( 219,233 ), wx.TE_MULTILINE|wx.TE_READONLY|wx.VSCROLL )
        bSizer10.Add( self.m_textCtrl4, 0, wx.ALL|wx.EXPAND, 5 )


        gbSizer1.Add( bSizer10, wx.GBPosition( 0, 1 ), wx.GBSpan( 2, 1 ), wx.EXPAND, 5 )

        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"总折扣", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )

        bSizer12.Add( self.m_staticText16, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, u"90", wx.DefaultPosition, wx.Size( 35,-1 ), style=wx.TE_PROCESS_ENTER,validator=Validator_0_100())
        bSizer12.Add( self.m_textCtrl5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"%", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText17.Wrap( -1 )

        bSizer12.Add( self.m_staticText17, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


        gSizer3.Add( bSizer12, 1, wx.FIXED_MINSIZE, 5 )

        bSizer121 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button4 = wx.Button( self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        bSizer121.Add( self.m_button4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.m_button5 = wx.Button( self, wx.ID_ANY, u"报表", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        bSizer121.Add( self.m_button5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


        gSizer3.Add( bSizer121, 1, wx.EXPAND, 5 )


        bSizer11.Add( gSizer3, 1, wx.EXPAND, 5 )

        self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"总价：0.00元", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText18.Wrap( -1 )

        bSizer11.Add( self.m_staticText18, 0, wx.ALL|wx.EXPAND, 5 )


        gbSizer1.Add( bSizer11, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )


        bSizer1.Add( gbSizer1, 1, wx.EXPAND, 5 )

        self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"根据《招标代理服务收费管理暂行办法》计价格[2002]1980 和 发改价格[2011]534号 计算", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText19.Wrap( -1 )

        self.m_staticText19.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

        bSizer1.Add( self.m_staticText19, 0, wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button7.Bind( wx.EVT_BUTTON, self.OnExit )
        self.m_textCtrl2.Bind( wx.EVT_TEXT_ENTER, self.OnGoalEnter )
        self.m_button2.Bind( wx.EVT_BUTTON, self.OnNewClick )
        self.m_textCtrl3.Bind( wx.EVT_TEXT_ENTER, self.OnDiscountEnter )
        self.m_button1.Bind( wx.EVT_BUTTON, self.OnCalClick )
        self.m_button3.Bind( wx.EVT_BUTTON, self.OnSaveClick )
        self.m_listBox2.Bind( wx.EVT_LISTBOX, self.OnListClick )
        self.m_button6.Bind( wx.EVT_BUTTON, self.OnCopyClick )
        self.m_button8.Bind( wx.EVT_BUTTON, self.OnClearClick )
        self.m_textCtrl5.Bind( wx.EVT_TEXT_ENTER, self.OnSumDiscountEnter )
        self.m_button4.Bind( wx.EVT_BUTTON, self.OnDeleteClick )
        self.m_button5.Bind( wx.EVT_BUTTON, self.OnOutputClick )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnExit( self, event ):
        event.Skip()

    def OnGoalEnter( self, event ):
        event.Skip()

    def OnNewClick( self, event ):
        event.Skip()

    def OnDiscountEnter( self, event ):
        event.Skip()

    def OnCalClick( self, event ):
        event.Skip()

    def OnSaveClick( self, event ):
        event.Skip()

    def OnListClick( self, event ):
        event.Skip()

    def OnCopyClick( self, event ):
        event.Skip()

    def OnClearClick( self, event ):
        event.Skip()

    def OnSumDiscountEnter( self, event ):
        event.Skip()

    def OnDeleteClick( self, event ):
        event.Skip()

    def OnOutputClick( self, event ):
        event.Skip()


