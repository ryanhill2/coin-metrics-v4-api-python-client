from flask import Flask

from example_app.call_coin_metrics_v4_api import get_coin_metrics_asset_data_service

app = Flask(__name__)


@app.get('/assets_only')
def get_coin_metrics_asset_data():
    return get_coin_metrics_asset_data_service()
