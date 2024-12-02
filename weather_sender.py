from psutil import process_iter
from subprocess import Popen
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def isChromeOpen():
    for proc in process_iter(['name']):
        if proc.info['name'] in ('chrome', 'chromium-browser'):
            return True
    return False

def launchChrome():
    if not isChromeOpen():
        Popen(['google-chrome', '--remote-debugging-port=9222'])

# def getWeatherData():
#     options = webdriver.ChromeOptions()
#     options.add_argument('--headless')
#     options.add_argument('--no-sandbox')
#     options.add_argument('--disable-dev-shm-usage')
    
#     driver = webdriver.Chrome(options=options)
#     driver.get('https://weather-app-topaz-nu-28.vercel.app/')
    
#     time.sleep(5)
    
#     input_element = driver.find_element(By.ID, 'CityInput') # need to add an id to the input
#     input_element.send_keys('Panama City, Panama')
    
#     button_element = driver.find_element(By.ID, 'ButtonElement') # need to add an id to the button
#     button_element.click()
    
#     time.sleep(3)
    
#     weatherData = driver.find_element(By.ID, 'weather-info-id').text # need to write a better scraper
#     return weatherData
    
def testWhatsapp(contacts):
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    driver.get('https://web.whatsapp.com')
    
    time.sleep(15)
    
    for contact in contacts:
        searchBox = driver.find_elements(By.XPATH, '//div[@role="textbox"]')[0]
        searchBox.send_keys(Keys.ESCAPE)
        searchBox.send_keys(contact)
        searchBox.send_keys(Keys.ENTER)
        time.sleep(2)
        
        messageBox = driver.find_elements(By.XPATH, '//div[@role="textbox"]')[1]
        messageBox.send_keys(f"Good morning! this is an automated message for {contact}.") # actually craft the message
        messageBox.send_keys(Keys.ENTER)
        time.sleep(15)
        
    driver.quit()
        
def main():
    # launchChrome()
    # weatherData = getWeatherData()
    testWhatsapp(['+507 6781-0007'])

if __name__ == '__main__':
    main()