from wiki_graph import Wiki_graph
from wiki_graph_v2 import Wiki_graph_v2
from Grapher import Grapher

if __name__ == '__main__':
    print('Hi User')

    # Uncomment the version you want to use

    wiki_obj = Wiki_graph()
    # wiki_obj = Wiki_graph_v2()

    wiki_obj.set_word("Shah_Rukh_Khan")
    wiki_obj.set_iter_budget(iter_budget=240)
    wiki_obj.wiki_iter(random_seed=0, limit=3)

    g = Grapher(dict_set=wiki_obj.dict_set,
                word=wiki_obj.word,
                whiter=False,
                labels=False,
                size=40)

    # Uncomment if you want a live grpah and the delay is in seconds.
    # g.live_graph(delay=2)
    g.develop_graph()
