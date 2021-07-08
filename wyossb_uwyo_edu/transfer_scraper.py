from devzillas_web_page_parser import DevzillasWebPageParser
from table_data_scraper import scrape_table
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from time import sleep
import requests


class TransferScraper(DevzillasWebPageParser):
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
    def search_and_get_source(url, parameters):
        state = parameters.get('state')
        college = parameters.get('college')
        usp_attribute = parameters.get('usp_attribute')
        form_data = {
            'state_in': state,
            'college_in': college,
            'College': '',
            'trf_subject_in': '',
            'trf_num_in': '',
            'trf_group_in': '',
            'uw_subject_in': '',
            'uw_num_in': '',
            'usp_attribute_in': usp_attribute,
        }
        return requests.post(url, data=form_data)

    @staticmethod
    def pars(driver, url, out_parsed_data_in_levels, parameters):
        page_source = TransferScraper.search_and_get_source(url, parameters)
        soup = BeautifulSoup(page_source.text, features="html.parser")
        transfer_equivalency_table = soup.find("table", {"class": "datadisplaytable"})
        rows = scrape_table(transfer_equivalency_table)
        out_parsed_data_in_levels.extend(rows)


