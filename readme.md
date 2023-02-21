## Project 4 - Run App
By Alec Hannaford

------

# Overview
- A CRUD App for the user to track time and mileage for their runs.
- A data dashboard with analytics and data visualisation.
- Wireframe https://imgur.com/6vsO4iN
- Backend Repo: https://github.com/AlecCodes/Project4Backend


# Stack
|   Tech used    | Description |
| ----------- | ----------- |
| Database   | bit.io        |
| Backend      |   Django     |
| Frontend   | React        |
| Deployment   | Netlify        |

# API
Backend Routes
- Route 1: CRUD operations
- Route 2: Analytics & Aggregates

# Frontend

React app routes
- Create Page
- Edit Page
- Run Page (displays data for run category)
- Show Page (displays data for individual run)
- Home Page (displays analytics)

# User Stories and Possibile features
- I can categorize my different runs, and select one from a template.
- I can see the average time for each run.
- Runs are categorized by location and distance.
- I have 2 routers on by backend, one for standard CRUD operations for runs (sends runtimes in minutes, which may be converted into hrs/mins/secs in the fronted), and one that returns aggregates, averages, analyitics, etc... 