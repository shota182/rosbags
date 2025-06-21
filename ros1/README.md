# 概要

bagファイルの説明

---

## ```/home/sskr3/bags/ros1/2025-05-11-16-27-40.bag```

### ```rosbag info 2025-05-11-16-27-40.bag```

```
path:        2025-05-11-16-27-40.bag
version:     2.0
duration:    1:32s (92s)
start:       May 11 2025 16:27:40.96 (1746948460.96)
end:         May 11 2025 16:29:13.50 (1746948553.50)
size:        1.4 MB
messages:    15812
compression: none [2/2 chunks]
types:       diagnostic_msgs/DiagnosticArray [60810da900de1dd6ddd437c3503511da]
             rosgraph_msgs/Log               [acffd30cd6b6de30f120938c17c593fb]
             sensor_msgs/Joy                 [5a9ea5f83505693b71e785041e67a8bb]
             std_msgs/Int32MultiArray        [1d99f79f8b325b44fee908053e9c945b]
topics:      /diagnostics                      82 msgs    : diagnostic_msgs/DiagnosticArray
             /joy                             575 msgs    : sensor_msgs/Joy                
             /rosout                            7 msgs    : rosgraph_msgs/Log               (2 connections)
             /sensor/mag                     1846 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/input/position    4616 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/current    4343 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/position   4343 msgs    : std_msgs/Int32MultiArray
```

### 説明

曲げたときに張力センサの値がちゃんと変化するか確かめるために実行したもののbagファイル。

extended位置制御による実行であり，```/sensor/motor/output/position```が制御したもの。
値が減るとワイヤが引っ張られる。

```/sensor/mag```の0，2番目の要素が増加していることがわかる。

---

## ```/home/sskr3/bags/ros1/2025-05-11-17-37-45.bag```

### ```rosbag info 2025-05-11-17-37-45.bag```

```
path:        2025-05-11-17-37-45.bag
version:     2.0
duration:    46.6s
start:       May 11 2025 17:37:45.29 (1746952665.29)
end:         May 11 2025 17:38:31.92 (1746952711.92)
size:        632.6 KB
messages:    7328
compression: none [1/1 chunks]
types:       diagnostic_msgs/DiagnosticArray [60810da900de1dd6ddd437c3503511da]
             rosgraph_msgs/Log               [acffd30cd6b6de30f120938c17c593fb]
             sensor_msgs/Joy                 [5a9ea5f83505693b71e785041e67a8bb]
             std_msgs/Int32MultiArray        [1d99f79f8b325b44fee908053e9c945b]
topics:      /diagnostics                      42 msgs    : diagnostic_msgs/DiagnosticArray
             /joy                             127 msgs    : sensor_msgs/Joy                
             /rosout                            7 msgs    : rosgraph_msgs/Log               (2 connections)
             /sensor/mag                      464 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/input/position    2320 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/current    2184 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/position   2184 msgs    : std_msgs/Int32MultiArray
```

### 説明

一定ステップ速度でモータを動かしたときに張力値がどのように変化するのか確認するためのbagファイル。
```/sensor/mag```の要素0が対象。

---

## ```/home/sskr3/bags/ros1/2025-05-11-17-46-12.bag```

### ```rosbag info 2025-05-11-17-46-12.bag```

```
path:        2025-05-11-17-46-12.bag
version:     2.0
duration:    1:16s (76s)
start:       May 11 2025 17:46:12.60 (1746953172.60)
end:         May 11 2025 17:47:29.17 (1746953249.17)
size:        1000.7 KB
messages:    11653
compression: none [2/2 chunks]
types:       diagnostic_msgs/DiagnosticArray [60810da900de1dd6ddd437c3503511da]
             rosgraph_msgs/Log               [acffd30cd6b6de30f120938c17c593fb]
             sensor_msgs/Joy                 [5a9ea5f83505693b71e785041e67a8bb]
             std_msgs/Int32MultiArray        [1d99f79f8b325b44fee908053e9c945b]
topics:      /diagnostics                      65 msgs    : diagnostic_msgs/DiagnosticArray
             /joy                             334 msgs    : sensor_msgs/Joy                
             /rosout                            7 msgs    : rosgraph_msgs/Log               (2 connections)
             /sensor/mag                      764 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/input/position    3584 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/current    3449 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/position   3450 msgs    : std_msgs/Int32MultiArray
```

### 説明

上と同じ

---

## ```/home/sskr3/bags/ros1/2025-05-11-17-55-37.bag```

### ```rosbag info 2025-05-11-17-55-37.bag```

```
path:        2025-05-11-17-55-37.bag
version:     2.0
duration:    1:13s (73s)
start:       May 11 2025 17:55:37.10 (1746953737.10)
end:         May 11 2025 17:56:50.39 (1746953810.39)
size:        965.2 KB
messages:    11447
compression: none [2/2 chunks]
types:       diagnostic_msgs/DiagnosticArray [60810da900de1dd6ddd437c3503511da]
             rosgraph_msgs/Log               [acffd30cd6b6de30f120938c17c593fb]
             sensor_msgs/Joy                 [5a9ea5f83505693b71e785041e67a8bb]
             std_msgs/Int32MultiArray        [1d99f79f8b325b44fee908053e9c945b]
topics:      /diagnostics                      68 msgs    : diagnostic_msgs/DiagnosticArray
             /joy                             115 msgs    : sensor_msgs/Joy                
             /rosout                            7 msgs    : rosgraph_msgs/Log               (2 connections)
             /sensor/mag                      730 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/input/position    3651 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/current    3438 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/position   3438 msgs    : std_msgs/Int32MultiArray
```

