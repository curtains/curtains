import ct

app = ct.Application()
win = ct.Window(size=(1024, 768))
win.show()
win.attach('resized', print, ("Window resized", "size"), None)
#win.detach('resized', print)
win.size = (500, 400)
app.main_loop()
