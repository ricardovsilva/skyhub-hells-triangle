# Hell Triangle Challenge - Made in Python
This repository contains code, in python3, that simples solve the Hell Triangle challenge.
This is a cool case to study because it envolves:
- Recursivity

## What is the Hell Triangle Challenge?
Given a triangle of numbers, find the maximum total from top to bottom.
But, an element can only be summed with one of the two nearest elements in the next row.
Consider triangle below:
```
        6
       3 5
      9 7 1
     4 6 8 4
```
In the above the total is: ​ 6 + 5 + 7 + 8 = 26
For example: The element 3 in the 2nd row can only be summed with 9 and 7, but not with 1.
Simple as that!

## Steps to download and run
In prior to run this application you need python 3 installed and pip package manager. If you don't have any of this, please refeer to official docs.

1. Download or clone this repository
2. Navigate to this repository
> $ cd ~/where-you-downloaded-repo
3. Install all dependencies with pip
> $ pip3 install -r requirements.txt
4. Run all tests to ensure that you don't have downloaded a broken version
> $ python3 tests/hell_triangle_tests.py
5. Run Hell Triangle Challenge
> $ python3 run.py

It will ask you for an array with the triangle, this array must be a valid triangle. A valid triangle has N lines and each line has one column more than previous line. You can type or simple copy and paste that triangle on terminal.

Example of a valid triangle:
> [[6],[3 5],[9 7 1],[4 6 8 4]]

Input an invalid triangle will result into a ValueError to be raised.

## Why python?
I just love python and I believe that it's language fit as a glove for that kind of problem. Python is a very simple language. Is very easy to write some algorithms and tests. Also, python is really good to manipulate data structures.
One downside of python, as any script language, is performance. In comparison to compiled language, it has a poor performance, so keep that in mind to each project that you will develop.