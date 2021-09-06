# leetcode 49
import collections

# time limit exceeded
def groupAnagrams_0(strs):
    unique_strs = list(set([''.join(sorted(string)) for string in strs]))

    result = [[] for i in range(len(unique_strs))]
    for string in strs:
        for i in range(len(unique_strs)):
            if ''.join(sorted(string)) == unique_strs[i]:
                result[i].append(string)

    return result


def groupAnagrams_A(strs):
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())


if __name__ == "__main__":
    print(groupAnagrams_A(["eat", "tea", "tan", "ate", "nat", "bat"]))