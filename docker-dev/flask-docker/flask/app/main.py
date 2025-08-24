# @Author: @iamrezamousavi
# @Date:   2023-02-26 20:02:00
# @Last Modified by:   @iamrezamousavi
# @Last Modified time: 2023-02-26 20:06:19

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'HELLO MY FRIEND'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
