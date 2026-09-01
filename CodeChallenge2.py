
savings = int(input("Enter Amount to Deposit ="))

onekey = savings // 1000
remain1key = savings % 1000

fiveeach = remain1key // 500
remain5each = remain1key % 500

twoeach = remain5each // 200
remain2each = remain5each % 200

oneeach = remain2each // 100
remain1each = remain2each % 100

fefty = remain1each // 50
remainfefty = remain1each % 50

bente = remainfefty // 20
remainbente = remainfefty % 20

sampu = remainbente // 10
remainsampu = remainbente % 10


lima = remainsampu // 5
remainlima = remainsampu % 5

osip = remainlima // 1
remainosip = remainlima % 1



print("1000 =", onekey)
print("500 =", fiveeach)
print("200 =", twoeach)
print("100 =", oneeach)
print("50 =", fefty)
print("20 =", bente)
print("10 =", sampu)
print("5 =", lima)
print("1 = ", osip)
