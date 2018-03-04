# window.py
#
# Copyright (C) 2018 somas95
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk
from .gi_composites import GtkTemplate


@GtkTemplate(ui='/org/gnome/Contador/window.ui')
class ContadorWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'ContadorWindow'

    counter_label, \
    title_stack, \
    title_entry, \
    title_label = GtkTemplate.Child.widgets(4)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.init_template()


    def count_value(self):
        count = int(self.counter_label.get_text())
        count += 1
        return count

    @GtkTemplate.Callback
    def on_key_press_event(self, window, event):
        if event.keyval == 32:
            value = self.count_value()
        if event.keyval == 114:
            value = 0
        self.counter_label.set_text(str(value))

    @GtkTemplate.Callback
    def on_title_label_focus(self, widget, event):
        self.title_stack.set_visible_child(self.title_entry)
        self.title_entry.grab_focus()

    @GtkTemplate.Callback
    def on_title_entry_focus_out(self, widget):
        print("tada")
        text = self.title_entry.get_text()
        self.title_label.set_text(text)
        self.title_stack.set_visible_child(self.title_label)
