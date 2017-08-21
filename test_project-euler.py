import soph
import time
import itertools
import pandas
import numpy
from imp import reload
from fractions import Fraction
from collections import Counter
from math import factorial
import networkx as nx


def prob_1():
    multiples = [i for i in range(999, 1, -1) if (i % 3 == 0) or (i % 5 == 0)]
    return sum(multiples)


def test_1():
    assert soph.hash(prob_1()) == "e1edf9d1967ca96767dcc2b2d6df69f4"


def SubFibEven(startNumber, endNumber):
    for cur in soph.F():
        if cur % 2 == 0:
            if cur > endNumber:
                return
            if cur >= startNumber:
                yield cur


def prob_2():
    return sum(SubFibEven(0, 4 * 10**6))


def test_2():
    assert soph.hash(prob_2()) == "4194eb91842c8e7e6df099ca73c38f28"


def prob_3():
    return max(soph.prime_factors(600851475143))


def test_3():
    assert soph.hash(prob_3()) == "94c4dd41f9dddce696557d3717d98d82"


def prob_4():
    from itertools import combinations
    n = range(100, 1000)
    p = {numpy.prod(i) for i in combinations(n, 2)}
    pal = [i for i in p if str(i) == str(i)[::-1]]
    return max(pal)


def test_4():
    assert soph.hash(prob_4()) == "d4cfc27d16ea72a96b83d9bdef6ce2ec"


def divisible_thru_19(target):
    divisible = True
    d = 19
    while divisible:
        if target % d != 0:
            divisible = False
        if d == 3:
            break
        else:
            d -= 1
    return divisible


def prob_5():
    candidate = 40
    divisible = False

    while not divisible:
        if divisible_thru_19(candidate):
            divisible = True
        else:
            candidate += 20
    return candidate


def test_5():
    assert soph.hash(prob_5()) == "bc0d0a22a7a46212135ed0ba77d22f3a"


def prob_6():
    return sum(range(1, 101))**2 - sum([i**2 for i in range(1, 101)])


def test_6():
    assert soph.hash(prob_6()) == "867380888952c39a131fe1d832246ecc"


def prob_7():
    n = 0
    i = 2
    stop_flag = False
    while not stop_flag:
        if soph.is_prime(i):
            n += 1
        if n == 10001:
            stop_flag = True
        else:
            i += 1
    return i


def test_7():
    assert soph.hash(prob_7()) == "8c32ab09ec0210af60d392e9b2009560"


def prob_8():
    one_thousand = """
    73167176531330624919225119674426574742355349194934
    96983520312774506326239578318016984801869478851843
    85861560789112949495459501737958331952853208805511
    12540698747158523863050715693290963295227443043557
    66896648950445244523161731856403098711121722383113
    62229893423380308135336276614282806444486645238749
    30358907296290491560440772390713810515859307960866
    70172427121883998797908792274921901699720888093776
    65727333001053367881220235421809751254540594752243
    52584907711670556013604839586446706324415722155397
    53697817977846174064955149290862569321978468622482
    83972241375657056057490261407972968652414535100474
    82166370484403199890008895243450658541227588666881
    16427171479924442928230863465674813919123162824586
    17866458359124566529476545682848912883142607690042
    24219022671055626321111109370544217506941658960408
    07198403850962455444362981230987879927244284909188
    84580156166097919133875499200524063689912560717606
    05886116467109405077541002256983155200055935729725
    71636269561882670428252483600823257530420752963450
    """
    one_thousand = "".join(one_thousand.split())
    one_thousand_list = [int(i) for i in one_thousand]
    best = [0, 0]
    for i in range(len(one_thousand_list) - 13):
        if numpy.prod(one_thousand_list[i:i + 13]) > best[0]:
            best = [numpy.prod(one_thousand_list[i:i + 13]), i]
    return best[0]


def test_8():
    assert soph.hash(prob_8()) == "0f53ea7949d32ef24f9186207600403c"


def prob_9():
    from itertools import combinations
    candidates = [[c[0], c[1], numpy.sqrt(c[0]**2 + c[1]**2)]
                  for c in combinations(range(1, 999), 2)
                  if numpy.sqrt(c[0]**2 + c[1]**2) % 1 == 0]
    candidates = [c for c in candidates if sum(c) == 1000]
    answer = candidates[0]
    return int(numpy.prod(answer))


def test_9():
    assert soph.hash(prob_9()) == "24eaa9820350012ff678de47cb85b639"


