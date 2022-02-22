#Pyramid, need a ball at the bottom
#First few lines always same, need if statements for last row
def pachinkoImage(f):
  print("       |       ")
  print("     /   \\    ")
  print()
  print("   / \\   / \\   ")
  print()
  print("  / \\ / \\ / \\ ")
  print()
  if (f == 1):
    print("|*| | | | | | |")
  elif (f == 2):
    print("| |*| | | | | |")
  elif (f == 3):
    print("| | |*| | | | |")
  elif (f == 4):
    print("| | | |*| | | |")
  elif (f == 5):
    print("| | | | |*| | |")
  elif (f == 6):
    print("| | | | | |*| |")
  else:
    print("| | | | | | |*|")
  print("---------------")
