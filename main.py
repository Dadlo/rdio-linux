#!/usr/bin/env python

import gtk
import webkit
import gobject


# init thread
gobject.threads_init()

window = gtk.Window()
window.set_title('Rdio for Linux')
window.maximize()

view = webkit.WebView()
browser = view.get_settings()
browser.set_property("enable-plugins", True)
browser.set_property("enable-private-browsing", True)
browser.set_property("enable-page-cache", True)
view.set_settings(browser)

view.open('https://www.rdio.com/signin/')

window.add(view)
window.show_all()
window.connect('delete-event', lambda window, event: gtk.main_quit())

gtk.main()
