from coinmetrics.api_client import CoinMetricsClient
from flask import Flask

app = Flask(__name__)
client = CoinMetricsClient()

# or to use community API:
client = CoinMetricsClient().catalog_assets()


def get_coin_metrics_asset_data_service():
    list_of_assets = []

    for asset in client:
        list_of_assets.append(asset.get('asset'))
    return list_of_assets
