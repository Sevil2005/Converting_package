n = int(input())
var_100 = "yüz"
var_1000 = "min"
list1 = ["bir", "iki", "üç", "dörd", "beş",
         "altı", "yeddi", "səkkiz", "doqquz"]
list2 = ["on", "iyirmi", "otuz", "qırx", "əlli",
         "altmış", "yetmiş", "səksən", "doqsan"]


def teklik(a):
    for i in range(1, 10):
        if a == i:
            return list1[i-1]


def onluq(a):
    for i in range(1, 10):
        if a == i:
            return list2[i-1]


def yuzluk(a):
    for i in range(1, 10):
        if a == i:
            if i == 1:
                return var_100
            else:
                return teklik(i) + " " + var_100


def minlik(a):
    for i in range(1, 10):
        if a == i:
            if i == 1:
                return var_1000
            else:
                return teklik(i) + " " + var_1000


if len(str(n)) == 1:
    print(teklik(n))
elif len(str(n)) == 2:
    print(onluq(n//10), teklik(n % 10))
elif len(str(n)) == 3:
    print(yuzluk(n//100), onluq((n//10) % 10), teklik(n % 10))
elif len(str(n)) == 4:
    print(minlik(n//1000), yuzluk((n//100) % 10),
          onluq((n//10) % 10), teklik(n % 10))