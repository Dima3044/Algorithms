from time_tests import *
import numpy as np


bubble_sort_time = []
bubble_sort_optim_time = []
insertion_sort_time = []
selection_sort_time = []

N = [1000, 5000, 15000, 20000, 25000, 30000]

for n in N:
    print('Пузырьковая сортировка')
    bubble_sort_time.append(test_sort(n, bubble_sort))

    print('Пузырьковая сортировка с оптимизацией')
    bubble_sort_optim_time.append(test_sort(n, bubble_sort_optim))

    print('Сортировка вставками')
    insertion_sort_time.append(test_sort(n, insertion_sort))

    print('Сортировка выбором')
    selection_sort_time.append(test_sort(n, selection_sort))



data = np.array([bubble_sort_time, bubble_sort_optim_time, 
                 insertion_sort_time, selection_sort_time])

algorithms = ['Bubble', 'Bubble Opt', 'Insertion', 'Selection']
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']

fig, ax = plt.subplots(figsize=(10, 6))

x = np.arange(len(N))
width = 0.2

for i in range(len(algorithms)):
    offset = (i - len(algorithms)/2 + 0.5) * width
    ax.bar(x + offset, data[i], width, label=algorithms[i], 
           color=colors[i], alpha=0.8)

ax.set_xticks(x)
ax.set_xticklabels([f'N={n}' for n in N])
ax.set_ylabel('Время в секундах')
ax.set_title('Сравнение алгоритмов сортировок')
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('time_tests.png')
plt.show()
