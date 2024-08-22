
import os
import shutil

GIF_LISTING = "../data/all_mp4.txt"

# for example
# ./MHD_256/MHDMa_0.7_Ms_0.5.hdf5/MHD_256-f0-density-c0/MHD_256-f0-density-s1-c0.gif
class GifInfo:

    def __init__(self, path):
        path = path.strip()
        self.path = path
        #print(path)
        sp = path.split('/')
        self.slice_num = self.field_dim = "n/a"
        self.field_type = self.field_id = "???"
        if len(sp) == 4:
            self.dims = 2
            [_, self.sim, self.hdf, gif] = sp
        elif len(sp) == 5:
            self.dims = 3
            [_, self.sim, self.hdf, self.field_id, gif] = sp
        else:
            raise ValueError("bad path " + repr(sp))
        prefix = gif.split('.')[0]
        gifsp = prefix.split('-')
        sim = gifsp[0]
        assert sim == self.sim, "sim mismatch " + sim + " " + self.sim + " " + repr(sp)
        field = None
        for component in gifsp[1:]:
            ind = component[0]
            suffix = component[1:]
            try:
                num = int(suffix)
            except ValueError:
                # special case for "d(0,0)"
                if ind == 'd' and suffix[0] == '(':
                    self.field_dim = suffix
                else:
                    assert field is None, "field already set " + repr([field, component]) + " " + repr(sp)
                    field = component
                    self.field = field
            else:
                if ind == 'f':
                    self.file_num = num
                elif ind == 's':
                    self.slice_num = num
                elif ind == 'c':
                    self.cond = num
                elif ind == 't':
                    self.field_type = num
                elif ind == 'd':
                    self.field_dim = num
                else:
                    raise ValueError("bad ind " + ind + " " + repr(sp))
                
    def sort_key(self):
        return (self.sim, self.field, self.cond, self.file_num, self.slice_num)
                
    def locate(self, root):
        if root[-1:] != '/':
            root += '/'
        self.location = self.path.replace("./", root)
        self.mp4 = self.location.replace(".gif", ".mp4")
        return self.location
    
    def __repr__(self) -> str:
        return giffmt.format( **self.__dict__)
    
    def html_table(self):
        return html_table_format.format( **self.__dict__)
    
    def img_tag(self):
        return f'<img src="{self.location}" alt="{self.path}"/>'
    
    def video_tag(self):
        return video_fmt.format(mp4=self.mp4)
    
video_fmt = '''
<video controls>
    <source src="{mp4}" type="video/mp4">
    Your browser does not support the video tag.
</video>
'''
    
giffmt = '''
GifInfo(
    path = {path},
    sim = {sim},
    field = {field},
    hdf = {hdf},
    file_num = {file_num},
    slice_num = {slice_num},
    cond = {cond},
    field_type = {field_type},
    field_dim = {field_dim}
    )
'''

html_table_format = '''
<table>
    <tr>
        <th>Path</th>
        <td>{path}</td>
    </tr>
    <tr>
        <th>Sim</th>
        <td>{sim}</td>
    </tr>
    <tr>
        <th>Field</th>
        <td>{field}</td>
    </tr>
    <tr>
        <th>HDF</th>
        <td>{hdf}</td>
    </tr>
    <tr>
        <th>File Num</th>
        <td>{file_num}</td>
    </tr>
    <tr>
        <th>Slice Num</th>
        <td>{slice_num}</td>
    </tr>
    <tr>
        <th>Condition</th>
        <td>{cond}</td>
    </tr>
    <tr>
        <th>Field Type</th>
        <td>{field_type}</td>
    </tr>
    <tr>
        <th>Field Dim</th>
        <td>{field_dim}</td>
    </tr>
</table>
'''

page_line_eg = '      - Page template: additional-pages/page-template.md'
line_name_eg = 'Page template'
line_path_eg = 'additional-pages/page-template.md'

def page_line(name, path):
    return f'      - {name}: {path}'

