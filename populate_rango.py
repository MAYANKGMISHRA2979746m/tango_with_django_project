import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')
django.setup()

from rango.models import Category, Page


def populate():
    python_pages = [
        {'title': 'Official Python Tutorial', 'url': 'https://docs.python.org/3/tutorial/', 'views': 128},
        {'title': 'Learn Python', 'url': 'https://www.learnpython.org/', 'views': 64},
        {'title': 'Real Python', 'url': 'https://realpython.com/', 'views': 32},
    ]

    django_pages = [
        {'title': 'Official Django Tutorial', 'url': 'https://docs.djangoproject.com/en/2.2/intro/tutorial01/', 'views': 128},
        {'title': 'Django Rocks', 'url': 'https://www.djangorocks.com/', 'views': 64},
        {'title': 'How to Tango with Django', 'url': 'http://www.tangowithdjango.com/', 'views': 32},
    ]

    other_pages = [
        {'title': 'BBC', 'url': 'http://www.bbc.co.uk/', 'views': 128},
        {'title': 'Google', 'url': 'http://www.google.com/', 'views': 64},
        {'title': 'Wikipedia', 'url': 'http://www.wikipedia.org/', 'views': 32},
    ]

    cats = {
        'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
        'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
        'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16},
    }

    for cat_name, cat_data in cats.items():
        c = add_cat(cat_name, views=cat_data['views'], likes=cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], views=p['views'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f"- {c} ({c.views} views, {c.likes} likes): {p} ({p.views} views)")


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
