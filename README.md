# Earth age calculator

![image](https://github.com/edu-data-mario/earth-age-calculator/assets/134017660/3117b1c5-0fd0-4db4-ba4e-b93199d14376)

- In collaboration with George Tilton, Patterson developed the uranium–lead dating method into lead–lead dating. By using lead isotopic data from the Canyon Diablo meteorite, he calculated an age for the Earth of 4.55 billion years, which was a figure far more accurate than those that existed at the time, and one that has remained largely unchanged since 1956.

### The History of Earth's Age Calculation
- [패터슨은](https://en.wikipedia.org/wiki/Clair_Cameron_Patterson) 조지 틸튼(George Tilton) 과 협력하여 우라늄-납 연대 측정 방법을 납-납 연대 측정 으로 개발했습니다 . 
- 그는 Canyon Diablo 운석 의 납 동위원소 데이터를 사용하여 지구의 나이를 45억 5천만년으로 계산했는데 , 
- 이는 당시 존재했던 수치보다 훨씬 더 정확한 수치였으며 1956년 이후 크게 변하지 않은 수치입니다.

### How to use
```bash
$ python
Python 3.9.17 (main, Jun 16 2023, 00:28:17) 
[Clang 14.0.0 (clang-1400.0.29.202)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import earth_age_calculator.earth as our_earth
>>> our_earth.calculate_earth_age(2023)
4550000067
>>> 
```

### Test
```bash
$ pytest
$ pytest -q
$ pytest -q tests/test_earth.py
```

### Thank you
```bash
Help on how to distribute pip was received in the repo below.

.　/＼＿／ヽ
／ _ノ　ヽ_ ＼
|　　━　 ━　i
＼ミ (_人_) 彡
　／￣￣⌒＼/⌒)―――― https://github.com/edu-data-mario/nothing-pip
. /　　　　＿／　
. |　　　＼
　＼ 〇_　 ＼
　　＼ノ.＼_ノ

& Thanks to the Boden scientists who did the research to determine the age of the Earth.
```
