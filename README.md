# Plannr


# How to populate the data

````
python manage.py shell
from seeder import seed_months
seed_months()
````

make sure you are in 'placeholder' directory.

# With a seeded and migrated database the website should be up with all the necesary resources

route to ``http://localhost:8000/month/july`` to see july month with dynamically updated amount of days and weeks.
can also route to ``http://localhost:8000/month/july/1`` to get a specific view of that day.


# Todo


* [0] fix today day being on every month
* [0] interaction, in some way shape or form
* [0] design the event creator page forms thing
* [0] design the specific day view
* [0] inbox view
* [0] landing page view
* [0] authenticate routes
* [x] make a database schema
* [x] url router
* [x] basic template for devving
* [x] basic admin page
* [x] realised django templates are trash asf
* [x] Event handler for the Event objects
* [x] Designing the Calendar views
* [x] making them reroute dynamically
* [x] Automatic routing to this the current month
* [0] converter from input data to Datetime objects(?)
* [x] clean up the admin page
* [0] make a landing page
* [x] login and user authentication
* [0] read / write authentication 