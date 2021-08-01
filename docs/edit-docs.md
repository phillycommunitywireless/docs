---
title: Editing these docs
---

# Editing these docs

## Editing files on GitHub

Edits can be made to the site's code directly from the [GitHub repository](https://github.com/phillycommunitywireless/docs/edit/main/docs/edit-docs.md), if you are listed as a contributor for the repo. Just find the file you'd like to edit (the filename will be the same as the page's slug -- "[edit-docs](https://github.com/phillycommunitywireless/docs)" for this page) and click the pencil icon in the corner. Once you've completed your changes, scroll to the bottom, add a commit message, and click "Commit changes". The public docs will update to reflect this.

## Editing files locally

To make edits to docs locally, all you need is `git` and a markdown editor of your choice. 

### Clone the repo

First things first: if you haven't already done so copy the docs repository to your local machine:

``` bash
git clone https://github.com/phillycommunitywireless/docs.git 
cd docs
```

If you already have the repo cloned, you should pull any new changes to synchronize with the remote repo:

``` bash
git pull
```

### Edit markdown files

You should see several markdown files in the `docs/docs` subfolder. These correspond to the pages on the main site. You can open and edit these files in a markdown editor of your choice!

### Finalizing your changes

Once you're confident in the changes you've made to the docs, you can push them back to the remote repo. [ReadTheDocs](https://readthedocs.io) will be notified of these changes and immediately rebuild the public site with your changes reflected.

``` bash
git add .
git commit -m "Add a message specifying what you changed"
git push
```

If this is your first time pushing, you may need to run this instead:

``` bash
git push --set-upstream origin main
```

### Adding new files

If you just add a new `.md` doc to the `docs` folder, you won't see it immediately reflected on the live site. To add it, you'll need to add it to the **site nav configuration**, which is set in the `mkdocs.yml` file at the root of the project.

``` yaml
# /mkdocs.yml

nav:
  - Home: index.md
  - Mesh Kit Setup Guide: mesh-kit/mesh-kit.md
  - Hardware: hardware.md
  - Onboarding: onboarding.md
  - Editing these docs: edit-docs.md
```
To add a new page, just add a new key-value pair to this list:
``` yaml
  - Your New Page: new-page.md
```

## Running a local version of the docs site

This is only necessary if you need to see how the docs are specifically rendered on our live site. Any markdown editor should be able to preview the docs as they will appear on the site, without much deviation. If you want to make styling / structural changes to the site and/or its [theme](https://squidfunk.github.io/mkdocs-material/), this is also the way to do that. 

### Clone the repo

[See above](#clone-the-repo)

### Option 1: Docker

1. Download [Docker](https://www.docker.com/get-started), which should include Docker Compose on most machines.
2. Run `docker-compose up` inside the project directory.
3. The mkdocs server will start up, and can be accessed at `localhost:8000'. Any changes made to the docs will automatically update the page. 

### Option 2: Setup Python Environment  
#### Set up a python virtual environment

_This step is optional but recommended._

It's best practice to use a python virtual environment to install and run mkdocs. To do so, first make sure you have python 3 installed, and run the following commands:

``` bash
# create a virtual environment in the .venv folder
python3 -m venv .venv
# activate the virtual environment
source .venv/bin/activate
```

You are now "in" a python virtual environment. You will leave the environment whenever you exit your terminal session, or when you run `deactivate`. Now, running `which python` should return a path in your `.venv/lib` folder, rather than a global install location like `/usr/bin`. 

#### Install dependencies
``` bash
pip install -r requirements.txt
```

#### Run the development server
``` bash
mkdocs serve
```

Congrats, should now have access to a live-updating version of your local docs site at https://localhost:8000. Pressing `ctrl-c` in the terminal will close the server. Make changes to the docs and see them reflected in real time!
