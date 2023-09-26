import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

 
def get_data():
    url = "https://www.trendyol.com/atari/retro-mini-620-mario-oyunlu-av-retro-mini-oyun-konsolu-scart-basliksiz-p-36587919"
    magaza_url = "https://www.trendyol.com/magaza/profil/"

    m_url = "https://www.trendyol.com/atari/retro-mini-620-mario-oyunlu-av-retro-mini-oyun-konsolu-scart-basliksiz-p-36587919/saticiya-sor?merchantId=139779&showSelectedSeller=true"
   
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the product data
        product_name = soup.find("h1", class_="pr-new-br").text
        brand = soup.find("a", class_="product-brand-name-with-link").text

        # Extract price data
        selling_price = float(soup.find("span", class_="prc-org").text.strip().replace("TL", "").replace(",", "").strip())
        discounted_price = float(soup.find("span", class_="prc-dsc").text.strip().replace("TL", "").replace(",", "").strip())

        # Extract category data
        category_hierarchy = [a.text for a in soup.find_all("a", class_="product-detail-breadcrumb-item")]

        # Extract merchant info
        merchant_name = soup.find("span", {"class":"product-description-market-place"}).text

        
        data = soup.findAll('div',attrs={'class':'seller-container'})
        other_merchants = {}
        for div in data:
            links = div.findAll('a')
            for a in links:
                other_merchants[a["title"]] = a["href"].split('=', 1)[1]


        all_merchs = other_merchants.copy()
        all_merchs[brand] = parse_qs(urlparse(m_url).query)["merchantId"][0]
        

    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)


    Tr2Eng = str.maketrans("çğıöşü", "cgiosu")
    
    for m in all_merchs.keys():
        m_merchant = "-".join(m.lower().translate(Tr2Eng).split())
        m_link = magaza_url + m_merchant + "-" + "m" + "-" + all_merchs[m]
        m_resp = requests.get(m_link)
        if m_resp.status_code == 200:
            
            m_soup = BeautifulSoup(m_resp.text, 'html.parser')
            konum_tag = m_soup.find('span', string='Konum')
            m_konum = str(konum_tag.find_next_siblings('span')).split(">", 1)[1].split("<", 1)[0]
            m_score = m_soup.find('span', class_='product-review-section-wrapper__wrapper__rating_wrapper__rating_value').text
            all_merchs[m] = [m_konum, m_score]

        else:
            print("Failed to retrieve the webpage. Status code:", response.status_code)

    city_name = all_merchs[brand][0]
    seller_score = float(all_merchs[brand][1])

    all_merchs.pop(brand)

    merchant_info = {brand:[city_name, seller_score]}
    #all_merchs = list(map(list, all_merchs.items()))


    result={"name":product_name,
            "brand":brand,
            "selling_price": selling_price,
            "discounted_price": discounted_price,
            "category": category_hierarchy,
            "merchant_info": merchant_info,
            "other_merchants": all_merchs}
    

    return result
