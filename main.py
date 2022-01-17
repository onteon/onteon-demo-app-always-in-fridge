import argparse
import logging

from flask import Flask, jsonify

api = Flask(__name__)


@api.route('/isAlive', methods=['GET'])
def is_alive():
    return ""


@api.route('/api/v1/items/', methods=['GET'])
def get_items():
    response = [
        {"name": "Milk", "category": "Milk", "amount": 300, "unit": "ml"},
        {"name": "Ham", "category": "Meat", "amount": 200, "unit": "g"},
        {"name": "Cheese", "category": "Cheese", "amount": 200, "unit": "g"},
    ]
    return jsonify(response)


def main():
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument('--port', default=5000, type=int)
    arg_parser.add_argument('--log_dir', default=".", type=str)

    args = arg_parser.parse_args()
    port = args.port
    log_dir = args.log_dir

    print("Starting...")
    init_logging(log_dir)
    print("Application started.")
    api.run(port=port)


def init_logging(log_dir):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(f"{log_dir}/log.json")
    stream_handler = logging.StreamHandler()

    stream_formatter = logging.Formatter('%(asctime)-15s %(levelname)-8s %(message)s')
    file_formatter = logging.Formatter(
        fmt="{'@timestamp':'%(created)s', 'logger_name': '%(name)s', 'thread_name': '%(threadName)s', 'level': '%(levelname)s', 'message': '%(message)s'}"
    )

    file_handler.setFormatter(file_formatter)
    stream_handler.setFormatter(stream_formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)


if __name__ == '__main__':
    main()
