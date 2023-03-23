# va_sokolov

This is my personal Django website, which will combine a portfolio, contacts, news feed. I'm learning Django and I think it would be a good project to start. It is currently under development, but I have a few ideas for filling it:

+ On the main page I will post a brief information about myself and contacts. Below will be a news feed
+ The portfolio section will allow you to view a list of my projects (and the skills involved in them). A detailed description will be available for each project
+ In the "Employers" section, vacancies that interest me and my competencies in them will be available
+ There will be an automatic resume generation button for each vacancy
+ The site will be multilingual. Initially, there will be Russian and English languages. Perhaps I will make translations for German, French and Yiddish
+ Not only the content will be translated, but also the models (using [modeltranslation](https://github.com/deschler/django-modeltranslation))

## Current status of the project

The homepage and the projects page have now been created. The home page displays some information about me and a stackoverflow widget. In the projects section, a ListView of projects has been created with a preview, name and skills used.

Since the widget uses the stackexchange API, and the number of daily requests is limited, a request registry has been created that stores the data of requests and responses to them. In the future, this registry will allow you to collect statistics and manage problems with obtaining external data.

## Road map

| Start of work | Deadline     | Status                     | Detail                                                                                           |
|:--------------|:-------------|:---------------------------|:-------------------------------------------------------------------------------------------------|
| `03/20/2023`  | `03/24/2023` | :heavy_check_mark: `Done`  | The main page will be created. At the moment, only basic information will be posted on it        |
| `03/21/2023`  | `03/27/2023` | :clock1: `In work`         | A news feed with a slider of attached images will be added. A translation (en, ru) will be added |
| `03/25/2023`  | `04/10/2023` | :clock930: `Waiting start` | A special model for contacts has been created. Special components will allow you to display the necessary information about me from profile sites |
| `03/25/2023`  | `03/31/2023` | :clock930: `Waiting start` | Additional widgets will be created for GitHub and Habr Career                                    |

## Ideas

+ I'm thinking about what functionality I can create in a project for Django Rest Framework
+ Using [django-components](https://github.com/EmilStenstrom/django-components) was a good solution
+ It is required to make a good tabular display of the ApiRegistator model in the Admin panel.
