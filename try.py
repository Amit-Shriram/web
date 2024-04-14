
import json
import requests
from bs4 import BeautifulSoup

data_list = [
    {"url": "https://www.nbcnews.com/health/coronavirus",
     "uppertag": "h2",
     "upperkey": "class",
     "uppervalue": "styles_teaseTitle__H4OWQ",
     "lowertag": "div",
     "lowerkey": "class",
     "lowervalue": "article-body__content",
     "imgtag": "figure",
     "imgkey": "class",
     "imgvalue": "article-hero__main",
     "imgname": "src",
     "credit_name":"nbcnews",
     "domain":"latest"},
    {"url": "https://www.businesstoday.in/",
     "uppertag": "li",
     "upperkey": "class",
     "uppervalue": "lst_li",
     "lowertag": "div",
     "lowerkey": "class",
     "lowervalue": "text-formatted field field--name-body field--type-text-with-summary field--label-hidden field__item",
     "imgtag": "div",
     "imgkey": "class",
     "imgvalue": "main-img",
     "imgname": "src",
     "credit_name":"businesstoday",
     "domain":"latest"},
    {"url": "https://www.indiatvnews.com/",
     "uppertag": "h2",
     "upperkey": "class",
     "uppervalue": "title",
     "lowertag": "div",
     "lowerkey": "class",
     "lowervalue": "content",
     "imgtag": "figure",
     "imgkey": "class",
     "imgvalue": "artbigimg row",
     "imgname": "data-original",
     "credit_name":"indiatvnews",
     "domain":"latest"},
    {"url": "https://www.moneycontrol.com/news/news-all/",
     "uppertag": "li",
     "upperkey": "class",
     "uppervalue": "clearfix",
     "lowertag": "div",
     "lowerkey": "class",
     "lowervalue": "content_wrapper arti-flow",
     "imgtag": "div",
     "imgkey": "class",
     "imgvalue": "article_image",
     "imgname": "data-src",
     "credit_name":"moneycontrol",
     "domain":"latest"},
    {"url": "https://indianexpress.com/",
     "uppertag": "h3",
     "upperkey": "class",
     "uppervalue": "",
     "lowertag": "div",
     "lowerkey": "class",
     "lowervalue": "story_details",
     "imgtag": "span",
     "imgkey": "class",
     "imgvalue": "custom-caption",
     "imgname": "src",
     "credit_name":"indianexpress",
     "domain":"latest"},
    {"url": "https://www.news18.com/",
     "uppertag": "li",
     "upperkey": "class",
     "uppervalue": "jsx-68b5a5b9c681585",
     "lowertag": "div",
     "lowerkey": "class",
     "lowervalue": "jsx-926f17af57ac97dc",
     "imgtag": "div",
     "imgkey": "class",
     "imgvalue": "jsx-926f17af57ac97dc article_byno_limg",
     "imgname": "src",
     "credit_name":"news18",
     "domain":"latest"},
    {"url": "https://scroll.in/latest/",
     "uppertag": "li",
     "upperkey": "class",
     "uppervalue": "row-story",
     "lowertag": "div",
     "lowerkey": "class",
     "lowervalue": "article-body",
     "imgtag": "figure",
     "imgkey": "class",
     "imgvalue": "featured-image",
     "imgname": "src",
     "credit_name":"scroll",
     "domain":"latest"},
    {"url": "https://www.livemint.com/",
     "uppertag": "h3",
     "upperkey": "class",
     "uppervalue": "",
     "lowertag": "div",
     "lowerkey": "class",
     "lowervalue": "mainArea",
     "imgtag": "figure",
     "imgkey": "data-vars-mediatype",
     "imgvalue": "image",
     "imgname": "src",
     "credit_name":"livemint",
     "domain":"latest"},
    {"url": "https://www.marca.com/en/",     #sports
     "uppertag": "div",
     "upperkey": "class",
     "uppervalue": "ue-c-cover-content__main",
     "lowertag": "div",
     "lowerkey": "class",
     "lowervalue": "ue-c-article__body",
     "imgtag": "div",
     "imgkey": "class",
     "imgvalue": "ue-c-article__media-img-container ue-l-article--expand-edge-right-until-tablet ue-l-article--expand-edge-left-until-tablet",
     "imgname": "src",
     "credit_name":"marca",
     "domain":"latest"},
    {"url": "https://techcrunch.com/",     #tech
     "uppertag": "header",
     "upperkey": "class",
     "uppervalue": "post-block__header",
     "lowertag": "div",
     "lowerkey": "class",
     "lowervalue": "article-content",
     "imgtag": "article",
     "imgkey": "class",
     "imgvalue": "article-container article--post",
     "imgname": "src",
     "credit_name":"techcrunch",
     "domain":"latest"}
]




list_link = []
list_headline = []
list_newsdes = []
list_img = []
# list_credit = []
# list_domain = []

def postdata():
    url = 'https://flaskkex.pythonanywhere.com/testingpostnews'
    headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
    data = {"links": list_link, "headlines": list_headline, "description":list_newsdes, "images":list_img}
    response = requests.post(url, json=json.dumps(data), headers=headers)
    
    if response.status_code == 200:
        print(f'POST request successful {len(list_link)}')
        print('Response:', response.text)
    else:
        print(f'POST request failed with status code {response.status_code}')
        print('Error message:', response.text)

def scrape_news_data():
    for item in data_list:
        url = item["url"]
        uppertag = item["uppertag"]
        upperkey = item["upperkey"]
        uppervalue = item["uppervalue"]
        lowertag = item["lowertag"]
        lowerkey = item["lowerkey"]
        lowervalue = item["lowervalue"]
        imgtag = item["imgtag"]
        imgkey = item["imgkey"]
        imgvalue = item["imgvalue"]
        imgname = item["imgname"]
        credit_name = item["credit_name"]
        domain = item["domain"]

        try:
            r = requests.get(url)
        except:
            print(f'Faild {url}')
            
        soup = BeautifulSoup(r.content, 'lxml')
        all_articles = soup.find_all(uppertag, {upperkey: uppervalue})
        all_articles = all_articles[:5]

        for article in all_articles:
            link = article.find('a')['href']
            headline = article.text.strip()
            page = requests.get(link)
            bsobj = BeautifulSoup(page.content, 'lxml')
            news_content = bsobj.find(lowertag, {lowerkey: lowervalue})
            image = bsobj.find(imgtag, {imgkey: imgvalue})
            img = None
            if image:
                try:
                    if credit_name == "The hindu":
                        img = image.find('source').get(imgname, None)
                    else:
                        img_tag = image.find('img')
                        img = img_tag.get(imgname, None) if img_tag else None
                except:
                    print(f'image error {url}')

            if news_content:
                newsdes = news_content.text.strip()
                list_link.append(link)
                list_headline.append(headline)
                list_newsdes.append(newsdes)
                list_img.append(img)
                # list_credit.append(credit_name)
                # list_domain.append(domain)
    postdata()

scrape_news_data()
