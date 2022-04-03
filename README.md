# CeneoScraper

## Analiza struktury opinii w serwisie Ceneo.pl(https://www.ceneo.pl/)

|Składowa|Selektor|Zmienna|Typ zmiennej|
|--------|--------|-------|------------|
|opinia|div.js_product-review|review|bs4.element.Tag|
|identyfikator opinii|\["data-entry-id"\]|review_id|str|
|autor|span.user-post__author-name|author|str|
|rekomendacja|span.user-post__author-recomendation > em|recommendation|bool|
|liczba gwiazdek|span.user-post__score-count|stars|float|
|treść|div.user-post__text|content|str|
|data wystawienia|span.user-post__published > time:nth-child(1)\[datetime\]|publish_date|str|
|data zakupu|span.user-post__published > time:nth-child(2)\[datetime\]|purchase_date|str|
|dla ilu przydatna|button.vote-yes > yes[date-total-vote] <br> 
button.vote-yes > span <br>
span[id^=votes-yes]|useful|int|
|dla ilu nieprzydatna|button.vote-no > no[date-total-vote] <br> 
button.vote-no > span <br>
span[id^=votes-no]|useless|int|
|lista zalet|div.review-feature__title--positives ~ review-feature__item <br>div.review-feature__col:has( > div.review-feature__title--positives) > review-feature__item
<br>
div.review-feature__title--positives ~ div.review-feature__item|pros|str|
|lista wad|div.review-feature__title--negatives ~ review-feature__item <br>div.review-feature__col:has( > div.review-feature__title--negatives) > review-feature__item
<br>
div.review-feature__title--negatives ~ div.review-feature__item|cons|str|

## Etapy pracy nad projektem
1) pobranie skladowych pojedyńczej opinii do niezależnych zmiennych 
2) zapisanie wszystkich składowych pojedynczej opinii do obiektu słownika (dictionary)
3) pobranie wszystkiech opinii z pojedynczej strony i zapisanie ich do listy słowników 
4) 