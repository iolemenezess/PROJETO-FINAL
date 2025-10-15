from flask import Flask
from core.aluno.aluno_controller import aluno_controller


app = Flask(__name__)


#registro das controllers
app.register_blueprint(aluno_controller)


if __name__=="__main__":
    app.run(debug=True)
