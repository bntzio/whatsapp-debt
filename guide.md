## Glossary

whatsapp_debt_framework :
Arguments
- production - Optional | Default : True
- message - Required - Raises ValueError if None example : Invalid Message Can Not Be None, Empty, or Null!
- debug - Optional - Default True - Turns Verbose on
- debug_data  - Optional - Default False - Switches from database mode to importing json data from debtor_data.json

Public methods:
- self.production -
- self.url_bin -
- self.notice -
- self.msg_count -

Private methods:
- self.queue -
- self._kill_on_auth -
- self._default_xpath_text_area -
- self._default_xpath_authenticated -
- self._callbacks -
- self._control_user -

Public Functions:
- self.collect -
  Arguments
    -
  Returns
    -

- self.authenticate
  Arguments
    - None

  Returns
    -

- self.connect - # Depreciated
  Arguments
    -None

  Returns
    -

- self.get_message -
  Arguments
    -target_data - required list(target,amount) Strict
    -message - Optional -Type: Str - Has preset text if left default - Default : 'default.upper()'

  Returns
    -

Private Functions:
- self._logit -
  Arguments
    - log_text - Required - Type: Str
    - verbose - Optional - Default False - Print or just Return logs (T/F) Overridden by self.debug
  Returns
    -
- self._set_chrome_options - Sets browser to headless and screen size to 1920x1080 Mac OSX headers
  Arguments
    - None
  Returns
    -
## About
Payment Gateways:
- N/A


<br/>

## Usage

Using the whats app debt framework is very straight forward.

example :

TARGETS = {'name': amount} # yep it is that easy, format the debtor and the value here and run!
whatsapp_debt_framework().start(targets=TARGETS)

name = str
amount = int

calling start() will automatically open an instance of chrome and request you scan the qr code for your whatsapp on your phone.
Once authenticated the framework will continue through your dictionary of 'TARGETS' and send a message to each debtor about the amount using a default message, if you want to personalize what message goes into the chat windows, refer to the following example:


TARGETS = {'name': amount} # yep it is that easy, format the debtor and the value here and run!
message = '{name} Don't forget you have an outstanding balance with Apple for {amount}'
whatsapp_debt_framework().start(targets=TARGETS,message=message)
