#!/bin/bash
root="./sunpy/v1"
echo "<html>
    <head>
        <title>Sunpy v1 sample data</title>
    </head>
    <body>
        <p> Sunpy v1 sample data, see <a href=https://github.com/sunpy/sample-data/tree/master/sunpy/v1>GitHub</a> for sources.
        <h2> File Listing</h2>

        "
echo "<ul>"
for file in "$root"/*; do
  parentpath="${file#*/}"
  filename="${file#*/}"
  echo "<li><a href=\"$parentpath\">$filename</a></li>"
done
echo "</ul>"
echo "</body>"
echo "</html>"
