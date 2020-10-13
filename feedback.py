from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep
from csv import reader

__tags = []

def getTags():
    global __tags
    if __tags != []:
        return __tags
    with open("feedback.csv", 'r') as f:
        for i in reader(f):
            __tags.append(i[0])
    return __tags

def fill_feedback():
    sleep(2)
    global driver
    tags = getTags()
    i=0
    for tag in tags:
        i+=1
        elm = driver.find_element_by_xpath(tag)
        elm.click()
        if(i==8):
            elm.send_keys("4")


url = 'https://gu.icloudems.com/corecampus/index.php'
driver = webdriver.Safari()  # todo: replace .Safari with your browser make sure driver is installed
driver.get(url)
print(driver.title)


# todo: enter id and password of gu.icloud separated by comma
id, pwd = "your id goes here", "your password goes here"

id_input = driver.find_element_by_xpath("//*[@id=\"useriid\"]")
id_input.send_keys(id)

pwd_input = driver.find_element_by_xpath("//*[@id=\"actlpass\"]")
pwd_input.send_keys(pwd)

login_bt = driver.find_element_by_xpath("//*[@id=\"psslogin\"]")
login_bt.click()

sleep(6)
feedback_bt = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/div/div[7]/a/img")
feedback_bt.click()

sleep(6)
select_class = driver.find_element_by_xpath("//*[@id=\"classid\"]/option[2]")
select_class.click()

start_bt = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[3]/div/div[3]/div[2]/center/input")
start_bt.click()

sleep(6)
nxt_bt = driver.find_element_by_xpath("/html/body/div[1]/div/div/center/div[1]/form[1]/div[3]/div/button")
for i in range(15):
    fill_feedback()
    nxt_bt.click()

submit_bt = driver.find_element_by_xpath("/html/body/div[1]/div/div/center/div[1]/form[3]/div[3]/div/div/input")
submit_bt.click()