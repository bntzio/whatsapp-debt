from whatsapp_framework import whatsapp_debt_framework


# pip install scheduler

TARGETS = {'GAGAN-DEV': 10} # yep it is that easy, format the debtor and the value here and run!
whatsapp_debt_framework().start(targets=TARGETS)
