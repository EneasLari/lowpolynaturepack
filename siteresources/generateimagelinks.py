# write-html.py
import os

from bs4 import BeautifulSoup


def setFileNamesToPath(stringtoputpath):
    currentpythonfilepath=os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    __location__=os.path.join(currentpythonfilepath,"img")
    __location__=os.path.join(__location__,"morepreviewimages")
    soup = BeautifulSoup()
    innerhtml = ""
    for dirpath, dirnames, files in os.walk(__location__):
        print(files)
        for file_name in files:
            if ".png" in file_name:
                message = stringtoputpath
                messageformated = message.format(file_name,file_name)
                innerhtml = innerhtml + messageformated
    return innerhtml


def replaceInnerHtml():
    # Open test.html for reading   
    currentpythonfilepath = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(currentpythonfilepath,"imageslinks.html")) as html_file:
        soup = BeautifulSoup(html_file.read(), features="html.parser")
        # Go through each tag and replace text with '-'
        for tag in soup.find_all("div", {"class": "images"}):
            innher = setFileNamesToPath("""<img class="card-img-top modalSource" src="siteresources/img/morepreviewimages/{}" alt="{}">""")
            for i in tag.contents:
                # print(i)
                i.replace_with("")
            tag.append(BeautifulSoup(innher, "html.parser"))

        # Store prettified version of modified html
        new_text = soup.prettify()
    # Write new contents to test.html
    with open(os.path.join(currentpythonfilepath,"imageslinks.html"), mode="w") as new_html_file:
        new_html_file.write(new_text)

def ParseHtmlToSoup(filepath):
        with open(filepath) as html_file:
                soup= BeautifulSoup(html_file.read(), features="html.parser")
                print(soup.prettify())
                return soup.prettify()

replaceInnerHtml()
# ParseHtmlToSoup("imageslinks.html")


class Person:
        personCount = 0    
        def __init__(self, name, salary):
           self.name = name
           self.salary = salary
           Person.personCount += 1
p1=Person("Eneas",800)
p2=Person("Eneas2",500)
p3=Person("Eneas3",500)
Person("Eneas34",500)
print(Person.personCount)