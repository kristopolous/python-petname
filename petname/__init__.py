#  petname: library for generating human-readable, random names
#           for objects (e.g. hostnames, containers, blobs)
#
#  Copyright 2014 Dustin Kirkland <dustin.kirkland@gmail.com>
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


import random, math
from .english import adverbs, adjectives, names


try:
    random = random.SystemRandom()
except NotImplementedError:
    pass # less secure

def generate(separator: str = "-", index: int = None) -> str:
    petname = []

    petname.append(adverbs[index % len(adverbs)])
    index = math.floor(index / len(adverbs))
    
    petname.append(adjectives[index % len(adjectives)])
    index = math.floor(index / len(adjectives))

    petname.append(names[index % len(names)])
    index = math.floor(index / len(names))

    if index % 2 == 1:
      petname[0], petname[1] = petname[1], petname[0]

    index = math.floor(index / 2)

    if index > 0:
      petname.append(str(index))

    return separator.join(petname)

Generate = generate
