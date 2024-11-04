
# Benchmarks

<p style="text-align: justify;">
To showcase the dataset and the associated benchmarking library, we provide a set of simple baselines time-boxed to 12 hours on a single NVIDIA H100 to demonstrate the effectiveness of naive approaches on these challenging problems and motivate the development of more sophisticated approaches. These baselines are trained on the forward problem - predicting the next snapshot of a given simulation from a short history of 4 time-steps. The models used here are the Fourier Neural Operator, Tucker-Factorized FNO, U-net and a modernized U-net using ConvNext blocks. The neural operator models are implemented using the <a href="https://neuraloperator.github.io/dev/index.html"> neuraloperator </a> library. 

We emphasize that these settings are not selected to explore peak performance of modern machine learning, but rather that they reflect reasonable compute budgets and off-the-shelf choices that might be selected by a domain scientist exploring machine learning for their problems. Therefore we focus on popular models using settings that are either defaults or commonly tuned.
</p>


<strong>Test set results for models performing best on the validation set:</strong>

| Dataset                          | FNO     | TFNO    | U-net   | CNextU-net       |
|----------------------------------|---------|---------|---------|------------------|
| $\texttt{acoustic\_scattering}$ (maze)     | 0.5062  | 0.5057  | 0.0351  | **0.0153**       |
| $\texttt{active\_matter}$                  | 0.3691  | 0.3598  | 0.2489  | **0.1034**       |
| $\texttt{convective\_envelope\_rsg}$        | **0.0269** | 0.0283  | 0.0555  | 0.0799          |
| $\texttt{euler\_multi\_quadrants}$ (periodic b.c.) | 0.4081  | 0.4163  | 0.1834  | **0.1531**  |
| $\texttt{gray\_scott\_reaction\_diffusion}$  | **0.1365** | 0.3633  | 0.2252  | 0.1761          |
| $\texttt{helmholtz\_staircase}$            | **0.00046** | 0.00346 | 0.01931 | 0.02758       |
| $\texttt{MHD\_64}$                         | 0.3605  | 0.3561  | 0.1798  | **0.1633**       |
| $\texttt{planetswe}$                      | 0.1727  | **0.0853** | 0.3620 | 0.3724         |
| $\texttt{post\_neutron\_star\_merger}$       | 0.3866  | **0.3793** | -     | -             |
| $\texttt{rayleigh\_benard}$                | 0.8395  | **0.6566** | 1.4860 | 0.6699         |
| $\texttt{rayleigh\_taylor\_instability}$ (At = 0.25) | >10     | >10     | >10     | >10    |
| $\texttt{shear\_flow}$                     | 0.1567  | **0.1348** | 0.5910 | 0.2037         |
| $\texttt{supernova\_explosion\_64}$         | 0.3783  | 0.3785  | **0.3063** | 0.3181       |
| $\texttt{turbulence\_gravity\_cooling}$     | 0.2429  | 0.2673  | 0.6753  | **0.2096**       |
| $\texttt{turbulent\_radiative\_layer\_2D}$   | 0.5001  | 0.5016  | 0.2418  | **0.1956**       |
| $\texttt{turbulent\_radiative\_layer\_3D}$   | 0.5278  | 0.5187  | 0.3728  | **0.3667**       |
| $\texttt{viscoelastic\_instability}$       | 0.7212  | 0.7102  | 0.4185  | **0.2499**       |

*Table 1: Model Performance Comparison - VRMSE metrics on test sets (lower is better) for models performing best on the validation set (results below). Best results are shown in bold. VRMSE is scaled such that predicting the mean value of the target field results in a score of 1.*

<strong>Validation set results:</strong>

| Dataset                              | FNO     | TFNO    | U-net   | CNextU-net       |
|--------------------------------------|---------|---------|---------|------------------|
| $\texttt{acoustic\_scattering}$ (maze)     | 0.5033  | 0.5034  | 0.0395  | **0.0196**       |
| $\texttt{active\_matter}$                  | 0.3157  | 0.3342  | 0.2609  | **0.0953**       |
| $\texttt{convective\_envelope\_rsg}$       | 0.0224  | **0.0195** | 0.0701  | 0.0663          |
| $\texttt{euler\_multi\_quadrants}$ (periodic b.c.) | 0.3993  | 0.4110  | 0.2046  | **0.1228** |
| $\texttt{gray\_scott\_reaction\_diffusion}$ | 0.2044  | **0.1784** | 0.5870  | 0.3596          |
| $\texttt{helmholtz\_staircase}$            | 0.00160 | **0.00031** | 0.01655 | 0.00146       |
| $\texttt{MHD\_64}$                         | 0.3352  | 0.3347  | 0.1988  | **0.1487**       |
| $\texttt{planetswe}$                       | **0.0855** | 0.1061  | 0.3498  | 0.3268         |
| $\texttt{post\_neutron\_star\_merger}$     | 0.4144  | **0.4064** | -       | -               |
| $\texttt{rayleigh\_benard}$                | 0.6049  | 0.8568  | 0.8448  | **0.4807**       |
| $\texttt{rayleigh\_taylor\_instability}$ (At = 0.25) | 0.4013  | **0.2251** | 0.6140  | 0.3771 |
| $\texttt{shear\_flow}$                     | 0.2963  | **0.2087** | 0.5799  | 0.3258         |
| $\texttt{supernova\_explosion\_64}$        | 0.3804  | 0.3645  | 0.3242  | **0.2801**       |
| $\texttt{turbulence\_gravity\_cooling}$    | 0.2381  | 0.2789  | 0.3152  | **0.2093**       |
| $\texttt{turbulent\_radiative\_layer\_2D}$ | 0.4906  | 0.4938  | 0.2394  | **0.1247**       |
| $\texttt{turbulent\_radiative\_layer\_3D}$ | 0.5199  | 0.5174  | 0.3635  | **0.3562**       |
| $\texttt{viscoelastic\_instability}$       | 0.7195  | 0.7021  | 0.3147  | **0.1966**       |

