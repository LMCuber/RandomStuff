from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time


positions = [
    "zeroth","first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth",
    "eleventh", "twelfth", "thirteenth", "fourteenth", "fifteenth", "sixteenth", "seventeenth", "eighteenth", "nineteenth", "twentieth",
    "twenty-first", "twenty-second", "twenty-third", "twenty-fourth", "twenty-fifth", "twenty-sixth", "twenty-seventh", "twenty-eighth", "twenty-ninth", "thirtieth",
    "thirty-first", "thirty-second", "thirty-third", "thirty-fourth", "thirty-fifth", "thirty-sixth", "thirty-seventh", "thirty-eighth", "thirty-ninth", "fortieth",
    "forty-first", "forty-second", "forty-third", "forty-fourth", "forty-fifth", "forty-sixth", "forty-seventh", "forty-eighth", "forty-ninth", "fiftieth",
    "fifty-first", "fifty-second", "fifty-third", "fifty-fourth", "fifty-fifth", "fifty-sixth", "fifty-seventh", "fifty-eighth", "fifty-ninth", "sixtieth",
    "sixty-first", "sixty-second", "sixty-third", "sixty-fourth", "sixty-fifth", "sixty-sixth", "sixty-seventh", "sixty-eighth", "sixty-ninth"
]
cur_pos = 7

driver = webdriver.Chrome()
driver.get("https://caeborg.com")

account_button = driver.find_element("xpath", "/html/body/section[1]/button[3]")
time.sleep(5)
account_button.click()
username_field = driver.find_element("xpath", "/html/body/section[1]/div[2]/input")
username_field.send_keys(f"The{positions[cur_pos].replace('-', '').title().replace(' ', '')}AdolfEichmann")
