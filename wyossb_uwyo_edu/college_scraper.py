from devzillas_web_page_parser import DevzillasWebPageParser
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from time import sleep
import requests


class CollegeScarper(DevzillasWebPageParser):
    def __init__(self):
        pass

    @staticmethod
    def get_driver():
        return None

    @staticmethod
    def urls_len(urls):
        return len(urls)

    @staticmethod
    def get_url(urls, index):
        return urls[index]['url']

    @staticmethod
    def get_parameters(urls, index):
        return urls[index]

    @staticmethod
    def select_state(driver, state):
        print(f'try to select state {state}')
        driver.find_element_by_xpath(f"//select[@name='state_in']/option[text()='{state}']").click()
        sleep(1)
        element = driver.find_element_by_id("id____UID0")
        element.click()
        sleep(2)

    @staticmethod
    def check_state_changed(driver, state):
        print(f'trying to check state{state} is changed.')
        soup = BeautifulSoup(driver.page_source, features="html.parser")
        state_selector = soup.find("select", id='state_in')
        select = Select(state_selector)
        option = select.first_selected_option()
        print(f'selected state is {option.text} my state is {state} ')
        return option.Text == state

    @staticmethod
    def pars(driver, url, out_parsed_data_in_levels, parameters):
        state = parameters.get('state')

        page_source = requests.post(url, data={'state_in': state})

        usp_attributes = parameters.get('usp_attributes')

        soup = BeautifulSoup(page_source.text, features="html.parser")

        colleges = []
        college_selector = soup.find("select", id='college_in')
        for item in college_selector.find_all('option'):
            college = item.get("value")
            if college:
                colleges.append(college)

        if colleges:
            out_parsed_data_in_levels.append({'url': url,
                                              'state': state,
                                              'usp_attributes': usp_attributes,
                                              'colleges': colleges,
                                              })