### 説明

目的は上と同じ。
各ポイント(張力0，張力最大)で5[sec]程度モータ入力を止めた。

---

## ```/home/sskr3/bags/ros1/2025-05-18-11-56-46.bag```

### ```rosbag info /home/sskr3/bags/ros1/2025-05-18-11-56-46.bag```

```
path:        /home/sskr3/bags/ros1/2025-05-18-11-56-46.bag
version:     2.0
duration:    29.9s
start:       May 18 2025 11:56:46.60 (1747537006.60)
end:         May 18 2025 11:57:16.47 (1747537036.47)
size:        407.8 KB
messages:    4634
compression: none [1/1 chunks]
types:       diagnostic_msgs/DiagnosticArray [60810da900de1dd6ddd437c3503511da]
             rosgraph_msgs/Log               [acffd30cd6b6de30f120938c17c593fb]
             sensor_msgs/Joy                 [5a9ea5f83505693b71e785041e67a8bb]
             std_msgs/Int32MultiArray        [1d99f79f8b325b44fee908053e9c945b]
topics:      /diagnostics                      27 msgs    : diagnostic_msgs/DiagnosticArray
             /joy                              39 msgs    : sensor_msgs/Joy                
             /rosout                            7 msgs    : rosgraph_msgs/Log               (2 connections)
             /sensor/mag                      295 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/input/position    1480 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/current    1393 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/position   1393 msgs    : std_msgs/Int32MultiArray
```

### 説明

固定端でモータ1を引っ張ったときのmagを見るためのデータ．

---

## ```/home/sskr3/bags/ros1/2025-05-18-11-57-21.bag```

### ```rosbag info /home/sskr3/bags/ros1/2025-05-18-11-57-21.bag```

```
path:        /home/sskr3/bags/ros1/2025-05-18-11-57-21.bag
version:     2.0
duration:    52.6s
start:       May 18 2025 11:57:21.96 (1747537041.96)
end:         May 18 2025 11:58:14.54 (1747537094.54)
size:        707.8 KB
messages:    8258
compression: none [1/1 chunks]
types:       diagnostic_msgs/DiagnosticArray [60810da900de1dd6ddd437c3503511da]
             rosgraph_msgs/Log               [acffd30cd6b6de30f120938c17c593fb]
             sensor_msgs/Joy                 [5a9ea5f83505693b71e785041e67a8bb]
             std_msgs/Int32MultiArray        [1d99f79f8b325b44fee908053e9c945b]
topics:      /diagnostics                      48 msgs    : diagnostic_msgs/DiagnosticArray
             /joy                             126 msgs    : sensor_msgs/Joy                
             /rosout                            7 msgs    : rosgraph_msgs/Log               (2 connections)
             /sensor/mag                      524 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/input/position    2619 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/current    2467 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/position   2467 msgs    : std_msgs/Int32MultiArray
```

### 説明

上と同じ．

---

## ```/home/sskr3/bags/ros1/2025-05-18-12-16-11.bag```

### ```rosbag info /home/sskr3/bags/ros1/2025-05-18-12-16-11.bag```

```
path:        /home/sskr3/bags/ros1/2025-05-18-12-16-11.bag
version:     2.0
duration:    58.0s
start:       May 18 2025 12:16:11.65 (1747538171.65)
end:         May 18 2025 12:17:09.67 (1747538229.67)
size:        768.2 KB
messages:    9053
compression: none [1/1 chunks]
types:       diagnostic_msgs/DiagnosticArray [60810da900de1dd6ddd437c3503511da]
             rosgraph_msgs/Log               [acffd30cd6b6de30f120938c17c593fb]
             sensor_msgs/Joy                 [5a9ea5f83505693b71e785041e67a8bb]
             std_msgs/Int32MultiArray        [1d99f79f8b325b44fee908053e9c945b]
topics:      /diagnostics                      53 msgs    : diagnostic_msgs/DiagnosticArray
             /joy                              81 msgs    : sensor_msgs/Joy                
             /rosout                            7 msgs    : rosgraph_msgs/Log               (2 connections)
             /sensor/mag                      578 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/input/position    2890 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/current    2722 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/position   2722 msgs    : std_msgs/Int32MultiArray
```

### 説明

上と同じ．

---

## ```/home/sskr3/bags/ros1/2025-05-18-13-40-12.bag```

### ```rosbag info /home/sskr3/bags/ros1/2025-05-18-13-40-12.bag```

```
path:        /home/sskr3/bags/ros1/2025-05-18-13-40-12.bag
version:     2.0
duration:    5:02s (302s)
start:       May 18 2025 13:40:12.83 (1747543212.83)
end:         May 18 2025 13:45:15.80 (1747543515.80)
size:        3.8 MB
messages:    47484
compression: none [5/5 chunks]
types:       diagnostic_msgs/DiagnosticArray [60810da900de1dd6ddd437c3503511da]
             rosgraph_msgs/Log               [acffd30cd6b6de30f120938c17c593fb]
             sensor_msgs/Joy                 [5a9ea5f83505693b71e785041e67a8bb]
             std_msgs/Int32MultiArray        [1d99f79f8b325b44fee908053e9c945b]
topics:      /diagnostics                      290 msgs    : diagnostic_msgs/DiagnosticArray
             /joy                              520 msgs    : sensor_msgs/Joy                
             /rosout                             7 msgs    : rosgraph_msgs/Log               (2 connections)
             /sensor/mag                      3027 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/input/position    15138 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/current    14251 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/position   14251 msgs    : std_msgs/Int32MultiArray
```

