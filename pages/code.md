---
layout: page
title: Sven Schippkus/code
site_header: code
---

#### published code

##### azimuthal anisotropy of rayleigh waves

repository: [github/schipp/azimuthal_anisotropy](https://github.com/schipp/azimuthal_anisotropy)

In Schippkus et al. ([2020](http://doi.org/10.1093/gji/ggz565)), we demonstrate that residual Rayleigh-wave group velocities after inversion for isotropic velocity maps contain information about the anisotropic structure of the Earth. This code is an updated version of the code originally used in the paper. This new version no longer relies on the parametrization of the isotropic inversion. It only requires inter-station measurements and station-pair locations as input, and can be rapidly applied to many already-existing data.

&nbsp;

##### TODO: moment tensor inversion

repository: [github/schipp/mti](https://github.com/schipp/mti)

Moment-tensor inversion by grid-searching the double-couple space, comparing synthetic with recorded waveforms. Waveform similarity is estimated by a combination of L1- and L2-norms. In Schippkus et al. ([2019](http://doi.org/10.17738/ajes.2019.0010)), we use this code to determine the moment tensor of the [Alland mainshock](https://www.zamg.ac.at/cms/de/geophysik/news/kraeftiges-erdbeben-im-osten-oesterreichs) near Vienna (ML 4.2 on April 25th 2016) using the [AlpArray](http://www.alparray.ethz.ch) network.

&nbsp;

##### bolide near salzburg on april 6th 2020

repository: [github/schipp/bolide_salzburg](https://github.com/schipp/bolide_salzburg)

Early data exploration to check for seismo-acoustic signals of the bolide that was seen near Salzburg on April 6th 2020. Some signals are present that were identified by [ZAMG](https://www.zamg.ac.at/cms/de/geophysik/news/feuerkugel-ueber-oesterreich-wurde-seismisch-registriert) to be caused by the bolide. Most stations do not show clear arrivals near expected times. Not finished, feel free to dig deeper.

&nbsp;

##### dotfiles

repository: [github/schipp/dot](https://github.com/schipp/dot)

Configuration files for my MacOS environment: Alacritty (Terminal), TMUX (Terminal Multiplexer), zsh (Shell), vim (Editor), jrnl (Journaling), Alfred (better spotlight)

&nbsp;

&nbsp;

#### useful libraries

##### scientific colourmaps

Fabio Crameri has published a [collection](http://www.fabiocrameri.ch/colourmaps.php) of perceptually uniform colormaps. Highly recommended.
