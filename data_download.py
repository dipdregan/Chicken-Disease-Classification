import os,sys
from kaggle.api.kaggle_api_extended import KaggleApi

def download_dataset(dataset_slug, save_directory):
    """
    Download a dataset from Kaggle to the specified directory.
    """
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(dataset=dataset_slug, path=save_directory, unzip=True)
    print("Download complete.")

# Example usage
dataset_slug = "kaggle competitions download -c house-prices-advanced-regression-techniques"  # Replace with the correct dataset slug
save_directory = os.getcwd()  # Replace with the desired save directory

# Download the dataset
download_dataset(dataset_slug, save_directory)