### 説明

マニピュレータの片側にワイヤを通したもの．
ゆっくり引っ張って止めるー＞緩める．
モータステップ角変化は線形

---

## ```/home/sskr3/bags/ros1/2025-05-18-14-05-19.bag```

### ```rosbag info /home/sskr3/bags/ros1/2025-05-18-14-05-19.bag```

```
path:        /home/sskr3/bags/ros1/2025-05-18-14-05-19.bag
version:     2.0
duration:    2:36s (156s)
start:       May 18 2025 14:05:19.38 (1747544719.38)
end:         May 18 2025 14:07:56.20 (1747544876.20)
size:        2.0 MB
messages:    24340
compression: none [3/3 chunks]
types:       diagnostic_msgs/DiagnosticArray [60810da900de1dd6ddd437c3503511da]
             rosgraph_msgs/Log               [acffd30cd6b6de30f120938c17c593fb]
             sensor_msgs/Joy                 [5a9ea5f83505693b71e785041e67a8bb]
             std_msgs/Int32MultiArray        [1d99f79f8b325b44fee908053e9c945b]
topics:      /diagnostics                     154 msgs    : diagnostic_msgs/DiagnosticArray
             /joy                              36 msgs    : sensor_msgs/Joy                
             /rosout                            7 msgs    : rosgraph_msgs/Log               (2 connections)
             /sensor/mag                     1566 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/input/position    7830 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/current    7373 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/position   7374 msgs    : std_msgs/Int32MultiArray
```

### 説明

マニピュレータの引っ張りの実験．上と同じ．
ピーク部分が，巻取りを止めたときに変化している気がしたので調べるため．
ピーク部分で少し長い時間止めるようにした．

---

## ```/home/sskr3/bags/ros1/2025-05-18-14-29-33.bag```

### ```rosbag info /home/sskr3/bags/ros1/2025-05-18-14-29-33.bag```

```
path:        /home/sskr3/bags/ros1/2025-05-18-14-29-33.bag
version:     2.0
duration:    2:32s (152s)
start:       May 18 2025 14:29:33.28 (1747546173.28)
end:         May 18 2025 14:32:06.10 (1747546326.10)
size:        2.1 MB
messages:    24859
compression: none [3/3 chunks]
types:       diagnostic_msgs/DiagnosticArray [60810da900de1dd6ddd437c3503511da]
             rosgraph_msgs/Log               [acffd30cd6b6de30f120938c17c593fb]
             sensor_msgs/Joy                 [5a9ea5f83505693b71e785041e67a8bb]
             std_msgs/Int32MultiArray        [1d99f79f8b325b44fee908053e9c945b]
topics:      /diagnostics                     148 msgs    : diagnostic_msgs/DiagnosticArray
             /joy                            1179 msgs    : sensor_msgs/Joy                
             /rosout                            7 msgs    : rosgraph_msgs/Log               (2 connections)
             /sensor/mag                     1525 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/input/position    7629 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/current    7185 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/position   7186 msgs    : std_msgs/Int32MultiArray
```

### 説明

マニピュレータ片側ワイヤの傾向を見るため．上と同じ．
上と異なるデータを用いており，モータはdata.1，磁気センサはdata.3を使っている．
csvファイルは見たい列の名前をdata0にしている．

---

## ```/home/sskr3/bags/ros1/2025-05-18-14-48-09.bag```

### ```rosbag info /home/sskr3/bags/ros1/2025-05-18-14-48-09.bag```

```
path:        /home/sskr3/bags/ros1/2025-05-18-14-48-09.bag
version:     2.0
duration:    3:11s (191s)
start:       May 18 2025 14:48:09.68 (1747547289.68)
end:         May 18 2025 14:51:21.50 (1747547481.50)
size:        2.9 MB
messages:    32886
compression: none [4/4 chunks]
types:       diagnostic_msgs/DiagnosticArray [60810da900de1dd6ddd437c3503511da]
             rosgraph_msgs/Log               [acffd30cd6b6de30f120938c17c593fb]
             sensor_msgs/Joy                 [5a9ea5f83505693b71e785041e67a8bb]
             std_msgs/Int32MultiArray        [1d99f79f8b325b44fee908053e9c945b]
topics:      /diagnostics                     184 msgs    : diagnostic_msgs/DiagnosticArray
             /joy                            3160 msgs    : sensor_msgs/Joy                
             /rosout                            7 msgs    : rosgraph_msgs/Log               (2 connections)
             /sensor/mag                     1915 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/input/position    9578 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/current    9021 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/position   9021 msgs    : std_msgs/Int32MultiArray
```

### 説明

上と同じ．モジュールの再現性チェック．
引っ張っていて後半でマニピュレータ先端が引っかかってしまったので，少し戻して再度挑戦ー＞直前で止めて緩めた．

---

## ```/home/sskr3/bags/ros1/2025-05-18-15-00-13.bag```

### ```rosbag info /home/sskr3/bags/ros1/2025-05-18-15-00-13.bag```