def prob_10():
    return sum(soph.sieve_of_eratosthenes(2000000))


def test_10():
    assert soph.hash(prob_10()) == "d915b2a9ac8749a6b837404815f1ae25"


def prob_11():
    grid = """
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
    """
    grid = [int(i) for i in grid.split()]
    directions = [[0, -20, -40, -60],  # up
                  [0, 20, 40, 60],  # down
                  [0, -1, -2, -3],  # left
                  [0, 1, 2, 3],  # right
                  [0, -19, -38, -57],  # d1
                  [0, 21, 42, 53],  # d2
                  [0, 19, 38, 57],  # d3
                  [0, -21, -42, -53]]  # d4
    best = [0, 0]
    for i in range(len(grid) - 3 * 21):
        candidates = [[i + j for j in direction] for direction in directions]
        for c in candidates:
            try:
                product = numpy.prod([grid[j] for j in c])
            except:
                product = 0
            if product > best[0]:
                best = [product, c]
    return best[0]


def test_11():
    assert soph.hash(prob_11()) == "678f5d2e1eaa42f04fa53411b4f441ac"


def prob_12():
    return 0


def test_12():
    assert soph.hash(prob_12()) == "8091de7d285989bbfa9a2f9f3bdcc7c0"


def prob_13():
    return 0


def test_13():
    assert soph.hash(prob_13()) == "361113f19fd302adc31268f8283a4f2d"


def prob_14():
    return 0


def test_14():
    assert soph.hash(prob_14()) == "5052c3765262bb2c6be537abd60b305e"


def prob_15():
    return 0


def test_15():
    assert soph.hash(prob_15()) == "928f3957168ac592c4215dcd04e0b678"


def prob_16():
    return 0


def test_16():
    assert soph.hash(prob_16()) == "6a5889bb0190d0211a991f47bb19a777"


def prob_17():
    return 0


def test_17():
    assert soph.hash(prob_17()) == "6a979d4a9cf85135408529edc8a133d0"


def prob_18():
    return 0


def test_18():
    assert soph.hash(prob_18()) == "708f3cf8100d5e71834b1db77dfa15d6"


def prob_19():
    return 0


def test_19():
    assert soph.hash(prob_19()) == "a4a042cf4fd6bfb47701cbc8a1653ada"


def prob_20():
    return 0


def test_20():
    assert soph.hash(prob_20()) == "443cb001c138b2561a0d90720d6ce111"


def prob_21():
    return 0


def test_21():
    assert soph.hash(prob_21()) == "51e04cd4e55e7e415bf24de9e1b0f3ff"


def prob_22():
    return 0


def test_22():
    assert soph.hash(prob_22()) == "f2c9c91cb025746f781fa4db8be3983f"


def prob_23():
    return 0


def test_23():
    assert soph.hash(prob_23()) == "2c8258c0604152962f7787571511cf28"


def prob_24():
    return 0


def test_24():
    assert soph.hash(prob_24()) == "7f155b45cb3f0a6e518d59ec348bff84"


def prob_25():
    return 0


def test_25():
    assert soph.hash(prob_25()) == "a376802c0811f1b9088828288eb0d3f0"


def prob_26():
    return 0


def test_26():
    assert soph.hash(prob_26()) == "6aab1270668d8cac7cef2566a1c5f569"


def prob_27():
    return 0


def test_27():
    assert soph.hash(prob_27()) == "69d9e3218fd7abb6ff453ea96505183d"


def prob_28():
    return 0


def test_28():
    assert soph.hash(prob_28()) == "0d53425bd7c5bf9919df3718c8e49fa6"


def prob_29():
    return 0


def test_29():
    assert soph.hash(prob_29()) == "6f0ca67289d79eb35d19decbc0a08453"


def prob_30():
    return 0


def test_30():
    assert soph.hash(prob_30()) == "27a1779a8a8c323a307ac8a70bc4489d"


def prob_31():
    return 0


def test_31():
    assert soph.hash(prob_31()) == "142dfe4a33d624d2b830a9257e96726d"


def prob_32():
    return 0


def test_32():
    assert soph.hash(prob_32()) == "100f6e37d0b0564490a2ee27eff0660d"


def prob_33():
    return 0


def test_33():
    assert soph.hash(prob_33()) == "f899139df5e1059396431415e770c6dd"


def prob_34():
    return 0


def test_34():
    assert soph.hash(prob_34()) == "60803ea798a0c0dfb7f36397d8d4d772"


def prob_35():
    return 0


