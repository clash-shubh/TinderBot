from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from secrets import username, password

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.likes=0

    def login(self):
        self.driver.get('https://tinder.com')

        #we will only login using fb credentials. fb creds are stored in secrets.py, you can enter your creds
        login_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')))
        login_btn.click()
        try:
            sleep(3)
            fb_btn = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button')))
            fb_btn.click()
        except Exception:
            more_option_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/button')
            more_option_btn.click()
            fb_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button')
            fb_btn.click()

        # switch to login popup
        sleep(5)
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        login_btn.click()
        #you can remove this sleep if you dont have 2factor auth on fb login
        
        sleep(30)
        
        try:
            conf_btn = self.driver.find_element_by_xpath('//*[@id="u_0_4"]/div[2]/div[1]/div[1]/button')
            conf_btn.click()
        except Exception:
            #skip
            print("confirmation skipped")
        
        self.driver.switch_to.window(base_window)
        #this is for when your fb login wont actually login and show some error, its simply logs you in without any authentication on a second click
        try:
            fb_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button')))
            fb_btn.click()
        except Exception:
            print("fb btn not found")
        sleep(10)
        try:
            popup_1 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
            popup_1.click()

            popup_2 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[2]')
            popup_2.click()
        except Exception:
            print("one of the two popups not found")
            
        sleep(10)
        
        while True:
            sleep(1)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()
    def like(self):
        self.likes=self.likes+1
        print("liked "+str(self.likes))
        try:
            like_btn = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button')))
        except Exception:
            like_btn = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')))
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        dislike_btn.click()
        

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]/span')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

bot = TinderBot()
bot.login()
