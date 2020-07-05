from selenium import webdriver
from time import sleep

from secrets import username, password

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.likes=0

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(3)
        #we will only login using fb credentials. fb creds are stored in secrets.py, you can enter your creds
        try:
            fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
            fb_btn.click()
        except Exception:
            more_option_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button')
            more_option_btn.click()
            fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
            fb_btn.click()

        # switch to login popup
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
        
        sleep(5)
        
        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]/span')
        popup_1.click()

        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]/span')
        popup_2.click()
        
        popup_cookies = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        popup_cookies.click()
        
        sleep(4)
        
        #popup_loc = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button/span')
        #popup_loc.click()
        
        sleep(6)
        
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
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
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
