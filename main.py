var_100 = "yüz"
var_1000 = "min"
list1 = ["bir", "iki", "üç", "dörd", "beş",
         "altı", "yeddi", "səkkiz", "doqquz"]
list2 = ["on", "iyirmi", "otuz", "qırx", "əlli",
         "altmış", "yetmiş", "səksən", "doxsan"]


def ones(a):
    for i in range(1, 10):
        if a == i:
            return list1[i-1]


def tens(a):
    for i in range(1, 10):
        if a == i:
            return list2[i-1]


def hundreds(a):
    for i in range(1, 10):
        if a == i:
            if i == 1:
                return var_100
            else:
                return ones(i) + " " + var_100


def thousands(a):
    for i in range(1, 10):
        if a == i:
            if i == 1:
                return var_1000
            else:
                return ones(i) + " " + var_1000


def convert_number_to_word(n):
    if len(str(n)) == 1:
        word = ones(n)
        return word
    elif len(str(n)) == 2:
        word = tens(n//10) + " " + ones(n % 10)
        return word
    elif len(str(n)) == 3:
        word = hundreds(n//100) + " " + tens((n//10) %
                                             10) + " " + ones(n % 10)
        return word
    elif len(str(n)) == 4:
        word = thousands(n//1000) + " " + hundreds((n//100) % 10) + \
            " " + tens((n//10) % 10) + " " + ones(n % 10)
        return word



