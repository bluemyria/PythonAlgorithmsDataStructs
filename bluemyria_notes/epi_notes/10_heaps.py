import collections
import itertools
import heapq

# take a sequence of string and return the k largest
def top_k(k: int, stream):
    # the next commented instr functions only for real streams/iterators!!
    # for arrays the islice doesn't cut away the first k, it just returns them
    # for streams/iterators they just disappear and the next for starts from the k+1 elem
    min_heap = [ (len(st), st) for st in itertools.islice(stream, k)]
    # min_heap = [ (0, "") for _ in range(k)] # alternative for arrays (input)
    # print(min_heap)
    heapq.heapify(min_heap)
    for st in stream:
        print(st, ",", len(st))
        # we need the k biggest elements, minheap pops *AWAY* always the smallest
        # so the biggest remain! 
        heapq.heappushpop(min_heap, (len(st), st))
        #print(min_heap)
        #print("\n")
    # heapq.nlargest returns the same k elements but in reverse order
    return [p for p in heapq.nsmallest(k, min_heap)] 


print(top_k(3,iter(["flesher", "hvy", "innoxiously", "asp", "woodpeckers", "helvin", "unthaw", "stample", "rasant", "duplicipennate", "hyperanarchic", "saltatorious", "anthropomantic", "filtrates", "asp", "turkeyback", "evictors", "bowlder", "clomp", "undy", "wino", "canaliculation", "warlikeness", "semioriental", "crackdown", "dogedom", "evictors", "feh", "endostraca", "semioriental", "flesher", "lub"])))
print("\n"*3)
print(top_k(4,iter(["crackdown", "azthionium", "balks", "ferter", "subnotochordal", "bowlder", "reen", "innoxiously", "reventilate", "bac", "recollections", "epoophoron", "womanly", "troubleshooted", "boh", "parachutism"])))