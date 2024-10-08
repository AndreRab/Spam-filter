from application import Application
from model import load_model, LM

model = load_model()
app = Application(model)
app.start()