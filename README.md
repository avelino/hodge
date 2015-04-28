# hodge

Hodge is a static site generator in python, the difference is that we give a free hosting for your blog (if you want)!


## Idea

### Start new site

    hodge init <site-name>


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


### Generate static html

    hodge build


## Templates feature

- Include file (read markdown)
- Content block (group news)
- Query set, dynamic populate "Content block"
