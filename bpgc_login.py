from selenium import webdriver
from selenium.webdriver.common.keys import Keys

creds = {
	'id' : '<userid>',
	'pwd' : '<password>'	
}


#BPGC page launch
driver = webdriver.Firefox()
driver.get("https://campnet.bits-goa.ac.in:8090/")


#checks for BPGC login page, else exits
assert "BITS Goa Campus Internet Portal" in driver.title

#find and enter stuff
user_id = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")
login_button = driver.find_element_by_id("loginbutton")


user_id.clear()
password.clear()
user_id.send_keys(creds["id"])
password.send_keys(creds["pwd"])

#login 

login_button.click()

#exit

driver.close()


