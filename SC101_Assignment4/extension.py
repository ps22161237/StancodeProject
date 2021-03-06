"""
File: extension.py
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names' + year + '.html'
        ##################
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)
        items = soup.find_all('table', {'class':'t-stripe'})
        male_number = 0
        female_number = 0
        values = []
        # 擷取文字
        for item in items:
            values = item.tbody.text.split()
        value = []
        # 把中文去掉留下數字
        for i in values:
            i = i.replace(',', '')
            if i.isdigit():
                value.extend([i])
        # 根據位置計算加總數目
        for j in range(1, len(value), 3):
            male_number += int(value[j])
            female_number += int(value[j+1])
        print('male_number: '+str(male_number))
        print('female_number: '+str(female_number))


if __name__ == '__main__':
    main()
