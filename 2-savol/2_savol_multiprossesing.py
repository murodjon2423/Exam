import requests
from concurrent.futures import ProcessPoolExecutor

def save_page_as_pdf(url, pdf_filename):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        with open(pdf_filename, 'wb') as pdf_file:
            pdf_file.write(response.content)
        print(f'{url} sahifasi PDF formatiga olingan.')
    except Exception as e:
        print(f'Error downloading {url}: {e}')

def download_pages(base_url, page_num):
    url = base_url + str(page_num)
    pdf_filename = f'page_{page_num}.pdf'
    save_page_as_pdf(url, pdf_filename)

num_processes = 10

base_url = 'https://tilshunos.com/paronims/?page='

with ProcessPoolExecutor(max_workers=num_processes) as executor:
    for page_num in range(1, 11):
        executor.submit(download_pages, base_url, page_num)

print('Barcha sahifalar PDF formatiga olingan.')
