# all imports and dependencies
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep
from csv import reader

# global vars
__tags = [] # stores all the xpath of tags in a feedback.csv file
__feedback_file_path = 'feedback.csv' # file path which stores all the tags

# function definiton
def getTags():
    '''
    returns __tags list if loaded elsee loaded it form file and return it
    '''
    global __tags, __feedback_file_path
    if __tags != []:
        return __tags
    with open(__feedback_file_path, 'r') as f:
        for i in reader(f):
            __tags.append(i[0])
    return __tags

def fill_feedback():
    '''
    iterates through each xpath and calls the .click() functions
    clicks radio button for each question in feedback form
    '''
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

        
# main program starts from here
url = 'https://gu.icloudems.com/corecampus/index.php'
driver = webdriver.Safari()  # todo: replace .Safari with your browser make sure driver is installed
driver.get(url)
print(driver.title)


# todo: enter id and password of gu.icloud separated by comma
id, pwd = "your id goes here", "your password goes here"

# enters user id
id_input = driver.find_element_by_xpath("//*[@id=\"useriid\"]")
id_input.send_keys(id)

# enters password
pwd_input = driver.find_element_by_xpath("//*[@id=\"actlpass\"]")
pwd_input.send_keys(pwd)

# clicks on login button
login_bt = driver.find_element_by_xpath("//*[@id=\"psslogin\"]")
login_bt.click()

sleep(6)
# clicks on start feedback form button after waiting for 6 sec
feedback_bt = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/div/div[7]/a/img")
feedback_bt.click()

sleep(6)
# selects second option which is different batch for different people/student
select_class = driver.find_element_by_xpath("//*[@id=\"classid\"]/option[2]")
select_class.click()


start_bt = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[3]/div/div[3]/div[2]/center/input")
start_bt.click()

sleep(6)
nxt_bt = driver.find_element_by_xpath("/html/body/div[1]/div/div/center/div[1]/form[1]/div[3]/div/button")
number_of_subjects = 15 # this variables tells how many times same feedback has to be filled for different subjects
i = 0
for i in range(number_of_subjects):
    i+=1
    print('Filling feedback form-{}'.format(i))
    fill_feedback()
    nxt_bt.click()

# after filling all forms clicks on the submit button 
submit_bt = driver.find_element_by_xpath("/html/body/div[1]/div/div/center/div[1]/form[3]/div[3]/div/div/input")
submit_bt.click()
