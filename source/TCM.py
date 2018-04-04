import wx
import mainwindow


class TCM(wx.App):
    def OnInit(self):
        self.mainw = mainwindow.MainWindow(None, wx.ID_ANY, "")
        self.mainw.Show()
        return True


if __name__ == "__main__":
    app = TCM(0)
    app.MainLoop()
