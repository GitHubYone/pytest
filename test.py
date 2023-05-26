import numpy as np

n = 10
for _ in range(5):
    # 中点則
    w = 1 / n
    a = (np.arange(1, n + 1) - 0.5) * w
    b = 4.0 / (1.0 + a ** 2)
    p1 = np.sum(b) * w
    print(n, p1, np.pi - p1)

    # 台形則
    c = np.linspace(0, 1, n + 1)
    d = 4.0 / (1.0 + c ** 2)
    p2 = np.trapz(d) * w
    print(n, p2, np.pi - p2)

    # シンプソン則
    p3 = (p1 * 2 + p2) / 3
    print(n, p3, np.pi - p3)
    n *= 1

