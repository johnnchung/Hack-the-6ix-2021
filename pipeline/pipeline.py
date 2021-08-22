from pipeline.links import scrape_page 
from pipeline.cloud_fetch import cloud_response
from pipeline.location import find_location 
from pipeline.browser_url import get_browser_url
from timeit import default_timer

class Pipeline: 
    def __init__(self, delay, gui):
        self.delay = delay
        self.gui = gui
        self.time = default_timer()
    
    def play(self): 
        self.gui.play()

    

    def set_interval(self):
        url = get_browser_url()
        start = default_timer()
    
        # while True:
        duration = default_timer() - start
        if duration > self.delay: 
            start = default_timer()
            new_url = get_browser_url()
            if new_url != url and new_url != None:  
                print(new_url + 'GOINGTHROUGH')
                url = new_url
                
                pipeline_result = self.get_coordinates(url)
                
                if pipeline_result: 
                    self.gui.duck.control_mouse(self.gui.cursor)
            

    def get_coordinates(self, url): 
        links = scrape_page(url)
        phishing_results = cloud_response(links)

        bad_links = [] 
        if(phishing_results != None):
            for index in range(len(phishing_results)): 
                if phishing_results[index] == 'bad':
                    bad_links.append(links[index]) 
            
            link_coordinate_array = find_location(url, bad_links) 
            return link_coordinate_array
        else:
            return None
    
    def detect_phishing(self, linkArray):
       
        for link in linkArray: 
            if link.checkbox( self.gui.cursor.pos_x,  self.gui.cursor.pos_y):
                return link
        return None
