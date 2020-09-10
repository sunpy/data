#!/bin/bash
root="./"
echo "<html>
    <head>
        <title>SunPy Data Store</title>
    </head>
    <body>
        <p> SunPy Data Repo, see <a href=https://github.com/sunpy/sample-data>GitHub</a> for sources.
        <h2> File Listing</h2>

        "
echo "<ul>"
for file in "$root"/*/*; do
  parentpath="${file#*/}"
  parent="${parentpath%/*}"
  filename="${file##*/}"
  if [[ -z $oldparent ]]; then
    echo "  <li> $parent </li>" && oldparent="$parent"
    echo "  <ul>"
  elif [[ $oldparent != $parent ]]; then
    echo "  </ul>"
    echo "  <li> $parent </li>" && oldparent="$parent"
    echo "  <ul>"
  fi
  echo "    <li><a href=\"$parentpath\">$filename</a></li>"
done
echo "  </ul>"
echo "</ul>"
echo "</body>"
echo "</html>"
