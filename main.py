from chestCancerClassifier import logger
from chestCancerClassifier.pipeline.stage_01_data_ingestion import \
    DataIngestionTrainingPipeline
from chestCancerClassifier.pipeline.stage_02_prepare_base_model import \
    PrepareBaseModelTrainingPipeline
from chestCancerClassifier.pipeline.stage_03_model_trainer import \
    ModelTrainingPipeline
from chestCancerClassifier.pipeline.stage_04_model_evaluation_with_mlflow import \
    EvaluationPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(
        f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==========x"
    )
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare base model"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(
        f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==========x"
    )
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Training"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(
        f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==========x"
    )
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Evaluation stage"

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
