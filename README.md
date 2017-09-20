

## Minikep Django Rest API project

#### Install project
	git clone <repo>
	cd minikep/
	pip install -r requirements.txt

#### Run the project:
	python manage.py runserver

#### Login:
    http://localhost:8000/api-auth/login/?next=/
    user: admin
    pass: asdasdasd

#### Datapoint page:
    http://localhost:8000/datapoints/

#### Tests:
    You can look to minikep/api/tests to check hoe CRUD work for Datapoint

#### About project:
    It's a simple Django Rest Api project with one model minikep.api.models.Datapoint. It has appropriate serializer
    minikep.api.serializers.DatapointSerializer that perform datato API and minikep.api.views.DatapointViewSet
    that create CRUD for model.
    Minikep.minikep is global Django settings for whole project.

#### Database
    Now project works with sqlite so you can easy install it and look how it works.


