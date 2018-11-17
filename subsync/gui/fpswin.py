import gui.fpswin_layout
import wx


class FpsWin(gui.fpswin_layout.FpsWin):
    def __init__(self, parent, subFps=None, refFps=None):
        gui.fpswin_layout.FpsWin.__init__(self, parent)

        self.subFps = subFps
        self.refFps = refFps

        if refFps:
            self.appendFpsToLabel(self.m_radioRef, refFps)
        else:
            self.m_radioRef.Disable()

        if subFps:
            self.appendFpsToLabel(self.m_radioSub, subFps)
        else:
            self.m_radioSub.Disable()

        if refFps:
            self.m_radioRef.SetValue(True)
            self.onRadioRefClick(None)
        elif subFps:
            self.m_radioSub.SetValue(True)
            self.onRadioSubClick(None)
        else:
            self.m_radioCustom.SetValue(True)
            self.m_comboFps.SetValue(23.976)
            self.onRadioCustomClick(None)

        self.Fit()
        self.Layout()

    def getFps(self):
        return self.m_comboFps.GetValue()

    def appendFpsToLabel(self, obj, fps):
        obj.SetLabel('{}: {:.3f} {}'.format(obj.GetLabel(), fps, _('fps')))

    def onRadioRefClick(self, event):
        self.m_comboFps.SetValue(self.refFps)
        self.m_comboFps.SetFocus()

    def onRadioSubClick(self, event):
        self.m_comboFps.SetValue(self.subFps)
        self.m_comboFps.SetFocus()

    def onRadioCustomClick(self, event):
        self.m_comboFps.SetFocus()

    def onComboFpsClick(self, event):
        self.m_radioCustom.SetValue(True)