```
path:        /home/sskr3/bags/ros1/2025-05-18-15-00-13.bag
version:     2.0
duration:    2:45s (165s)
start:       May 18 2025 15:00:13.23 (1747548013.23)
end:         May 18 2025 15:02:59.17 (1747548179.17)
size:        2.1 MB
messages:    25852
compression: none [3/3 chunks]
types:       diagnostic_msgs/DiagnosticArray [60810da900de1dd6ddd437c3503511da]
             rosgraph_msgs/Log               [acffd30cd6b6de30f120938c17c593fb]
             sensor_msgs/Joy                 [5a9ea5f83505693b71e785041e67a8bb]
             std_msgs/Int32MultiArray        [1d99f79f8b325b44fee908053e9c945b]
topics:      /diagnostics                     155 msgs    : diagnostic_msgs/DiagnosticArray
             /joy                             141 msgs    : sensor_msgs/Joy                
             /rosout                            7 msgs    : rosgraph_msgs/Log               (2 connections)
             /sensor/mag                     1657 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/input/position    8286 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/current    7803 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/position   7803 msgs    : std_msgs/Int32MultiArray
```

### 説明

上と同じ．ぶつかって無いバージョン．
例によってcsvのコラムを入れ替えている．

---

## ```/home/sskr3/bags/ros1/2025-05-18-15-18-30.bag```

### ```rosbag info /home/sskr3/bags/ros1/2025-05-18-15-18-30.bag```

```
path:        /home/sskr3/bags/ros1/2025-05-18-15-18-30.bag
version:     2.0
duration:    2:36s (156s)
start:       May 18 2025 15:18:30.40 (1747549110.40)
end:         May 18 2025 15:21:06.74 (1747549266.74)
size:        2.0 MB
messages:    24379
compression: none [3/3 chunks]
types:       diagnostic_msgs/DiagnosticArray [60810da900de1dd6ddd437c3503511da]
             rosgraph_msgs/Log               [acffd30cd6b6de30f120938c17c593fb]
             sensor_msgs/Joy                 [5a9ea5f83505693b71e785041e67a8bb]
             std_msgs/Int32MultiArray        [1d99f79f8b325b44fee908053e9c945b]
topics:      /diagnostics                     149 msgs    : diagnostic_msgs/DiagnosticArray
             /joy                             153 msgs    : sensor_msgs/Joy                
             /rosout                            7 msgs    : rosgraph_msgs/Log               (2 connections)
             /sensor/mag                     1561 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/input/position    7807 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/current    7351 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/position   7351 msgs    : std_msgs/Int32MultiArray
```

### 説明

引っ張るー＞止めるー＞緩める

上記の止める場所をいろいろ変えて調査した．
csvコラム調整済み．

---

## ```/home/sskr3/bags/ros1/2025-05-18-15-21-08.bag```

### ```rosbag info /home/sskr3/bags/ros1/2025-05-18-15-21-08.bag```

```
path:        /home/sskr3/bags/ros1/2025-05-18-15-21-08.bag
version:     2.0
duration:    2:03s (123s)
start:       May 18 2025 15:21:08.90 (1747549268.90)
end:         May 18 2025 15:23:12.46 (1747549392.46)
size:        1.6 MB
messages:    19272
compression: none [2/2 chunks]
types:       diagnostic_msgs/DiagnosticArray [60810da900de1dd6ddd437c3503511da]
             rosgraph_msgs/Log               [acffd30cd6b6de30f120938c17c593fb]
             sensor_msgs/Joy                 [5a9ea5f83505693b71e785041e67a8bb]
             std_msgs/Int32MultiArray        [1d99f79f8b325b44fee908053e9c945b]
topics:      /diagnostics                     116 msgs    : diagnostic_msgs/DiagnosticArray
             /joy                             133 msgs    : sensor_msgs/Joy                
             /rosout                            7 msgs    : rosgraph_msgs/Log               (2 connections)
             /sensor/mag                     1234 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/input/position    6168 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/current    5807 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/position   5807 msgs    : std_msgs/Int32MultiArray
```

### 説明

引っ張るー＞止めるー＞緩めるー＞途中で止めるー＞引っ張るー＞...

上記をしたデータ．
csvコラム調整済み．

---

## ```/home/sskr3/bags/ros1/2025-05-18-16-25-18.bag```

### ```rosbag info /home/sskr3/bags/ros1/2025-05-18-16-25-18.bag```

```
path:        /home/sskr3/bags/ros1/2025-05-18-16-25-18.bag
version:     2.0
duration:    1:10s (70s)
start:       May 18 2025 16:25:18.61 (1747553118.61)
end:         May 18 2025 16:26:29.16 (1747553189.16)
size:        940.1 KB
messages:    11084
compression: none [2/2 chunks]
types:       diagnostic_msgs/DiagnosticArray [60810da900de1dd6ddd437c3503511da]
             rosgraph_msgs/Log               [acffd30cd6b6de30f120938c17c593fb]
             sensor_msgs/Joy                 [5a9ea5f83505693b71e785041e67a8bb]
             std_msgs/Int32MultiArray        [1d99f79f8b325b44fee908053e9c945b]
             std_msgs/String                 [992ce8a1687cec8c8bd883ec73ca41d1]
topics:      /diagnostics                      64 msgs    : diagnostic_msgs/DiagnosticArray
             /joy                             162 msgs    : sensor_msgs/Joy                
             /joy/button_pressed                3 msgs    : std_msgs/String                
             /rosout                            8 msgs    : rosgraph_msgs/Log               (2 connections)
             /sensor/mag                      703 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/input/position    3518 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/current    3313 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/position   3313 msgs    : std_msgs/Int32MultiArray
```

