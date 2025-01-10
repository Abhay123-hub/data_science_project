from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_evaluation import ModelEvaluation
import os

from src.datascience import logger
STAGE_NAME = "MODEL EVALUATION"

os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/rajputjiabhay3002/data_science_project.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "rajputjiabhay3002"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "dd0e974ea15bb466fff31d13a07eddd4b98b86db"

class ModelEvaluationPipeLine:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        model_eval_config = config.get_model_evaluation_config()
        model_eval = ModelEvaluation(config = model_eval_config)
        model_eval.log_into_mlflow()
    
