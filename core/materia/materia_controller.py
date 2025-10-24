from flask import Blueprint, request, jsonify
from core.materia.materia_service import MateriaService
from core.materia.materia import Materia
from core.autenticacao.autenticacao import autenticacao

materia_service = MateriaService()

materia_controller = Blueprint('materia', __name__, url_prefix='/materias')


# criar decoreitor
@materia_controller.route('/', methods=['GET'])
@autenticacao
def listar_materias():
    materias = materia_service.listar_materias()
    return jsonify(materias)

@materia_controller.route('/', methods=['POST'])
@autenticacao
def adicinar_materia():
    dados = request.get_json()
    obj_materia = Materia(id=0,nome=dados["nome"], idade=dados["idade"], cpf=dados["cpf"])
    materia = materia_service.adicionar_materia(obj_materia)
    return jsonify(materia), 201

@materia_controller.route('/<int:id>', methods=['GET'])
@autenticacao
def obter_materia(id):
    materia = materia_service.obter_materia_por_id(id)
    if materia:
        return jsonify(materia)
    else:
        return jsonify({"erro": " Professor não encontrado"}), 404   

@professor_controller.route('/<int:id>', methods=['DELETE'])
@autenticacao
def remover_professor(id):
    sucesso = professor_service.remover_professor(id)
    return jsonify(sucesso)

@professor_controller.route('/', methods=['PUT'])
@autenticacao
def atualizar_professor():
    dados = request.get_json()
    obter_professor = Professor(id=dados["id"], nome=dados["nome"], idade=dados["idade"], cpf=dados["cpf"])
    professor = professor_service.atualizar_professor(obter_professor)
    if professor:
        return jsonify(professor)
    else:
        return jsonify({"erro": "Professor não encontrado"}), 404
    