import networkx as nx
import matplotlib.pyplot as plt
import math
from textblob import TextBlob

nodes={}
connections = {}
sentiments={}

#I got it from https://sfy.ru/transcript/matrix_ts
f1 =   open("matrix.txt")

def get_sentiment(s):
        ss = TextBlob(s)
        return ss.sentiment.polarity 

s='_'
while s:
        s  = f1.readline().replace('\r','').replace('\n','')
        record = s.split(':')
        if len(record) == 2:
                who = record[0].strip()
                sentence = record[1].strip()

                if who not in nodes:
                        nodes[who]= 1
                else:
                        nodes[who] += 1

                for p in nodes:
                        if p in sentence:
                                if (who,p) not in connections:
                                        connections[(who,p)]  = 1
                                        sentiments[(who,p)] = get_sentiment(sentence)
                                else:
                                        connections[(who,p)]  += 1
                                        sentiments[(who,p)] += get_sentiment(sentence)
            

G = nx.DiGraph()

G.add_edges_from(  connections.keys() )

#for n in G.nodes():
#    G[n][size] = nodes[n]


hot_edges = [ t  for t in sentiments  if sentiments[t] > 0 ]
cold_edges = [ t  for t in sentiments  if sentiments[t] <= 0 ]

pos = nx.spring_layout(G)
plt.figure()
plt.title("Relations in The Matrix")

nx.draw_networkx_nodes(G, pos, node_color = 'g', alpha=0.8, node_size = [ nodes[n]*5 for n in G.nodes()] )
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edgelist=hot_edges, edge_color='r', arrows=False)
nx.draw_networkx_edges(G, pos, edgelist=cold_edges,edge_color='b', arrows=False)

plt.axis('off')
plt.savefig("theMatrix.png") 
plt.show()



