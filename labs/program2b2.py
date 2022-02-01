# Program 2B2
# Katie Devinney
# Calculates the number of trees that can be planted along a fence

fenceLength = float(input("Enter the length of the fence: "))
radius = float(input("Enter the length of the radius of one fully grown tree: "))
treeType = input("Enter the type of tree: ")

diameter = radius * 2
numberOfTrees = str(int(fenceLength // diameter))
print("The number of " + treeType + " trees is " + numberOfTrees)