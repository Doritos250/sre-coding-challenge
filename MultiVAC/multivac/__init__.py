import os
from logging import StreamHandler
from flask import Flask
from flask.ext.rq import RQ
from flask.ext.bootstrap import Bootstrap
from flask.ext.debugtoolbar import DebugToolbarExtension


def create_app(config_object=None, db_name=None):  # pragma: no cover
    app_settings = os.getenv('APP_SETTINGS')
    from dotenv import load_dotenv
    if app_settings:
        load_dotenv(app_settings)
    else:
        load_dotenv('development.env')
    app = Flask(__name__, static_url_path=os.environ.get("STATIC_URL"))
    if config_object is None:
        app.config.from_object('config.BaseConfiguration')
    else:
        app.config.from_object(config_object)
    if not app.logger.handlers:
        stream_handler = StreamHandler()
        app.logger.addHandler(stream_handler)
    if app.debug:
        app.logger.setLevel("DEBUG")
        app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
        app.config["DEBUG_TB_PROFILER_ENABLED"] = \
            os.environ.get("PROFILER", "False") == 'True'
        app.config['RQ_DEFAULT_URL'] = os.environ.get("REDIS_URL")
    else:
        app.logger.setLevel("INFO")
    RQ(app)
    Bootstrap(app)
    DebugToolbarExtension(app)
    from multivac.views import multivac_bp
    app.register_blueprint(multivac_bp)

    return app
