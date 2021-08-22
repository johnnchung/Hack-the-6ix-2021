
# from browser_url.py import current_browser_url 

from links import scrape_page 

from cloud_fetch import cloud_response

from location import find_location 

def app(): 
    
    # loop every 5 seconds 
    
    #somehow detect that url changes and only 
    # url = current_browser_url()
    
    url = "https://www.stackoverflow.com/"
    
    links = scrape_page(url)
    phishing_results = cloud_response(links)
    
    bad_links = [] 
    for index in range(len(phishing_results)): 
        if phishing_results[index] == 'bad':
            bad_links.append(links[index]) 
        
    
    link_coordinate_array = find_location(url, bad_links) 

    #send coordinates of bad links to tkinter control as an array of objects
    
    # tkinter_control(link_coordinate_array)
    
app()