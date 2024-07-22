# the_well_web
Tools for building a website featuring visualizations from polymathic/the_well

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

