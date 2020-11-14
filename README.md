# Django Rest Framework learning journal

[Django Rest Framework home page](https://www.django-rest-framework.org/)

This document is about my advancement on the Django Rest Framework tutorial.
This is mostly copy/pasted code, and commented sections when the tutorial improves the current code.
(The tutorial follows an iterative construction of the code, by reducing all boilerplate step by step)

## Consistency problem in project organization between Quickstart and Tutorial

When wanting to go from the Quickstart to the first Tutorial page, I had some issues (which made me lose time) with the django project structure.
- The Quickstart put its `quickstart` app nested inside the "main app" folder ;
- The Tutorial 1. Serialization put its `snippets` app inside the project folder.

After consulting StackOverflow (really?), I came upon this discussion:
https://stackoverflow.com/questions/56161475/django-rest-framework-quickstart-tutorial-error-the-included-urlconf-tutorial-u

I finally decided to stick to the tutorial way of doing things, and moved the `quickstart` up in the folder structure, to put it alongside its sibling `snippets`. The Quickstart pages states that there is some advantage to follow its way of doing things, but since I will pass probably more time in the actual Tutorial, I prefer to stick to the Tutorial methodology.

Changes to be made on the `quickstart` app:
- replace all `tutorial.quickstart.*` imports by `quickstart.*`
- register `'quickstart.apps.QuickstartConfig',`