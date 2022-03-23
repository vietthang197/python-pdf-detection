#first step: [pip3 install pymupdf]
import re

import fitz

doc = fitz.open('D:/mycv.pdf')
page = doc[0]
line = page.get_text()
match = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', line)
email = match.group(0)
print(email)
rect = page.search_for(email)
GRAY = (0.96,0.24,0.67,0)
for location in rect:
    page.wrap_contents()
    page.draw_rect(location,color=[0.96,0.24,0.67,0],fill=GRAY,stroke_opacity=1, fill_opacity=1, oc=0)
    page.add_redact_annot(location)
    page.apply_redactions(images=fitz.PDF_REDACT_IMAGE_PIXELS)

match2 = re.search(r'(84|0[3|5|7|8|9])+([0-9]{8})\b', line)
phone = match2.group(0)
print(phone)
rect2 = page.search_for(phone)
for location in rect2:
    page.wrap_contents()
    page.draw_rect(location,color=[0.96,0.24,0.67,0], fill=GRAY,stroke_opacity=1, fill_opacity=1, oc=0)
    page.add_redact_annot(location)
    page.apply_redactions(images=fitz.PDF_REDACT_IMAGE_PIXELS)

def findUrl(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)
    return [x[0] for x in url]

url_arr = findUrl(line)
print(url_arr)
for urlhide in  url_arr:
    rect3 = page.search_for(urlhide)
    for location in rect3:
        page.wrap_contents()
        page.draw_rect(location,color=[0.96,0.24,0.67,0], fill=GRAY,stroke_opacity=1, fill_opacity=1, oc=0)
        page.add_redact_annot(location)
        page.apply_redactions(images=fitz.PDF_REDACT_IMAGE_PIXELS)

doc.save('D:/cv_output.pdf')
