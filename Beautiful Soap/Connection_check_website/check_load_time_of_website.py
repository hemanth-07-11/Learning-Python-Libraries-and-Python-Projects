from urllib.request import urlopen
import time

def get_load_time(url):
    if ("https" or "http") in url: 
        open_this_url = urlopen(url) 
    else:
        open_this_url = urlopen("https://" + url) 
    start_time = time.time() 
    open_this_url.read()  
    end_time = time.time()  
    open_this_url.close()  
    time_to_load = end_time - start_time

    return time_to_load


if __name__ == '__main__':
    url = input("Enter the website whose loading time needs to be checked: ")
    print(f"\nThe time taken to load {url} is {get_load_time(url):.2} seconds.")
