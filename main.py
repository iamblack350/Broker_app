from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    app.register_blueprint()
    app.register_blueprint()
    app.register_blueprint()

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host = "0.0.0.0", debug=True)
