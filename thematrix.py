# Data Visualization report #2       
# by Ghicheon Lee


import networkx as nx
import matplotlib.pyplot as plt
import math
from textblob import TextBlob   #for sentiment analysis

#characters
nodes={}

#for edge
connections = {}

#result of sentiment analysis 
sentiments={}

#I got the matrix script from https://sfy.ru/transcript/matrix_ts
f1 =   open("matrix.txt")

#It return -1 to 1.  positive values mean good releationship.
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
            

#let's draw with networkx

G = nx.DiGraph()

G.add_edges_from(  connections.keys() )

hot_edges=[]
cold_edges=[]
for t in sentiments:
  if sentiments[t] > 0 :
        hot_edges.append(t)
  else:
        cold_edges.append(t)

pos = nx.spring_layout(G)
plt.figure()
plt.title("Relations & Sentiment analysis in The Matrix")

nx.draw_networkx_nodes(G,pos,node_color= 'g', alpha=0.7, node_size= [ nodes[n]*5 for n in G.nodes()] )
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G,pos,edgelist=hot_edges,edge_color='r',arrows=False)
nx.draw_networkx_edges(G,pos,edgelist=cold_edges,edge_color='b',arrows=False)
plt.axis('off')
plt.savefig("theMatrix.png") 
plt.show()



