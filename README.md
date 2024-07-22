# the_well_web
Tools for building a website featuring visualizations from polymathic/the_well
-- 
<a href="https://thewell.flatironinstitute.org/">https://thewell.flatironinstitute.org/</a>.

# Prerequisites

This site generator uses 
<a href="https://www.python.org/downloads/">Python 3</a>, 
<a href="https://www.mkdocs.org/">MkDocs</a>. and
<a href="https://github.com/squidfunk/mkdocs-material">Material for MkDocs</a>.


# Preview the mkdocs website template structure

```bash
cd $root/template
mkdocs serve
```

# Build the mkdocs markdown tree

```bash
cd $root/scripts
python gif_parser.py
```

# Preview the mkdocs site

```
cd $root/mkdocs
mkdocs serve
```

# Build the static site from the generated mkdocs tree

```
cd $root/mkdocs
mkdocs build
```

The generated site is created in `$root/mkdocs/site`.

