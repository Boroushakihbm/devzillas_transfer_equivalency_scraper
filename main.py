from time import perf_counter

from wyossb_uwyo_edu.state_usp_scraper import StateAndUspScraper
from wyossb_uwyo_edu.college_scraper import CollegeScarper
from wyossb_uwyo_edu.transfer_scraper import TransferScraper
from wyossb_uwyo_edu.univercity_of_wayoming_mapper import map_data
from devzillas_crawler import DevzillasCrawler


def transfer_equivalency_scraping(max_crawl_pages):
    start_time = perf_counter()
    states = []
    max_level_of_crawl = 1
    DevzillasCrawler.start_concurrent_crawling(max_crawl_pages,
                                               max_level_of_crawl,
                                               (StateAndUspScraper,),
                                               states,
                                               None)

    state_pool = [{'url': item['url'],
                   'usp_attributes': item['usp_attributes'],
                   'state': state} for item in states for state in item['states']]

    unrefined_pool = []
    DevzillasCrawler.start_concurrent_crawling(max_crawl_pages,
                                               max_level_of_crawl,
                                               (CollegeScarper,),
                                               unrefined_pool,
                                               state_pool)

    pool = []
    for state in unrefined_pool:
        for college in state['colleges']:
            for usp_attribute in state['usp_attributes']:
                if state['state'] != '*':
                    data = {'url': state['url'],
                            'state': state['state'],
                            'college': college,
                            'usp_attribute': usp_attribute}
                    pool.append(data)

    # print(pool)
    transfer_data = []
    print(len(pool))
    DevzillasCrawler.start_concurrent_crawling(max_crawl_pages,
                                               max_level_of_crawl,
                                               (TransferScraper,),
                                               transfer_data,
                                               pool,
                                               50)

    end_time = perf_counter()
    content = {'total_time_of_crawling_scraping': end_time - start_time,
               'average_time_per_page': (end_time - start_time) / max_crawl_pages,
               'max_crawl_pages': max_crawl_pages,
               'max_level_of_crawl': max_level_of_crawl,
               'data': map_data(transfer_data),
               }
    print(f'total_time_of_crawling_scraping :{end_time - start_time}')
    return content


if __name__ == '__main__':
    crawl_pages = 300
    scraped_data = transfer_equivalency_scraping(crawl_pages)
    print(scraped_data['data'])
