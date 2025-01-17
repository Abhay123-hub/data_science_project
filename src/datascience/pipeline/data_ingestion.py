from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_ingestion import DataIngestion

from src.datascience import logger
STAGE_NAME = "DATA INGESTION"

class DataIngestionTrainingPipeLine:
    def __init__(self):
        pass
    def initiate_data_ingestion(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


## now doing execution of my code
if __name__ == "__main__":
    try:
        logger.info(f">>>> {STAGE_NAME} started <<<<<")
        obj = DataIngestionTrainingPipeLine()
        obj.initiate_data_ingestion()
        logger.info(f">>> Stage {STAGE_NAME} completed")
    except Exception as e:
        raise e