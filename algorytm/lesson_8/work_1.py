# 1) Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:

# func("papa") pap apa pa ap p a
# 6
# func("sova") sov ova so ov va s o v a
# 9

import hashlib

#print(hashlib.sha256(b'papa').hexdigest())

a = 'sova'  # s so sov sova
print(a[1:2+2])
#spam = hashlib.sha256(string[i].encode('utf-8')).hexdigest()

#pazz paz azz pa az zz p a z
#zzza zzz zza zz za z a
# aaaa aaa aa a

def m_hash(string):
    lst = []
    n = 1
    for i in range(len(string)):
        spam = hashlib.sha256(string[i].encode('utf-8')).hexdigest()
        if spam not in lst:
            lst.append(spam)
        n += 1
        for j in range(len(string)):
            spam = hashlib.sha256(string[i:j+n].encode('utf-8')).hexdigest()
            if spam not in lst:
                lst.append(spam)
    spam = hashlib.sha256(string.encode('utf-8')).hexdigest()
    if spam in lst:
        lst.remove(spam)

    return len(lst)




print(m_hash('aaaa'))#3
print(m_hash('zzza'))#6
print(m_hash('pazz'))#8
print(m_hash('sova'))#9
print(m_hash('papa'))#6
print(m_hash('papadsadasfg'))#69







