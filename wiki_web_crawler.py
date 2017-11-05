import requests  #to get HTML from webpage
import time      #to allow for a break in the code processing
import bs4       #to parse through the imported HTML and pull out the links
import urllib    #to parse urls

start_url = "https://en.wikipedia.org/wiki/Special:Random"
#do they really all end at Philosopy?
target_url = "https://en.wikipedia.org/wiki/Philosophy"

def find_first_link(wiki_url):
    """
    Pulls the first article from the URL, parses it, and pulls out the first new link for the article chain.
    
    Takes wiki_url, a URL from Wikipedia, set above.
    """
    # get the HTML from "url", use the requests library
    response = requests.get(wiki_url)
    html = response.text
    # feed the HTML into Beautiful Soup
    soup = bs4.BeautifulSoup(html, 'html.parser')
    # find the first link in the article
    # This div contains the article's body
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")

    # stores the first link found in the article, if the article contains no
    # links this will remain None
    article_link = None

    # Find all the direct children of content_div that are <p>
    for element in content_div.find_all('p', recursive=False):
        # Find the first anchor tag that's a direct child of a paragraph.
        # It's important to only look at direct children, because other types
        # of link, e.g. footnotes and pronunciation, could come before the
        # first link to an article. Those other link types aren't direct
        # children though, they're in divs of various classes.
        if element.find('a', recursive=False):
            article_link = element.find('a', recursive=False).get('href')
            break
    if not article_link:
        return
    # Build a full url from the relative article_link url
    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)
    return first_link

def continue_crawl(search_history, target_url, limit = 25):
    """
    Checks to see if the program will continue crawling.
    
    Takes search_history, target_url - set above, and a loop limit variable, that has a set default of 25.
    """
    if search_history[-1] == target_url:
        # Check to see if you've reached the target URL
        print("You have reached your target URL!")
        return False
    elif len(search_history) > limit:
        # Check to see if you've reached the loop limit
        print("You have gone through more than 25 pages.")
        return False
    elif search_history[-1] in search_history[:-2]:
        # Verify you aren't in a repeating loop
        print("You are cycling through the same pages again and again.")
        return False
    else:
        return True

article_chain = [start_url]

while continue_crawl(article_chain, target_url):
    print(article_chain[-1])
    # download html of last article in article_chain
    # find the first link in that html
    first_link = find_first_link(article_chain[-1])
    if not first_link:
        print("We've arrived at an article with no links! Ending search.")
        break
    # add the first link to article_chain
    article_chain.append(first_link)
    # delay for about two seconds
    time.sleep(2)
