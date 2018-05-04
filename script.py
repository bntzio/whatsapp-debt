from urllib.parse import quote
from time import sleep
from pyperclip import copy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

TARGET = 'WhatsApp Name'
PRODUCTION = False
SCANNED = False
HOST = 'http://localhost:3000'
MESSAGE = 'Your message'

if PRODUCTION is True:
    HOST = 'http://whatsapp-monitor.now.sh'
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=1920x1080')
chrome_options.add_argument(
    'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36'
)
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('https://web.whatsapp.com')
while SCANNED is False:
    image = browser.find_element_by_tag_name('img')
    image_src = image.get_attribute('src')
    encoded = quote(image_src, safe='')
    url = HOST + '/' + encoded
    copy(url)
    print('\nLink copied to your clipboard, you got 20 seconds to visit it and scan your QR code.')
    print('Waiting QR Scanning...')
    sleep(20)
    try:
        notice = browser.find_element_by_class_name('iHhHL')
        if notice.text == 'Keep your phone connected':
            SCANNED = True
            print('Success!')
    except NoSuchElementException:
        pass
search = browser.find_element_by_tag_name('input')
search.click()
search.send_keys(TARGET)
chats = browser.find_elements_by_class_name('matched-text')
found = False
for chat in chats:
    name = chat.text
    if name == TARGET:
        chat.click()
        text_area = browser.find_element_by_xpath("//*[contains(text(), 'Type a message')]")
        text_input_class = browser.execute_script("return arguments[0].nextSibling.classList[0]", text_area)
        text_input = browser.find_element_by_class_name(text_input_class)
        text_input.send_keys(MESSAGE)
        text_input.send_keys(Keys.ENTER)
        found = True
        break
if found == True:
    print('Done!')
else:
    print('Oops. No chats found!')
