import requests

class WikiGuessApp:
    WIKI_RANDOM_SUMMARY = "https://ro.wikipedia.org/api/rest_v1/page/random/summary"

    def __init__(self):
        self.options = "1 - articol nou, 2 - EXIT: "
        self.headers = {"User-Agent": "WikiGuessApp"}
    
    def display(self):
        print(
            "\nBun venit in aplicatia 'Wikipedia Guess'!\n"
            "Primesti TITLUL unui articol aleator de pe Wikipedia.\n"
            "Incearca sa ghicesti despre ce e vorba, apoi iti arat rezumatul.\n"
        )
    
    def get_random_article(self):
        try:
            response = requests.get(self.WIKI_RANDOM_SUMMARY,
                                    headers = self.headers,
                                    timeout = 10)
            response.raise_for_status()
            data = response.json()

            title = data.get("title", "Fara titlu")
            extract = data.get("extract", "Fara descriere")
            url = data.get("contents_urls", {}).get("desktop", {}).get("page", "")

            return title, extract, url
        except Exception as e:
            return "Eroare la preluarea articolului: ", str(e), ""
    
    def run(self):
        self.display()

        while True:
            choice = input(self.options).strip()

            if choice == "1":
                title, extract, url = self.get_random_article()

                if title.startswith("Eroare"):
                    print(title)
                    print(extract)
                    continue

                print(f"\nTitlu: {title}")
                input("Ce crezi ca este? Scrie pe scurt si apasa Enter: ")

                print("\n----- Rezumat -----")
                print(extract)

                if url:
                    print(f"\nPagina completa: {url}\n")
            elif choice == "2":
                print("La revedere!")
                break
            else:
                print("Alege comanda 1 sau 2.")

if __name__ == "__main__":
    app = WikiGuessApp()
    app.run()