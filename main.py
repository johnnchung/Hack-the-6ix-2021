from links import scrape_page 
from cloud_fetch import cloud_response
from location import find_location 
from browser_url import get_browser_url
from timeit import default_timer
    
    # loop every 5 seconds 
    
def pipeline(url):
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
        return 'jason'
    
def set_interval(second_delay):
    url = get_browser_url()
    start = default_timer()
    
    while True:
        duration = default_timer() - start
        if duration > second_delay:
            start = default_timer()
            new_url = get_browser_url()
            if new_url != url and new_url != None:  
                print(new_url + 'GOINGTHROUGH')
                url = new_url
                pipeline_result = pipeline(url)
                

#send coordinates of bad links to tkinter control as an array of objects

# tkinter_control(link_coordinate_array)
    
if __name__ == "__main__":
    set_interval(5)