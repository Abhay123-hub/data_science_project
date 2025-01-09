from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_validation import DataValidation

from src.datascience import logger
STAGE_NAME = "DATA VALIDATION"

class DataValidationTrainingPipeLine:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_validation_data_config() ## get_validation_data_config
        data_validation = DataValidation(config = data_validation_config)
        data_validation.validate_all_columns()
## execution of the code
if __name__ == "__main__":
    try:
        logger.info(f">>> stage {STAGE_NAME} started <<<<")
        obj = DataValidationTrainingPipeLine()
        obj.main()
        logger.info(f"stage {STAGE_NAME} completed <<<<")
    except Exception as e:
        logger.excpetion(e)
        raise e