from flask import Flask
from core.aluno.aluno_controller import aluno_controller
from core.usuario.usuario_controller import usuario_controller


app = Flask(__name__)


#registro das controllers
app.register_blueprint(aluno_controller)
app.register_blueprint(usuario_controller)


if __name__=="__main__":
    app.run(debug=True)
