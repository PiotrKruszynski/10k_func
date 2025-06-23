# for i in range(1,1001):
#     print(f'#{i}')
from functools import reduce


#1 policz pole kwadratu

def square_area(a):
    return a * a

assert square_area(2) == 4
assert square_area(4) == 16
assert square_area(10) == 100

#2 someone has gone and switched their heads and tails around! Save the animals by switching them back.
def fix_the_meerkat(arr):
    return arr[::-1]

assert fix_the_meerkat(["tail", "body", "head" ]) == ["head", "body", "tail"]
assert fix_the_meerkat([1,2,3 ]) == [3,2,1]

#3 someone has gone and switched their heads and tails around! Save the animals by switching them back.
def fix_the_meerkat_rev(arr):
    return list(reversed(arr))

assert fix_the_meerkat_rev(["tail", "body", "head" ]) == ["head", "body", "tail"]
assert fix_the_meerkat_rev([1,2,3 ]) == [3,2,1]

#4 Is it possible to get to the pump?

def zero_fuel(distance_to_pump, kpl, fuel_left):
    return kpl * fuel_left >= distance_to_pump

assert zero_fuel(50, 25, 2) == True
assert zero_fuel(50.1, 25, 2) == False
assert zero_fuel(0, 25, 2) == True

#5 Is even?

def is_even(number):
    return number % 2 == 0

assert is_even(2) == True
assert is_even(3) == False

#6 Is odd?

def is_odd(number):
    return number % 2 != 0

assert is_odd(3) == True
assert is_odd(2) == False

#7 generate hello

def greet(name, languages = 'polish'):
    greetings = {
        "polish": f'Cześć {name}',
        "english": f'Hello {name}',
        "spanish": f"Hola {name}"
    }
    return greetings.get(languages, f"Sorry we dont support {languages} language.")

assert greet("Piotr") == "Cześć Piotr"
assert greet("Anna", "german") == "Sorry we dont support german language."
assert greet("Piotr") == "Cześć Piotr"
assert greet("Piotr") == "Cześć Piotr"

#8 print numbers from 1 do range
def list_of_number(number):
    return [number +1 for number in range(number)]

assert list_of_number(5) == [1,2,3,4,5]
assert list_of_number(0) == []

#9 sorting by arguments
def sort_by_args(pairs):
    pairs.sort(key=lambda pair: pair[1])
    return pairs

assert sort_by_args([(1, 'b'), (2,'a')]) == [(2, 'a'), (1, 'b')]
assert sort_by_args([(1, 'b'), (2,'a'), (3,'c')]) == [(2, 'a'), (1, 'b'), (3,"c")]

#10 Is it plural ?
def plural(n):
    return n != 1

assert plural(0) == True
assert plural(1) == False
assert plural(1000) == True

#11 Adding numbers
def add(x,y):
    return x + y

assert add( 2,5) == 7
assert add(-2, 12) == 10

#12 Modulus-zwraca resztę z dzielenia
def modulo(a, b):
    return a % b

assert modulo(53,17) == 2
assert modulo(4,3) == 1

#13 Subtraction
def sub(a, b):
    return a - b

assert sub(10, 5) == 5
assert sub(2, 2) == 0

#14 multiplication
def multiplication(a, b):
    return a * b

assert multiplication(100, 3) == 300
assert multiplication(0, 4924371) == 0

#15 division
def div(a, b):
    return a / b

assert div(10,5) == 2
assert div(9, 4) == 2.25

#16 exponentation
def exponentation(a, b):
    return a ** b

assert exponentation(10,3) == 1000
assert exponentation(2, 5) == 32

#17 floor division
def floordivision(a, b):
    return a // b

assert floordivision(10, 9) == 1
assert floordivision(3, 4) == 0

#18 collecting union of sets
def sets_union(*sets):
    if not sets:
        return set()
    result = set()
    for s in sets:
        result |= s
    return result

assert sets_union({1, 2, 42, 666}, {42, 2, 3}, {666}) == {1,2,42,666,3}
assert sets_union(set()) == set()

#19 intersection_of_set
def sets_intersection(*sets):
    if not sets:
        return set()
    result = sets[0].copy()
    for s in sets[1:]:
        result &= s
    return result

assert sets_intersection({1, 2, 42, 666}, {42, 2, 3}, {42, 666, 2}) == {2, 42}

#20 mean values
def mean(*numbers):
    if not numbers:
        return None
    for n in numbers:
        if not isinstance(n, (int, float)):
            return None
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)

assert mean(1,3) == 2
assert mean(1, 'sfsvs') is None


