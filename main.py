from src.datascience import logger
from src.datascience.pipeline.data_ingestion import DataIngestionTrainingPipeLine 
from src.datascience.pipeline.data_validation import DataValidationTrainingPipeLine
from src.datascience.pipeline.data_transformation import DataTransformationTrainingPipeLine
from src.datascience.pipeline.model_trainer import ModelTrainerTrainingPipeLine
from src.datascience.pipeline.model_evaluation import ModelEvaluationPipeLine
import os
logger.info("Welcome to our custom logging data science ")
STAGE_NAME = "DATA INGESTION"
STAGE_NAME_VALIDATION = "DATA VALIDATION"
STAGE_NAME_TRANSFORMATION= "DATA TRANSFORMATION"
STAGE_NAME_TRAINER = "MODEL TRAINER"
STAGE_NAME_EVALUATION = "MODEL EVALUATION"


## now doing execution of my code
if __name__ == "__main__":
    try:
        logger.info(f">>>> {STAGE_NAME_VALIDATION} started <<<<<")
        obj = DataValidationTrainingPipeLine()
        obj.main()
        logger.info(f">>> Stage {STAGE_NAME_VALIDATION} completed")
    except Exception as e:
        raise e

if __name__ == "__main__":
    try:
        logger.info(f">>> stage {STAGE_NAME_TRANSFORMATION} started <<< ")
        obj = DataTransformationTrainingPipeLine()
        obj.initiate_data_transformation()
        logger.info(f">> stage {STAGE_NAME_TRANSFORMATION} completed")
    except Exception as e:
        raise e

if __name__ == "__main__":
    try:
        logger.info(f">>> stage {STAGE_NAME_TRAINER} started <<<")
        obj = ModelTrainerTrainingPipeLine()
        obj.main()
        logger.info(f">>stage {STAGE_NAME_TRAINER} completed <<<")
    except Exception as e:
        raise e
if __name__ == "__main__":
    try: 
        logger.info(f">>> stage {STAGE_NAME} started <<<< ")
        obj = ModelEvaluationPipeLine()
        obj.main()
        logger.info(f">> stage {STAGE_NAME} completed <<<")
    except Exception as e:
        raise e





