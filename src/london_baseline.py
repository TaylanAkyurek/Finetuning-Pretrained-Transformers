# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
import utils

path = "birth_dev.tsv"
f = open(path, "r")
n = len(f.readlines())

pred = []
for i in range(n):
    pred.append("London")
print(utils.evaluate_places(path, pred))