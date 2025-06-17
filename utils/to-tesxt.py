import markdown
from bs4 import BeautifulSoup

with open("./output_test/income_tax.md", "r", encoding="utf-8") as md_file:
    markdown_text = md_file.read()

html = markdown.markdown(markdown_text)

soup = BeautifulSoup(html, "html.parser")

text = soup.get_text()

with open("./output_test/income_tax.txt", "w", encoding="utf-8") as txt_file:
    txt_file.write(text)
