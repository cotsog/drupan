# drupan - static site generator
drupan is a static site generator. You can use it for blogs, sites or anything
you can imagine. Adding new features is easy thanks to an easy to use plugin
system.

[![Build Status](https://travis-ci.org/fallenhitokiri/drupan.png?branch=development)](https://travis-ci.org/fallenhitokiri/drupan)

## Installation
You can install drupan with an easy ```pip install drupan``` or ```easy_install```
if you have to use it.

If you just check out the source use ```dp.py``` instead of ```drupan``` if you
follow the quick start guide. Make sure you have all dependencies installed, run 
```pip install -r requirements.txt```.

## Quick Start
Run ```drupan --init path-to-site```. You find a template for a post or a
page in your new sites path in the directory ```draft```.

Run ```drupan path-to-site --no-deploy --serve``` and visit your new site
on ```http://localhost:9000```.

## Features
  - Markdown support
  - Image support
  - Deploy with git
  - Generate archives and RSS Feeds
  - Easily extend it using plugins
  - Minimal external dependencies
  - syntax highlighting using pygments

### Jinja
drupan uses Jinja as template system and you can access everything drupan considers
Content in every template. So your imagination is the limit of your site. (Well
beside some technical stuff)

### Dependencies
  - PyYAML
  - Jinja2
  - markdown2
  - pygments

If you do not want to use Jinja as templating engine or markdown for your posts
you can deactive both plugins in your configuration file and ignore the packages.
They are only needed by the corresponding plugin.

## Python support
drupan is tested against Python 2.6 and 2.7. Currently Python 3.0 is *not* 
supported.
