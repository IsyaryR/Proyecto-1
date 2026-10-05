import os
import math
from GrafoLib import (
    grafoMalla, grafoErdosRenyi, grafoGilbert,
    grafoGeografico, grafoBarabasiAlbert, grafoDorogovtsevMendes
)

TAMANOS = [50, 200, 500]
CARPETA = "grafos_generados"
os.makedirs(CARPETA, exist_ok=True)


def ruta(nombre, n):
    return os.path.join(CARPETA, f"{nombre}_{n}.dot")


for N in TAMANOS:
    print(f"\n=== N = {N} ===")

    # --- Malla (lo más cuadrada posible, con al menos N nodos) ---
    m = math.ceil(math.sqrt(N))
    filas = math.ceil(N / m)
    g = grafoMalla(m, filas)
    print(f"  Malla {m}x{filas}: {g.numeroNodos()} nodos, {g.numeroAristas()} aristas")
    g.guardarGraphViz(ruta("malla", N), f"Malla_{N}")

    # --- Erdös-Rényi ---
    m_aristas = 2 * N
    g = grafoErdosRenyi(N, m_aristas)
    print(f"  Erdos-Renyi: {g.numeroNodos()} nodos, {g.numeroAristas()} aristas")
    g.guardarGraphViz(ruta("erdos", N), f"Erdos_{N}")

    # --- Gilbert (p reducido para que escale con N) ---
    p = min(0.1, 4 / N)
    g = grafoGilbert(N, p)
    print(f"  Gilbert (p={p:.4f}): {g.numeroNodos()} nodos, {g.numeroAristas()} aristas")
    g.guardarGraphViz(ruta("gilbert", N), f"Gilbert_{N}")

    # --- Geografico ---
    r = 0.3
    g = grafoGeografico(N, r)
    print(f"  Geografico (r={r}): {g.numeroNodos()} nodos, {g.numeroAristas()} aristas")
    g.guardarGraphViz(ruta("geografico", N), f"Geografico_{N}")

    # --- Barabasi-Albert ---
    d = 3
    g = grafoBarabasiAlbert(N, d)
    print(f"  Barabasi-Albert (d={d}): {g.numeroNodos()} nodos, {g.numeroAristas()} aristas")
    g.guardarGraphViz(ruta("barabasi", N), f"Barabasi_{N}")

    # --- Dorogovtsev-Mendes ---
    g = grafoDorogovtsevMendes(N)
    print(f"  Dorogovtsev-Mendes: {g.numeroNodos()} nodos, {g.numeroAristas()} aristas")
    g.guardarGraphViz(ruta("dorogovtsev", N), f"Dorogovtsev_{N}")
