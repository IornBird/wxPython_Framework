from MainFrame import *

if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame("Title", (800, 600))
    frame.Show()
    app.MainLoop()
