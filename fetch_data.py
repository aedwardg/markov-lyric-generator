"""
Functions to get artist lyrics from azlyrics.com and write them to file
by aedwardg
"""

from bs4 import BeautifulSoup
import requests
import time 
import random 

# Parses html from page_link and saves all links from page to all_links
def get_links(page_link):
    page_response = requests.get(page_link, timeout=5)
    full_html = BeautifulSoup(page_response.content, 'html.parser')
    all_links = full_html.find_all('a')
    return all_links

# removes unnecessary page links and duplicates
def get_song_links(links):
    song_links = []
    # As of Feb. 2020 there are 28 links in the navbar, 3 share links (FB, Twitter, Mail), and 8 links at the bottom of the page
    # This number may change and need to be updated
    for link in range(31, (len(links) - 8)):
        song_links.append(links[link].get('href'))
    song_links = list(set(song_links))
    for entry in song_links:
        if entry == '#' or entry == None:
            song_links.remove(entry)
        else:
            continue
    print('Retrieved links for {} songs'.format(len(song_links)))
    return song_links


"""
`fix_links` was necessary due to relative links in the html.
E.g., '../d/drake/song_name'
"""
def fix_links(links):
    print('Fixing song links')
    for x in range(0, len(links)):
        if list(links[x])[0] == '.' and list(links[x])[1] == '.':
            links[x] = 'https://www.azlyrics.com' + ''.join(list(links[x])[2:])
    return links


"""
Returns lyrics in list of phrases.  
Pauses for 10 to 20 seconds between scraping each page of lyrics.
May need to update cleaning loop in the future if page changes.
"""
def get_lyrics(urls, max_songs=None, sleep_min=10, sleep_max=20):
    start_time = time.time()
    all_text = []

    link_requests = 0

    if max_songs is not None:
        num_songs = max_songs
    else:
        num_songs = len(urls)

    for link in urls[:num_songs]:
        print('Scraping: {}'.format(link))
        
        try:
            url_response = requests.get(link, timeout=10)
        except:
            print('Read timout')
            pass
        
        # Removes unnecessary text on page
        url_html = BeautifulSoup(url_response.content, 'html.parser')
        for script in url_html(['head', 'script', 'style', 'span', 'a', 'h1', 'h2', 'small', 'b', 'i']):
            script.extract()
        
        # Removes informational blocks after lyrics
        for tag in url_html.find_all('div', class_='panel'):
            tag.extract()

        for string in url_html.stripped_strings:
            all_text.append(string)

        current_time = time.time()
        elapsed_time = current_time - start_time
        link_requests += 1

        print('Songs scraped: {0} of {1}'.format(link_requests, num_songs))
        print('Elapased Time: {} minutes'.format(elapsed_time/60))
        print('Pausing...')    
        time.sleep(random.uniform(sleep_min, sleep_max))  
    return all_text

"""Writes all the lyrics to a file for that artist"""
def write_to_file(artist_file, lyric_list):
    with open(artist_file, 'w') as f:
        for phrase in lyric_list:
            f.write(phrase + '\n')
