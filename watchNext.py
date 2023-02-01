import spacy

nlp = spacy.load("en_core_web_md")

# Movie function 
def movieWatch():
    iWatched = """Planet Hulk :Will he save their world or destroy it? 
    When the Hulk becomes too dangerous for the Earth, the illuminati tricked Hulk into a shuttle, 
    And lunched him into space to a planet where the Hulk can live in peace.
    Unfortunately halk land on the planet sakaar where he is sold into slavery and trained as a gladiator. """
    return iWatched

watch = open("movies.txt")


watchNlp = nlp(movieWatch())

for nextWatch in watch:
    
    similarity = nlp(nextWatch).similarity(watchNlp)

print("\nYour next movie.....\n")
print(nextWatch + " - ", similarity, "\n")



