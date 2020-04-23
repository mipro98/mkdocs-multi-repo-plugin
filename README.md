# Mkdocs plugin: `multi_repo`

Inspired by https://gitlab.com/paulrbr/mkdocs-edit-url/



Use different git repositories in one documentation. Therefore, the `edit_url` gets adjusted to point the right repo by taking the folder name as repository name. **Currently only repos from the same owner can be used**.

This is intended if you build a documentation exclusively out of different repositories. So the folder structure should be:

```
├── docs
│   ├── first-repo
│   │   ├── documentation.md
│   │   └── ...
│   ├── another-repo
│   │   └── information.md
│   │   └── ...
│   └── other-repo
│       └── some-article.md
│       └── ...
└── mkdocs.yml
```

Each folder inside `docs` is its own git repository. The **folder name has to be the one of the git repository** (it will be used when creating the url).

**Note:** the link button to the repository will just bring you to your Github/Gitlab/Gitea/etc. profile.

## Installation

Just execute

```sh
sudo pip3 install .
```

inside the base directory of this repo (`setup.py` will be executed)

## Usage

Say in your `mkdocs.yml` configuration file:

```yaml
plugins:
  - multi_repo
  - ...
```

Also, in your `mkdocs.yml`, the `repo_url` has to be adjusted to just point to your profile, e.g. `repo_url: 'https://github.com/username'` instead of `repo_url: 'https://github.com/username/repositoryname'`.

The edit url can stay the same (e.g. `edit_uri: 'edit/master'`). The resulting edit url when clicking the edit button inside a doc will then be:

```
${repo_url} + ${root_foldername_of_file} + ${edit_uri} + ${relative_filename_path}
```

 
