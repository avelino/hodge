# hodge

Hodge is a static cms generator in python, the difference is that we give a free hosting for your cms (if you want)!


## Idea

### Start new project

    hodge init <project-name>


### Create new content

    hodge newpost

    Hodge new post create...
    Title: Writting idea to used hodge
    Slug [writting-idea-to-used-hodge]:
    Tags (hodge, static) []:
    Date [2015/04/28 15:33:16]:
    File name [2015_04_28_writting-idea-to-used-hodge.md]:


### Example file generate

    ---
    title: {{ title }}
    date: {{ date }}
    tags: {{ slug }}
    ---

    Writting text here!


### Generate html's

    hodge build


## Templates feature

- Include file (read markdown)_
- Content bock (group news)
- Query set, dynamic populate "Content block"
