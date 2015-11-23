from selenium.webdriver.common.keys import Keys

class GooglePage:
    URL='http://www.google.com'
    TEXTBOX_NAME='q'

    def __init__(self, driver):
        self.driver = driver

    def open_url(self):
        self.driver.get(self.URL)

    def enter_search_term(self, query):
        element=self.driver.find_element_by_name(self.TEXTBOX_NAME)
        element.send_keys(query)
        element.send_keys(Keys.RETURN)

    def check_result(self, name):
        assert name in self.driver.page_source
