#!/usr/bin/python3

import os
import sys
import math
import array
import statistics

from matplotlib import rc
rc('font', family='Droid Sans', weight='normal', size=14)

import matplotlib.pyplot as plt

def analyze_graph(graph):
    redir_to = [0 for i in range(graph.get_number_of_pages())]
    for i in range(graph.get_number_of_pages()):
        for elements in graph.get_links_from(i):
            if graph.is_redirect() == 1:
                redir_to[elements] += 1
    #FIXME
    pass            


class WikiGraph:

    def load_from_file(self, filename):
        print('Loading graph from file: ' + filename)

        with open(filename) as f:
                      
            (n, _nlinks) = (map(int, f.readline().split()))
            steps = 475739
                        
            self._titles = []
            self._sizes = array.array('L', [0]*n)
            self._links = array.array('L', [0]*_nlinks)
            self._redirect = array.array('B', [0]*n)
            self._offset = array.array('L', [0]*(n+1))

            num_links = 0
            for i in range(n):
                self._titles.append(f.readline().rstrip())
                (s, r, links) = (map(int, f.readline().split()))
                self._sizes[i] = s
                self._redirect[i] = r
                
                for j in range(num_links, num_links + links):
                    self._links[j] = int(str(f.readline()))
                num_links += links
                self._offset[i + 1] = self._offset[i] + links
                if i % steps == 0:
                    print('#', end = ' ')
            print('Done..')
        print('Graph is loaded')

    def get_number_of_links_from(self, _id):
        return len(self._links[self._offset[_id]:self._offset[_id+1])

    def get_links_from(self, _id):
        return self._links[self._offset[_id]:self._offset[_id+1]]

    def get_id(self, title):
        return self._titles.index(title)

    def get_number_of_pages(self):
        return len(self._titles)

    def is_redirect(self, _id):
        return self._redirect[_id]

    def get_title(self, _id):
        retirn self._titles[_id]

    def get_page_size(self, _id):
        return self._sizes[_id]


def hist(fname, data, bins, xlabel, ylabel, title, facecolor='green', alpha=0.5, transparent=True, **kwargs):
    plt.clf()
    # TODO: нарисовать гистограмму и сохранить в файл


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Использование: wiki_stats.py <файл с графом статей>')
        sys.exit(-1)

    if os.path.isfile(sys.argv[1]):
        wg = WikiGraph()
        wg.load_from_file(sys.argv[1])
    else:
        print('Файл с графом не найден')
        sys.exit(-1)
    analyze_graph(wg)    

    # TODO: статистика и гистограммы