*Table 2: Dataset and model comparison in VRMSE metric on the validation sets, best result in bold. VRMSE is scaled such that predicting the mean value of the target field results in a score of 1.*

<strong> Rollout loss: </strong>

| Dataset                              | FNO (6:12) | FNO (13:30) | TFNO (6:12) | TFNO (13:30) | U-net (6:12) | U-net (13:30) | CNextU-net (6:12) | CNextU-net (13:30) |
|--------------------------------------|------------|-------------|-------------|--------------|--------------|---------------|--------------------|---------------------|
| $\texttt{acoustic\_scattering}$ (maze)     | 1.06       | 1.72        | 1.13        | 1.23         | **0.56**     | <u>0.92</u>   | 0.78               | 1.13               |
| $\texttt{active\_matter}$                  | $>$10      | $>$10       | 7.52        | 4.72         | 2.53         | <u>2.62</u>   | **2.11**           | 2.71               |
| $\texttt{convective\_envelope\_rsg}$       | **0.28**   | <u>0.47</u> | 0.32        | 0.65         | 0.76         | 2.16          | 1.15               | 1.59               |
| $\texttt{euler\_multi\_quadrants}$         | 1.13       | <u>1.37</u> | 1.23        | 1.52         | **1.02**     | 1.63          | 4.98               | $>$10              |
| $\texttt{gray\_scott\_reaction\_diffusion}$ | 0.89       | $>$10       | 1.54        | $>$10        | 0.57         | $>$10         | **0.29**           | <u>7.62</u>        |
| $\texttt{helmholtz\_staircase}$            | **0.002**  | <u>0.003</u>| 0.011       | 0.019        | 0.057        | 0.097         | 0.110              | 0.194              |
| $\texttt{MHD\_64}$                         | **1.24**   | <u>1.61</u> | 1.25        | 1.81         | 1.65         | 4.66          | 1.30               | 2.23               |
| $\texttt{planetswe}$                       | 0.81       | 2.96        | **0.29**    | 0.55         | 1.18         | 1.92          | 0.42               | <u>0.52</u>        |
| $\texttt{post\_neutron\_star\_merger}$     | 0.76       | 1.05        | **0.70**    | <u>1.05</u>  | ---          | ---           | ---                | ---                |
| $\texttt{rayleigh\_benard}$                | $>$10      | $>$10       | $>$10       | $>$10        | $>$10        | $>$10         | $>$10              | $>$10              |
| $\texttt{rayleigh\_taylor\_instability}$   | $>$10      | $>$10       | **6.72**    | $>$10        | $>$10        | <u>2.84</u>   | $>$10              | 7.43               |
| $\texttt{shear\_flow}$                     | 1.62       | $>$10       | 1.63        | $>$10        | 1.22         | $>$10         | 0.32               | 1.91               |
| $\texttt{supernova\_explosion\_64}$        | 2.41       | $>$10       | 1.86        | $>$10        | **0.94**     | <u>1.69</u>   | 1.12               | 4.55               |
| $\texttt{turbulence\_gravity\_cooling}$    | 3.55       | 5.63        | 4.49        | 6.95         | 7.14         | 4.15          | **1.30**           | <u>2.09</u>        |
| $\texttt{turbulent\_radiative\_layer\_2D}$ | 1.79       | 3.54        | 6.01        | $>$10        | 0.66         | 1.04          | **0.54**           | <u>1.01</u>        |
| $\texttt{turbulent\_radiative\_layer\_3D}$ | 0.81       | 0.94        | $>$10       | $>$10        | 0.95         | 1.09          | **0.77**           | <u>0.86</u>        |
| $\texttt{viscoelastic\_instability}$       | 4.11       | ---         | 0.93        | ---          | 0.89         | ---           | **0.52**           | ---               |

*Table: Time-Averaged Losses by Window - VRMSE metrics on test sets (lower is better), averaged over time windows (6:12) and (13:30). Best results are shown in bold for (6:12) and underlined for (13:30). VRMSE is scaled such that predicting the mean value of the target field results in a score of 1.*

