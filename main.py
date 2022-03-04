import sys, os, re

def convert(text: str):
    texts = text.splitlines()
    for i in range(len(texts)):
        if headline(texts[i]) != False:
            texts[i] = f"<h{headline(texts[i])}>{texts[i][1+headline(texts[i]):]}</h{headline(texts[i])}>"
        if re.search("\*{3}[^\*]+\*{3}",texts[i]):
            texts[i] = re.sub("\*{3}([^\*]+)\*{3}","<b><i>\\1</i></b>",texts[i])
        if re.search("\*{2}[^\*]+\*{2}",texts[i]):
            texts[i] = re.sub("\*{2}([^\*]+)\*{2}","<b>\\1</b>",texts[i])
        if re.search("\*{1}[^\*]+\*{1}",texts[i]):
            texts[i] = re.sub("\*{1}([^\*]+)\*{1}","<i>\\1</i>",texts[i])
        if re.search("\_{3}[^\_]+\_{3}",texts[i]):
            texts[i] = re.sub("\_{3}([^\_]+)\_{3}","<i><u>\\1</u></i>",texts[i])
        if re.search("\_{2}[^\_]+\_{2}",texts[i]):
            texts[i] = re.sub("\_{2}([^\_]+)\_{2}","<u>\\1</u>",texts[i])
        if re.search("\_{1}[^\_]+\_{1}",texts[i]):
            texts[i] = re.sub("\_{1}([^\_]+)\_{1}","<i>\\1</i>",texts[i])
        if re.search("\~{2}[^\~]+\~{2}",texts[i]):
            texts[i] = re.sub("\~{2}([^\~]+)\~{2}","<s>\\1</s>",texts[i])
        if re.fullmatch("\-{3,}", texts[i]):
            texts[i] = "<hr>"
    text = "<br>\n".join(texts)
    text = re.sub("(.*)(</h[1-6]>|</div>|<hr>)<br>", "\\1\\2", text)
    return text


# Headline checker(内包表記とか色々使えばもっと楽になりそう)
def headline(text):
    if text[0:1] != "#":
        return False
    if text[0:7] == "###### ":
        return 6
    if text[0:6] == "##### ":
        return 5
    if text[0:5] == "#### ":
        return 4
    if text[0:4] == "### ":
        return 3
    if text[0:3] == "## ":
        return 2
    if text[0:2] == "# ":
        return 1
    return False

text = """# The hello!!
---
Noticy!
"""

print(convert(text))
