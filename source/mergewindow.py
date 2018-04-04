import os
import datetime
import wx
# import magic
import gui


class MergeWindow(gui.SummaryFrame):
    def __init__(self, *args, **kwargs):
        gui.SummaryFrame.__init__(self, *args, **kwargs)

    def set_msg(self, message):
        self.text_ctrl_msg.AppendText(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S :: '))
        self.text_ctrl_msg.AppendText(message)
        self.text_ctrl_msg.AppendText("\r\n")

    def do_verify(self, path):
        self.set_msg("start merging...")
        self.set_msg("checking file...")
        if not os.path.isfile(path):
            self.set_msg("ERROR: File not exist!")
            return False

        #f = open(path, 'rb')
        #data = f.read()
        #print(data)

        kind = filetype.guess(path)
        # print(kind.extension)
        print(kind.mime)


    def on_button_select(self, event):
        self.set_msg("select file:")
        filedialog = wx.FileDialog(
            self, "Choose SummaryReport File",
            defaultDir=os.getcwd(),
            defaultFile="",
            # wildcard="*.*",
            wildcard="TXT files (.txt)|*.txt|XLS files (.xls)|*.xls|CSV files (.csv)|*.csv|ALL files (.*)|*.*",
            style=wx.FD_OPEN | wx.FD_CHANGE_DIR | wx.FD_FILE_MUST_EXIST | wx.FD_PREVIEW
        )

        if filedialog.ShowModal() == wx.ID_OK:
            path = filedialog.GetPaths()[0]
            self.set_msg("selected file: %s " % path)
            self.text_ctrl_filepath.SetValue(path)

        filedialog.Destroy()

    def on_button_merge(self, event):
        path = self.text_ctrl_filepath.GetValue()
        # print(magic.from_file(path))