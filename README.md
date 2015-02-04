# Plog - on a quest to seek the holy grail

A minimalist blog app running with [Djangae](https://github.com/potatolondon/djangae), based on the [Djangae-Scaffold Project](https://github.com/potatolondon/djangae-scaffold).

To get started:

 - Clone this repo (don't forget to change the origin to your own repo!)
 - Run `./install_deps` (this will pip install requirements, and download the App Engine SDK)
 - `python manage.py checksecure --settings=scaffold.settings_live`
 - `python manage.py runserver`
 - Visit `http://127.0.0.1:8000/blog`

You can log into the admin interface (just check yourself as administrator) and start writing articles

## Caution

This app is really basic and minimalist and is not intended to be actually used. It was mostly an occasion for me to experience the Django framework, thus the application has some serious security issues. I would recommend you to start over with your own blog based on [Djangae-Scaffold](https://github.com/potatolondon/djangae-scaffold), you'll find it quite easy to learn and interesting to code :)