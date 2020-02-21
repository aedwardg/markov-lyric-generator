# markov-lyric-generator
This program is designed to collect lyrics for an artist of choice via www.azlyrics.com, write them to a text file, then run a random selection of the lyrics through Codecademy's Markov Chain Generator to create a new "song."  The new song will be output to another text file.

Use of lyrics should be strictly limited to personal use and not for any commercial purposes to avoid any legal issues.

## Program prerequisites
In order to run this program, the user must have BeautifulSoup4 installed, and must clone the Codecademy Markov Chain Generator to the same file.  The Markov Chain Generator, (link: https://github.com/Codecademy/markov_python) will also need to be altered to be compatible with Python 3.  I will not specify which changes need to be made, as this is good practice for any other Codecademy students looking to do their Python Final Project with Python 3 instead of Python 2.

## Run Program
1. Create two blank text documents in the folder: one for the original artist lyrics (e.g., "drake.txt") and one for the output (e.g., "output.txt").
2. Open run.py and specify the artist's azlyrics link (e.g., "http://www.azlyrics.com/d/drake.html") as well as file names for the two text documents you created.
3. Execute run.py in the terminal.  (Note: progam is scraping html from several pages, so it will take up to 30 seconds to complete)

## Issues and Disclaimer
The primary issue I ran into with this program is that azlyrics doesn't seem to take kindly to their site being scraped.  Despite only disallowing bots in one folder (see their robots.txt), they appeared to block my IP when I would scrape multiple pages at once.  This means that for many users, this program will be a one-off.  If you are using a VPN, this doesn't present a problem.  Otherwise, use at your own risk.  In the fetch_data.py file, the number of songs to be scraped is set at a default of 25.  This can be adjusted, but I would recommend keeping it below 50, as the site may try to block you mid-scrape if you do too many pages at once.  
Again, the use of this program to gather lyrics for personal, non-commercial use complies with the website's policies, but automated security measures kick in and block your IP when you scrape too many pages, so use this program at your own discretion.
