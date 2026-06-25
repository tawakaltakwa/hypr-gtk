#!/usr/bin/env python3
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
import os
import subprocess

class ListConfig(Gtk.Window):
    def __init__(self):
        super().__init__(title="Aplikasi Favorit")
        
        # Pengaturan Window
        self.set_border_width(20)
        self.set_name("window-utama")

        # Main Layout (Vertical Box)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
        vbox.set_halign(Gtk.Align.FILL)
        vbox.set_valign(Gtk.Align.CENTER)
        self.add(vbox)

        # Judul Pop-up
        title_label = Gtk.Label(label="DAFTAR APLIKASI/DISEKTORI YANG SERING DIBUKA")
        title_label.set_name("judul")
        title_label.set_halign(Gtk.Align.CENTER)
        vbox.pack_start(title_label, False, False, 0)

        # Grid untuk Tabel
        grid = Gtk.Grid()
        grid.set_column_spacing(25)
        grid.set_row_spacing(12)
        grid.set_halign(Gtk.Align.CENTER)
        vbox.pack_start(grid, True, True, 0)

        # Header Tabel
        headers = ["Nama", "Path/Deskripsi", "Aksi"]
        for col_idx, text in enumerate(headers):
            lbl = Gtk.Label(label=text)
            lbl.set_name("table-header")
            if col_idx < 2:
                lbl.set_halign(Gtk.Align.START)
            else:
                lbl.set_halign(Gtk.Align.CENTER)
            grid.attach(lbl, col_idx, 0, 1, 1)

        # Data Baris: (Nama, Path/Deskripsi, Action Type, Action Target, Label Tombol)
        rows_data = [
            ("MEGA", "mega cloud data", "cmd", "megasync", "Run"),
            ("Brisk", "Brisk download manager", "cmd", "brisk", "Run"),
            ("Warung", "~/SagalaAya/data/MEGA/Warung", "path", "~/SagalaAya/data/MEGA/Warung", "Buka Direktori"),
        ]

        for row_idx, (name, display_val, action_type, action_target, btn_label) in enumerate(rows_data, start=1):
            # Kolom 1: Nama
            name_lbl = Gtk.Label(label=name)
            name_lbl.get_style_context().add_class("key-cell")
            name_lbl.set_halign(Gtk.Align.START)
            grid.attach(name_lbl, 0, row_idx, 1, 1)

            # Kolom 2: Path/Deskripsi
            path_lbl = Gtk.Label(label=display_val)
            path_lbl.get_style_context().add_class("desc-cell")
            path_lbl.set_halign(Gtk.Align.START)
            grid.attach(path_lbl, 1, row_idx, 1, 1)

            # Kolom 3: Tombol Aksi
            btn = Gtk.Button(label=btn_label)
            btn.set_name("tombol")
            btn.connect("clicked", self.on_buka_clicked, action_type, action_target)
            grid.attach(btn, 2, row_idx, 1, 1)

        # Tombol Tutup di bawah
        btn_tutup = Gtk.Button(label="Tutup")
        btn_tutup.set_name("tombol")
        btn_tutup.connect("clicked", Gtk.main_quit)
        btn_tutup.set_halign(Gtk.Align.CENTER)
        vbox.pack_start(btn_tutup, False, False, 5)

        # Load Styling CSS
        self.load_css()
        self.show_all()

    def load_css(self):
        css_provider = Gtk.CssProvider()
        # Mendapatkan path file CSS
        script_dir = os.path.dirname(os.path.abspath(__file__))
        local_css = os.path.join(script_dir, "popup-style.css")
        home_css = os.path.expanduser("~/.config/hypr/waybar/popup-style.css")

        css_file = local_css if os.path.exists(local_css) else home_css
        if os.path.exists(css_file):
            css_provider.load_from_path(css_file)
            Gtk.StyleContext.add_provider_for_screen(
                Gdk.Screen.get_default(),
                css_provider,
                Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
            )

    def on_buka_clicked(self, widget, action_type, action_target):
        if action_type == "path":
            expanded_path = os.path.expanduser(action_target)
            try:
                subprocess.Popen(["nautilus", expanded_path])
            except Exception as e:
                print(f"Gagal membuka path dengan nautilus: {e}")
        elif action_type == "cmd":
            try:
                subprocess.Popen(action_target, shell=True)
            except Exception as e:
                print(f"Gagal menjalankan perintah: {e}")
        # Gtk.main_quit()

if __name__ == "__main__":
    win = ListConfig()
    win.connect("destroy", Gtk.main_quit)
    Gtk.main()
