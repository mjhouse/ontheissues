from bs4 import BeautifulSoup
import requests

class Search:

    def __init__(self, chamber:str, name: str):
        self.chamber = chamber.lower()
        self.name = name
        self.slug = '_'.join([p.capitalize() for p in name.split() if p])

        page = requests.get(f"https://www.ontheissues.org/{self.chamber}/{self.slug}.htm")
        
        if page.status_code != 200:
            raise RuntimeError("Could not find person")
        
        body = BeautifulSoup(page.text)

        print(page.text)

    def issues(self) -> list[str]:
        pass

    def positions(self, issue: str) -> list[str]:
        pass

    def quotes(self, issue: str) -> list[str]:
        pass

    def description(self) -> str:
        pass

