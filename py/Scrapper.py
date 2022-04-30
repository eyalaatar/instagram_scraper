import json
from bs4 import BeautifulSoup


class Scrapper():
    def __init__(self, driver):
        self.driver = driver
        self.posts = self.get_posts()

    def get_posts(self):
        posts = []
        links = self.driver.find_elements_by_tag_name('a')
        for link in links:
            post = link.get_attribute('href')
            if '/p/' in post:
                posts.append(post)
        return posts

    def get_product_types(self):
        L = []
        for post in self.posts:
            shortcode = post.split("/")[-2]
            html = self.driver.get(f"https://www.instagram.com/p/{shortcode}/?__a=1")
            soup = BeautifulSoup(self.driver.page_source, "html.parser").get_text()
            jsondata = json.loads(soup)
            L.append(jsondata['items'][0]['product_type'])
        return tuple(L)

    def scrap(self):
        data = {}
        index = 0
        for post in self.posts:
            shortcode = post.split("/")[-2]
            html = self.driver.get(f"https://www.instagram.com/p/{shortcode}/?__a=1")
            soup = BeautifulSoup(self.driver.page_source, "html.parser").get_text()
            jsondata = json.loads(soup)
            ### Carosel
            if jsondata['items'][0]['product_type'] == 'carousel_container':
                for i in range(int(jsondata['items'][0]['carousel_media_count'])):
                    L = [jsondata['items'][0]['caption']['text'],
                         jsondata['items'][0]['carousel_media'][i]['image_versions2']['candidates'][0]['url'],
                         jsondata['items'][0]['like_count']
                         ]
                    data[str(index)] = L
                    index += 1
            ## Video
            if jsondata['items'][0]['is_unified_video']:
                L = [jsondata['items'][0]['caption']['text'],
                     jsondata['items'][0]['video_versions'][0]['url'],
                     jsondata['items'][0]['like_count']]
                data[str(index)] = L
                index += 1
            ##Image
            if jsondata['items'][0]['product_type'] == 'feed':
                L = [jsondata['items'][0]['caption']['text'],
                     jsondata['items'][0]['image_versions2']['candidates'][0]['url'],
                     jsondata['items'][0]['like_count']]
                data[str(index)] = L
                index += 1
        print("Scrapping Done")
        return data
