import sys

sys.path.insert(1, 'projects/hog/')

from projects.hog import hog

print(hog.swap_strategy(13, 18, 1, 6))