class SimsInfo:

    def __init__(self, lines):
        self.sims = {}
        #gifinfos = [GifInfo(line) for line in lines]
        gifinfos = []
        self.gifinfos = gifinfos
        for line in lines:
            try:
                gifinfo = GifInfo(line)
                gifinfos.append(gifinfo)
            except ValueError:
                print("bad line", line)
        for gifinfo in gifinfos:
            self.sims[gifinfo.sim] = {}
        for gifinfo in gifinfos:
            self.sims[gifinfo.sim][gifinfo.cond] = {}
        for gifinfo in gifinfos:
            self.sims[gifinfo.sim][gifinfo.cond][gifinfo.field] = {}
        for gifinfo in gifinfos:
            self.sims[gifinfo.sim][gifinfo.cond][gifinfo.field][gifinfo.sort_key()] = gifinfo

    def locate(self, root):
        for gifinfo in self.gifinfos:
            gifinfo.locate(root)

    def generate_page_lines(self):
        lines = []
        simlinks = self.simlinks
        for sim in sorted(self.sims.keys()):
            lines.append(page_line(sim, simlinks[sim]))
        return "\n".join(lines)

    def generate_markdown_files(self, to_dir, markdown_root):
        self.simlinks = simlinks = {}
        for sim, conds in self.sims.items():
            filename = sim + ".md"
            filepath = os.path.join(to_dir, filename)
            self.generate_markdown_file(filepath, sim, conds)
            markdownpath = os.path.join(markdown_root, filename)
            simlinks[sim] = markdownpath
        return simlinks

    def generate_markdown_file(self, filepath, sim, conds):
        with open(filepath, 'w') as f:
            f.write(f"# Simulation: {sim}\n\n")
            for cond in sorted(conds.keys()):
                fields = conds[cond]
                f.write(f"## Initial condition: {cond}\n\n")
                for field in sorted(fields.keys()):
                    gifs = fields[field]
                    f.write(f"### Field: {field}\n\n")
                    for srt in sorted(gifs.keys()):
                        gif = gifs[srt]
                        f.write(gif.html_table() + "\n\n")
                        #f.write(gif.img_tag() + "\n\n")
                        f.write(gif.video_tag() + "\n\n")

    def generate_markdown_file0(self, filepath, sim, conds):
        with open(filepath, 'w') as f:
            f.write(f"# Simulation: {sim}\n\n")
            for cond, gifs in conds.items():
                f.write(f"## Initial condition: {cond}\n\n")
                for fn, gif in gifs.items():
                    f.write(gif.html_table() + "\n\n")
                    f.write(gif.img_tag() + "\n\n")

    def __repr__(self) -> str:
        lines = []
        for sim, conds in self.sims.items():
            lines.append("")
            lines.append("SIMULATION:: " + repr(sim))
            for cond, gifs in conds.items():
                lines.append(":: " + repr(cond))
                for fn, gif in gifs.items():
                    lines.append(repr(gif)) 
        return "\n".join(lines)

def get_sims_info(from_file=GIF_LISTING):
    with open(from_file, 'r') as f:
        lines = f.readlines()
    return SimsInfo(lines)


RUSTY_GIF_LOCATION = "/mnt/home/awatters/public_www/polymathic/assets/gifs"

def generate_site(at_folder, gif_folder):
    print ("Generating mkdocs site at", at_folder, "from gifs at", gif_folder)
    sims_info = get_sims_info()
    if not os.path.exists(gif_folder):
        if os.path.exists(RUSTY_GIF_LOCATION):
            shutil.copytree(RUSTY_GIF_LOCATION, gif_folder)
        else:
            print("Please get gifs from the rusty cluster at", RUSTY_GIF_LOCATION)
            print("and put them here: ", gif_folder)
            raise ValueError("no gif folder at " + gif_folder)
    if os.path.exists(at_folder):
        shutil.rmtree(at_folder)
    shutil.copytree("../template", at_folder)
    shutil.copytree(gif_folder, os.path.join(at_folder, "docs/assets/gifs"))
    # gif location relative to markdown files
    gif_location = "../../assets/gifs"
    sims_info.locate(gif_location)
    mdroot = "additional-pages"
    mdpath = at_folder + "/docs/" + mdroot
    simlinks = sims_info.generate_markdown_files(mdpath, mdroot)
    # The page lines are now static (not generated)
    if 0:
        page_lines = sims_info.generate_page_lines()
        config_template = open("../template/mkdocs.yml").read()
        config = config_template.replace(page_line_eg, page_lines)
        with open(at_folder + "/mkdocs.yml", 'w') as f:
            f.write(config)

def test():
    generate_site("../mkdocs", "../gifs")

def test1():
    generate_site("/Users/awatters/repos/the_well_web/mkdocs", "/Users/awatters/misc/polymathic/gifs")

def test0():
    sims_info = get_sims_info()
    #print(repr(sims_info))
    mdpath = "/tmp/markdown"
    mdroot = "/additional/pages"
    if not os.path.exists(mdpath):
        os.mkdir(mdpath)
    sims_info.locate(mdroot)
    simlinks = sims_info.generate_markdown_files(mdpath, mdroot)
    print(sims_info.generate_page_lines())

if __name__ == '__main__':
    test()