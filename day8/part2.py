instructions = []
with open('E:\code\AoC\day8\input.txt') as fp:
  line = fp.readline()
  while line:
    tokens = line.strip().split()
    instructions.append((tokens[0], int(tokens[1])))
    line = fp.readline()
#print(instructions)
# ptr means position tracker or pointer
def execute(instrs):
  hasLoop = False
  visited = set()
  ptr = acc = 0
  #print(ptr)
  while ptr < len(instrs):
    op, value = instrs[ptr]
    if ptr in visited:
      hasLoop = True
      break
    visited.add(ptr)
    if op == 'jmp':
      ptr = ptr + value
      continue
    elif op == 'acc':
      acc = acc + value
    ptr = ptr + 1
  return (acc, hasLoop)

print(f'Part 1\n{execute(instructions)[0]}\n')

swapDict = {'nop':'jmp','jmp':'nop'}
for i, (op,value) in enumerate(instructions):
  #print(i, op, value)
  if op == 'nop' or op == 'jmp':
    swappedOp = [(swapDict[op], value)]
    newInstructions = instructions[:i] + swappedOp + instructions[i+1:]
    accValue, hasLoop = execute(newInstructions)
    # Ok this method takes the approach of changing every single nop or jmp
    # one at a time and gets the result with the execute for that operation change until
    # he gets the correct result without falling in a infinite loop.
    # the variables names were less than ideal but I learned 
    # that ptr means pointer which was useful. The list addition and indexing of the swapped operation
    # was clever too
    if not hasLoop:
      print(f'Part 2\n{accValue}')
