from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from app.crawler import crawler

schedule = BlockingScheduler()


schedule.add_job(crawler, 'interval', id='ntd_swtch_crw', minutes=3, jitter=60)


schedule.start()