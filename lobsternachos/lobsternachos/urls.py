from django.conf.urls.defaults import *
from lobsternachos.controllers.home import *
from lobsternachos.controllers.items import *


urlpatterns = patterns('',

    # Default
    (r'^sign$', sign_post),
    (r'^$', main_page),

    # Items
    (r'^items/index$', index),

    # Accounts
    (r'^lock_screen.html$', lock_screen),
    (r'^login.html$', login),
    (r'^profile.html$', profile),
    (r'^register.html$', register),

    # Home
    (r'^contact.html$', contact),
    (r'^faq.html$', faq),
    (r'^index.html$', index),
    (r'^landing.html$', landing),
    (r'^search_result.html$', search_result),

    # Orders
    (r'^invoice.html$', invoice),

    # Temp
    (r'^blog.html$', blog),
    (r'^calendar.html$', calendar),
    (r'^chat.html$', chat),
    (r'^gallery.html$', gallery),
    (r'^inbox.html$', inbox),
    (r'^movie.html$', movie),
    (r'^pricing.html$', pricing),
    (r'^single_post.html$', single_post),
    (r'^timeline.html$', timeline),

    # Email
    (r'^email_selection.html$', email_selection),
    (r'^email_template_blue.html$', email_template_blue),
    (r'^email_template_dark.html$', email_template_dark),
    (r'^email_template_green.html$', email_template_green),
    (r'^email_template_orange.html$', email_template_orange),
    (r'^email_template_purple.html$', email_template_purple),
    (r'^email_template_red.html$', email_template_red),

    # Errors
    (r'^error404.html$', error404),
    (r'^error500.html$', error500),

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
