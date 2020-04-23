import sys
import os
from selenium import webdriver

path = "~/Documents/Projects/"
browser = webdriver.Chrome()

browser.get('https://github.com/login')

def login():
        project_name = str(sys.argv[1])

        # git login
        python_button = browser.find_element_by_xpath("//*[@id='login_field']")
        python_button.send_keys('<username>')
        python_button = browser.find_element_by_xpath("//*[@id='password']")
        python_button.send_keys('password')
        python_button = browser.find_element_by_xpath("//*[@id='login']/form/div[4]/input[9]")
        python_button.click()

        # init push
        browser.get('https://github.com/new')
        python_button = browser.find_element_by_xpath("//*[@id='repository_name']")
        python_button.send_keys(project_name)
        python_button = browser.find_element_by_css_selector("button.first-in-line")
        python_button.submit()

        browser.quit()

if __name__ == "__main__":
        login()
