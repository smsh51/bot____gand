# Generated by SmS.Hz
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

s = False
if s:
    globals()['video_category'] ='فیلم و سینما'
    globals()['chanel_name'] = "https://www.namasha.com/TinTama"
    globals()['username_ifilo'] = 'momtaa'
    globals()['password_ifilo'] = 'test123321'
else:
    globals()['chanel_name'] = input('Enter url of chanel : ')
    globals()['video_category'] = input('Enter category of videos : ')
    globals()['username_ifilo'] = 'momtaa'
    globals()['password_ifilo'] = 'test123321'

# %% upload
class TestUpload:

    def setup_method(self, method):
        self.driver = webdriver.Chrome('Driver/chromedriver109.exe')
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_upload(self, video_data: dict):
        # Test name: upload
        # Step # | name | target | value
        # 1 | open | /upload |
        try:
            self.driver.get("https://ifilo.net/login")
        except:
            print('Error === 101')
            return None
        # login
        user_selector = 'body > div:nth-child(1) > article > section > div:nth-child(2) > form > div:nth-child(1) > input'
        self.driver.find_element(By.CSS_SELECTOR, user_selector).send_keys(globals()['username_ifilo'])
        pass_selector = '#password'
        self.driver.find_element(By.CSS_SELECTOR, pass_selector).send_keys(globals()['password_ifilo'])
        self.driver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(1) > article > section > div:nth-child(2) > form > button').click()

        # upload
        self.driver.get('https://ifilo.net/upload')
        # 2 | setWindowSize | 564x708 |
        self.driver.set_window_size(564, 708)
        # 3 | click | id=tablistItem2 |
        self.driver.find_element(By.ID, "tablistItem2").click()
        # 4 | click | name=tVideoUrl |
        self.driver.find_element(By.NAME, "tVideoUrl").clear()
        # 5 | type | name=tVideoUrl | https://www.namasha.com/videos/dl/7394578709-1080p/%D9%81%DB%8C%D9%84%D9%85-%D8%B4%D9%85%D8%A7-%D9%85%D8%B1%D8%AF%D9%85-%D8%A8%D8%A7-%D8%B2%DB%8C%D8%B1%D9%86%D9%88%DB%8C%D8%B3-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-You-People-2023-1080p.mp4
        self.driver.find_element(By.NAME, "tVideoUrl").send_keys(video_data['down_url'])
        # 6 | click | id=startUrlUpload |
        self.driver.find_element(By.ID, "startUrlUpload").click()
        # 7 | click | css=.ng-invalid |
        self.driver.find_element(By.CSS_SELECTOR, ".ng-invalid").clear()
        # 8 | type | css=.ng-valid-maxlength | عنوان
        self.driver.find_element(By.CSS_SELECTOR, ".ng-valid-maxlength").send_keys(video_data['title'])
        # 9 | click | css=.post-category > .ng-pristine |
        while True:
            if '100' in self.driver.find_element(By.CSS_SELECTOR, "#uploadPrg > div.number-pb-num").text:
                break
            time.sleep(4)
            if '' == self.driver.find_element(By.CSS_SELECTOR, "#uploadPrg > div.number-pb-num").text:
                return None

        # 10 | select | css=.post-category > .ng-untouched | label=فیلم و سینما
        dropdown = self.driver.find_element(By.CSS_SELECTOR, ".post-category > .ng-untouched")
        dropdown.find_element(By.XPATH, "//option[. = '{}']".format(video_data['category'])).click()
        # 11 | click | css=.bf > .ng-pristine |
        self.driver.find_element(By.CSS_SELECTOR, "#basicField > div:nth-child(3) > div > textarea").clear()
        # 12 | type | css=.ng-valid-parse:nth-child(1) | توضیحات فیلم
        self.driver.find_element(By.CSS_SELECTOR, "#basicField > div:nth-child(3) > div > textarea").send_keys(video_data['des'])
        # 13 | click | css=.number-pb-num |
        # self.driver.find_element(By.CSS_SELECTOR, ".number-pb-num").click()

        # 14 | click | css=.\_fit |
        self.driver.find_element(By.CSS_SELECTOR, ".\\_fit").click()
        # 15 | click | css=.ng-binding |
        self.driver.find_element(By.CSS_SELECTOR, ".ng-binding").click()
        # 16 | click | css=.co-m12 > p |
        self.driver.find_element(By.CSS_SELECTOR, ".co-m12 > p").click()
        # 17 | close |  |
        self.driver.close()


