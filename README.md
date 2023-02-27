# uav-rental-project


### Project Screenshoots
- Link Below;
  - https://github.com/volkannaktass/uav-rental-project/blob/main/project-screenshoots/home_page.png
  - https://github.com/volkannaktass/uav-rental-project/blob/main/project-screenshoots/login_page.png
  - https://github.com/volkannaktass/uav-rental-project/blob/main/project-screenshoots/logout_page.png
  - https://github.com/volkannaktass/uav-rental-project/blob/main/project-screenshoots/register_page.png
  - https://github.com/volkannaktass/uav-rental-project/blob/main/project-screenshoots/reset_pass.png
  - https://github.com/volkannaktass/uav-rental-project/blob/main/project-screenshoots/reset_pass_message.png
  - https://github.com/volkannaktass/uav-rental-project/blob/main/project-screenshoots/search_and_filter_uav_listing.png
  - https://github.com/volkannaktass/uav-rental-project/blob/main/project-screenshoots/uav_listing.png
  - https://github.com/volkannaktass/uav-rental-project/blob/main/project-screenshoots/uav_register.png
  - https://github.com/volkannaktass/uav-rental-project/blob/main/project-screenshoots/uav_register_edit_control_panel.png
  - https://github.com/volkannaktass/uav-rental-project/blob/main/project-screenshoots/uav_registered_successfuly.png
  - https://github.com/volkannaktass/uav-rental-project/blob/main/project-screenshoots/uav_update.png
  - https://github.com/volkannaktass/uav-rental-project/blob/main/project-screenshoots/unit_test_successfully.png

###  Development Setup

- install Docker and Docker-compose 

Follow the instructions from the link below;
	-https://docs.docker.com/engine/install/
	-https://docs.docker.com/compose/



First run docker-compose in detach mode by executing this command then;
```
docker-compose up -d
```

- run this command to create migrations
```
docker-compose exec web python manage.py makemigrations
```

- migrate the database
```
docker-compose exec web python manage.py migrate
```

Go to http://0.0.0.0:8000/

To stop all services:

```
docker-compose down
```
