import re

def extract_hashtags(text):
    hashtag_pattern = r'#\w+'
    hashtags = re.findall(hashtag_pattern, text)
    return hashtags


social_media_post = "Just practicing some #regex and #python. #programming is fun! #coding"
hashtags = extract_hashtags(social_media_post)

for tag in hashtags:
    print(tag)

