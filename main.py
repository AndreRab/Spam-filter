from application import Application
from model_manager import ModelManager
from model import LM

model = ModelManager()
app = Application(model)
app.start()