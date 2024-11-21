<head>
    <link rel="stylesheet" href="style.css">
</head>

<div class="title-container">
    <img src="/assets/images/_TheWell Color.svg" alt="The Well Icon" class="title-icon">
</div>


<figure class="video_container">
  <video allowfullscreen="true" autoplay loop>
    <source src="/assets/videos/background.mp4" type="video/mp4">
  </video>
</figure>


Welcome to the Well, a large-scale collection of machine learning datasets containing numerical simulations of a wide variety of spatiotemporal physical systems. The Well draws from domain scientists and numerical software developers to provide 15TB of data across 16 datasets covering diverse domains such as biological systems, fluid dynamics, acoustic scattering, as well as magneto-hydrodynamic simulations of extra-galactic fluids or supernova explosions. These datasets can be used individually or as part of a broader benchmark suite for accelerating research in machine learning and computational sciences.

<br><br>

# Getting Started

## Prerequisites

The Well datasets range between 6.9GB and 5.1TB of data each, for a total of 15TB for the full collection. Ensure that your system has enough free disk space to accomodate the datasets you wish to download.

If you plan to use The Well datasets to train or evaluate deep learning models, we recommend to use a machine with enough computing resources.

## Installation

First, create and activate a new Python (>=3.10) environment, for example with <a href="https://docs.python.org/3/library/venv.html" target="_blank">venv</a>.

```console
~ $ python -m venv path/to/myenv
~ $ source path/to/myenv
```

Then, clone the <a href="https://github.com/PolymathicAI/the_well" target="_blank">project repository</a> and install the `the_well` package with its dependencies.

```console
(myenv) ~ $ git clone https://github.com/PolymathicAI/the_well
(myenv) ~ $ cd the_well
(myenv) ~/the_well $ pip install . --extra-index-url https://download.pytorch.org/whl/cu121
```

You should replace `cu121` depending on you hardware. If you want to run the benchmarks, you should install additional dependencies.

```console
(myenv) ~/the_well $ pip install .[benchmark] --extra-index-url https://download.pytorch.org/whl/cu121
```

## Downloading a dataset

Once `the_well` is installed, you can use the `the-well-download` command to download any dataset of The Well. By default, the dataset will be downloaded in the corresponding subfolder of datasets as provided with this repository. However, it is possible to override the download location with the `--output_dir` argument.

```console
(env) ~/the_well $ the-well-download --dataset active_matter --output_dir path/to/datasets
```

If the `--dataset` argument is omitted, all datasets will be downloaded. This could take a while!

## Using a dataset

Please refer to the [tutorials](/tutorials/dataset).
