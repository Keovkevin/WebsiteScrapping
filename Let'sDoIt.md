# Inspecting the Webpage

 ## Example Website 
 https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India
 
 
1. First, right-click and open your browser’s inspector to inspect the webpage.
2. Try hovering your cursor on the text or number that you want to scrap and you should be able to see a blue box surrounding it. If you click                  it, the related HTML will be selected in the browser console.
3. You will know the unique location of your data with the help of class tags.
4. Now **import** all the libraries used to query a website.
5. `Note` on importing  **urllib2** sometimes you will get error like ```import urllib2
    ModuleNotFoundError: No module named 'urllib2```
6. Import the Beautiful soup functions to parse the data returned from the website    
7. Next, declare a variable for the url of the page.
8. Query the website and return the html to the variable page like this

    ```
    import urllib.request
    from bs4 import BeautifulSoup
    quote_page = urllib.request.Request('https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India') 
    page = urllib.request.urlopen(quote_page)
    ```

9. Parse the html in the 'page' variable, and store it in Beautiful Soup format.
10. As we are seeking a table to extract information about state capitals, we should identify the right table first. Let’s write the command to extract information within all **table** tags.
11. Now extract the information to Dataframes.We have imported pandas to convert list to data frame.
12. You can now print the informations in your terminals.
```
Python has several other options for HTML scraping in addition to BeatifulSoup. Here are some others:
     a.mechanize
     b.scrapemark
     c.scrapy
```
