import re

def remove_html_tags(text):
    
    html_tags_pattern = r'<.*?>'
    clean_text = re.sub(html_tags_pattern, '', text)
    return clean_text
html_text = "<p>This is <b>bold</b> and <i>italic</i> text.</p>"
clean_text = remove_html_tags(html_text)
print(clean_text)

