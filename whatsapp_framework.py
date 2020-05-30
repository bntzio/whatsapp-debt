from urllib.parse import quote
import traceback
from time import sleep,time
from datetime import datetime
from pyperclip import copy
import random as r
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

class whatsapp_debt_framework:

   def __init__(self,production=True,message=None,debug=True,debug_data=False):
       if production is False:
           if debug_data is True:
              with open('debtor_data.json') as debtor_data:
                   self.debtor_data = json.load(debtor_data)
                   self._consume_json_data = True
       with open('conf.json') as conf:
           paramaters = json.load(conf)
       self.debug = debug # _logit -> verbose
       if debug:
           message = 'None'
       if message is None:
           raise ValueError('Invalid Message Can Not Be None, Empty, or Null!')
       else:
           self.message = message

       #public
       self.production = production # False
       self.url_bin = {'whats_app':'https://web.whatsapp.com/'}
       self.notice = {'html_key':'iHhHL','text':'Keep your phone connected'}
       self.msg_count = 0
       self.data_wait = r.choice([0.22,0.3,0.25,0.23,0.34,0.35])

       #private
       # self._queue = {} # Future Release for Micro services
       self._kill_on_auth = int(paramaters['kill_on_auth'])
       self._clock = []
       self._default_xpath_text_area = paramaters['default_xpath_text_area']
       self._default_xpath_target_user = paramaters['default_xpath_target_user']
       self._default_xpath_authenticated = paramaters['default_xpath_authenticated']
       self._default_xpath_searchbar = paramaters['default_xpath_searchbar']
       self._default_xpath_send_button = paramaters['default_xpath_send_button']
       self._callbacks = {} # used for internal key based data & frame management.
       self._control_user = paramaters['control_user']

   def _logit(self,log_text: str,verbose=False):
       if self.debug:
           verbose = True
       """
       A custom logging function
       :param (str) log_text: The text that you want to log
       :return: prints the current timestamp with the log_text after it
       """
       if verbose is True:
           return print(str(datetime.fromtimestamp(time())) + '\t' + log_text)
       else:
           return str(datetime.fromtimestamp(time())) + '\t' + log_text

   def _safe_exit_on_error(self,error=None,session=None,verbose=True):
       if self.debug: # true = print stack
          if error is not None:
             self._logit(f'Noticed Exception : [{error.__traceback__}]')
       if session is not None:
           return [session.quit(),exit()]
       else:
           return exit()

   def _set_chrome_options(self):
       chrome_options = Options()
       chrome_options.add_argument('--headless')
       chrome_options.add_argument('--window-size=1920x1080')
       chrome_options.add_argument(
       'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36'
       )
       return chrome_options

   def collect(self,whatsapp_session,message,targets=None): # find the names send the messages.
       if targets is None:
           if self._consume_json_data:
              targets = self.debtor_data
           else:
              try:
                 raise ValueError('Targets Can Not Be None')
              except ValueError as VE:
                 self._safe_exit_on_error(error=VE,session=whatsapp_session)
       else:
           for _target in targets:
               target_data = [_target,targets[_target]]
               message = self.get_message(message=message,*target_data)
               searchbar = whatsapp_session.find_element_by_xpath(self._default_xpath_searchbar)
               searchbar.click()
               searchbar.send_keys(_target)
               self._logit('Waiting for Data Send')
               sleep(self.data_wait)
               target = whatsapp_session.find_element_by_xpath(self._default_xpath_target_user % _target)
               name = target.text
               _number_of_debtors = len(targets)
               if str(name) == str(_target):
                    target.click()
                    text_area = whatsapp_session.find_element_by_xpath(self._default_xpath_text_area)
                    text_area.click()
                    text_area.send_keys(message)
                    element = WebDriverWait(whatsapp_session, 20).until(
                    EC.presence_of_element_located((By.XPATH, self._default_xpath_send_button))) # raise exception if not found
                    send_button = whatsapp_session.find_element_by_xpath(self._default_xpath_send_button)
                    if send_button:
                        #send_button.click()
                        # detect os in later versions
                        #send_button.send_keys(Keys.RETURN) # linux
                        send_button.click() # windows
                        self._logit('Waiting for Data Send')
                        sleep(self.data_wait)
                    else:
                        raise Exception('Not Sent Element Not Found')
                    self.msg_count =+ 1
                    self._logit('{}/{} People Have been Reminded about their outstanding balance!'.format(self.msg_count,_number_of_debtors))

           return self._logit(f'Done!, all reminders have been sent... a total of {_number_of_debtors} Debtors have been notified.'),self._clock.append(time()),self.end(session=whatsapp_session)

   def start(self,targets,message='default'.upper()):
       self._clock.append(time())
       session = self.authenticate()
       return self._logit(self.collect(session,message,targets))

   def end(self,session):
       return self._logit(f'Collection Proccess took {round(self._clock[1] - self._clock[0],2)} Seconds!'),session.quit(),exit()

   def authenticate(self): #handle QR authentication
       self._logit('Starting Authentication, allow a few seconds, get your phone ready for the QR code... (3-7 Seconds)')
       sleep(r.randrange(3,7))
       browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
       if self.debug:
           if browser:
               if self.debug:
                   self._logit(f'Launched Browser Instance : {browser} at {str(datetime.fromtimestamp(time()))}')
       browser.get(self.url_bin["whats_app"])
       radio_button_sign_in_xpath = "//input[@name='rememberMe']" # name=rememberMe going with CSS lots of 'input' tags
       radio_button = browser.find_element_by_xpath(radio_button_sign_in_xpath).is_selected()
       if radio_button is False:
           radio_button.click()
           self._logit('Enabled Persistant Login..')
       else:
           self._logit('Persistant Login Option Detected State: [ ON ]')
       authenticated = False
       # Explicit wait referenced below
       _local_element_wait = 120
       #
       self._logit(f'Scan QR Code Now! You have {_local_element_wait} Second(s)')
       sleep(5)
       try:
           element = WebDriverWait(browser, _local_element_wait).until(
           EC.presence_of_element_located((By.XPATH, self._default_xpath_authenticated)))
           self._logit('Successfully Authenticated')
           if self._kill_on_auth == int(1):
              self._safe_exit_on_error(session=browser)
           else:
               return browser
       except Exception as te:
           self._safe_exit_on_error(error=te,session=browser)



   def connect(self,*K): # handle the initial connection and authentication into What's app return the login access
       pass


   def get_message(self,*target_data,message): # pretty done with this function for now
       if message == 'default'.upper():
           message = "Beep Boop! I'm a robot... {debtor}, I'm here to remind you that you owe money to {debt_collector}. Please deposit {amount} {currency_format} to bank account {bank_account}. Thanks!"
       else:
           message = message
       target = target_data[0]
       amount = target_data[1]
       return message.format(debtor=target,debt_collector=self._control_user["user"],amount=amount,currency_format=self._control_user["currency_format"],bank_account=self._control_user["bank_account"])
