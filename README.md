# Mkdocs plugin: `edit_url`

This is a fork of https://gitlab.com/paulrbr/mkdocs-edit-url/

## TL;DR

use different git repositories in one documentation. Therefore, the edit_url gets adjusted to the right repo


## Usage

Include this plugin in your documentation repository inside a `plugins/` directory.

Finally, load it in your `mkdocs.yml` configuration file as such:

```yaml
plugins:
  - edit_url
  - ...
```
