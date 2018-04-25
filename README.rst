webclean
========

Download and clean articles from the web.

webclean creates cleaned up HTML or text output of articles from the web
similar to the reader feature of most modern browsers.

Usage
-----

Download a news article and display it in w3m
``webclean 'http://annoyinglyformattednews.com/article.html' | w3m -T text/html``

Download a news article and view it as text
``webclean --text 'http://annoyinglyformattednews.com/article.html'``

Installation
------------

``pip install git+https://github.com/phha/webclean``
