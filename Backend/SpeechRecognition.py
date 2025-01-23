#pip install selenium
#pip install webdriver_manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

Link = r'C:\Users\KIIT\Desktop\Jarvis\Backend\Voice.html'
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--use--fake-ui-for-media-stream")
chrome_options.add_argument("--use--fake-device-for-media-stream") 
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=chrome_options)
driver.get(Link)
sleep(2) 
def SpeechRecognition():
    driver.find_element(by=By.ID, value="start").click()
    print("listening...")
    while True:
        Text = driver.find_element(by=By.ID,value="output").text
        if Text:
            driver.find_element(by=By.ID,value="end").click()
            return Text
        else:
            sleep(0.222)

while True:
    Text = SpeechRecognition()
    print(Text)            

