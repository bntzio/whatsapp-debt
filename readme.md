# WhatsApp Debt (in progress)

Stable Releases:

OS:

Ubuntu 18.04 LTS [TESTED] : Working no Issues

Else:

Not Tested


[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

> Automating the tedious task of collecting debts 💰

### Todos
  BASE

- [ ] Add CLI args to turn on/off production mode
- [ ] Add cronfile to specify the time the bot will run
- [ ] Create a json file to save debt info
- [ ] Add deployment instructions
- [ ] Update readme
- [ ] Add GIF demo
- [ ] Add GIF Demos for conf.json with Screenshots and guide on how to use selenium ide to fetch xpath fields.
- [x] Add MIT license
- [ ] Depreciate Connect until Persistence issues are fixed
- [ ] Scope, Rename, Finish Alpha Collect()
- [x] Complete Alpha Stages of Authenticate()
- [x] Temp Depreciated connect
- [ ] Create private function (in init) that loads configs
- [x] Create conf.json file
- [ ] Restructure application to a proper file hierarchy

  EXTENDED

  [ ] Resolve issues with solving the QR via image (driver.element.screenshot(filename='name.png')) when displaying on local machine or web, can not verify
  [ ] Find Solution for persistent Headless Login

### Roadmap

- [ ] Add Stripe/Paypal support (remove person if a deposit is made)
- [ ] Add Bitcoin/Ethereum support (remove person if a deposit is made)
- [ ] Create app & database to dynamically add or remove people from debt

**Feel free to collaborate!**
For information about Issues see issue_guide.md



### For Usage Guides Check guide.md!
### For Issue Guide check out issue_guide.md

This platform was built with the idea of making collection of automated payments through whats app an easy process. A Final version of this platform should be applicable to facilitate P2P Loans with Ease. This system should also be able to be adapted for instance for monthly payments, if a store were to collect 29.99 every 31 days, this can be a general use case for this type of platform.




### Installation & Deployment


Step 1: Download the source code to your local working directory

Step 2: cd into the directory and create a virtual environemnt called wdf

Step 3: activate your virtual env

Step 4: install the requirements with pip install -r requirements.txt

Step 5: Navigate to conf.json Replace control_user information with relevant information

Step 6: Navigate to unit_test.py and Complete the TARGET information

Step 7: Navigate to your console and run python3 unit_test.py

Your done!




### Notes

An example of using the platform in it's default form, is in unit_test.py, the way this framework was built is to do all of the heavy lifting for you, feed the target, amount, and authenticate it will handle the rest for you.


An example of using a Scheduler with this type of application to run every x time frame and so on, is in scheduler.py, A more advanced tutorial will be made available in latter versions.


###Useful Information


conf.json is per say the configuration file for this framework, you will notice these elements at the time of writing :



{
  "default_xpath_text_area": "//footer/div/div[2]/div/div[2]",
  "default_xpath_authenticated": "//*[text() = 'Keep your phone connected']",
  "default_xpath_searchbar":"//div[@id='side']/div/div/label/div/div[2]",
  "default_xpath_send_button":"//div[3]/button/span",
  "default_xpath_target_user":"//span[contains(.,'%s')]",
  "control_user": {"user":"Enrique","currency_format":"$","bank_account":"4531-2321-3421-3421"},
  "kill_on_auth":"0"
}


The First element default_xpath_text_area Defines : The chat space to use the send_keys() functions to send a message in whatsapp web (authenticated)

The Second Element default_xpath_authenticated Defines: A point of the whatsapp website that undeniably proves you are authenticated e.g the search bar.

The Third Element default_xpath_searchbar Defines: The Search bar behind whatsapp web (authenticated)

The Fourth Element default_xpath_send_button Defines: The send a message button in a whatsapp chat

The Fifth Element default_xpath_target_user Defines : The xpath used to identify a web element with the text of the target user for per say the chat window we need to click

The Sixth Element control_user Defines: Default control user settings that defines who the debt collector is (user), The currency format ($), and the bank account associated (will be changed later for other payment methods)
