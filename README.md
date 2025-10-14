# LeetCode 문제 풀이 저장소 🐍

Python을 사용한 LeetCode 알고리즘 문제 풀이를 저장하는 레포지토리입니다.

## 📌 목적

- LeetCode 문제 풀이 연습 및 기록
- 다양한 알고리즘 접근 방법 학습
- 코드 리뷰 및 개선을 위한 이력 관리

## 📂 구조

```
PythonAlgorithmnInterview/
├── [번호].py              # LeetCode 문제 번호로 명명된 파일
├── [설명적이름].py        # 문제 이름으로 명명된 파일
└── README.md
```

### 파일 명명 규칙

- **숫자 형식**: `1.py`, `42.py` - LeetCode 문제 번호
- **설명적 이름**: `ValidPalindrome.py`, `GroupAnagrams.py` - 문제 이름

## 📝 문제 목록

| 번호 | 문제 이름 | 파일명 | 난이도 | 주요 개념 |
|------|-----------|--------|--------|-----------|
| 1 | Two Sum | `1.py` | Easy | Hash Map, Array |
| 5 | Longest Palindromic Substring | `5.py` | Medium | Two Pointers, String |
| 9 | Palindrome Number | `9.py` | Easy | Math |
| 13 | Roman to Integer | `13.py` | Easy | Hash Map, String |
| 14 | Longest Common Prefix | `14.py` | Easy | String |
| 20 | Valid Parentheses | `20.py` | Easy | Stack |
| 26 | Remove Duplicates from Sorted Array | `26.py` | Easy | Two Pointers, Array |
| 27 | Remove Element | `27.py` | Easy | Two Pointers, Array |
| 28 | Find the Index of the First Occurrence | `28.py` | Easy | String |
| 42 | Trapping Rain Water | `42.py` | Hard | Two Pointers, Stack |
| 242 | Valid Anagram | `242.py` | Easy | Hash Map, String |
| - | Valid Palindrome | `ValidPalindrome.py` | Easy | String, Two Pointers |
| - | Reverse String | `ReverseString.py` | Easy | String, Two Pointers |
| - | Reorder Data in Log Files | `ReorderDataInLogFiles.py` | Medium | String, Sorting |
| - | Most Common Word | `mostCommonWord.py` | Easy | Hash Map, String |
| - | Group Anagrams | `GroupAnagrams.py` | Medium | Hash Map, String |

## 🚀 사용 방법

### 실행 환경
- Python 3.10 이상 권장
- Type Hints 사용

### 실행 예시

```python
# 파일 실행
python 1.py

# 또는 함수 임포트
from Solution import twoSum
result = twoSum([2, 7, 11, 15], 9)
print(result)  # [0, 1]
```

## 💡 특징

- **다양한 풀이 방법**: 하나의 문제에 대해 여러 접근 방식 제공
- **한글 주석**: 이해하기 쉬운 한글 설명 포함
- **시간/공간 복잡도**: 각 풀이의 효율성 분석

### 풀이 예시

```python
# 1. Brute Force 방법
def solution1(nums):
    # O(n²) 시간 복잡도
    pass

# 2. 최적화된 방법
def solution2(nums):
    # O(n) 시간 복잡도 (Hash Map 사용)
    pass
```

## 📚 참고 자료

- [LeetCode](https://leetcode.com/)
- [Python Algorithm Interview](https://github.com/onlybooks/algorithm-interview)

## 📊 진행 상황

- ✅ 완료: 16문제
- 🔄 진행 중: -
- 📝 예정: -

---

**Last Updated**: 2025.10.14

