from algorithms import read_graph, dijkstra, PID_FROM_PTITLE, PTITLE_FROM_PID


if __name__ == '__main__':
    PATH = 'simple_english_wiki_pagelinks.csv'
    graph = read_graph(path=PATH, weithed=True)
    ana_alg_path = dijkstra(graph, PID_FROM_PTITLE['Analytics'],
                            PID_FROM_PTITLE['Algorithm'])
    print(len(''.join([PTITLE_FROM_PID[id] for id in ana_alg_path])))
    print('->'.join([PTITLE_FROM_PID[id] for id in ana_alg_path]))
    # Analytics->Data->Word->Letter->F->Logic->Algorithm
