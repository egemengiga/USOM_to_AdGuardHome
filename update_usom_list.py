import requests

def update_usom_list():
    try:
        # USOM URL listesini indir
        url = "https://www.usom.gov.tr/url-list.txt"
        response = requests.get(url)

        if response.status_code == 200:
            url_list = response.text.splitlines()

            # URL'leri istenilen formata dönüştür
            formatted_urls = [f"||{url}^" for url in url_list]

            # Yeni formatta bir txt dosyasına yaz
            output_file = "formatted_url_list.txt"
            with open(output_file, "w") as file:
                for formatted_url in formatted_urls:
                    file.write(formatted_url + "\n")

            print(f"İşlem tamamlandı. Yeni dosya: {output_file}")
        else:
            print(f"URL listesini indirme başarısız oldu. Status code: {response.status_code}")
            print(response.text)  # Hata mesajını göster

    except Exception as e:
        print("Bir hata oluştu:", str(e))

if __name__ == "__main__":
    update_usom_list()
