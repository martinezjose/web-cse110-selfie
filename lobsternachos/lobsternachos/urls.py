from django.conf.urls.defaults import *
from lobsternachos.controllers.home import *
import lobsternachos.controllers.menu  as menu
import lobsternachos.controllers.categories as categories
import lobsternachos.controllers.accounts as accounts


urlpatterns = patterns('',
    # Dashboard
    (r'^$', index),

    # Menu
    (r'^menu$', menu.index),
    (r'^menu/new$', menu.new),

    # Categories
    (r'^categories/create$', categories.create),

    # Accounts
    (r'^lock_screen.html$', lock_screen),
    (r'^accounts/login$', accounts.login),
    (r'^profile.html$', profile),

    # Home
    (r'^contact.html$', contact),
    (r'^faq.html$', faq),
    (r'^index.html$', index),
    (r'^landing.html$', landing),
    (r'^search_result.html$', search_result),

    # Orders
    (r'^invoice.html$', invoice),

    # UI Elements
    (r'^form_element.html$', form_element),
    (r'^form_wizard.html$', form_wizard),
    (r'^nestable_list.html$', nestable_list),
    (r'^tab.html$', tab),
    (r'^table.html$', table),
    (r'^ui_element.html$', ui_element),
    (r'^widget.html$', widget),
    (r'^button.html$', button),

    # Blank
    (r'^blank.html$', blank),
)
