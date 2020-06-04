import networkx as nx
import matplotlib.pyplot as plt
Gr = nx.gnm_random_graph(6,6)
plt.subplot(121)
nx.draw(Gr, with_labels=True, font_weight='bold')
print( "Медиана: ",nx.barycenter(Gr))
plt.show()