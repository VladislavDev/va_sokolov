# va_sokolov

This is my personal Django website, which will combine a portfolio, contacts, news feed. 
I'm learning Django and I think it would be a good project to start. It is currently under development, but I have a few ideas for filling it:

+ On the main page I will post a brief information about myself and contacts. Below will be a news feed
+ The portfolio section will allow you to view a list of my projects (and the skills involved in them). A detailed description will be available for each project
+ In the "Employers" section, vacancies that interest me and my competencies in them will be available
+ There will be an automatic resume generation button for each vacancy
+ The site will be multilingual. Initially, there will be Russian and English languages. Perhaps I will make translations for German, French and Yiddish
+ Not only the content will be translated, but also the models (using [modeltranslation](https://github.com/deschler/django-modeltranslation))

## Current status of the project

Apps for projects and skills have now been created. They contain model data, a ListView template has been created for projects.

## Road map

+ 03/20/2023 - 03/24/2023 The main page will be created. At the moment, only basic information will be posted on it.
+ 03/21/2023 - 03/27/2023 A news feed with a slider of attached images will be added. A translation (en, ru) will be added.
+ 03/25/2023 - 04/10/2023 A special model for contacts has been created. Special components will allow you to display the 
necessary information about me from profile sites.
