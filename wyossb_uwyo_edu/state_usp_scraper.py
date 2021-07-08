from devzillas_web_page_parser import DevzillasWebPageParser
from bs4 import BeautifulSoup
import requests


class StateAndUspScraper(DevzillasWebPageParser):
    def __init__(self):
        pass

    @staticmethod
    def get_driver():
        return None

    @staticmethod
    def urls_len(urls):
        return 1

    @staticmethod
    def get_url(urls, index):
        return "https://wyossb.uwyo.edu/bnrprod/bwckytfc.p_display_transfer_catalog"

    @staticmethod
    def get_parameters(urls, index):
        return None

    @staticmethod
    def pars(driver, url, out_parsed_data_in_levels, parameters):

        page_source = requests.post(url)
        soup = BeautifulSoup(page_source.text, features="html.parser")
        states = []
        usp_attributes = []

        state_selector = soup.find("select", id='state_in')
        for item in state_selector.find_all('option'):
            state = item.get("value")
            if state:
                states.append(state)

        ups_selector = soup.find("select", id='usp_attribute_in')
        for item in ups_selector.find_all('option'):
            usp_attribute = item.get("value")
            if usp_attribute:
                usp_attributes.append(usp_attribute)

        out_parsed_data_in_levels.append({'url': url,
                                          'states': states,
                                          'usp_attributes': usp_attributes,
                                          })
        x = 1
