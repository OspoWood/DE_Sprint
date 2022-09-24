import json
from time import sleep
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://spb.hh.ru/search/vacancy?from=suggest_post&area=&hhtmFrom=vacancy_search_list&text="
PAGE_ATTRIBUTE = "&page="
VACANCY = "python+разработчик"


def get_html(url: str) -> str:
    headers = {
        'User-Agent': 'My User Agent 1.0',
    }
    return requests.get(url=url, headers=headers).text


def get_bs4_page(url: str) -> BeautifulSoup:
    return BeautifulSoup(get_html(url), 'html.parser')


def get_page_vacancy_urls(num_page: int) -> [str]:
    pageUrl = BASE_URL + VACANCY + PAGE_ATTRIBUTE + str(num_page)
    vacancy = get_bs4_page(pageUrl).findAll("div", {"class": "vacancy-serp-item-body__main-info"})
    return [a.a["href"] for a in vacancy]


def get_total_page_vacancy(vacancy: str) -> int:
    pageUrl = BASE_URL + vacancy
    return int(list(map(lambda x : x.text,  get_bs4_page(pageUrl).findAll("span",{"class":"pager-item-not-in-short-range"})))[-1:][0])


def get_all_url_vacancy(vacancy: str) -> [str]:
    return sum([get_page_vacancy_urls(x) for x in range(get_total_page_vacancy(vacancy=vacancy))], [])


def parse_single_vacancy(url: str) -> {}:
    vacancy = dict()
    bs4 = get_bs4_page(url)
    try:
        title = bs4.h1.text
        vacancy["title"] = title
    except Exception:
        print("element title not present")
    try:
        work_experience = bs4.find("span", {"data-qa": "vacancy-experience"}).text
        vacancy["work_experience"] = work_experience
    except Exception:
        print("element work_experience not present")
    try:
        region = bs4.find("p", {"data-qa": "vacancy-view-location"}).text
        vacancy["region"] = region
    except Exception:
        print("element work_experience not present")
    try:
        salary = bs4.find("span", {"data-qa": "vacancy-salary-compensation-type-net"}).text
        vacancy["salary"] = salary
    except Exception:
        print("element salary npt present")
    return vacancy


def main():
    data = {"data": []}
    for url in get_all_url_vacancy(VACANCY):
        data["data"].append(parse_single_vacancy(url))
    data["count"] = len(data["data"])
    with open("data.json", "w") as file:
        json.dump(data, file, ensure_ascii=False)


if __name__ == '__main__':
    main()
