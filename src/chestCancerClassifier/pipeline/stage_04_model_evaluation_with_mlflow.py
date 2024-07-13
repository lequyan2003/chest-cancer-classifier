import os

from chestCancerClassifier import logger
from chestCancerClassifier.components.model_evaluation_with_mlflow import \
    Evaluation
from chestCancerClassifier.config.configuration import ConfigurationManager

STAGE_NAME = "Evaluation stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        # evaluation.log_into_mlflow()


if __name__ == "__main__":
    os.environ["repo_owner"] = "lequyan2003"
    os.environ["repo_name"] = "chest-cancer-classifier"
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(
            f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==========x"
        )
    except Exception as e:
        logger.exception(e)
        raise e
