---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.8'
    jupytext_version: 1.4.1+dev
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Digital Mapping

This tutorial will give a short introduction to some digital mapping concepts, tools, and data.

## What is digital mapping?

Digital mapping uses computer software (either desktop or web based) to create digital maps. The basic components of digital mapping are **geospatial data** and specialized software called **GIS** ( **G**eographic **I**nformation **S**ystems ). We'll look at each of the these in more detail below.

## Components of digital mapping

### Geographic data vs. geospatial data

**Geographic data** is data about locations on or near the surface of the earth. It can scale from the very local all the way up to a global level.
```{note} Because geographic data only includes data on or near the surface of the earth it does not include data about outer space or other planets!
```
```{image} ../images/potw2013a.jpg
:alt: Hubble Space Telescope image of a Cannibal Galaxy
:height: 100px
```
Image source: [https://www.nasa.gov/mission_pages/hubble/multimedia/index.html](target "https://www.nasa.gov/mission_pages/hubble/multimedia/index.html")

**Geospatial data** on the other hand is data...