#21 List append
def list_append(coll, item):
    coll.append(item)
    return coll

assert list_append([1,2,3], 'ala') == [1,2,3,'ala']
assert list_append([], 'ala') == ['ala']

#22 adding element to list
def magic_pro(item, array=None):
    if array is None:
        array = []
    array.append(item)
    return array

assert magic_pro(42) == [42]
assert magic_pro(42, [1,2,3]) == [1,2,3,42]

#23 Is palindrome?
def is_palindrome(text):
    return text.lower()[::-1] == text.lower()

assert is_palindrome('ALA') == True
assert is_palindrome('KAJAK') == True
assert is_palindrome('(())))') == False

#24 Memoize , pamięć podręczna, cache

def memoize():
    cache = {}

    def inner(a,b):
        key = f"{a},{b}"
        if key not in cache:
            # intensive CPU task
            cache[key] = a + b
        return cache[key]

    return inner

memoized_add = memoize()
assert memoized_add(2, 3) == 5
assert memoized_add(2, 3) == 5 # from cache

#25 Capitalize text
def capitalize(text):
    result = text.capitalize()
    return result

assert capitalize("ala") == "Ala"
assert capitalize("ala ma konta") == "Ala ma konta"

#26 Count element in collection
def count_item(coll, item):
    # czy sprawdzić, czy coś jest kolekcja? działa dla tuple i list
    return coll.count(item)

assert count_item(['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana'],'apple') == 2
assert count_item([],'') == 0
assert count_item(('orange', 'apple', 'pear'),'apple') == 1

#27 simple calculator
def calculator(x, y, op):
    operation = {
        "+": x + y,
        "-": x - y,
        "*": x * y,
        "/": x / y,
    }
    if op not in operation:
        return "unknown value"
    return operation[op]

assert calculator(2,3,"+") == 5
assert calculator(2,3,"-") == -1
assert calculator(2,3,"*") == 6


#28 better calculator
def calculator(x, y, op):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return "unknown value"

    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        if y == 0:
            return "unknown value"
        return x / y
    else:
        return "unknown value"

assert calculator(2,3,"+") == 5
assert calculator(2,3,"-") == -1
assert calculator(2,3,"*") == 6
assert calculator(6,3,"/") == 2
assert calculator(3,0,"/") == "unknown value"

#29 Koszerne rozwiązanie
def calculator(x,y,op):
    try:
        return {'+': x + y, '-': x - y, '*': x * y, '/': x / y}[op]
    except (TypeError, KeyError, ZeroDivisionError):
        return 'unknown value'

assert calculator(2,3,"+") == 5
assert calculator(2,3,"-") == -1
assert calculator(2,3,"*") == 6
assert calculator(6,3,"/") == 2
assert calculator(3,0,"/") == "unknown value"

#30 title
def title(text):
    return text.title()

sentence = 'ala ma kota i wszy'
assert title(sentence) == 'Ala Ma Kota I Wszy'

#31 reverse
def reverse(text):
    return text[::-1]

assert reverse(sentence) == 'yzsw i atok am ala'

#32 add_dot
def add_dot(text):
    return text + '.'

assert add_dot(sentence) == 'ala ma kota i wszy.'

#33 reduce
def all_in_one(*functions):
    return reduce(lambda acc, cb: cb(acc),functions, sentence)

assert all_in_one(title, reverse, add_dot) == 'yzsW I atoK aM alA.'

#34 Area or a circuit

def calc_area_or_circuit(height, width, kind='area'):
    if kind == 'area':
        return height * width
    else:
        return 2*(height + width)
assert calc_area_or_circuit(2,2) == 4
assert calc_area_or_circuit(0,2) == 0
assert calc_area_or_circuit(2,2, 'ala') == 8

#35 Is it hot?
def is_hot(temp):
    if temp <0:
        return 'zimno'
    elif temp >= 21:
        return 'ciepło'
    else:
        return 'chłodno'

assert is_hot(12) == 'chłodno'
assert is_hot(34) == 'ciepło'

#36 Return max from collection
def my_max(collection):
    temp = collection[0]
    for item in collection:
        if item > temp:
            temp = item
    return temp

assert my_max([1, 2, 3, 4, 5, 2]) == 5

#37 Average v1
def find_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

assert find_average([1,2,3]) == 2
assert find_average(0) == 0
assert find_average([-1,1]) == 0

#38 Average v2
def find_average(array):
    try:
        return sum(array) / len(array)
    except ZeroDivisionError:
        return 0

assert find_average([1,2,3]) == 2
assert find_average([0]) == 0
assert find_average([-1,1]) == 0

