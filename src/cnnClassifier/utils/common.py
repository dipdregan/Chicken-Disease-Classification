import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotation
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotation
def read_yaml(path_to_yaml: Path)->ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file :{path_to_yaml } loaded successfully !")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError('yaml file is empty') 
    except Exception as e:
        raise e
    
@ensure_annotation
def create_directories(path_to_directories: list, verbose =True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok= True)
        if verbose:
            logger.info(f"create directory at : {path}")

@ensure_annotation
def save_json(path: Path, data:dict):
    with open(path, "w") as f:
        json.dump(data,f,indent= 4)

    logger.info(f"json file saved at : {path}")

@ensure_annotation
def load_json(path:Path) ->ConfigBox:
    with open(path) as f:
        content = json.load(f)
    
    logger.info(f"json file loaded successfully from :{path}")
    return ConfigBox(content)

@ ensure_annotation
def save_bin(data:Any, path:Path):
    joblib.dump(value=data,filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotation
def load_bin(path : Path)-> Any:
    data = joblib.load(path)
    logger.info(f"Binary file loaded from : {path}")

@ensure_annotation
def get_size(path: Path) ->str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb}"

def decodeImage(imgstring,fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath,'rb') as f:
        return base64.b64encode(f.read())