# https://adventofcode.com/2020/day/7
# Every type of bag must contain specific quantities of other specific coloured bags.
# From a list of these requirements, find out how many bags allow you to carry a "shiny gold" bag at some point.

def find_parents(child_bag):
    for parent in bags_dict:
        contents = bags_dict[parent]
        if child_bag in contents:
            find_parents(parent)
            confirmed_bags.add(parent)         # The set add() method adds a given element to a set 
                                               # if the element is not present in the set.
    return


with open('E:\code\AoC\day7\input.txt', "r") as bags:
    bags = bags.read().split("\n")

bags_dict = {}
for bag in bags:
    bag = bag.replace(" bags", "").replace(" bag", "")  
    #cleans the string to list the *parent bag and the *content/s bag/s
    parent, content = bag.split(" contain ")
    #print(bag)
    bags_dict[parent] = content
confirmed_bags = set()
find_parents("shiny gold")
print("Total: ", len(confirmed_bags))
