import os
import datetime
import wx
import magic
import gui


class MergeWindow(gui.SummaryFrame):
    def __init__(self, *args, **kwargs):
        gui.SummaryFrame.__init__(self, *args, **kwargs)

    def set_msg(self, message):
        self.text_ctrl_msg.AppendText(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S :: '))
        self.text_ctrl_msg.AppendText(message)
        self.text_ctrl_msg.AppendText("\r")

    def do_verify(self, path):
        self.set_msg("start merging...")
        self.set_msg("checking file...")
        if os.path.isfile(path):
            self.set_msg("INF: Verify file path done.")
        else:
            self.set_msg("ERR: File not exist!")
            return False

        if "ASCII text" in magic.from_file(path):
            self.set_msg("INF: Verify file type done.")
        else:
            self.set_msg("ERR: File type invalid. (Current: %s)" % magic.from_file(path))
            return False

        return True

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
        if not self.do_verify(path):
            self.set_msg("ERR: File verify failed.")
            return

        f = open(path, 'r')
        fn = f.readline()
        if "Incident #" in fn:
            fieldname = fn.split("\t")
            self.set_msg("INF: Field Name model created with %d items" % len(fieldname))
        else:
            self.set_msg("ERR: File format invalid, missing FIELD NAME in first line.")
            f.close()
            return

        a = 0

        for fc in f.readlines():
            fieldvalue = fc.split("\t")
            self.set_msg("DBG: Line split to %d strings" % len(fieldvalue))