#39 Average v3
def find_average(array):
    if len(array) != 0:
        return sum(array) / len(array)
    else:
        return 0

#40 Average v4
def find_average(array):
    sum = 0
    for num in array:
        sum += num
    try:
        return sum/len(array)
    except ZeroDivisionError:
        return 0

#41 Is it empty?
def is_all(iterable):
    return all(iterable)

assert is_all([1,2,3]) == True
assert is_all([]) == True

#42 abs()
def is_abs(number):
    return abs(number)

assert is_abs(-7) == 7

#43 any()
def is_any(iterable):
    return any(iterable)

assert is_any([0, None, 42]) == True

#44 ascii
def is_ascii(text):
    return ascii(text)[1:-1]

assert is_ascii('ala') == 'ala'


#45 dict
def make_dict(sample):
    return dict(sample)

assert dict(a=1,b=42,c=4) == {'a':1,'b':42,'c':4}

#46 Napisz funkcję shorten, która przyjmie dowolnie długi napis, po czym zwróci skrót napisu, jak w przykładzie:
def shorten(text):
    text_list = text.split()
    return "".join([word.upper()[0] for word in text.split()])


assert shorten("Don't repeat yourself") == 'DRY'
assert shorten("Rage Against The Machine") == 'RATM'


#47 Napisz funkcję name_sorter, która przyjmie jako parametr listę imion.
def name_sorter(list_names):
    temp = {"female": [], "male": []}
    for name in list_names:
        if name[-1].upper() == "A":
            temp["female"].append(name)
        else:
            temp["male"] = []
            return temp["male"].append(name)

print(name_sorter(["Andrzej", "Henryk", "Alicja", "Cezary", "Barbara"]))
assert name_sorter(["Andrzej", "Henryk", "Alicja", "Cezary", "Barbara"]) == {'female': ['Alicja', 'Barbara'], 'male': ['Andrzej', 'Cezary', 'Henryk']}


