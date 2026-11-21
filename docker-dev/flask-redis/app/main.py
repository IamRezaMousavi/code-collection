from http import HTTPStatus
from typing import Any

from flask import Flask, Response, jsonify, request
from redis import Redis

app = Flask(__name__)
redis_client = Redis(host='redis', port=6379, decode_responses=True)


@app.get('/')
def say_hello() -> str:
    name = redis_client.get('name') or 'World'
    return f'Hello {name}\n'


@app.post('/name')
def set_name() -> tuple[Response, int]:
    data: dict[str, Any] | None = request.get_json(silent=True)
    if data is None:
        return jsonify({'error': 'A valid name is required'}), HTTPStatus.BAD_REQUEST

    name = data.get('name')
    if name is None:
        return jsonify({'error': 'A valid name is required'}), HTTPStatus.BAD_REQUEST

    redis_client.set('name', str(name))
    return (
        jsonify(
            {
                'message': 'Name updated successfully',
                'name': name,
            }
        ),
        HTTPStatus.OK,
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
