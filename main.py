from src.salaryprediction_mlops.logging import logger
from src.salaryprediction_mlops.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME="Data Ingestion Stage"
try:
    logger.info(f"Starting {STAGE_NAME}")
    Data_Ingestion = DataIngestionTrainingPipeline()
    Data_Ingestion.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    raise e