### 説明

接触をセンサで計測できるかチェックするため．
マニピュレータがぶつかったタイミングで/joy/button_pressedがpublishされる．

---

## ```2025-05-26-08-01-10.bag```

### ```rosbag info 2025-05-26-08-01-10.bag```

```
path:        2025-05-26-08-01-10.bag
version:     2.0
duration:    2:44s (164s)
start:       May 26 2025 08:01:10.39 (1748214070.39)
end:         May 26 2025 08:03:54.76 (1748214234.76)
size:        2.1 MB
messages:    25966
compression: none [3/3 chunks]
types:       diagnostic_msgs/DiagnosticArray [60810da900de1dd6ddd437c3503511da]
             rosgraph_msgs/Log               [acffd30cd6b6de30f120938c17c593fb]
             sensor_msgs/Joy                 [5a9ea5f83505693b71e785041e67a8bb]
             std_msgs/Int32MultiArray        [1d99f79f8b325b44fee908053e9c945b]
topics:      /diagnostics                     152 msgs    : diagnostic_msgs/DiagnosticArray
             /joy                             507 msgs    : sensor_msgs/Joy                
             /rosout                            8 msgs    : rosgraph_msgs/Log               (2 connections)
             /sensor/mag                     1641 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/input/position    8204 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/current    7727 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/position   7727 msgs    : std_msgs/Int32MultiArray
```

### 説明

最大まで引いた後に，一瞬だけ緩めてみたもの．
摩擦の影響で力の釣り合いの収束が遅れると考えたため．
magの位置ミスったからデータおかしいね．
ー＞と思ったけど参照するデータ間違えてただけだった．

---

## ```2025-05-26-08-13-15.bag```

### ```rosbag info /home/sskr3/bags/ros1/2025-05-26-08-13-15/2025-05-26-08-13-15.bag```

```
path:        /home/sskr3/bags/ros1/2025-05-26-08-13-15/2025-05-26-08-13-15.bag
version:     2.0
duration:    3:52s (232s)
start:       May 26 2025 08:13:15.87 (1748214795.87)
end:         May 26 2025 08:17:08.84 (1748215028.84)
size:        2.9 MB
messages:    36400
compression: none [4/4 chunks]
types:       diagnostic_msgs/DiagnosticArray [60810da900de1dd6ddd437c3503511da]
             rosgraph_msgs/Log               [acffd30cd6b6de30f120938c17c593fb]
             sensor_msgs/Joy                 [5a9ea5f83505693b71e785041e67a8bb]
             std_msgs/Int32MultiArray        [1d99f79f8b325b44fee908053e9c945b]
topics:      /diagnostics                      223 msgs    : diagnostic_msgs/DiagnosticArray
             /joy                              292 msgs    : sensor_msgs/Joy                
             /rosout                             8 msgs    : rosgraph_msgs/Log               (2 connections)
             /sensor/mag                      2328 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/input/position    11639 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/current    10955 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/position   10955 msgs    : std_msgs/Int32MultiArray
```

### 説明

上でミスったから再度取り直したやつ．

---

## ```2025-05-26-08-32-51.bag```

### ```rosbag info /home/sskr3/bags/ros1/2025-05-26-08-32-51/2025-05-26-08-32-51.bag```

```
path:        /home/sskr3/bags/ros1/2025-05-26-08-55-23/2025-05-26-08-55-23.bag
version:     2.0
duration:    2:14s (134s)
start:       May 26 2025 08:55:23.54 (1748217323.54)
end:         May 26 2025 08:57:37.86 (1748217457.86)
size:        1.7 MB
messages:    21159
compression: none [2/2 chunks]
types:       diagnostic_msgs/DiagnosticArray [60810da900de1dd6ddd437c3503511da]
             rosgraph_msgs/Log               [acffd30cd6b6de30f120938c17c593fb]
             sensor_msgs/Joy                 [5a9ea5f83505693b71e785041e67a8bb]
             std_msgs/Int32MultiArray        [1d99f79f8b325b44fee908053e9c945b]
topics:      /diagnostics                     119 msgs    : diagnostic_msgs/DiagnosticArray
             /joy                             362 msgs    : sensor_msgs/Joy                
             /rosout                            8 msgs    : rosgraph_msgs/Log               (2 connections)
             /sensor/mag                     1341 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/input/position    6707 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/current    6311 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/position   6311 msgs    : std_msgs/Int32MultiArray/ros1/2025-05-26-08-32-51/2025-05-26-08-32-51.bag
version:     2.0
duration:    7:13s (433s)
start:       May 26 2025 08:32:51.79 (1748215971.79)
end:         May 26 2025 08:40:05.47 (1748216405.47)
size:        5.6 MB
messages:    68581
compression: none [7/7 chunks]
types:       diagnostic_msgs/DiagnosticArray [60810da900de1dd6ddd437c3503511da]
             rosgraph_msgs/Log               [acffd30cd6b6de30f120938c17c593fb]
             sensor_msgs/Joy                 [5a9ea5f83505693b71e785041e67a8bb]
             std_msgs/Int32MultiArray        [1d99f79f8b325b44fee908053e9c945b]
topics:      /diagnostics                      394 msgs    : diagnostic_msgs/DiagnosticArray
             /joy                             1380 msgs    : sensor_msgs/Joy                
             /rosout                            11 msgs    : rosgraph_msgs/Log               (2 connections)
             /rosout_agg                         4 msgs    : rosgraph_msgs/Log              
             /sensor/mag                      4325 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/input/position    21671 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/current    20398 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/position   20398 msgs    : std_msgs/Int32MultiArray
```

