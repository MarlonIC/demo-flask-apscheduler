from flask import Flask
from app.utils.scheduler import scheduler


def create_app():
    app = Flask(__name__)

    from .cron import job
    try:
        scheduler.init_app(app)
        scheduler.start()
        scheduler.api_enabled = True
    except Exception as error:
        print(error)
    return app


api = create_app()
if __name__ == '__main__':
    api.run()
