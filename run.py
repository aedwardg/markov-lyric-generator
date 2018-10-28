from fetch_data import *
from markov_python.cc_markov import MarkovChain

# Insert the artist page link from azlyrics.com
page_link = "https://www.azlyrics.com/a/aesoprock.html"
# Insert name of text file for lyric all lyrics
file = "aesop.txt"
# Insert name of output file
output = "output.txt"


def save_lyrics(url, doc):
    all_links = get_links(url)
    songs = get_song_links(all_links)
    fix_links(songs)
    lyrics = get_lyrics(songs)
    write_to_file(doc, lyrics)



def write_song(doc1, doc2):
    mc = MarkovChain()
    verse = 1
    mc.add_file(doc1)
    with open(doc2, "w") as f:
        while verse < 5:
            f.write(("Verse %s" + "\n") % (verse))
            for x in range(4):
                line = mc.generate_text()
                join_line = " ".join(line)
                f.write(join_line.capitalize() + "\n")
            verse += 1





save_lyrics(page_link, file)
write_song(file, output)
