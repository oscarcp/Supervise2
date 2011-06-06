Supervise 2.0
=============

Supervise 2 is a remake of "Supervise" a project management tool made on top of the django framework. Due to the new django releases and the early stage of the old project, it has been rewritten.

Install
=======

Currently Supervise 2 is not stable. The instructions here are for a testing installation.

**Get the source code from a repository** (Gitorious and GitHub are available)
    git clone git://gitorious.org/supervise2/mainline.git
    git clone git://github.com/oscarcp/Supervise2.git

**Collect all the static files**
    python manage.py collectstatic
    
**Create a new database**
    python manage.py syncdb

**Start the development server**
    python manage.py runserver
