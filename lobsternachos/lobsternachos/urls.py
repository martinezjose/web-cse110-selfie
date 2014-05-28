from django.conf.urls.defaults import *

# Home
urlpatterns = patterns('lobsternachos.controllers.home',

    # Dashboard
    (r'^$', 'index'),

    # Accounts
    (r'^lock_screen.html$', 'lock_screen'),
    (r'^profile.html$', 'profile'),

    # Home
    (r'^contact.html$', 'contact'),
    (r'^faq.html$', 'faq'),
    (r'^landing.html$', 'landing'),
    (r'^search_result.html$', 'search_result'),

    # Orders
    (r'^invoice.html$', 'invoice'),

    # UI Elements
    (r'^form_element.html$', 'form_element'),
    (r'^form_wizard.html$', 'form_wizard'),
    (r'^nestable_list.html$', 'nestable_list'),
    (r'^tab.html$', 'tab'),
    (r'^table.html$', 'table'),
    (r'^ui_element.html$', 'ui_element'),
    (r'^widget.html$', 'widget'),
    (r'^button.html$','button'),

    # Blank
    (r'^blank.html$', 'blank'),
)


# Menu
urlpatterns += patterns('lobsternachos.controllers.menu',
    url(r'^menu$','index',name='menuIndex'),
    (r'^menu/new$', 'new'),
)

# Accounts
urlpatterns += patterns('lobsternachos.controllers.accounts',
  (r'^accounts/login$', 'login'),
)

# Categories
urlpatterns += patterns('lobsternachos.controllers.categories',
  (r'^categories/create$', 'create'),
  (r'^categories/delete$', 'delete'),
  (r'^categories/update$', 'update'),

)

# Web API
urlpatterns += patterns('lobsternachos.controllers.webapi.categories',
    (r'^webapi/categories$','get_all'),
)
urlpatterns += patterns('lobsternachos.controllers.webapi.items',
    (r'^webapi/items$','index'),
)
urlpatterns += patterns('lobsternachos.controllers.webapi.recommendations',
    (r'^webapi/recommendations$','index'),
)
urlpatterns += patterns('lobsternachos.controllers.webapi.orders',
    (r'^webapi/orders$','index'),
)
urlpatterns += patterns('lobsternachos.controllers.webapi.pings',
    (r'^webapi/pings$','index'),
)
urlpatterns += patterns('lobsternachos.controllers.webapi.tables',
    (r'^webapi/tables$','index'),
)
