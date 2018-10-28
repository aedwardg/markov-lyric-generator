"""
Functions to get artist lyrics from azlyrics.com and write them to file
by aedwardg
"""

from bs4 import BeautifulSoup
import requests

# Parses html from page_link and saves all links from page to all_links
def get_links(page_link):
    page_response = requests.get(page_link, timeout=5)
    full_html = BeautifulSoup(page_response.content, "html.parser")
    all_links = full_html.find_all("a")
    return all_links

# removes unnecessary page links and duplicates
def get_song_links(links):
    song_links = []
    for link in range(28, (len(links) - 7)):
        song_links.append(links[link].get("href"))
    song_links = list(set(song_links))
    for entry in song_links:
        if entry == "#" or entry == None:
            song_links.remove(entry)
        else:
            continue
    return song_links

'''
fix_links was necessary because of the html in the links on an artist's page.
pulling the links returned many that were '../d/drake/song_name'
'''
def fix_links(links):
    for x in range(0, len(links)):
        if list(links[x])[0] == "." and list(links[x])[1] == ".":
            links[x] = "https://www.azlyrics.com" + "".join(list(links[x])[2:])
    return links

'''
returns lyrics in list of phrases
choose number of links to scrape at your own discretion.
I have successfully scraped up to 50 before they block my ip address,
but 25 is a safer bet.
'''
def get_lyrics(urls):
    all_text = []
    for link in urls[:25]:
        url_response = requests.get(link, timeout=5)
        url_html = BeautifulSoup(url_response.content, "html.parser")
        for script in url_html(["head", "script", "style","span", "a", "h2", "small"]):
            script.extract()
        for string in url_html.stripped_strings:
            all_text.append(string)
    return all_text

# Writes all the lyrics to a file for that artist
def write_to_file(artist_file, lyric_list):
    with open(artist_file, "w") as f:
        for phrase in lyric_list:
            f.write(phrase + "\n")
