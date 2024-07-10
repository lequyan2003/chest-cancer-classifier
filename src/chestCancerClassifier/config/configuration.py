import os
import shutil
from pathlib import Path

from chestCancerClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from chestCancerClassifier.entity.config_entity import (DataIngestionConfig,
                                                        EvaluationConfig,
                                                        PrepareBaseModelConfig,
                                                        TrainingConfig)
from chestCancerClassifier.utils.common import create_directories, read_yaml


class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config

    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model

        create_directories([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
        )

        return prepare_base_model_config

    def copy_relevant_classes(self, src_dir, dest_dir, classes):
        """
        Copy only the relevant classes from the source directory to the
                                                    destination directory.

        Parameters:
        src_dir (str): Source directory containing the full dataset.
        dest_dir (str): Destination directory to contain only the relevant
                                                                    classes.
        classes (list): List of class names to be copied.
        """
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        for class_name in classes:
            src_class_dir = os.path.join(src_dir, class_name)
            dest_class_dir = os.path.join(dest_dir, class_name)

            if not os.path.exists(dest_class_dir):
                os.makedirs(dest_class_dir)

            # Copy all files from the source class directory to the destination
            # class directory
            for filename in os.listdir(src_class_dir):
                src_file = os.path.join(src_class_dir, filename)
                dest_file = os.path.join(dest_class_dir, filename)
                shutil.copyfile(src_file, dest_file)

    def get_training_config(self) -> TrainingConfig:
        training = self.config.training
        prepare_base_model = self.config.prepare_base_model
        params = self.params

        # Define source and destination directories
        src_dir = os.path.join(
            self.config.data_ingestion.unzip_dir, "Data", "test"
        )
        dest_dir = os.path.join(
            self.config.data_ingestion.unzip_dir, "Data", "new"
        )

        # List of relevant classes
        relevant_classes = ['adenocarcinoma', 'normal']

        # Copy relevant classes
        self.copy_relevant_classes(src_dir, dest_dir, relevant_classes)

        print("Relevant classes copied successfully!")

        training_data = dest_dir
        create_directories([
            Path(training.root_dir)
        ])

        training_config = TrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            updated_base_model_path=Path(
                prepare_base_model.updated_base_model_path
            ),
            training_data=Path(training_data),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE,
        )

        return training_config

    def get_evaluation_config(self) -> EvaluationConfig:
        eval_config = EvaluationConfig(
            path_of_model="artifacts/training/model.h5",
            training_data="artifacts/data_ingestion/Data/new",
            mlflow_uri=(
                "https://dagshub.com/lequyan2003/"
                "chest-cancer-classifier.mlflow"
            ),
            all_params=self.params,
            params_image_size=self.params.IMAGE_SIZE,
            params_batch_size=self.params.BATCH_SIZE
        )

        return eval_config
