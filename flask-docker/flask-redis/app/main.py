from redis import Redis

from flask import Flask

app = Flask(__name__)
r = Redis(host='redis', port=6379)


@app.route('/')
def say_hello() -> str:
    name = r.get('name').decode()
    return f'Hello {name}\n'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
