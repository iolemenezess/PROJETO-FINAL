import base64
from functools import wraps
from flask import request, jsonify

from core.usuario.usuario_service import UsuarioService

def autenticacao(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers.get("Authorization")

        if not auth or not auth.startswith("Basic "):
            return jsonify({"erro": "Credenciais ausentes"}), 401

        # Remove o prefixo "Basic "
        token = auth.split(" ")[1]
        try:
            # Decodifica Base64 usuario:senha
            decoded = base64.b64decode(token).decode("utf-8")
            usuario, senha = decoded.split(":")
        except Exception:
            return jsonify({"erro": "Credenciais inválidas"}), 401

        # Verifica o usuário cadastrado no banco de dados e suas credenciais de acesso
        service = UsuarioService()
        user = service.obter_usuario_por_usuario_senha(usuario, senha)
        if (
            not user
            or user["senha"] != senha
            or not user["ativo"]
            or user["usuario"] != usuario
        ):
            return jsonify({"erro": "Usuário ou senha inválidos"}), 401

        return f(*args, **kwargs)

    return decorated