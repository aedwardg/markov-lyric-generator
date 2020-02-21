# markov-lyric-generator
This program is designed to collect lyrics for an artist of choice via www.azlyrics.com, write them to a text file, then run a random selection of the lyrics through Codecademy's Markov Chain Generator to create a new "song."  The new song will be output to another text file.

Use of lyrics should be strictly limited to personal use and not for any commercial purposes to avoid any legal issues.

## Program prerequisites
The easiest way to run this program is to clone this repo and ensure that BeautifulSoup4 is installed.  (`pip install bs4`, or `conda install bs4` for Anaconda distributions)
The Markov Chain Generator was originally from the Codecademy Python 2 capstone project, (link: https://github.com/Codecademy/markov_python) which I altered to be compatible with Python 3.

## Run Program
1. Navigate to the directory containing this repo using the command prompt/terminal.
2. Open run.py and specify the artist's azlyrics link (e.g., "http://www.azlyrics.com/d/drake.html") as well as file names for the two text documents where you want the scraped lyrics and generated lyrics to be saved.  You can also specify the number of songs you want to scrape to provide the Markov Chain generator with lyrics.  If you select `None`, the program will scrape all songs by that artist (this may take a while since the program has to pause 10 to 20 seconds between each song in order to not crash the site).
3. Save run.py with these changes.
4. Execute run.py in the terminal.  (Note: progam is scraping html from several pages, so it will take up to 30 seconds to complete)
