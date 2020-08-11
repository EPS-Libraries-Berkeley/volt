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
```{image} ./images/no_potw2013a.jpg
:alt: Hubble Space Telescope image of a Cannibal Galaxy
:height: 100px
:align: center
```
<em>Image source: [https://www.nasa.gov/mission_pages/hubble/multimedia/index.html](https://www.nasa.gov/mission_pages/hubble/multimedia/index.html)</em>

Geographic data uses human-understandable means to describe and represent location. For example, a town name (San Jose) or a street intersection (Hearst & Euclid) both describe locations in ways that humans can interpret relatively easily and set in context. Geographic data can also include **attributes** about a location, for example how many people live in a city or the name of a building.

**Geospatial data** on the other hand encodes location with coordinates. It consists of geometric representations. This type of representation using geospatial coordinates allows a computer to understand the location. Correctly interpreting the town name "San Jose" requires context (which country? which state?), but geospatial coordinates are (relatively) unambiguous. Just like geographic data, geospatial data can also include **attribute** information about a location.

Geospatial data is powerful! It can be:
* mapped!
* used to derive spatial measurements like area and distance
* used for determine spatial relationships like inside, next to, etc.

## To be continued... :)
