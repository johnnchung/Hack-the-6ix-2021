from pipeline.links import scrape_page 
from pipeline.cloud_fetch import cloud_response
from pipeline.location import find_location 
from pipeline.browser_url import get_browser_url
from timeit import default_timer

class Pipeline:
    def __init__(self, delay, cursor):
        self.delay = delay
        self.cursor = cursor
        self.time = default_timer()
        self.url = None
        self.links = []

    def set_interval(self):
        duration = default_timer() - self.time
        if duration > self.delay: 
            self.time = default_timer()
            new_url = get_browser_url()
            if new_url != self.url and new_url != None:  
                print(new_url + 'GOINGTHROUGH')
                self.url = new_url
                pipeline_result = self.get_coordinates(self.url)
                self.links = pipeline_result
                return pipeline_result
        return None

    def get_coordinates(self, url): 
        links = scrape_page(url)
        phishing_results = cloud_response(links)

        bad_links = [] 
        if phishing_results != None:
            for index in range(len(phishing_results)):
                if phishing_results[index] == 'bad':
                    bad_links.append(links[index]) 
            
            link_coordinate_array = find_location(url, bad_links) 
            return link_coordinate_array
        else:
            return None

    def detect_phishing(self, linkArray):
        for link in linkArray:
            if link.checkbox(self.cursor.pos_x,  self.cursor.pos_y):
                return link
        return None
