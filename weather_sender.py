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

def getWeatherData():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(options=options)
    driver.get('https://weather-app-topaz-nu-28.vercel.app/')
    
    time.sleep(5)
    
    input_element = driver.find_element(By.ID, 'CityInput')
    input_element.send_keys('Panama City, Panama')
    
    button_element = driver.find_element(By.ID, 'ButtonElement')
    button_element.click()
    
    time.sleep(3)
    
    weatherData = driver.find_element(By.ID, 'current-weather').text
    temperatureData = driver.find_element(By.ID, 'current-temp').text
    feelsLikeData = driver.find_element(By.ID, 'feels-like-temp').text
    return { "weatherData": weatherData, "temperatureData": temperatureData, "feelsLike": feelsLikeData }
    
def sendWhatsappMessages(weatherData, contacts):
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    driver.get('https://web.whatsapp.com')
        
    time.sleep(15)
    
    for contact in contacts:
        message = f"Good morning, {contact}! Here's today's weather: In Panama City it's currently {weatherData['weatherData']}. Temperature is {weatherData['temperatureData']}, but it {weatherData['feelsLike']}. Hope you have a great day!"
        
        searchBox = driver.find_elements(By.XPATH, '//div[@role="textbox"]')[0]
        searchBox.send_keys(Keys.ESCAPE)
        searchBox.send_keys(contact)
        searchBox.send_keys(Keys.ENTER)
        time.sleep(2)
        
        messageBox = driver.find_elements(By.XPATH, '//div[@role="textbox"]')[1]
        messageBox.send_keys(message)
        messageBox.send_keys(Keys.ENTER)
        time.sleep(15)
        
    driver.quit()
        
def main():
    launchChrome()
    weatherData = getWeatherData()
    sendWhatsappMessages(weatherData, ['+507 6781-0007', 'Ale', 'G8', 'Boobs fans club'])

if __name__ == '__main__':
    main()