# %% video
class TestSaveurl:
    def setup_method(self, method):
        self.driver = webdriver.Chrome('Driver/chromedriver109.exe')
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_saveurl(self, chanel_url: str = "https://www.namasha.com/TinTama"):
        # Test name: save_url
        # Step # | name | target | value
        # 1 | open | /TinTama |
        try:
            self.driver.get(chanel_url)
        except:
            return None
        
        # 2 | setWindowSize | 564x708 |
        self.driver.set_window_size(564, 708)
        # 3 | click | id=load-more-btn |
        while True:
            try:
                self.driver.find_element(By.ID, "load-more-btn").click()
                time.sleep(0.5)
            except:
                break  
        
        video_urls = []
        video_selector = 'body > div.container-fluid > main > div > article > div.row.list-row > div:nth'
        video_selector = 'body > div.container-fluid > main > div > article > div.row.list-row > div'
        videos = self.driver.find_elements(By.CSS_SELECTOR, video_selector)
        for video in videos:
            url = video.find_element(By.TAG_NAME, 'a')
            url.get_attribute('title').replace('/', '').replace(' ', '-')+'-720p.mp4'
            video_urls.append(url.get_attribute('href'))
        
        return video_urls
        base_url_download = 'https://www.namasha.com/videos/dl/7346668488-720p/'
        # 4 | runScript | window.scrollTo(0,13364) |
        self.driver.execute_script("window.scrollTo(0,13364)")
        # 5 | click | css=.list-row |
        self.driver.find_element(By.CSS_SELECTOR, ".list-row").click()
        # 6 | click | linkText=فیلم جدید ران اشتباه رفته دوبله فارسی / Ron's Gone Wrong 2021 |
        self.driver.find_element(By.LINK_TEXT, "فیلم جدید ران اشتباه رفته دوبله فارسی / Ron\'s Gone Wrong 2021").click()
        # 7 | click | css=.jw-video |
        self.driver.find_element(By.CSS_SELECTOR, ".jw-video").click()
        # 8 | close |  |
        self.driver.close()

    def export_video_data(self, video_url: str):
        video_data = {'category': globals()['video_category']}
        try:
            self.driver.get(video_url)
        except Exception as e:
            print(e)
            return None

        self.driver.fullscreen_window()
        # downoad url
        down_selector = 'body > div.container-fluid > main > div > article > div > div:nth-child(2) > div > div.col-lg-7.col-xl-8.px-0.px-lg-3 > div.action-buttons.d-flex.mx-3.mt-2.mt-xl-3.ml-xl-0 > div.col.col-xl-auto.position-relative.ml-xl-3.p-0.order-4.order-lg-3 > div > div > div.scroll-bar.scroll-bar-y.flex-grow-1 > a:nth-child(1)'
        video_data['down_url'] = self.driver.find_element(By.CSS_SELECTOR, down_selector).get_attribute('href')        

        # des 
        next_selector = '#video-description-wrapper > button'
        self.driver.find_element(By.CSS_SELECTOR, next_selector).click()
        video_data['des'] = self.driver.find_element(By.ID, 'video-desc').text

        # title
        title_selector = 'body > div.container-fluid > main > div > article > div.row > div:nth-child(2) > div > div.col-lg-7.col-xl-8.px-0.px-lg-3 > div.d-flex.justify-content-between.align-items-start.pt-2.px-3.px-lg-0.mr-lg-3.position-relative > div > h1'
        video_data['title'] = self.driver.find_element(By.CSS_SELECTOR, title_selector).text
        
        return video_data


# %% main 
def main(s):
    if not s:
        quit()
    # ============================== export url video
    self = TestSaveurl()
    self.setup_method(None)
    video_urls = self.test_saveurl(globals()['chanel_name'])
    self.teardown_method(None)

    # =========================== up
    self = TestUpload()
    # ===========================

    for video_url in video_urls:
        self.setup_method(None)
        video_data = self.export_video_data(video_url)
        self.teardown_method(None)
    # ============================== upload video
        self.setup_method(None)
        self.test_upload(video_data)


# %% code
if __name__ == '__main__':
    main(True)

