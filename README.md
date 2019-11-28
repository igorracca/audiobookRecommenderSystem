# Audiobook Recommendation System
A system that recommends additional audiobooks to each user based on other users reviews.  Supposing that there is an online audiobook store that displays common properties for each audiobook offered for sale. Such properties include the ratings given by previous buyers, a summary, name of the author, narrator, and length. Users can rate audiobooks on a five-point scale.

---

## Introduction

Let us assume, that there is an online audiobook store that displays common properties for each audiobook offered for sale. Such properties include the ratings given by previous buyers, a summary, name of the author, narrator, and length. Users can rate audiobooks on a five-point scale. Based on these reviews, the system recommends additional audiobooks to each user.

---

## Input

The first line of input contains the number of known ratings, users and audiobooks. Then each line contains a user ID, an audiobook ID, and the corresponding rating. The fields are separated by a tab. Example:

60000 500 200

0 3 4

0 31 3

0 87 2

...

499 192 5

499 198 4



## Output

The output contains the IDs of the top 10 recommended audiobooks for each user,
separated by tabs.
Audiobook Identifiers should be ordered such that the top of the list, i.e. the most
recommended audiobook, comes first. However, the list should not include an
audiobook whose rating is known (already given by that user)! The rows should follow
each other in the order of user IDs. These IDs should not be displayed.
In case of the example above, the output contains 500 lines:

175 21 76 77 119 2 40 42 56 117

32 142 38 111 14 18 101 138 64 29

75 88 47 43 18 150 83 124 166 182

...

---

## Requirements

- Python

---

## Configuration

- You can turn on the Debug Mode setting it True on line 7

`DEBUG = True` 

- You must choose the number of k-similar users on line 10

`K_NEIGHBORS = 2`

- You can choose the number of top audiobooks recommended to be displayed in the output on line 13

`TOP = 10`


---

## Running

You can find sample input files in the folder *sample-inputs*.
You only has to run Python using redirecting the input file to stdin as following

  `py recommender.py < sample-inputs/2.in`