### 説明

「一瞬だけ緩める」を連続で行ったもの．
上の現象から，摩擦が原因と考えた．
* 板バネプーリの角度を前後で同じ(5[deg])にした．これは張力のバネ方向成分が鉛直下向きになるように．
* マニピュレータ側のプーリの位置を調整し，マニピュレータに入るワイヤの角度を水平にした．これは穴部分でこすれていたため．

* ◯ばねワイヤ角度
* ◯マニピュレータ側プーリあり
* ◯マニピュレータワイヤ角度
* ×急激な動作

実際，急激に変化する現象が起きていないので摩擦により一次遅れのようなことが起きていたのではないか．

---

## ```2025-05-26-08-55-23.bag```

### ```rosbag info /home/sskr3/bags/ros1/2025-05-26-08-55-23/2025-05-26-08-55-23.bag```

```
path:        /home/sskr3/bags/ros1/2025-05-26-08-55-23/2025-05-26-08-55-23.bag
version:     2.0
duration:    2:14s (134s)
start:       May 26 2025 08:55:23.54 (1748217323.54)
end:         May 26 2025 08:57:37.86 (1748217457.86)
size:        1.7 MB
messages:    21159
compression: none [2/2 chunks]
types:       diagnostic_msgs/DiagnosticArray [60810da900de1dd6ddd437c3503511da]
             rosgraph_msgs/Log               [acffd30cd6b6de30f120938c17c593fb]
             sensor_msgs/Joy                 [5a9ea5f83505693b71e785041e67a8bb]
             std_msgs/Int32MultiArray        [1d99f79f8b325b44fee908053e9c945b]
topics:      /diagnostics                     119 msgs    : diagnostic_msgs/DiagnosticArray
             /joy                             362 msgs    : sensor_msgs/Joy                
             /rosout                            8 msgs    : rosgraph_msgs/Log               (2 connections)
             /sensor/mag                     1341 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/input/position    6707 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/current    6311 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/position   6311 msgs    : std_msgs/Int32MultiArray
```

### 説明

上の条件は2点改善したため，これは板バネ前後のワイヤ角度だけ合わせたversion．
* 板バネプーリの角度を前後で同じ(5[deg])にした．これは張力のバネ方向成分が鉛直下向きになるように．

* ◯ばねワイヤ角度
* ◯マニピュレータ側プーリあり
* ×マニピュレータワイヤ角度
* ×急激な動作

マニピュレータ側プーリの角度はある程度ついているため入り口で摩擦がある程度ありそう．

---

## ```2025-05-26-09-10-39.bag```

### ```rosbag info /home/sskr3/bags/ros1/2025-05-26-09-10-39/2025-05-26-09-10-39.bag```

```
path:        /home/sskr3/bags/ros1/2025-05-26-09-10-39/2025-05-26-09-10-39.bag
version:     2.0
duration:    2:58s (178s)
start:       May 26 2025 09:10:39.70 (1748218239.70)
end:         May 26 2025 09:13:37.99 (1748218417.99)
size:        2.2 MB
messages:    27723
compression: none [3/3 chunks]
types:       diagnostic_msgs/DiagnosticArray [60810da900de1dd6ddd437c3503511da]
             rosgraph_msgs/Log               [acffd30cd6b6de30f120938c17c593fb]
             sensor_msgs/Joy                 [5a9ea5f83505693b71e785041e67a8bb]
             std_msgs/Int32MultiArray        [1d99f79f8b325b44fee908053e9c945b]
topics:      /diagnostics                     173 msgs    : diagnostic_msgs/DiagnosticArray
             /joy                              92 msgs    : sensor_msgs/Joy                
             /rosout                            8 msgs    : rosgraph_msgs/Log               (2 connections)
             /sensor/mag                     1781 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/input/position    8904 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/current    8382 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/position   8383 msgs    : std_msgs/Int32MultiArray
```

### 説明

* ◯ばねワイヤ角度
* ◯マニピュレータ側プーリあり
* ◯マニピュレータワイヤ角度
* ◯急激な動作

---

## ```2025-05-26-09-19-20/2025-05-26-09-19-20.bag```

### ```rosbag info /home/sskr3/bags/ros1/2025-05-26-09-19-20/2025-05-26-09-19-20.bag```

```
path:        /home/sskr3/bags/ros1/2025-05-26-09-19-20/2025-05-26-09-19-20.bag
version:     2.0
duration:    2:40s (160s)
start:       May 26 2025 09:19:20.56 (1748218760.56)
end:         May 26 2025 09:22:01.07 (1748218921.07)
size:        2.0 MB
messages:    25164
compression: none [3/3 chunks]
types:       diagnostic_msgs/DiagnosticArray [60810da900de1dd6ddd437c3503511da]
             rosgraph_msgs/Log               [acffd30cd6b6de30f120938c17c593fb]
             sensor_msgs/Joy                 [5a9ea5f83505693b71e785041e67a8bb]
             std_msgs/Int32MultiArray        [1d99f79f8b325b44fee908053e9c945b]
topics:      /diagnostics                     150 msgs    : diagnostic_msgs/DiagnosticArray
             /joy                             300 msgs    : sensor_msgs/Joy                
             /rosout                            8 msgs    : rosgraph_msgs/Log               (2 connections)
             /sensor/mag                     1603 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/input/position    8015 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/current    7544 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/position   7544 msgs    : std_msgs/Int32MultiArray
```

