from algorithms import (
    shortest_path,
    read_graph,
    PID_FROM_PTITLE,
    PTITLE_FROM_PID
    )


if __name__ == '__main__':
    PATH = 'simple_english_wiki_pagelinks.csv'
    graph = read_graph(PATH)
    ana_alg_path = shortest_path(graph, PID_FROM_PTITLE['Analytics'],
                                 PID_FROM_PTITLE['Algorithm'])
    print('->'.join([PTITLE_FROM_PID[id] for id in ana_alg_path]))
    # Analytics->Computer_programming->Computer_program->Computer_science->Algorithm
