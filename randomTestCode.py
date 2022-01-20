import numpy as np
import matplotlib.pyplot as plt
from timeit import timeit

# N = 10
# _s = np.random.rand(N)
# _t = np.random.rand(N)
# _u = np.random.rand(N)
# _v = np.random.rand(N)
# x = []
# y = []
# for s, t, u, v in zip(_s, _t, _u, _v):
#     x.append(s)
#     x.append(u)
#     x.append(None)
#     y.append(t)
#     y.append(v)
#     y.append(None)
# plt.plot(x, y)
# plt.show()

def process_sale(amount: str) -> float:
    without_dollar = amount[1:]
    return float(without_dollar)

def process_sales(amounts: [str]) -> [float]:
    result = []
    for amount in amounts:
        result.append(process_sale(amount))
    return result


def remove_bad_sales(commands: [str]) -> [str]:
    result = []
    for command in commands:
        if "$" in command:
            result.append(command)
    return result

def get_first_year(commands: [str]) -> [str]:
    result = []
    taking = True
    for command in commands:
        if command == "Happy new year":
            taking = False
        elif taking:
            result.append(command)
    return result

def average(amounts: [float]) -> float:
    if not amounts:
        return None
    total = 0
    count = 0
    for amount in amounts:
        total += amount
        count += 1
    return total/count

def average_sales(commands: str) -> float:
    commands = commands.split(",")
    commands = get_first_year(commands)
    commands = remove_bad_sales(commands)
    amounts = process_sales(commands)
    return average(amounts)

print(average_sales("$2.50,$4.50,$3.50"))
print(average_sales("$2.00,$4.00,Happy new year!,$5.00"))
print(average_sales("Happy new year!"))

# def average_sales(commands: str) -> float:
#     summed = 0
#     count = 0
#     taking = True
#     for command in commands.split(","):
#         if command == "Happy new year":
#             taking = False
#         elif taking:
#             if "$" in command:
#                 summed = summed + float(command[1:])
#             count += 1
#     if count:
#         return summed/count
#     else:
#         return None
#
# print(average_sales("what?,error?,Happy new year!"))
