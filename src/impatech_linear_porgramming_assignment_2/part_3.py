import matplotlib.pyplot as plt
from .part_2 import grafo, img_original

# Criação da imagem nova
fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(img_original, cmap='gray')

# Arestas correspondentes às passagens livres
for u, v in grafo.arestas:
    x_u, y_u = grafo.coords[u]
    x_v, y_v = grafo.coords[v]
    
    ax.plot([x_u, x_v], [y_u, y_v], color='purple', linewidth=2, zorder=1)

# Vértices do grafo
for u in range(grafo.sz):
    x, y = grafo.coords[u]
    ax.scatter(x, y, color='blue', s=15, zorder=2)

# Vértices de entrada e saída
x_ent, y_ent = grafo.coords[0]
x_sai, y_sai = grafo.coords[grafo.sz - 1]
ax.scatter(x_ent, y_ent, color='green', s=67, label='Entrada', zorder=3)
ax.scatter(x_sai, y_sai, color='red', s=67, label='Saída', zorder=3)

# Exibição do gráfico
ax.set_title("Grafo sobreposto ao Labirinto")
ax.axis('off')
plt.show()