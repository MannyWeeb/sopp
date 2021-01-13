#With props

commons = {
    "title"   : "h2 #basic-philosophy",
    "content" : ["p"]
}

def what(doc):
    # Oftentimes, a user may want more control over the data, fret not.
    # Just declare a method, make sure it returns something and jam it in as a value on a URL.
    # The method will automatically get a copy of a complete BeautifulSoup object containing the target document.
    # ofc, you can reuse it on other URLs, 
    return "[redacted] text from doc"

{
    "http://localhost/b*zzfeed/politics/controversial/index.html" : what
}

#Target any <h1> tag with an id of page-title
#Target any tags with an id of page-content and page-references
#Essentially combines the first two examples

#Without props
form = {
    "http://localhost/lamden/intro/philosophy/index.html" : {
        "title"   : "h2 #basic-philosophy",
        "content" : ["p"]
    },
    "http://localhost/xxx/morexxx/index.html" : ["p .captions" , "b .authors"]
}

# Target any <tag>
#Yeah, same thing, 
# "url" : "[INTERNAL] [NO_STRUCTS_DEFINED] | whole page content? idk" 