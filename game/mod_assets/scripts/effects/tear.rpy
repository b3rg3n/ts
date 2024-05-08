# ПЕРЕДЕЛАННЫЙ ЭФФЕКТ ГЛИТЧА ИЗ ОРИГ ДОКИ
# ТЕПЕРЬ КРАШИТЬ НЕ ДОЛЖЕН
# Since 2024
screen ts_tears(number=10, offtimeMult=1, ontimeMult=1, offsetMin=0, offsetMax=50, srf=None):
    zorder 150
    add tsTear(number, offtimeMult, ontimeMult, offsetMin, offsetMax, srf) size (config.screen_width,config.screen_height)
    on "show" action Function(hide_windows_enabled, enabled=False)
    on "hide" action Function(hide_windows_enabled, enabled=True)


init 4 python:

    class tsTearPiece:
        def __init__(self, startY, endY, offtimeMult, ontimeMult, offsetMin, offsetMax):
            self.startY = startY
            self.endY = endY
            self.offTime = (random.random() * 0.2 + 0.2) * offtimeMult
            self.onTime = (random.random() * 0.2 + 0.2) * ontimeMult
            self.offset = 0
            self.offsetMin = offsetMin
            self.offsetMax = offsetMax
        
        def update(self, st):
            st = st % (self.offTime + self.onTime)
            if st > self.offTime and self.offset == 0:
                self.offset = random.randint(self.offsetMin, self.offsetMax)
            elif st <= self.offTime and self.offset != 0:
                self.offset = 0

    class tsTear(renpy.Displayable):
        def __init__(self, number, offtimeMult, ontimeMult, offsetMin, offsetMax, srf=None):
            super(tsTear, self).__init__()
            self.width, self.height = renpy.get_physical_size()
            if float(self.width) / float(self.height) > 16.0/9.0:
                self.width = self.height * 16 / 9
            else:
                self.height = self.width * 9 / 16
            self.number = number
            if not srf: self.srf = screenshot_srf()
            else: self.srf = srf
            self.pieces = []
            tearpoints = [0, self.height]
            for i in range(number):
                tearpoints.append(random.randint(10, self.height - 10))
            tearpoints.sort()
            for i in range(number+1):
                self.pieces.append(tsTearPiece(tearpoints[i], tearpoints[i+1], offtimeMult, ontimeMult, offsetMin, offsetMax))
        
        def render(self, width, height, st, at):
            render = renpy.Render(self.width, self.height)
            render.blit(self.srf, (0,0))
            for piece in self.pieces:
                piece.update(st)
                subsrf = self.srf.subsurface((0, max(0, piece.startY - 1), self.width, max(0, piece.endY - piece.startY)))
                render.blit(subsrf, (piece.offset, piece.startY))
            renpy.redraw(self, 0)
            return render

    def screenshot_srf():
        srf = renpy.display.draw.screenshot(None)
        
        return srf

    def hide_windows_enabled(enabled=True):
        global _windows_hidden
        _windows_hidden = not enabled