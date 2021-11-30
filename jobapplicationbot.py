from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "D:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
sign_in = driver.find_element_by_xpath("/html/body/div[1]/header/nav/div/a[2]")
sign_in.click()
username_path = driver.find_element_by_xpath('//*[@id="username"]')
username_path.send_keys("av4861@srmist.edu.in")
password = driver.find_element_by_id("password")
password.send_keys("anirudh@03042001")
entry = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
entry.click()

#all_jobs = driver.find_elements_by_xpath('//*[@id="ember297"]')
#print(all_jobs)
#all_jobs.click()
apply_class = driver.find_element_by_class_name(".artdeco-button__text")
apply_class.click()
number_path = driver.find_element_by_xpath('//*[@id="urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2814831478,38260514,phoneNumber~nationalNumber)"]')
number_path.send_keys("8124107143")
submit = driver.find_element_by_xpath('//*[@id="ember401"]/span')
submit.click()