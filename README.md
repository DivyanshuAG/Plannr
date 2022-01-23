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


* [ ] fix today day being on every month
* [ ] interaction, in some way shape or form
* [ ] design the event creator page forms thing
* [ ] design the specific day view
* [ ] inbox view
* [ ] landing page view
* [ ] authenticate routes
* [x] make a database schema
* [x] url router
* [x] basic template for devving
* [x] basic admin page
* [x] realised django templates are trash asf
* [x] Event handler for the Event objects
* [x] Designing the Calendar views
* [x] making them reroute dynamically
* [x] Automatic routing to this the current month
* [ ] converter from input data to Datetime objects(?)
* [x] clean up the admin page
* [ ] make a landing page
* [x] login and user authentication
* [ ] read / write authentication 