#48
#49
#50
#51
#52
#53
#54
#55
#56
#57
#58
#59
#60
#61
#62
#63
#64
#65
#66
#67
#68
#69
#70
#71
#72
#73
#74
#75
#76
#77
#78
#79
#80
#81
#82
#83
#84
#85
#86
#87
#88
#89
#90
#91
#92
#93
#94
#95
#96
#97
#98
#99
#100
#101
#102
#103
#104
#105
#106
#107
#108
#109
#110
#111
#112
#113
#114
#115
#116
#117
#118
#119
#120
#121
#122
#123
#124
#125
#126
#127
#128
#129
#130
#131
#132
#133
#134
#135
#136
#137
#138
#139
#140
#141
#142
#143
#144
#145
#146
#147
#148
#149
#150
#151
#152
#153
#154
#155
#156
#157
#158
#159
#160
#161
#162
#163
#164
#165
#166
#167
#168
#169
#170
#171
#172
#173
#174
#175
#176
#177
#178
#179
#180
#181
#182
#183
#184
#185
#186
#187
#188
#189
#190
#191
#192
#193
#194
#195
#196
#197
#198
#199
#200
#201
#202
#203
#204
#205
#206
#207
#208
#209
#210
#211
#212
#213
#214
#215
#216
#217
#218
#219
#220
#221
#222
#223
#224
#225
#226
#227
#228
#229
#230
#231
#232
#233
#234
#235
#236
#237
#238
#239
#240
#241
#242
#243
#244
#245
#246
#247
#248
#249
#250
#251
#252
#253
#254
#255
#256
#257
#258
#259
#260
#261
#262
#263
#264
#265
#266
#267
#268
#269
#270
#271
#272
#273
#274
#275
#276
#277
#278
#279
#280
#281
#282
#283
#284
#285
#286
#287
#288
#289
#290
#291
#292
#293
#294
#295
#296
#297
#298
#299
#300
#301
#302
#303
#304
#305
#306
#307
#308
#309
#310
#311
#312
#313
#314
#315
#316
#317
#318
#319
#320
#321
#322
#323
#324
#325
#326
#327
#328
#329
#330
#331
#332
#333
#334
#335
#336
#337
#338
#339
#340
#341
#342
#343
#344
#345
#346
#347
#348
#349
#350
#351
#352
#353
#354
#355
#356
#357
#358
#359
#360
#361
#362
#363
#364
#365
#366
#367
#368
#369
#370
#371
#372
#373
#374
#375
#376
#377
#378
#379
#380
#381
#382
#383
#384
#385
#386
#387
#388
#389
#390
#391
#392
#393
#394
#395
#396
#397
#398
#399
#400
#401
#402
#403
#404
#405
#406
#407
#408
#409
#410
#411
#412
#413
#414
#415
#416
#417
#418
#419
#420
#421
#422
#423
#424
#425
#426
#427
#428
#429
#430
#431
#432
#433
#434
#435
#436
#437
#438
#439
#440
#441
#442
#443
#444
#445
#446
#447
#448
#449
#450
#451
#452
#453
#454
#455
#456
#457
#458
#459
#460
#461
#462
#463
#464
#465
#466
#467
#468
#469
#470
#471
#472
#473
#474
#475
#476
#477
#478
#479
#480
#481
#482
#483
#484
#485
#486
#487
#488
#489
#490
#491
#492
#493
#494
#495
#496
#497
#498
#499
#500
#501
#502
#503
#504
#505
#506
#507
#508
#509
#510
#511
#512
#513
#514
#515
#516
#517
#518
#519
#520
#521
#522
#523
#524
#525
#526
#527
#528
#529
#530
#531
#532
#533
#534
#535
#536
#537
#538
#539
#540
#541
#542
#543
#544
#545
#546
#547
#548
#549
#550
#551
#552
#553
#554
#555
#556
#557
#558
#559
#560
#561
#562
#563
#564
#565
#566
#567
#568
#569
#570
#571
#572
#573
#574
#575
#576
#577
#578
#579
#580
#581
#582
#583
#584
#585
#586
#587
#588
#589
#590
#591
#592
#593
#594
#595
#596
#597
#598
#599
#600
#601
#602
#603
#604
#605
#606
#607
#608
#609
#610
#611
#612
#613
#614
#615
#616
#617
#618
#619
#620
#621
#622
#623
#624
#625
#626
#627
#628
#629
#630
#631
#632
#633
#634
#635
#636
#637
#638
#639
#640
#641
#642
#643
#644
#645
#646
#647
#648
#649
#650
#651
#652
#653
#654
#655
#656
#657
#658
#659
#660
#661
#662
#663
#664
#665
#666
#667
#668
#669
#670
#671
#672
#673
#674
#675
#676
#677
#678
#679
#680
#681
#682
#683
#684
#685
#686
#687
#688
#689
#690
#691
#692
#693
#694
#695
#696
#697
#698
#699
#700
#701
#702
#703
#704
#705
#706
#707
#708
#709
#710
#711
#712
#713
#714
#715
#716
#717
#718
#719
#720
#721
#722
#723
#724
#725
#726
#727
#728
#729
#730
#731
#732
#733
#734
#735
#736
#737
#738
#739
#740
#741
#742
#743
#744
#745
#746
#747
#748
#749
#750
#751
#752
#753
#754
#755
#756
#757
#758
#759
#760
#761
#762
#763
#764
#765
#766
#767
#768
#769
#770
#771
#772
#773
#774
#775
#776
#777
#778
#779
#780
#781
#782
#783
#784
#785
#786
#787
#788
#789
#790
#791
#792
#793
#794
#795
#796
#797
#798
#799
#800
#801
#802
#803
#804
#805
#806
#807
#808
#809
#810
#811
#812
#813
#814
#815
#816
#817
#818
#819
#820
#821
#822
#823
#824
#825
#826
#827
#828
#829
#830
#831
#832
#833
#834
#835
#836
#837
#838
#839
#840
#841
#842
#843
#844
#845
#846
#847
#848
#849
#850
#851
#852
#853
#854
#855
#856
#857
#858
#859
#860
#861
#862
#863
#864
#865
#866
#867
#868
#869
#870
#871
#872
#873
#874
#875
#876
#877
#878
#879
#880
#881
#882
#883
#884
#885
#886
#887
#888
#889
#890
#891
#892
#893
#894
#895
#896
#897
#898
#899
#900
#901
#902
#903
#904
#905
#906
#907
#908
#909
#910
#911
#912
#913
#914
#915
#916
#917
#918
#919
#920
#921
#922
#923
#924
#925
#926
#927
#928
#929
#930
#931
#932
#933
#934
#935
#936
#937
#938
#939
#940
#941
#942
#943
#944
#945
#946
#947
#948
#949
#950
#951
#952
#953
#954
#955
#956
#957
#958
#959
#960
#961
#962
#963
#964
#965
#966
#967
#968
#969
#970
#971
#972
#973
#974
#975
#976
#977
#978
#979
#980
#981
#982
#983
#984
#985
#986
#987
#988
#989
#990
#991
#992
#993
#994
#995
#996
#997
#998
#999
#1000