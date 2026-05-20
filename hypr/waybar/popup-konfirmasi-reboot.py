#!/usr/bin/env python3
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
import os

class KonfirmasiReboot(Gtk.Window):
    def __init__(self):
        super().__init__(title="Konfirmasi Reboot")
        
        # Pengaturan Window
        self.set_border_width(20)
        # self.set_default_size(400, 100)
        # self.set_position(Gtk.WindowPosition.CENTER)
        self.set_name("window-utama")

        # Main Layout (Vertical Box)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
        vbox.set_halign(Gtk.Align.CENTER)
        vbox.set_valign(Gtk.Align.CENTER)
        self.add(vbox)

        # Judul Pop-up
        title_label = Gtk.Label(label="KONFIRMASI")
        title_label.set_name("judul")
        title_label.set_halign(Gtk.Align.CENTER)
        vbox.pack_start(title_label, False, False, 0)

        # Judul Pop-up
        title_label = Gtk.Label(label="Apakah Anda yakin ingin me-reboot system?")
        title_label.set_name("cumateks")
        title_label.set_halign(Gtk.Align.CENTER)
        vbox.pack_start(title_label, False, False, 0)

        # Tombol "Ya" dan "Tidak"
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox.set_halign(Gtk.Align.CENTER)
        vbox.pack_start(hbox, False, False, 0)

        btn_ya = Gtk.Button(label="Ya")
        btn_ya.set_name("tombol")
        btn_ya.connect("clicked", self.on_ya_clicked)
        hbox.pack_start(btn_ya, True, True, 0)

        btn_tidak = Gtk.Button(label="Tidak")
        btn_tidak.set_name("tombol")
        btn_tidak.connect("clicked", Gtk.main_quit)
        hbox.pack_start(btn_tidak, True, True, 0)

        # Load Styling CSS
        self.load_css()
        self.show_all()

    def load_css(self):
        css_provider = Gtk.CssProvider()
        css_file = os.path.expanduser("~/.config/hypr/waybar/popup-style.css")
        if os.path.exists(css_file):
            css_provider.load_from_path(css_file)
            Gtk.StyleContext.add_provider_for_screen(
                Gdk.Screen.get_default(),
                css_provider,
                Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
            )

    def on_ya_clicked(self, widget):
        # Melakukan reboot system
        os.system("systemctl reboot")
        Gtk.main_quit()

if __name__ == "__main__":
    win = KonfirmasiReboot()
    Gtk.main()