from src.datascience import logger
from src.datascience.pipeline.data_ingestion import DataIngestionTrainingPipeLine 
from src.datascience.pipeline.data_validation import DataValidationTrainingPipeLine

logger.info("Welcome to our custom logging data science ")
STAGE_NAME = "DATA INGESTION"
STAGE_NAME = "DATA VALIDATION"


## now doing execution of my code
if __name__ == "__main__":
    try:
        logger.info(f">>>> {STAGE_NAME} started <<<<<")
        obj = DataValidationTrainingPipeLine()
        obj.main()
        logger.info(f">>> Stage {STAGE_NAME} completed")
    except Exception as e:
        raise e


