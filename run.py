from fetch_data import *
from markov_python.cc_markov import MarkovChain

# Insert the artist page link from azlyrics.com
page_link = 'https://www.azlyrics.com/b/billieeilish.html'
# Insert name of text file for lyric all lyrics
full_file = 'billie.txt'
# Insert name of output file
output = 'output.txt'
# Insert limit on number of songs or None to scrape all songs
max_songs = 25

def save_lyrics(url, doc, max_songs=None):
    all_links = get_links(url)
    songs = get_song_links(all_links)
    fix_links(songs)
    lyrics = get_lyrics(songs, max_songs=max_songs)
    write_to_file(doc, lyrics)

 
def write_song(doc1, doc2):
    mc = MarkovChain()
    verse = 1
    mc.add_file(doc1)
    with open(doc2, 'w') as f:
        while verse < 5:
            f.write(('Verse %s' + '\n') % (verse))
            for x in range(4):
                line = mc.generate_text()
                join_line = ' '.join(line)
                f.write(join_line.capitalize() + '\n')
            f.write('\n')
            verse += 1


def run_all(artist=page_link, lyric_file=full_file, output_doc=output, max_songs=max_songs):
    save_lyrics(page_link, full_file, max_songs=max_songs)
    write_song(full_file, output)

if __name__ == '__main__':
    run_all()