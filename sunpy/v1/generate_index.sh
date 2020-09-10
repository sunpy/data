#!/bin/bash
root="./*"
echo "<html>
    <head>
        <title>Sunpy v1 sample data</title>
    </head>
    <body>
        <p> Sunpy v1 sample data, see <a href=https://github.com/sunpy/sample-data>GitHub</a> for sources.
        <h2> File Listing</h2>

        "
echo "<ul>"
for file in $root; do
  filename="${file##*/}"
  echo " <li><a>$filename</a></li>"
done
echo "</ul>"
echo "</body>"
echo "</html>"
