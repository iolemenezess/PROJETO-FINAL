from flask import Blueprint, request, jsonify
from core.aluno.aluno_service import AlunoService
from core.aluno.aluno import Aluno
from core.autenticacao.autenticacao import autenticacao

aluno_service = AlunoService()

aluno_controller = Blueprint('aluno', __name__, url_prefix='/alunos')


# criar decoreitor
@aluno_controller.route('/', methods=['GET'])
@autenticacao
def listar_alunos():
    alunos = aluno_service.listar_alunos()
    return jsonify(alunos)

@aluno_controller.route('/', methods=['POST'])
@autenticacao
def adicinar_aluno():
    dados = request.get_json()
    obj_aluno = Aluno(id=0,nome=dados["nome"], idade=dados["idade"], cpf=dados["cpf"])
    aluno = aluno_service.adicionar_aluno(obj_aluno)
    return jsonify(aluno), 201

@aluno_controller.route('/<int:id>', methods=['GET'])
@autenticacao
def obter_aluno(id):
    aluno = aluno_service.obter_aluno_por_id(id)
    if aluno:
        return jsonify(aluno)
    else:
        return jsonify({"erro": " Aluno não encontrado"}), 404   

@aluno_controller.route('/<int:id>', methods=['DELETE'])
@autenticacao
def remover_aluno(id):
    sucesso = aluno_service.remover_aluno(id)
    return jsonify(sucesso)

@aluno_controller.route('/', methods=['PUT'])
@autenticacao
def atualizar_aluno():
    dados = request.get_json()
    obter_aluno = Aluno(id=dados["id"], nome=dados["nome"], idade=dados["idade"], cpf=dados["cpf"])
    aluno = aluno_service.atualizar_aluno(obter_aluno)
    if aluno:
        return jsonify(aluno)
    else:
        return jsonify({"erro": "Aluno não encontrado"}), 404
    