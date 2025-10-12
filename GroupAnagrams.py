import collections


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagrams = collections.defaultdict(list)
    for str in strs:
        anagrams["".join(sorted(str))].append(str)

    return list(anagrams.values())
