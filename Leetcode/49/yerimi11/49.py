import sys
import collections
input = sys.stdin.readline

strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

def groupAnagrams(strs) :
        # 문자열 배열을 받아 애너그램 단위로 그룹핑하라.
        # 애너그램 : 문자를 뒤집어서 다른 뜻을 가진 단어로 바꾸는 것 (언어유희) ex:문전박대->대박전문

    anagrams = collections.defaultdict(list)
    # 만약 존재하지 않는 키를 삽입하려 할 경우 keyerror가 발생하므로, 항상 디폴트를 생성해준다.
    # 매번 키 존재 여부를 체크하지 않고 비교 구문을 생략해 간결하게 구성할 수 있다.
    # 만약 defaultdict 없으면 anagrams = {} 설정-> if word not in strs: anagrams[0] = [] 로 써야한다.

    # 애너그램 관계인 단어들을 정렬하면 서로 같은 값을 갖기 때문에
    # 애너그램을 판단하는 가장 간단한 방법은 정렬하여 비교하는 것이다.
    for word in strs :
        #정렬하여 딕셔너리에 추가. 정렬한 단어가 딕셔너리의 키가 되고(애너그램끼리는 같은 키를 가짐), 여기에 단어들을 append 한다.
        # print(sorted(word)) = ['aet', 'aet', 'ant', 'aet', 'ant', 'abt']
        anagrams[''.join(sorted(word))].append(word)

    return list(anagrams.values())    