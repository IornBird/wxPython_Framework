import wx
import threading


class MainFrame(wx.Frame):
    def __init__(self, title: str, size):
        super().__init__(parent=None, id=wx.ID_ANY, title=title, size=size)
        self.mutex = threading.Lock()
        self.processing = False
        self.closeReq = False
        # place elements here
        self.CreateControls()
        self.Bind(wx.EVT_CLOSE, self.OnClose)

    # private
    def CreateControls(self):
        """
        how elements placed
		example:
            panel = wx.Panel(self)
            sizer = wx.BoxSizer()
            child = wx.Panel(panel)
            [optional] child.Bind(wx.EVT, self.Function)
            [optional] child.SetBackgroundColour(wx.BLACK)

            sizer.Add(child [, 1, wx.EXPAND | wx.ALL, 5])
            panel.SetSizerAndFit(sizer)
        """
        return

    def DoBackgroundProcess(self):
        wx.CallAfter(self.BGProcess)

    def BGProcess(self):
        self.mutex.acquire()
        try:
            if not self.processing: return
            # all GUI changes must be in main thread
        except:
            pass
        self.mutex.release()

    """
    how events handled, and call algorithms in event handler
	examples:
    def OnButtonClicked(self, evt):
        if self.processing: return
        bck = threading.Thread(target=self.buttonJob)
        bck.start()
        bck.join()

    def buttonJob(self):
        if self.processing: return
        self.processing = True
        try:
            # code that ran in another thread
            pass
        except:
            pass
        self.processing = False
    """

    def OnClose(self, closeEvt):
        if self.processing:
            closeEvt.Veto()
            self.closeReq = True
        else:
            self.Destroy()

    def loadFile(self, mess="OpenFile") -> str:
        fd = wx.FileDialog(self, mess, "", "", "All files(*.*)|*.*"
                           , wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if fd.ShowModal() == wx.CANCEL:
            return ""
        return fd.GetPath()

    def saveFile(self, mess="Save as") -> str:
        fd = wx.FileDialog(self, mess, "", "", "All files(*.*)|*.*"
                           , wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if fd.ShowModal() == wx.CANCEL:
            return ""
        return fd.GetPath()
