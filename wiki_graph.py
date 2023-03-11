import json
import random
import requests


# logging.basicConfig(filename="wiki.log", filemode='w', level=logging.DEBUG)
# logger = logging.getLogger(__name__)


# Create whole 20 points as nodes
class Wiki_graph:

    def __init__(self):
        self.word = "Apple"
        self.iter_budget = 50
        self.word_set = set()
        self.dict_set = {}
        self.base_url = "https://en.wikipedia.org/api/rest_v1/page/related"

    def set_word(self, word='Apple'):
        self.word = word

    def set_iter_budget(self, iter_budget=50):
        self.iter_budget = iter_budget

    def wiki_rel(self, word, random_seed=-1, limit=10):
        self.word_set.add(word)
        word_list = []

        base_rel_url = f"{self.base_url}/{word}"
        resp = requests.get(base_rel_url)
        body = resp.json()

        for index, i in enumerate(body['pages']):
            if index > limit:
                break
            title = i['title']
            word_list.append(title)
            self.word_set.add(title)

        self.dict_set[word] = word_list

        if random_seed == 0:
            # return random.choice(word_list)
            return word_list[random.randint(1, len(word_list) - 1)]
        else:
            return word_list[-1]

    def wiki_iter(self, random_seed=-1, limit=10):
        word = self.word

        for iteration in range(self.iter_budget):
            next_word = self.wiki_rel(word, random_seed=random_seed, limit=limit)
            word = next_word

            print(f"Iteration {iteration + 1} done")

    def display(self):

        print(json.dumps(self.dict_set, indent=4))
