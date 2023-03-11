import matplotlib.pyplot as plt
import networkx as nx


class Grapher:

    def __init__(self, dict_set=None, word=None, whiter=False, labels=False, size=50, gtype='graph', pos='spring'):
        self.dict_set = dict_set
        self.word = word
        self.whiter = whiter
        self.labels = labels
        self.size = size
        self.gtype = gtype
        self.pos = pos

    def develop_graph(self):
        print(f"Graph mode : {self.gtype} | {self.pos} | {self.size} ")

        default_color = 'blue' if not self.whiter else 'white'
        g = nx.Graph() if self.gtype == 'graph' else nx.DiGraph()
        g.add_node(self.word, color='green' if not self.whiter else 'white')

        for key in self.dict_set:
            if key != self.word:
                g.add_node(key, color='red' if not self.whiter else 'white')
            for value in self.dict_set[key]:
                g.add_node(value)
                g.add_edge(key, value)

        plt.figure(figsize=(self.size, self.size))
        colored_dict = nx.get_node_attributes(g, 'color')
        color_seq = [colored_dict.get(node, default_color) for node in g.nodes()]
        d = dict(g.degree)

        # pos creation


        nx.draw(G=g,
                with_labels=self.labels,
                node_color=color_seq,
                nodelist=d.keys(),
                node_size=[v *150 for v in d.values()],
                pos=nx.spring_layout(g))

        plt.savefig("figure1.pdf")

    def live_graph(self, delay=5):

        print(f"Graph mode : {self.gtype} | {self.pos} | {self.size} ")

        default_color = 'blue' if not self.whiter else 'white'
        lg = nx.Graph() if self.gtype == 'graph' else nx.DiGraph()
        with plt.ion():

            plt.figure(figsize=(self.size, self.size))

            lg.add_node(self.word, color='green' if not self.whiter else 'white')
            for key in self.dict_set:
                if key != self.word:
                    lg.add_node(key, color='red' if not self.whiter else 'white')
                for value in self.dict_set[key]:
                    lg.add_node(value)
                    lg.add_edge(key, value)

                colored_dict = nx.get_node_attributes(lg, 'color')
                color_seq = [colored_dict.get(node, default_color) for node in lg.nodes()]
                d = dict(lg.degree)

                # pos creation


                plt.clf()
                nx.draw(G=lg,
                        with_labels=self.labels,
                        node_color=color_seq,
                        nodelist=d.keys(),
                        node_size=[v * 50 for v in d.values()],
                        pos=nx.spring_layout(lg))

                plt.pause(delay)
