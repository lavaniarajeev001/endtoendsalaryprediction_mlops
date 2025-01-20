import os
import sys
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s]: %(message)s"
)

project_name="salaryprediction_mlops"

list_of_file=[
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/data_validation.py",
    f"src/{project_name}/components/model_evaluation.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/stage_01_data_ingestion.py",
    f"src/{project_name}/pipeline/stage_02_data_validation.py",
    f"src/{project_name}/pipeline/stage_03_data_transformation.py",
    f"src/{project_name}/pipeline/stage_04_model_trainer.py",
    f"src/{project_name}/pipeline/stage_05_model_evaluation.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    "config/config.yaml",
    "research/trial.ipynb",
    "research/1.data_ingestion.ipynb",
    "research/2.data_validation.ipynb",
    "research/3.data_transformation.ipynb",
    "research/4.model_trainer.ipynb",
    "research/4.model_evaluation.ipynb",
    "templates/index.html",
    "templates/results.html",
    "Dockerfile",
    "app.py",
    "dvc.yaml",
    "main.py",
    "params.yaml",
    "requirements.txt",
    "schema.yaml",
    "setup.py"  
]

for filepath in list_of_file:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating the file {filedir} with name {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w"):
            pass
        logging.info(f"created empty file {filename}")
    else:
        logging.info(f"{filename} already exists")
    
                     
