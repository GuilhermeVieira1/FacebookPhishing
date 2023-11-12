from flask import Flask, request
import sendEmail

app = Flask(__name__)

@app.route('/enviar', methods=['POST'])
def enviar_email_formulario():
    # Obtenha os dados do formulário
    usuario = request.form['usuario']
    senha = request.form['senha']
    # Outros dados...

    # Chame sua função de envio de e-mail
    sendEmail.enviar_email(usuario, senha)

    # Retorne uma resposta para o cliente, se necessário
    return 'E-mail enviado com sucesso!'

if __name__ == '__main__':
    app.run(debug=True)