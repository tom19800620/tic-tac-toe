import datetime
import math
from csv import writer

import requests
header_names = ['FIRST_NAME', 'LAST_NAME', 'GENDER', 'LOCATION_OF_MEDICAL_TRAINING', 'PROFESSIONAL_DEGREE_FROM',
                    'SERVICE_LINE', 'PARENT_FACILITY', 'ADDRESS', 'CITY', 'STATE', 'ZIP', 'OCCUPATION', 'SITE']
file_path = "C:\\Temp\\output\\provider.csv"
def write_header():
    with open(file_path, 'w', newline='') as f_object:
        writer_object = writer(f_object, delimiter=',', quotechar='"')
        writer_object.writerow(header_names)
        f_object.close()

def append_data(data1):

    with open(file_path, 'a', newline='') as f_object:
        writer_object = writer(f_object, quotechar='"')
        writer_object.writerow(data1)
        f_object.close()


def scrape_site() -> None:
    url1 = 'https://www.accesstocare.va.gov/OurProviders/SearchResults'
    header1 = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,he;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'www.accesstocare.va.gov',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    s = requests.session()
    r = s.get(url=url1, headers=header1, verify=False, timeout=6)
    # print(r.text)
    cookies = r.cookies.get_dict()
    print(cookies)
    ARRAffinity = cookies['ARRAffinity']
    ARRAffinitySameSite = cookies['ARRAffinitySameSite']
    # loop through each state
    # state_no = 1
    for state_no in range(1, 53):
        url2 = 'https://www.accesstocare.va.gov/capi/SearchResults?e=0&p=10&s=' + str(state_no) + '&'
        header2 = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,he;q=0.8',
            'Connection': 'keep-alive',
            'Cookie': 'ARRAffinity=' + ARRAffinity + '; ARRAffinitySameSite=' + ARRAffinitySameSite + '; ai_user=S8vSY|2022-12-21T10:54:47.043Z; _ga=GA1.3.648995513.1671620087; _gid=GA1.3.1075391321.1671620087; _gat_GSA_ENOR0=1; ai_session=9i1vn|1671620087198|1671620087198',
            'Host': 'www.accesstocare.va.gov',
            'Referer': 'https://www.accesstocare.va.gov/OurProviders/SearchResults',
            'Request-Id': '|Hhs8n.yRByc',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        }
        num_records = 0
        r1 = s.get(url=url2, headers=header2, verify=False, timeout=6)
        print(r1.status_code)
        print(r1.text)
        json = r1.json()
        total_records = math.ceil(json['c'])
        current_count = 0
        fetch_count = 10

        while current_count < total_records:
            # read date 10 records from results
            # header_desc = 'F=FNAME L=LNAME G=GENDER M=LOCATION_OF_M P=PROFESSION S=SERVICE_LINE V=PARENT_FAC A=ADDRESS ' \
            #               'Y=CITY T=STATE Z=ZIP O=OCCUPATION'
            for x in range(json['r'].__len__()):
                data1 = [json['r'][x]['f'], json['r'][x]['l'], json['r'][x]['g'], json['r'][x]['m'], json['r'][x]['p'],
                         json['r'][x]['s'], json['r'][x]['v'], json['r'][x]['a'], json['r'][x]['y'], json['r'][x]['t'],
                         json['r'][x]['z'], json['r'][x]['o'], url2]
                append_data(data1)
                print(data1)

            # increment count
            current_count += fetch_count
            url2 = 'https://www.accesstocare.va.gov/capi/SearchResults?e=' + str(current_count) + '&p=10&s=' + str(
                state_no) + '&'
            print(url2)
            print('Current count', current_count)
            # fetch next page
            r1 = s.get(url=url2, headers=header2, verify=False, timeout=6)
            json = r1.json()


if __name__ == '__main__':
    t1 = datetime.datetime.now()
    write_header()

    scrape_site()

    t2 = datetime.datetime.now() - t1
    print(t2)
    pass
