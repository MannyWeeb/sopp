# Quick Guide

## First Sip

The script will only ask for two optional command-line arguments, those are

1. **form-name**

    *-Loads a python file within the current directory(/src/) as the main form, defaults to form\.py*
    *-Automatically finds a python file(\.py) so just give it the name*

2. **output-file**

    *-Denotes the output file which will contain the script's result after execution. defaults to /data/dump\.json*
    *-Output format is based on the given extension name that the user provides, currently supports json and csv only.*

### Examples

``` powershell
PS C:\Users\Manny\Desktop\Sopp\src> python core.py -myform -myhugedump.json
PS C:\Users\Manny\Desktop\Sopp\src> python core.py -goodform -firstdumpinweeks.csv
```

Omitting or providing an invalid value on any of these arguments would cause the program to use the given defaults.

## Getting Acquainted

First let's create a valid form file, but what is it anyways?

**Form** - *A python module/file which contains most elements such as the target URL, and other attributes required by the script.*

Since the script was written around reading a python module/file, this automatically allows
users to dynamically alter the variables such as the url, props, values and so on.

Here's a basic snippet of how it should look like, we'll go through the details in a jiffy.

### Sample #1

``` python
# And yes, you should declare a dictionary variable named form, script'll be awry otherwise
form = {
    "http://localhost/lamden/intro/philosophy/index.html" : {
        "title"   : "h2 #main-title",
        "content" : ["p"]
    },
    "http://localhost/xxx/morexxx/index.html" : ["p .captions" , "b .authors"]
}
```

*The form variable declares two URLs to fetch, it's designated value defines how the resultant data is defined in the final output.*

#### Sample #1 Under the Microscope

Lamden
> Declares two properties, each of which defines it's target elements. these pairs are then the output for this specific URL.

xxx
> Flatly defines it's targets without declaring any props. in this case the extracted data is appended as the value for this specific URL.

### Sample #2

``` python
def what(doc):
    # Oftentimes, a user may want more control over the data, fret not.
    # Just declare a method, make sure it returns something and jam it in as a value on a URL.
    # The method will automatically get a copy of a complete BeautifulSoup object containing the target document.
    # ofc, you can reuse it on other URLs, 
    return "[redacted] texts from doc"

# Sites stated are completely made up btw, except theonion, a reliable news source.
form = {
    "http://localhost/b*zzfeed/politics/controversial/index.html" : what,
    "http://localhost/theonion/index.html" : {
        "heading" : what
    }
}
```

#### Sample #2 Under the Microscope

This example is similar to the first one, it just uses the returned value from a function as the value for whatever key it's paired with(on a prop or the URL itself).

## Clearing up confusions

a few lines of text to clear up some clouds.

> **For the love of god, how does this dumb script know which elements to target?**
> *This answer only applies when using either a string or an array of it, each string targets
> a different set of elements, their rulesets are independent from other strings. they are also
> inspired by how jquery targets html elements, so a prefix of "." would denote a class, "#"
> denotes an id and so on.*
>
> using sample #1 as our example...
>
> ``` python
>    "http://localhost/lamden/intro/philosophy/index.html" : {
>        "title"   : "h2 #main-title", # This targets any h2 elements with the id "main-title".
>        "content" : ["p" , "label .content"] # on the other hand, this targets any p or label element. the latter also requires the element to contain a "content" class
>    }
> ```
>
> Inferring from the example, targets of type list/array will match multiple elements while the other doesn't
