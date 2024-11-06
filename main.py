from TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.logging import logger


STAGE_NAME = "data_ingestion_stage"
try:
    logger.info(f">>> Stage {STAGE_NAME} started <<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>> Stage {STAGE_NAME} completed <<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e