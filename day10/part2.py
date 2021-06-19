with open('E:\code\AoC\day10\input3.txt', 'r') as input:
    adapters = list(map(int, input.read().strip().split('\n')))
adapters.sort()
#print(adapters)
#print(len(adapters))
print(' ')

memo = {0: 1}
for adapter in adapters:
  memo[adapter] = memo.get(adapter-3,0) + memo.get(adapter-2,0)+ memo.get(adapter-1,0)
print(memo[adapters[-1]])
