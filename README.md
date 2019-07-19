# Hybrid-Korean-Spacing-Module-using-dictionary-and-and-heuristic
어절사전 및 형태소사전과 휴리스틱 방법을 이용한 Hybrid 한국어 띄어쓰기 모듈

## Introduction
자연언어처리에서 가장 밑 단계인 띄어쓰기 모듈에 관한 내용입니다.
딥러닝 기반 방식이 성능이 높으나 본 논문은 규칙기반과 통계기반의 Hybrid 방식을 이용하여 구현하였습니다.
자세한 내용은 논문을 참조해주세요.

## Execution

python3 main.py inut.txt

input.txt 대신 여러분의 테스트 셋을 이용해보세요.
output.txt에 결과가 쓰여집니다.

## Dictionary
세종말뭉치 기반으로 만들었습니다.

Download Link
https://drive.google.com/drive/folders/1EtB1tSkA_UiF_0f2mZfBeXvK7Js_kJJD?usp=sharing

## Test
test.py를 통하여 precision,recall,f1-score를 계산할 수 있습니다.
- pip3 install statistics
- ref와 pred 디렉토리를 만들어주세요.
- ref의 정답을 pred에 띄어쓰기 결과를 각각 넣어주세요. (.txt)

## Cite

```
@{article,
  author       = {Chanjun Park(박찬준)},
  title        = {어절사전 및 형태소사전과 휴리스틱 방법을 이용한 Hybrid 한국어 띄어쓰기 모듈(Korean Spacing Module using Eojeol dictionary and Morpheme dictionary )},
  year         = {2018}
}
```
