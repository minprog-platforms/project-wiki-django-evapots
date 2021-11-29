# Design Document: *Encyclopedia*

## Application Workflow
The workflow of the webpage of *Encyclopedia* is going to be in line with the image displayed below.
1. The squares represent the html webpages, the title of the webpage is stated above these squares.
2. The grey rectangle in these squares represent the sidebar, which content is also displayed in the lower left corner.
3. The content of the webpage is displayed in the square.
4. The arrows represent the connections between the various html pages. 
5. Connections are made by:
    - clicking on buttons
    - clicking on text
    - typing in text in the 'search bar'
    - typing in the TITLE in the html link /wiki/TITLE

![alt text](/images/page_sketch.png "Workflow of website")

In line with the workflow, the following HTML files need to be created:
* Index / Home page
* Entry page(s) for all the different encyclopedia subjects
* Error page
* Edit page
* Search Result page
* Page to create a new page


## Adding a new page

A new page can be added by the following steps:
1. Clicking on *Create new page* in the sidebar
2. At the *Page to create a new page*, enter the title of the page and add markdown content
3. Hit the save button, whenever the entrys title does not yet exist (in `list_entries`) a new page is created (by `save_entry`)

Multiple other files and webpages should be updated whenever this procedure is finished.
- the new entry should be included in the list of entries
- thereby, the index page should be updated 
- consequently, also the data underlying the 'search' and 'random' actions should be adjusted

Question: what files should you change