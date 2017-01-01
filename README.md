# FullStack-Movies

## Introduction

This is my Project: Movie Trailer Website for the Programming Foundations with Python module of the Udacity Nanodegree for Full Stack Web Development.
The code generates a html file which, when opened, displays the list of the 88th Academy Awards Best Picture Nominees.
Clicking the movie posters brings up a linked YouTube video of the movie's trailer.

The project was writen in Python 2.7.

## How It Works

1. Clone or download this repository to your computer.
2. Run the "entertainment_center.py" file.
4. Once the program has finished running, a file named "fresh_tomatoes88.html" should be written to the directory you ran the "entertainment_center" program from.
5. Open "fresh_tomatoes88.html" and enjoy your new website!


## Modules & Libraries
* media.py
* entertainment_center.py
* fresh_tomatoes88.py


**media.py** contains the code for the class "Movies". Dependencies: webbrowser (standard library).

**entertainment_center.py** instantiates the movie objects, creates and array of the objects, and runs the open_movies_page function contained in the fresh_tomatoes88.py file. Dependencies: fresh_tomatoes88 and media.

**fresh_tomatoes88.py** contains the html formatting of the page as well as python scripting for the movie titles and creation of the hmtl page (fresh_tomatoes88.html). Dependencies: webbrowser, os, and re modules. This module was derived from fresh_tomatoes.py provided by Udacity.

## Using the Application
1. Clone or download this repository to your computer.
2. Run the "entertainment_center.py" file.
4. Once the program has finished running, a file named "fresh_tomatoes88.html" should be written to the directory you ran the "entertainment_center" program from.
5. Open "fresh_tomatoes88.html" and watch the trailers 88th Academy Awards Best Picture Nominees.
 
