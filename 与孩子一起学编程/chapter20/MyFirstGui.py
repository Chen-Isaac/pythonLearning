from PythonCard import model
#import PythonCard
class MainWindow(model.Background):
    pass

app = model.Application(MainWindow)
app.MainLoop()
