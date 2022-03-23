#first step: [pip3 install pymupdf]
import fitz
import re

doc = fitz.open('D:/cv_input.pdf')
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
doc.save('D:/cv_output.pdf')
