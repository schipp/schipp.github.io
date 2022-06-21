---
layout: page
title: Sven Schippkus/code
site_header: /code
---

#### [· numerical matched field processing](https://github.com/schipp/matched_field_processing)

[<img src="/home/data/previews/mfp_new_preview.png" width="100px" style="float:left; padding-right:15px">](https://github.com/schipp/matched_field_processing)

Matched Field Processing (MFP) is a technique to locate the source of a recorded wave field. It is the generalization of beamforming, allowing for curved wavefronts. In the standard approach to MFP, simple analytical Green's functions are used as synthetic wave fields that the recorded wave fields are matched against. We introduce an advancement of MFP by utilizing Green's functions computed numerically for real Earth structure as synthetic wave fields. This allows in principle to incorporate the full complexity of elastic wave propagation, and through that provide more precise estimates of the recorded wave field's origin.

#### [· eikonal tomography](https://github.com/schipp/eikonal_tomography)

[<img src="/home/data/previews/eikonal_preview.png" width="100px" style="float:left; padding-right:15px">](https://github.com/schipp/eikonal_tomography)

The Eikonal equation relates local phase velocity c to the local gradient of travel times ∇T: ∇T = 1/c. When a wave field is densely sampled, the travel-time field can be reconstructed and velocity maps can be computed directly from its gradient. This is a synthetic demonstration of this concept. Travel times in a random velocity model are computed by Fast-Marching-Method for specific station locations and the travel time field is reconstructed from these.

&nbsp;

#### [· azimuthal anisotropy of rayleigh waves](https://github.com/schipp/azimuthal_anisotropy)

[<img src="/home/data/previews/aniso_preview.png" width="100px" style="float:left; padding-right:15px">](https://github.com/schipp/azimuthal_anisotropy)

In Schippkus et al. ([2020](http://doi.org/10.1093/gji/ggz565)), we demonstrate that residual Rayleigh-wave group velocities after inversion for isotropic velocity maps contain information about the anisotropic structure of the Earth. This code is an updated version of the code used in the paper. This version no longer relies on the specific parametrization of the isotropic inversion. It can be rapidly applied to many already-existing data.

&nbsp;

#### [· standard matched field processing](https://github.com/schipp/matched_field_processing_simple)

[<img src="/home/data/previews/mfp_preview.png" width="100px" style="float:left; padding-right:15px">](matched_field_processing_simple)

Matched Field Processing is Beamforming in the spatial domain and is thus not limited to the plane-wave assumption. Beampowers are computed using the Bartlett processor. A sample source is placed in the underground and randomly stations resolve this source. The code is a synthetic demonstration of the methodology detailed in Umlauft & Korn ([2019](http://doi.org/10.1093/gji/ggz385)).

&nbsp;

#### [· moment tensor inversion](https://github.com/schipp/moment_tensor_inversion)

[<img src="/home/data/previews/mt_preview.png" width="100px" style="float:left; padding-right:15px">](https://github.com/schipp/moment_tensor_inversion)

Moment-tensor inversion by grid-searching the double-couple space, comparing synthetic with recorded waveforms. Waveform similarity is estimated by a combination of L1- and L2-norms. In Schippkus et al. ([2019](http://doi.org/10.17738/ajes.2019.0010)), we use this code to determine the moment tensor of the [Alland mainshock](https://www.zamg.ac.at/cms/de/geophysik/news/kraeftiges-erdbeben-im-osten-oesterreichs) near Vienna (ML 4.2 on April 25th 2016) using the [AlpArray](http://www.alparray.ethz.ch) network.

&nbsp;

#### [· bolide near salzburg on april 6th 2020](https://github.com/schipp/bolide_salzburg)

Early data exploration to check for seismo-acoustic signals of the bolide that was seen near Salzburg on April 6th 2020. Some signals are present that were identified by [ZAMG](https://www.zamg.ac.at/cms/de/geophysik/news/feuerkugel-ueber-oesterreich-wurde-seismisch-registriert) to be caused by the bolide. Most stations do not show clear arrivals near expected times. Not finished, feel free to dig deeper.

&nbsp;

#### [· dotfiles](https://github.com/schipp/dot)

Configuration files for my MacOS environment: zsh (Shell), Alacritty (Terminal), TMUX (Terminal Multiplexer)

&nbsp;

#### useful external libraries

##### [· scientific colourmaps](http://www.fabiocrameri.ch/colourmaps.php)
