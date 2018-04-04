import wx
import gui
import mergewindow


class MainWindow(gui.MainFrame):
    def __init__(self, *args, **kwargs):
        gui.MainFrame.__init__(self, *args, **kwargs)
        pass

    def __set_gui_properties(self):
        pass

    def on_menu_exit(self, event):
        self.Destroy()

    def on_menu_mergesummaryreport(self, event):
        mergewindow.MergeWindow(self, wx.ID_ANY, "").Show()



