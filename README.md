![status](https://github.com/recourcefulcoder/NodeStory/actions/workflows/cd.yml/badge.svg)

# NodeStory

This app is an online web-site for communal storywriting.

The main idea is to build an app where each story can from each place be 
continued by community writers, thus creating variable developments for the 
main plot. Each part of the story (e.i. "node") is graded by users, providing 
an opportunity for the best narration to pop up on the top of each story. 

### Fixtures

There are two fixture files - _fixture.json_ (main, updated if neccessary, 
old data may be changed/deleted if needed) and _test_fixture.json_, which is
used in testing and which data must not be deleted/changed as it can affect 
tests' work

download fixture data by using
```bash
cd nodestory
python maange.py loaddata fixtures/fixture.json
```

in root directory of the project

##### Default fixture users
* admin, password: "admin" - superuser
* farnaKK, password: "Hemaphoho54" - casual user
* farMak, password: "Giggily15!" - casual user

These users are guaranteed for both fixture.json and test_fixture.json

### Models documentation
#### Model "StoryNode"
Each instance of the model MUST be created within the program using create() 
method of manager, because crucial database changes, related to addition of new
StoryNode are executed within this method (adding records to ClosureTable table);
will be edited in following versions 

Children of one StoryNode may be accessed via 
[RelatedManager](https://docs.djangoproject.com/en/5.1/topics/db/queries/#following-relationships-backward) 
called "children", so syntax is basically following: FOO.children.all() 
(where FOO is name of specific StoryNode instance).

### Database documentation
![ER diagram](ER.jpg "ER diagram")
Sotries are stored in database as trees, the structure used for storage - ClosureTable.

Practically there are two tables:
* StoryNode, which keeps the "nodes", or parts of the story
* ClosureTable, which is used for storage of relations between nodes.

Recordings to ClosureTable are added automatically via calling "create" method of NodeStory Manager

Heads (and only heads!) of story trees have relation to themselves in ClosureTable
(i.e. record looking like "ancestor_id: 1", "descendant_id: 1")

This structure allows efficient access to all the descendants of 
particular node, as well as to all parents/any child, which is crucial for efficient
Depth-first search (DRF) of the tree.

* StoryHead table - label for stories, attached to "tree roots" and keeps 
* general story info - title, tags etc. 

### Docs
Service logic is splitted to three apps: 
+ [**users**](#users) (for handling account changes/auth, etc.), 
+ [**homepage**](#homepage) (for main page endpoints, not related to functionality direcly) 
+ [**stories**](#stories) (for main functionality as story creation/searching/etc.)


##### users
Besides basic auth endpoints (auth, signup, change password, etc.) these are added:
+ settings/ - allows seeing and changing account info + contains 
  + stories/ page - shows user's stories (in development now)  

##### homepage
Has only one endpoint - main page, which is associated with endpoint "/"

##### stories
Allows edition and view of  specific story based on it's id, creation of new story.