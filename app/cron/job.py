from app.utils.scheduler import scheduler
from app.utils.logger import logger


@scheduler.task('interval', id='test_task_interval', seconds=5)
def test_interval():
    logger.info('TEST INTERVAL EACH 5 SECONDS')


@scheduler.task('cron', id='test_task_cron', second=10)
def test_cron():
    logger.info('TEST CRON IN SECOND 10')
