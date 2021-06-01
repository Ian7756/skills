from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/param')
def root():
    parameter_dict = request.args.to_dict()
    if len(parameter_dict) == 0:
        return 'No parameter'

    parameters = ''
    for key in parameter_dict.keys():
        parameters += 'key: {}, value: {}\n'.format(key, request.args[key])
    return parameters

if __name__ == "__main__":
    app.run(port=80)