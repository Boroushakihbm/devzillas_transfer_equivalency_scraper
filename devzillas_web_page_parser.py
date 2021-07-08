from abc import ABC

class DevzillasWebPageParser(ABC):

    @staticmethod
    def get_driver():
        pass

    @staticmethod
    def urls_len(urls):
        return len(urls)


    @staticmethod
    def get_url(urls, index):
        return urls[index]


    @staticmethod
    def get_parameters(urls, index):
        return urls[index]


    @staticmethod
    def pars(driver, url, out_parsed_data_in_levels, parameters):
        raise Exception('parse method is undefined.')


    @staticmethod
    def get_value_by_xpath_attribute(driver, attribute, xpath, try_condition, try_count, wait):
        counter = 0
        while counter < try_count:
            driver.implicitly_wait(wait)
            try:
                elem = driver.find_element_by_xpath(xpath)
                result = elem.get_attribute(attribute)
            except Exception as err:
                counter += 1
                print(f"method : {__name__} has error {str(counter)} times. error is {err}")
                continue

            if result not in try_condition:
                return result
            counter += 1


    @staticmethod
    def send_keys_by_xpath(driver, xpath, data, try_count, wait):
        counter = 0
        while counter < try_count:
            driver.implicitly_wait(wait)
            # sleep(wait)
            try:
                element = driver.find_element_by_xpath(xpath)
                element.send_keys(data)
                return
            except Exception as err:
                counter += 1
                print(f"method : {__name__} has error {str(counter)} times. error is {err}")
                continue


    @staticmethod
    def click_by_xpath(driver, xpath, try_count, wait):
        counter = 0
        while counter < try_count:
            driver.implicitly_wait(wait)
            # sleep(wait)
            try:
                element = driver.find_element_by_xpath(xpath)
                element.click()
                return
            except Exception as err:
                counter += 1
                print(f"method : {__name__} has error {str(counter)} times. error is {err}")
                continue


    @staticmethod
    def get_active_code_from_inbox(driver, try_count, wait):
        counter = 0
        while counter < try_count:
            driver.implicitly_wait(wait)
            # sleep(wait)
            try:
                code_element = str(driver.find_element_by_class_name('inbox-dataList').text).split('\n')
                text_list = [s for s in code_element if 'is your Instagram code' in s]
                active_code = [int(s) for s in text_list[0].split() if s.isdigit()]
                if active_code is not None:
                    return active_code[0]
                else:
                    counter += 1
            except Exception as err:
                counter += 1
                print(f"method : {__name__} has error {str(counter)} times. error is {err}")
                continue


    @staticmethod
    def save_data(data):
        file1 = open("data.txt", "a+")
        file1.write(str({data: data}))
        file1.close()


    @staticmethod
    def close_driver(driver):
        driver.close()
