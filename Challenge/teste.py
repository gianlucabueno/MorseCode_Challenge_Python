from flask import Flask,request
import morse
import re 
pattern = "^[A-Za-z0-9]*$"

# create the Flask app
app = Flask(__name__)

@app.route('/',methods=['POST'])
def translateMorseCode():
    try:
        message = request.args.get('messagem')
        state = bool(re.findall(pattern, message)) 
        print(state)
        if state == False:
            valor = morse.decrypt(message)
            return "{}".format(valor)
        else:
            valor = morse.encrypt(message.upper())
            string = "INPUT: {} \n".format(message)
            string += "OUTPUT: {}".format(valor)
            return string
    except:
        return "Erro na inseção de dados"
        

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)