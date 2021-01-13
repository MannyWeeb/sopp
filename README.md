# Sopp

> A small python script for quickly scraping data from most websites

## Overview

Sopp attempts to simplify scraping tasks by abstracting away most of the setup which are normally required.
While the underlying library that this script relies on(BeautifulSoup) requires little to no setup in itself, the user
is required to manually manipulate and wrestle with the library itself to get the values that they want, then arbitrarily
deal with said data afterwards.

## How does it work?

The whole script works by allowing the user to only modify a file called a "form".py, which requires a few
pre-requisites before being considered a valid "form", this file is required since it dictates which elements are targeted
and how the resulting data are grouped together.

## Is this right for my purposes?

Since the goal of the script is to abstract some parts of the setup and scraping processes, this comes at a cost of
reducing the flexibility of the underlying library(bs4) and the user's overall control of the data.

## Known Issues

The author boasts little to no experience with python so there are bound
to be some if not many issues still needing to be resolved, Obvious ones are as follows.

* Only outputs data in JSON format (for now)
* Inability to fetch documents using other protocols other than GET.
* Fixed k/v arrangement of resultant data, which may be a bit limiting for those wanting to exercise greater control over how it's layed out in the final output.
* Overall Code legibility

## Tasks to consider

* [ ] Basic CLI interface.

* [X] Support CSV output.

* [ ] Create test suites.

## How to Contribute

For those who think they can improve or add useful features on this script, I'd like to encourage you to contribute as I'm unlikely to push any major changes on it(It already served it's purpose, at least in my case)
