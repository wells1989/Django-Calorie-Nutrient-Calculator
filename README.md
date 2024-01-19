# MacroNutrient / Calorie Calculator

The Macronutrient / calorie counter is a django based calculator which takes what you've eaten in a day, and gives you information about calory intake as a percentage of daily allowances. It also gives you a visual breakdown of the nutrients (carb / fat / protein percentages) via JSChart.

## Tech Stack
- __HTML and Bootstrap 5.3.1__: HTML templating and UI styling
- __Javascript and JSChart__: Dynamic UI rendering
- __Python / django / SQLite3__: Back-end logic and database integration

## Installation

Requirements.txt

```python
asgiref==3.7.2
black==23.12.1
click==8.1.7
colorama==0.4.6
Django==5.0.1
mypy-extensions==1.0.0
packaging==23.2
pathspec==0.12.1
platformdirs==4.1.0
sqlparse==0.4.4
tzdata==2023.4
```

## UI

The UI allows user operations such as:
- Searching for a food to add out of the Food model.
- Adding or removing said food to your daily intake.
- Viewing your total calories / nutrients in a table or chart format, in addition to viewing your calories as a percentage of the daily recommended allowance.

![Screenshot (513)](https://github.com/wells1989/Django-Calorie-Nutrient-Calculator-mini-project/assets/122035759/0b5a5fe7-c8ee-4a54-a4d2-d541d0a6c110)


## Project Notes / areas for future improvement
- The project focus areas were on creating a good amount of functionality in a basic UI view, rather than creating multiple views for each website function, in addition to using JS / JSChart with Django templates for more dynamic content.
- Ideas for Future Improvement:
1. The Food model was hardcoded for simplicity, but an API (for instance https://api-ninjas.com/api/nutrition could be used to provide more in-depth information.)
2. The site could have been more personalised to the user, for instance by allowing users to create an account which would give them personalised calorie / nutrient goals depending on factors such as weight and personal goals etc. 
3. Using the above suggestion, the app could incorporate a social feel to it, for example by allowing users to get success points by hitting their daily targets, and by inviting other users to become part of their 'friends' could see how their friends were doing etc.

