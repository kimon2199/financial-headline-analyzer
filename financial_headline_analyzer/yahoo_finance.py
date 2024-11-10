import requests
import xml.etree.ElementTree as ET

def get_yahoo_finance_headlines():    
    # Send a request to the RSS feed
    rss_url = "https://finance.yahoo.com/rss/"
    response = requests.get(rss_url)
    
    headlines = []
    
    if response.status_code == 200:
        # Parse the XML response
        root = ET.fromstring(response.content)

        # Find all the <item> elements (which represent individual headlines)
        items = root.findall(".//item")
        
        # Loop through each <item> and extract title, link, and pubDate
        for idx, item in enumerate(items, start=1):
            article_info = {
                "title": item.find("title").text, 
                "link": item.find("link").text,
                "pub_date": item.find("pubDate").text
            } 
            
            print(f"{idx}. {article_info['title']}")
            print(f"   Link: {article_info['link']}")
            print(f"   Published: {article_info['pub_date']}")
            print("-" * 50)

            headlines.append(article_info)
    else:
        print("Failed to retrieve the RSS feed.")
    
    return headlines
