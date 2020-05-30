from whatsapp_framework import whatsapp_debt_framework
import schedule
import time

# pip install scheduler

TARGETS = {'GAGAN-DEV': 10} # yep it is that easy, format the debtor and the value here and run!


def job():
    return whatsapp_debt_framework()._logit(f'Running Job...'),whatsapp_debt_framework().start(targets=TARGETS)

schedule.every().day.at('15:16').do(job) #24hr format

whatsapp_debt_framework()._logit(f'Waiting for Scheduled Jobs to Trigger...')
while True:
    schedule.run_pending()
    time.sleep(1) # reduce CPU load with a wait
