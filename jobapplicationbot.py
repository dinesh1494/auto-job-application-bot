from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pynput.keyboard import Listener, Key

def on_press(key):
    if key == Key.esc:
        driver.quit()
        return False
print("TRUST US YOUR EMAIL_ID AND PASSWORD WILL NOT BE STORED AND WILL NOT BE SHARED WITH ANY THIRD PARTY")
email = input("enter your email id:")
phone_number = input("enter your phone number:")
password = input("enter your password:")
job_type = input("enter your job prefernce:")
job_loc = input("enter location:")
print("make it full screen to avoid error:")
print("enter 'ESP' to quite the program:")
time.sleep(5)


chrome_driver_path="C:\chrome driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
wait = WebDriverWait(driver, 10)
driver.get("https://www.linkedin.com/home")
time.sleep(2)
username = driver.find_element(By.ID, 'session_key')
username.send_keys(email)
pass_word = driver.find_element(By.ID, 'session_password')
pass_word.send_keys(password)
time.sleep(2)
pass_word.send_keys(Keys.ENTER)
time.sleep(20)
get_url = driver.current_url
new_url = get_url + "/new-page"
driver.get(new_url)
time.sleep(5)



#job = driver.find_element(By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[3]/a')
#job.click()
#get_url = driver.current_url
#new_url = get_url + "/new-page"
driver.get("https://www.linkedin.com/jobs/")
time.sleep(15)
searchbox = driver.find_element(By.CSS_SELECTOR, ".jobs-search-box__inner input")
#wait.until(EC.visibility_of(searchbox))
time.sleep(2)
searchbox.send_keys(job_type)
#searchloc = driver.find_element(By.CLASS_NAME , "jobs-search-box__text-input")
#time.sleep(2)
#wait.until(EC.visibility_of(searchloc))
#searchloc.send_keys(job_loc)
time.sleep(2)
searchbox.send_keys(Keys.ENTER)


get_url = driver.current_url
new_url = get_url + "/new-page"
driver.get(new_url)

time.sleep(5)
easy_apply = driver.find_element(By.CSS_SELECTOR, ".search-reusables__filter-binary-toggle button")
#wait.until(EC.visibility_of(easy_apply))
time.sleep(5)
easy_apply.click()
time.sleep(10)


#exp = driver.find_element(By.CSS_SELECTOR,".search-reusables__filter-trigger-and-dropdown button")
#wait.until(EC.visibility_of(element))
#time.sleep(5)
#exp.click()


all_listings = driver.find_elements(By.CSS_SELECTOR,".job-card-container--clickable")
for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    try:
        apply_button = driver.find_element(By.XPATH, '//*[@id="ember5225"]')
        apply_button.click()
        time.sleep(5)

        phone = driver.find_element(By.XPATH, '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3507648603-83062306-phoneNumber-nationalNumber"]')
        if phone.text == "":
            phone.send_keys(phone_number)

        submit_button = driver.find_element(By.XPATH,'//*[@id="ember5635"]')

        h1 = driver.find_element(By.XPATH,'//*[@id="ember5905"]/div/div[2]/form/div/div/h3')
        if h1.text == "Resume":
            choose = driver.find_element(By.XPATH, '//*[@id="ember798"]')
            submit_button = driver.find_element(By.XPATH, '//*[@id="ember797"]')
        else:
            close_button = driver.find_element(By.XPATH,'//*[@id="ember1378"]/li-icon/svg')
            close_button.click()
            discard_button = driver.find_element(By.XPATH,'//*[@id="ember1411"]')
            discard_button.click()
            continue


        if h1.text == "Additional Questions":
            time.sleep(60)
        time.sleep(2)
        close_button = driver.find_element(By.CSS_SELECTOR,"artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:

        continue


with Listener(on_press=on_press) as listener:
    listener.join()