### 説明

* ◯ばねワイヤ角度
* ◯マニピュレータ側プーリあり
* ◯マニピュレータワイヤ角度
* △急激な動作(一度に緩める時間を伸ばした)

---

## ```2025-05-26-09-30-11.bag```

### ```rosbag info /home/sskr3/bags/ros1/2025-05-26-09-30-11/2025-05-26-09-30-11.bag```

```
path:        /home/sskr3/bags/ros1/2025-05-26-09-30-11/2025-05-26-09-30-11.bag
version:     2.0
duration:    3:44s (224s)
start:       May 26 2025 09:30:11.69 (1748219411.69)
end:         May 26 2025 09:33:56.06 (1748219636.06)
size:        2.8 MB
messages:    34905
compression: none [4/4 chunks]
types:       diagnostic_msgs/DiagnosticArray [60810da900de1dd6ddd437c3503511da]
             rosgraph_msgs/Log               [acffd30cd6b6de30f120938c17c593fb]
             sensor_msgs/Joy                 [5a9ea5f83505693b71e785041e67a8bb]
             std_msgs/Int32MultiArray        [1d99f79f8b325b44fee908053e9c945b]
topics:      /diagnostics                      218 msgs    : diagnostic_msgs/DiagnosticArray
             /joy                              135 msgs    : sensor_msgs/Joy                
             /rosout                             8 msgs    : rosgraph_msgs/Log               (2 connections)
             /sensor/mag                      2241 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/input/position    11206 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/current    10548 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/position   10549 msgs    : std_msgs/Int32MultiArray
```

### 説明

* ◯ばねワイヤ角度
* ◯マニピュレータ側プーリあり
* ◯マニピュレータワイヤ角度
* ×急激な動作

各動作後に停止させる時間を伸ばした．

---

## ```2025-05-26-10-06-44.bag```

### ```rosbag info /home/sskr3/bags/ros1/2025-05-26-10-06-44/2025-05-26-10-06-44.bag```

```
path:        /home/sskr3/bags/ros1/2025-05-26-10-06-44/2025-05-26-10-06-44.bag
version:     2.0
duration:    10:49s (649s)
start:       May 26 2025 10:06:44.13 (1748221604.13)
end:         May 26 2025 10:17:33.77 (1748222253.77)
size:        8.0 MB
messages:    100922
compression: none [10/10 chunks]
types:       diagnostic_msgs/DiagnosticArray [60810da900de1dd6ddd437c3503511da]
             rosgraph_msgs/Log               [acffd30cd6b6de30f120938c17c593fb]
             sensor_msgs/Joy                 [5a9ea5f83505693b71e785041e67a8bb]
             std_msgs/Int32MultiArray        [1d99f79f8b325b44fee908053e9c945b]
topics:      /diagnostics                      638 msgs    : diagnostic_msgs/DiagnosticArray
             /joy                              198 msgs    : sensor_msgs/Joy                
             /rosout                             8 msgs    : rosgraph_msgs/Log               (2 connections)
             /sensor/mag                      6494 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/input/position    32471 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/current    30556 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/position   30557 msgs    : std_msgs/Int32MultiArray
```

### 説明

* ◯ばねワイヤ角度
* ◯マニピュレータ側プーリあり
* ◯マニピュレータワイヤ角度
* ×急激な動作

速度を10[step/sec](上のbagの1/20)で動作させた．
準静的を見たかった．

---

## ```2025-05-26-10-25-33.bag```

### ```rosbag info /home/sskr3/bags/ros1/2025-05-26-10-25-33/2025-05-26-10-25-33.bag```

```
path:        /home/sskr3/bags/ros1/2025-05-26-10-25-33/2025-05-26-10-25-33.bag
version:     2.0
duration:    4:02s (242s)
start:       May 26 2025 10:25:33.16 (1748222733.16)
end:         May 26 2025 10:29:35.84 (1748222975.84)
size:        3.1 MB
messages:    37962
compression: none [4/4 chunks]
types:       diagnostic_msgs/DiagnosticArray [60810da900de1dd6ddd437c3503511da]
             rosgraph_msgs/Log               [acffd30cd6b6de30f120938c17c593fb]
             sensor_msgs/Joy                 [5a9ea5f83505693b71e785041e67a8bb]
             std_msgs/Int32MultiArray        [1d99f79f8b325b44fee908053e9c945b]
topics:      /diagnostics                      225 msgs    : diagnostic_msgs/DiagnosticArray
             /joy                              346 msgs    : sensor_msgs/Joy                
             /rosout                             8 msgs    : rosgraph_msgs/Log               (2 connections)
             /sensor/mag                      2425 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/input/position    12124 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/current    11417 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/position   11417 msgs    : std_msgs/Int32MultiArray
```

### 説明

* ◯ばねワイヤ角度
* ◯マニピュレータ側プーリあり
* ◯マニピュレータワイヤ角度
* ◯急激な動作

ある特定のモータステップ角での磁気センサ値がどうなるのか調べるためにとった．

---

## ```2025-05-26-10-46-29.bag```

