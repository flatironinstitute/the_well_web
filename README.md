# Note: This historical proof of concept has been superceded

The officially released version is here: 
<a href="https://github.com/PolymathicAI/the_well/tree/master/docs">https://github.com/PolymathicAI/the_well/tree/master/docs</a>.


# the_well_web
Proof of concept tools for building a website featuring visualizations from polymathic/the_well
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

The preview site has everything except individual animations for each simulation.
The animation pages are stubs which are replaced by the build script explained below.

To modify the site please edit the pages in the template directory and preview them
using `serve` in the template directory.

## Editing the simulation descriptions

The description pages for the simulations are located in `template/docs/descriptions` -- modify
the files in that folder to edit the descriptions.  

For example to change the description for the `acoustic scattering maze 2d` simulation edit the content
of the file

`template/docs/descriptions/acoustic_scattering_maze_2d.md`

## Editing the trailer information

At the bottom of each page is a "trailer" which lists the arxiv paper, email address, and github repository.
This trailer is defined in the main html template located here:

`template/docs/overrides/main.html`

To edit the trailer change the HTML under the comment

`<!-- This is the standard trailing HTML content. -->`

# Build the mkdocs markdown tree

To build the full site, including all the animation links, run the following python script.

```bash
cd $root/scripts
python gif_parser.py
```

# Preview the mkdocs site

To preview the full site, serve the generated site as follows:

```
cd $root/mkdocs
mkdocs serve
```

# Build the static site from the generated mkdocs tree

To build the static HTML tree for publication, use `mkdocs build` as follows:

```
cd $root/mkdocs
mkdocs build
```

The generated site is created in `$root/mkdocs/site`.

