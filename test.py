from kaggle.api.kaggle_api_extended import KaggleApi

# Instantiate the Kaggle API
api = KaggleApi()

# Test API authentication
try:
    api.authenticate()
    print("API authentication successful!")
except Exception as e:
    print("API authentication failed:", str(e))
