import json
import random

import requests


# logging.basicConfig(filename="wiki.log", filemode='w', level=logging.DEBUG)
# logger = logging.getLogger(__name__)

# Select only a limit and that too random
class Wiki_graph_v2:

    def __init__(self):
        self.word = "Apple"
        self.iter_budget = 50
        self.word_set = set()
        self.dict_set = {}
        self.base_url = "https://en.wikipedia.org/api/rest_v1/page/related"
        self.g = None

    def set_word(self, word='Apple'):
        self.word = word

    def set_iter_budget(self, iter_budget=50):
        self.iter_budget = iter_budget

    def wiki_rel(self, word, random_seed=0, limit=6):
        self.word_set.add(word)
        word_list = []

        base_rel_url = f"{self.base_url}/{word}"
        resp = requests.get(base_rel_url)
        body = resp.json()

        for index, i in enumerate(body['pages']):
            title = i['title']
            word_list.append(title)
        random_sub_list = random.sample(word_list, limit)

        self.dict_set[word] = random_sub_list
        for val in random_sub_list:
            self.word_set.add(val)

        if random_seed == 0:
            # return random.choice(random_sub_list)
            return random_sub_list[random.randint(1, len(random_sub_list) - 1)]
        else:
            return random_sub_list[-1]

    def wiki_iter(self, random_seed=0, limit=6):
        word = self.word

        for iteration in range(self.iter_budget):
            next_word = self.wiki_rel(word, random_seed=random_seed, limit=limit)
            word = next_word

            print(f"Iteration {iteration + 1} done")

    def display(self):

        print(json.dumps(self.dict_set, indent=4))
