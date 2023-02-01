import spacy # Importing Spacy 

nlp = spacy.load("en_core_web_md")
print("\nCHECKING SIMILARITY OF THINGS!\n")

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

# print(f"\n{word1} & {word2} got: {word1.similarity(word2)}00% similarity!")
print("\n")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


"""
NOTE.

After running the monkey similarity, I found out that Cats don't really have similarities with bananas, 
meaning they don’t really eat bananas, while monkey has a very high percentage of similarity with banana,
which means they eat bananas a lot, also monkey and cat has the highest percentage cause both are mammals  
and animals.
"""

nlp = spacy.load("en_core_web_sm")
print("My example!")
print("\nCHECKING SIMILARITY OF THINGS!\n")

# Naming the things to check
str_1 = nlp("man")
str_2 = nlp("car")
wstr_3 = nlp("Lion")

# Returning the similarity
print("\n")
print(str_1.similarity(str_2))
print(wstr_3.similarity(str_2))
print(wstr_3.similarity(str_1))

"""
NOTE. 
"en_core_web_md" 
Only returns the actual similarity percentage, while 

"en_core_web_sm"
returns Userwarning message followed by the similarity percentage 
but the percentage seem higher than that of "en_core_web_md" 
so it seem "en_core_web_sm" works better with list while "en_core_web_md" works more with stings
"""