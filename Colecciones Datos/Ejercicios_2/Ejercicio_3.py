import operator
resultados = [
    '0013',
    '0023',
    '0054',
    '0072',
    '0189',
    '0198',
    '0214',
    '0222',
    '0251',
    '0252',
    '0270',
    '0286',
    '0358',
    '0386',
    '0428',
    '0526',
    '0529',
    '0533',
    '0551',
    '0589',
    '0700',
    '0756',
    '0779',
    '0785',
    '0792',
    '0852',
    '0856',
    '1083',
    '1091',
    '1095',
    '1120',
    '1155',
    '1253',
    '1266',
    '1271',
    '1287',
    '1293',
    '1449',
    '1468',
    '1511',
    '1544',
    '1588',
    '1667',
    '1680',
    '1692',
    '1692',
    '1780',
    '1803',
    '1814',
    '1819',
    '1878',
    '1943',
    '1964',
    '1999',
    '2003',
    '2077',
    '2081',
    '2115',
    '2123',
    '2161',
    '2201',
    '2376',
    '2383',
    '2403',
    '2433',
    '2451',
    '2502',
    '2508',
    '2520',
    '2555',
    '2661',
    '2667',
    '2690',
    '2730',
    '2735',
    '2743',
    '2818',
    '2917',
    '2975',
    '2989',
    '3004',
    '3013',
    '3043',
    '3047',
    '3087',
    '3106',
    '3119',
    '3130',
    '3187',
    '3192',
    '3243',
    '3247',
    '3352',
    '3386',
    '3391',
    '3393',
    '3452',
    '3459',
    '3463',
    '3587',
    '3639',
    '3689',
    '3986',
    '3991',
    '3997',
    '4062',
    '4071',
    '4081',
    '4186',
    '4232',
    '4243',
    '4287',
    '4299',
    '4357',
    '4378',
    '4416',
    '4436',
    '0446',
    '4469',
    '4501',
    '4513',
    '4534',
    '4566',
    '4590',
    '4615',
    '4650',
    '4655',
    '4672',
    '4746',
    '4798',
    '4824',
    '4836',
    '4861',
    '5011',
    '5044',
    '5118',
    '5226',
    '5325',
    '5364',
    '5404',
    '5416',
    '5504',
    '5570',
    '5610',
    '5637',
    '5648',
    '5664',
    '5707',
    '5723',
    '5761',
    '5762',
    '5775',
    '5813',
    '5837',
    '5865',
    '5932',
    '5935',
    '6027',
    '6092',
    '6125',
    '6145',
    '6219',
    '6289',
    '6325',
    '6409',
    '6409',
    '6434',
    '6490',
    '6598',
    '6629',
    '6698',
    '6805',
    '6809',
    '6850',
    '6900',
    '6903',
    '6919',
    '6954',
    '7095',
    '7143',
    '7202',
    '7249',
    '7280',
    '7303',
    '7327',
    '7371',
    '7381',
    '7420',
    '7423',
    '7452',
    '7461',
    '7483',
    '7490',
    '7492',
    '7522',
    '7608',
    '7627',
    '7630',
    '7639',
    '7640',
    '7713',
    '7773',
    '7816',
    '7842',
    '7848',
    '7974',
    '8002',
    '8008',
    '8028',
    '8034',
    '8083',
    '8149',
    '8183',
    '8309',
    '8325',
    '8344',
    '8355',
    '8368',
    '8378',
    '8435',
    '8495',
    '8513',
    '8538',
    '8553',
    '8573',
    '8584',
    '8604',
    '8630',
    '8661',
    '8780',
    '8824',
    '8894',
    '8906',
    '8923',
    '8930',
    '8961',
    '8985',
    '9098',
    '9164',
    '9205',
    '9209',
    '9240',
    '9267',
    '9269',
    '9279',
    '9318',
    '9511',
    '9535',
    '9560',
    '9567',
    '9722',
    '9749',
    '9753',
    '9774',
    '9797',
    '9820',
    '9829',
    '9831',
    '9839',
    '9853',
    '9862',
    '9862',
    '9862',
    '9862',
    '9898',
    '9955',
    '9973',
    '9999',
    '5149'
]

resultados.sort()

resultados2 = []

for resultado in resultados:

    x = [int(numero) for numero in list(resultado)]

    x.sort()

    resultados2.append(''.join(map(str, x)))


mas_salen = {}


resultados2.sort()



for resultado in resultados2:
    try:
        mas_salen[resultado]
    except KeyError:
        mas_salen[resultado] = 0

    mas_salen[resultado] += 1


res = sorted(mas_salen.items(), key=operator.itemgetter(1))
res.reverse()
print(res)
print("======================================================================")
print("Permutaciones")
from itertools import *
lista = list(permutations([2,6,8,9]))
print(len(lista))
print(lista)