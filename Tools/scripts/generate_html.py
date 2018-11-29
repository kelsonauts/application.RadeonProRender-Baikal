#!/usr/bin/env python

import os
import sys

argvs = sys.argv

if len(argvs) == 3:
    images_dir = argvs[1]
    output_html_filename = argvs[2]
else:
	sys.exit('Wrong argument count!')

filenames = os.listdir(images_dir)

f = open(output_html_filename,"w+")
f.write("""<!DOCTYPE html>
<html>
    <head>
    <style>
        h1 {border-radius: 25px; background-color: #333333; color: #FFFFFF; font-family: sans-serif; padding: 1%; box-shadow: 0 1px 4px rgba(0, 0, 0, .4); }
        body {background-color: #BBBBBB; color: #FFFFFF; font-family: sans-serif;}
        details {border-radius: 5px; background-color: #FDFDFD; border: 1px solid #B1B1B1; box-shadow: 0 1px 4px rgba(0, 0, 0, .4); color: #262626; margin: 0 0 .5em; padding: 0.2%; font: 8pt monospace;}
        summary {font: 13pt Verdana, Geneva, sans-serif; color: #FFFFFF; background-color: #555555; padding: 2px; border-radius: 5px; }
        div {max-width: 128px; min-height: 32px; word-wrap: break-word;}
    </style>

    <meta charset="utf-8">
        <title>Output Test Images</title>
    </head>
    <body>
    <h1>Output Test Images</h1>
""")

filenames.sort()

tests_map = {}
for fname in filenames:

    if fname.find(".png") == -1:
        continue

    pos = fname.find("_")
    if pos == -1:
        key = "Other"
    else:
        key = fname[:fname.find("_")]
    if key in tests_map:
        tests_map[key].append(fname)
    else:
        tests_map[key] = [fname]

for k in tests_map.keys():
    write_str = """
        <details>
            <summary>{0} Test</summary>
            <table>
        """.format(k)
    f.write(write_str)

    line = 0
    for i in tests_map[k]:
        if line % 11 == 0:
            f.write("<tr>")

        write_str = """
                        <td>
                            <img src="{1}/{0}" width="128">
                            <br>
                            <div>{0}</div>
                        </td>
        """.format(i, images_dir)

        f.write(write_str)

        if line % 11 == 10:
            f.write("</tr>")
        line = line + 1

    write_str = """
            </table>
        </details>
    """

    f.write(write_str)



f.write("""
    </body>
</html>
""")
