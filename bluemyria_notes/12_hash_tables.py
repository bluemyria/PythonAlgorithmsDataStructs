import functools
import collections

def string_hash(s, mod):
    MULT = 997
    v = 0
    for c in s:
        v = v * MULT + ord(c)
        print(v)
    print(functools.reduce(lambda v, c: (v * MULT + ord(c)) , s, 0))
    return functools.reduce(lambda v, c: (v * MULT + ord(c)) % mod, s, 0)

def find_anagrams(dictionary):
    sorted_string_to_anagrams = collections.defaultdict(list)
    for s in dictionary:
        sorted_string_to_anagrams["".join(sorted(s))].append(s)
    return [
        v for v in sorted_string_to_anagrams.values() if len(v)>=2
    ]

print("\nEND\n", string_hash("MariaBlum",30))
mydict = {"debitcard", "elvis", "silent", "badcredit", "lives", "freedom", "listen", "levis", "money" }
print(mydict)
print(find_anagrams(mydict))


s = set()
s.add(42)

s.remove(42)

s.add(43)
s.add(44)
#also x in s, s < t, s - t 
# you cannot use hash on mutable objects like set, so use
print(hash(frozenset(s)))

# discard: Remove an element from a set if it is a member.
# If the element is not a member, do nothing.
s.discard(123)