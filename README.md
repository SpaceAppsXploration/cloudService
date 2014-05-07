Chronos REST Service and Xploration Webapp
===============================

A REST-like service for serving data about mission planning at the front-end.
With a Demo WebApp for mission design simulation.

Back-end in `Django Python2.7`. this service is running on `Red Hat Openshift` at http://www.spacexplore.it

REST docs at http://www.spacexplore.it/api/docs

Code is not optimized, refactorying needed.
The webapp is just a demo, different apps for different clients are to be implemented.
Django Caching is in the project, but not implemented in the code yet.

`Service` back-end's code is in `wsgi/openshift/chronos`
The missions' simulator code is in `simulate.py`
The REST back-end and common views are in `views.py`

`Webapp's` views are in `wsgi/openshift/webapp/views.py`

License is `GNU GPL`. This is Free Software.

Thanks to `Django Framework`, `Django-REST Framework` and `Django-Swagger`.

Credits to `2014 SpaceApps Challenge Rome Chronos/Xploration team`
https://2014.spaceappschallenge.org/project/chronos/

---


