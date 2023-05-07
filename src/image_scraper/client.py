from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from . import response
import time
import json

class Driver: 
    def __init__(self, url: str):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        options.add_experimental_option('detach', True)

        caps = DesiredCapabilities.CHROME
        caps['goog:loggingPrefs'] = {'performance': 'ALL'}

        self.driver = webdriver.Chrome(options=options, desired_capabilities=caps)
        self.url = url

        # start 
        self.driver.get(self.url)
        
    def click_button(self, text: str) -> bool:
        buttons = self.driver.find_elements(By.XPATH, '//button')
        for button in buttons:
            if button.text == text:
                button.click()
                return True
            
        return False

    def write_search_bar(self, text: str):
        text_areas = self.driver.find_elements(By.XPATH, '//textarea')
        for text_area in text_areas:
            text_area.send_keys(text)
            return True
        
        return False
    
    def submit(self) -> bool:
        buttons = self.driver.find_elements(By.XPATH, '//button')
        for button in buttons:
            if button.get_attribute("type") == "submit":
                button.click()
                return True
        
        return False
    
    def scroll_down(self) -> bool:
        self.driver.execute_script("window.scrollTo(0, 10*1080)") 
        time.sleep(1)
        
        return False
    
    def get_urls(self) -> bool:
        browser_log = self.driver.get_log('performance')
        events = [json.loads(entry['message'])['message'] for entry in browser_log]
        for event in events:
            url = response.get_image_url(event)
            if url != '':
                print(url)
                
        return False

def Init() -> int:
    driver = Driver(url="https://www.images.google.com")
    
    # Accept agreement
    if driver.click_button("Accept all"):
        print('clicked')
        
    # Search for dogs
    if driver.write_search_bar("tree"):
        print('searched for dogs')
        
    # Submit
    if driver.submit():
        print('submit')
        
    driver.get_urls()
    
    return 1