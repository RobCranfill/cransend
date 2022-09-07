#!/bin/bash
# test of python script

BODY=\
'<p>This is a test of my Emailer Class.</p>\n
<p>This is another paragraph.</p>\n
<ul>\n
<li>This is a list item</li>\n
<li>This is a list item</li>\n
<li>This is a list item</li>\n
</ul>\n
<pre>\n
This is preformatted, useful?\n
This 2 is preformatted, useful?\n
This 3 is preformatted, useful?\n
</pre>\n'

echo -e $BODY | ./cransend.py -s "Test from script" robcranfill@robcranfill.net

