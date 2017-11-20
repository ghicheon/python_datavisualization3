import networkx as nx
import matplotlib.pyplot as plt

nodes={}
connections = {}

#I got it from https://sfy.ru/transcript/matrix_ts
f1 =   open("matrix.txt")

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
                                else:
                                        connections[(who,p)]  += 1

G = nx.MultiGraph()

for (p1,p2) in connections:
    G.add_edge(p1,p2)

plt.figure()
plt.title("Relations in The Matrix")

pos=nx.spring_layout(G)

d = G.degree()
ll = []
for (a,b) in d:
    ll.append(b)

nx.draw(G,pos,with_labels=True,
            node_size=[ int(v)*100    for v in ll ], alpha=0.7 ,node_color='b' )


plt.show()



import math
from textblob import TextBlob

print(nodes)
print(connections.keys())
print(connections.values())
print(get_sentiment( "I love you very much more than anything."))
print(get_sentiment( "I hate it."))
print(get_sentiment( "I dont like it."))




########################################################################
# G = nx.Graph()
# size_list=[]
# 
# for n in nodes:
#     G.add_node(n,label=n)
#     size_list.append( nodes[n])
# 
# 
# for (p1,p2) in connections:
#     G.add_edge(p1,p2, weight = connections[(p1,p2)] )
# 
# plt.figure()
# plt.title("Relations in The Matrix")
# 
# 
# #nx.draw(G,node_size= size_list , font_size=10,with_labels=True)
# 
# pos=nx.spring_layout(G)
# 
# for n in nodes:
#         nx.draw_networkx(G,pos,nodelist= [n] , with_labels=True,
#                     node_size=[nodes[n]*10], alpha=0.7 ,node_color='b' )
# 
# plt.show()
# 
# 

#nx.draw_networkx_nodes(G,pos,nodelist= list(nodes.keys()) , with_labels=True,
#            node_size=[nodes[v]*10 for v in nodes], alpha=0.7 ,node_color='b')
#
#for from_to in connections:
#        nx.draw_networkx_edges(G,pos, edgelist=[from_to], 
#                               width= connections[from_to],alpha=0.7,edge_color='r')
#
#i=0
#labels={}
#for l in nodes.keys():
#    labels[i] = l
#    i += 1
#
#print(labels)
#
#nx.draw_networkx_labels(G,pos,labels,font_size=16)
#
#plt.axis('off')
#plt.savefig("theMatrix.png") 
#plt.show()
##################################################################################