### ```rosbag info /home/sskr3/bags/ros1/2025-05-26-10-46-29/2025-05-26-10-46-29.bag```

```
path:        /home/sskr3/bags/ros1/2025-05-26-10-46-29/2025-05-26-10-46-29.bag
version:     2.0
duration:    4:40s (280s)
start:       May 26 2025 10:46:29.54 (1748223989.54)
end:         May 26 2025 10:51:10.34 (1748224270.34)
size:        3.5 MB
messages:    44034
compression: none [5/5 chunks]
types:       diagnostic_msgs/DiagnosticArray [60810da900de1dd6ddd437c3503511da]
             rosgraph_msgs/Log               [acffd30cd6b6de30f120938c17c593fb]
             sensor_msgs/Joy                 [5a9ea5f83505693b71e785041e67a8bb]
             std_msgs/Int32MultiArray        [1d99f79f8b325b44fee908053e9c945b]
topics:      /diagnostics                      261 msgs    : diagnostic_msgs/DiagnosticArray
             /joy                              522 msgs    : sensor_msgs/Joy                
             /rosout                             8 msgs    : rosgraph_msgs/Log               (2 connections)
             /sensor/mag                      2805 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/input/position    14028 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/current    13205 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/position   13205 msgs    : std_msgs/Int32MultiArray
```

### 説明

* ×ばねワイヤ角度
* ◯マニピュレータ側プーリあり
* ◯マニピュレータワイヤ角度
* ◯急激な動作

調査のため一応．

## ```2025-05-26-10-58-34.bag```

### ```rosbag info /home/sskr3/bags/ros1/2025-05-26-10-58-34/2025-05-26-10-58-34.bag```

```
path:        /home/sskr3/bags/ros1/2025-05-26-10-58-34/2025-05-26-10-58-34.bag
version:     2.0
duration:    5:47s (347s)
start:       May 26 2025 10:58:34.47 (1748224714.47)
end:         May 26 2025 11:04:21.55 (1748225061.55)
size:        4.4 MB
messages:    54616
compression: none [6/6 chunks]
types:       diagnostic_msgs/DiagnosticArray [60810da900de1dd6ddd437c3503511da]
             rosgraph_msgs/Log               [acffd30cd6b6de30f120938c17c593fb]
             sensor_msgs/Joy                 [5a9ea5f83505693b71e785041e67a8bb]
             std_msgs/Int32MultiArray        [1d99f79f8b325b44fee908053e9c945b]
topics:      /diagnostics                      321 msgs    : diagnostic_msgs/DiagnosticArray
             /joy                              829 msgs    : sensor_msgs/Joy                
             /rosout                             8 msgs    : rosgraph_msgs/Log               (2 connections)
             /sensor/mag                      3468 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/input/position    17342 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/current    16324 msgs    : std_msgs/Int32MultiArray       
             /sensor/motor/output/position   16324 msgs    : std_msgs/Int32MultiArray
```

### 説明

* ◯ばねワイヤ角度
* ×マニピュレータ側プーリあり
* ◯マニピュレータワイヤ角度
* ◯急激な動作

これも調査のため一応．
速度は一般(200[step/sec])だが急激変化の現象が現れている．

---
---
---

# 補足

## csvファイルに落とす

```
rostopic echo -b your.bag -p /your/topic > topic.csv
```

# PID制御のbag(通信速度あまり速くないときなので今は使えないかも)

## ```2025-06-07-16-40-56.bag```

P30.0

## ```2025-06-07-16-57-44.bag```

P55.0

## ```2025-06-07-17-02-36.bag```

P55.0, I0.5

## ```2025-06-07-17-12-24.bag```

P55.0, I0.5, D0.5

## ```2025-06-07-18-03-54.bag```

P60.0

## ```2025-06-07-18-07-31.bag```

P60.0, I10.0

## ```2025-06-07-18-09-08.bag```

P60.0, I10.0, D1.0

## ```2025-06-07-18-13-38.bag```

P60.0, I10.0, D0.5

## ```2025-06-07-18-15-29.bag```

P60.0, I5.0, D0.5

# PID制御のbag(tensionの周波数100[Hz])

## ```2025-06-07-21-24-37.bag```

P20.0

## ```2025-06-07-21-35-36.bag```

P20.0, I2.0

# PID制御のbag

## ```2025-06-07-21-58-05.bag```

P30.0

## ```2025-06-07-22-05-39.bag```

P20.0

## ```2025-06-07-22-16-03.bag```

P20.0, I5.0

## ```2025-06-07-22-20-17.bag```

P20.0, I5.0, D0.5

## ```2025-06-16-11-41-41.bag```

1セクション2ワイヤのバイラテラル．
前半左右接触．

## ```2025-06-16-12-22-22.bag```

2セクション4ワイヤのバイラテラル．
前半左右接触．

## ```2025-06-16-12-38-32.bag```

2セクション4ワイヤのバイラテラル．
セクションごとに異なる曲率を実現

## ```2025-06-21-13-08-26.bag```

2セクション4ワイヤのバイラテラル．
masterのoutput ｰ> slaveのinputでダイレクトに入れている．

## ```2025-06-21-13-36-53.bag```

2セクション4ワイヤのバイラテラル．
無駄な初期化プロセス削除後．

## ```2025-06-21-13-58-49.bag```

2セクション4ワイヤのバイラテラル．
debug logで見えるかもと考えた．
txtにログがある．