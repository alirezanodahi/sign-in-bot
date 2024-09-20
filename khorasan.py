from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

sms_time = '00:04'   # time care change it  if not may not work ##########################################################################
wait_state  = True
# Configure Selenium 
options = Options()
options.page_load_strategy = 'eager'
options.add_argument('--ignore-certificate-errors')
driver_path = 'chromedriver.exe'
driver = webdriver.Chrome(service=Service(driver_path), options=options)
# Define a wait to ensure elements are loaded
wait = WebDriverWait(driver, 200)

print('WebDriver started.')
#khorasan  point
points = [[
    (60, 23, 12.30, 34, 35, 39.73),    
    (60, 24, 31.7, 34, 36, 54.46),    
    (60, 28, 58.87, 34, 34, 8.12),    
    (60, 28, 39.64, 34, 33, 24.57) 
],  
[
    (60, 23, 1.0, 34, 37, 2.46),    
    (60, 25, 23.71, 34, 37, 1.47),    
    (60, 25, 29.35, 34, 35, 3.83),    
    (60, 23, 0.92, 34, 35, 0.25) 
]]

def loggin():
    # URL of the login page
    login_url = 'https://cadastre.mimt.gov.ir/default.aspx'

    driver.get(login_url)

    # Input username
    username_field = wait.until(EC.visibility_of_element_located((By.ID, 'ULogin1_txt_Username')))
    username_field.send_keys("Radinkavosh") # opalkanekav

    # Input password
    password_field = driver.find_element(By.ID, 'ULogin1_txt_Pass')
    password_field.send_keys("46265126Im@")  # 46265126Im

    # Wait for user to complete CAPTCHA and SMS verification manually 
    
    while True:
        current_time = time.strftime('%H:%M')
        print(current_time)
        if current_time >= sms_time:
            print('now')
            break
        time.sleep(3)  # Check every 5 second
    
    try:
        post_login_element = wait.until(EC.visibility_of_element_located((By.ID, 'ULogin1_LblUser')))
        print('Login successful.')
    except Exception as e:
        print(f'Login verification failed or timed out: {e}')
    
#---------------------------------------------------------------------------------------------------------------------
def main(points):

    # Navigate to the new page
    map_url = 'https://cadastre.mimt.gov.ir/Map/RegMap.aspx'
  
    driver.get(map_url)
    
    def find_with_wait(xpath):
        return WebDriverWait(driver, timeout=9000).until(EC.element_to_be_clickable((By.XPATH, xpath)))



    def select_from_menu(xpath, item):
        find_with_wait(xpath).click()
        item_list = find_with_wait(xpath[:-7] + 'DropDown"]/div/ul').find_elements(By.TAG_NAME, 'li')
        for elem in item_list:
            if elem.get_attribute('innerHTML') == item:
                time.sleep(0.5)
                elem.click()
                break


    # step 1: select province
    def select_province():
        select_from_menu('//*[@id="ctl00_ContentPlaceHolder1_CmbEstate_Input"]', 'خراسان رضوی')
        # refresh if we stuck
        while True:
            try:
                WebDriverWait(driver, timeout=10000).until(
                    EC.invisibility_of_element_located((By.CLASS_NAME, 'raDiv')))
                break
            except  Exception as e :
                driver.refresh()
                print(e)
                select_from_menu('//*[@id="ctl00_ContentPlaceHolder1_CmbEstate_Input"]', 'خراسان رضوی')
        time.sleep(1)

    select_province()
    
    def select_mineral_material():
        select_from_menu('//*[@id="ctl00_ContentPlaceHolder1_CmbGroup_Input"]', 'گروه 5')
        # refresh if we stuck
        while True:
            try:
                WebDriverWait(driver, timeout=999999).until(
                    EC.invisibility_of_element_located((By.CLASS_NAME, 'raDiv')))
                break
            except Exception as e :
                print(e)
                driver.refresh()
                # TODO: idk this is needed or not
                select_province()
                select_from_menu('//*[@id="ctl00_ContentPlaceHolder1_CmbGroup_Input"]', 'گروه 5')
        time.sleep(0.5)
    select_mineral_material()
                        
    # Handle selection from the table    
    while True:
        try:
            table_button = wait.until(EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_RadButton1_input")))
            driver.execute_script("arguments[0].click();", table_button)

            # Switch to the iframe containing the table
            wait.until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe")))

            # Select the item from the table
            WebDriverWait(driver,99999).until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[4]/div/div[2]/table/tbody/tr[5]'))).click()
           
            WebDriverWait(driver,99999).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="RadButton1_input"]'))).click()
            print("Item selected and confirmed.")
            
            break
        except Exception as e:
            print(f"Error during selection process: {e}")
            
    driver.switch_to.default_content()
    
    def insert_points(points):
        for point in points:
            print(point)
            
            xd = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_LngD"]')))
            xd.clear()
            xd.send_keys(point[0])
            
            xm = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_LngM"]')))
            xm.clear()
            xm.send_keys(point[1])
            
            xs = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_LngS"]')))
            xs.clear()
            xs.send_keys(point[2])
            
            yd = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_LatD"]')))
            yd.clear()
            yd.send_keys(point[3])
            
            ym = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_LatM"]')))
            ym.clear()
            ym.send_keys(point[4])
            
            ys = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_LatS"]')))
            ys.clear()
            ys.send_keys(point[5])
        
            time.sleep(0.5)
            # Click the "Darj" button
            driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_Btn_AddPoint_input"]').click()
            time.sleep(1)
            WebDriverWait(driver, 50).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'raDiv')))
            
        # Click the "Calculate" button after all points are entered
        driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_BtnCalc_input"]').click()
        #time to enter capcha and get تایید
        time.sleep(25)
        
    insert_points(points)
                
#-----------------------------------------------------------------------------------------------------------------
login = False

for i in (points):
    if login == False:
        loggin()
        login = True
    main(i)
    time.sleep(5)
    
    