from src.datascience import logger
from src.datascience.pipeline.data_ingestion import DataIngestionTrainingPipeLine 

logger.info("Welcome to our custom logging data science ")
STAGE_NAME = "DATA INGESTION"


## now doing execution of my code
if __name__ == "__main__":
    try:
        logger.info(f">>>> {STAGE_NAME} started <<<<<")
        obj = DataIngestionTrainingPipeLine()
        obj.initiate_data_ingestion()
        logger.info(f">>> Stage {STAGE_NAME} completed")
    except Exception as e:
        raise e


