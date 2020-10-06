import clipboard
import re as regex

# everything_before_pattern = regex.compile("^(.*?)http")
everything_after_pattern = regex.compile("^(.*?)http")
text = clipboard.paste()
textlines = text.splitlines()
urls = []
urls_to_copy = ""
for textline in textlines:
    if "http" in textline:
        urls.append(textline)

for url in urls:
    to_remove = regex.search(everything_after_pattern, url)
    url = url.replace(to_remove.group(0), "http")
    urls_to_copy += url
    urls_to_copy += "\n"
    print(url)


clipboard.copy(urls_to_copy)
print("done!")