def test_35():
    assert soph.hash(prob_35()) == "b53b3a3d6ab90ce0268229151c9bde11"


def prob_36():
    return 0


def test_36():
    assert soph.hash(prob_36()) == "0e175dc2f28833885f62e7345addff03"


def prob_37():
    return 0


def test_37():
    assert soph.hash(prob_37()) == "cace46c61b00de1b60874936a093981d"


def prob_38():
    return 0


def test_38():
    assert soph.hash(prob_38()) == "f2a29ede8dc9fae7926dc7a4357ac25e"


def prob_39():
    return 0


def test_39():
    assert soph.hash(prob_39()) == "fa83a11a198d5a7f0bf77a1987bcd006"


def prob_40():
    return 0


def test_40():
    assert soph.hash(prob_40()) == "6f3ef77ac0e3619e98159e9b6febf557"


def prob_41():
    return 0


def test_41():
    assert soph.hash(prob_41()) == "d0a1bd6ab4229b2d0754be8923431404"


def prob_42():
    return 0


def test_42():
    assert soph.hash(prob_42()) == "82aa4b0af34c2313a562076992e50aa3"


def prob_43():
    return 0


def test_43():
    assert soph.hash(prob_43()) == "115253b7721af0fdff25cd391dfc70cf"


def prob_44():
    return 0


def test_44():
    assert soph.hash(prob_44()) == "2c2556cb85621309ca647465ffa62370"


def prob_45():
    return 0


def test_45():
    assert soph.hash(prob_45()) == "30dfe3e3b286add9d12e493ca7be63fc"


def prob_46():
    return 0


def test_46():
    assert soph.hash(prob_46()) == "89abe98de6071178edb1b28901a8f459"


def prob_47():
    return 0


def test_47():
    assert soph.hash(prob_47()) == "748f517ecdc29106e2738f88aa7530f4"


def prob_48():
    return 0


def test_48():
    assert soph.hash(prob_48()) == "0829124724747ae1c65da8cae5263346"


def prob_49():
    return 0


def test_49():
    assert soph.hash(prob_49()) == "0b99933d3e2a9addccbb663d46cbb592"


def prob_50():
    return 0


def test_50():
    assert soph.hash(prob_50()) == "73229bab6c5dc1c7cf7a4fa123caf6bc"


def prob_51():
    return 0


def test_51():
    assert soph.hash(prob_51()) == "e2a8daa5eb919905dadd795593084c22"


def prob_52():
    return 0


def test_52():
    assert soph.hash(prob_52()) == "a420384997c8a1a93d5a84046117c2aa"


def prob_53():
    return 0


def test_53():
    assert soph.hash(prob_53()) == "e3b21256183cf7c2c7a66be163579d37"


def prob_54():
    return 0


def test_54():
    assert soph.hash(prob_54()) == "142949df56ea8ae0be8b5306971900a4"


def prob_55():
    return 0


def test_55():
    assert soph.hash(prob_55()) == "077e29b11be80ab57e1a2ecabb7da330"


def prob_56():
    return 0


def test_56():
    assert soph.hash(prob_56()) == "c22abfa379f38b5b0411bc11fa9bf92f"


def prob_57():
    return 0


def test_57():
    assert soph.hash(prob_57()) == "b3e3e393c77e35a4a3f3cbd1e429b5dc"


def prob_58():
    return 0


def test_58():
    assert soph.hash(prob_58()) == "b62fc92a2561538525c89be63f36bf7b"


def prob_59():
    return 0


def test_59():
    assert soph.hash(prob_59()) == "68f891fe214e2bfa07c998ad5d0a390f"


def prob_60():
    return 0


def test_60():
    assert soph.hash(prob_60()) == "68f891fe214e2bfa07c998ad5d0a390f"


def prob_61():
    return 0


def test_61():
    assert soph.hash(prob_61()) == "68f891fe214e2bfa07c998ad5d0a390f"


def prob_62():
    return 0


def test_62():
    assert soph.hash(prob_62()) == "68f891fe214e2bfa07c998ad5d0a390f"


def prob_63():
    return 0


def test_63():
    assert soph.hash(prob_63()) == "68f891fe214e2bfa07c998ad5d0a390f"


def prob_64():
    return 0


def test_64():
    assert soph.hash(prob_64()) == "68f891fe214e2bfa07c998ad5d0a390f"


def prob_65():
    return 0


def test_65():
    assert soph.hash(prob_65()) == "68f891fe214e2bfa07c998ad5d0a390f"
