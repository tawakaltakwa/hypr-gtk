#!/usr/bin/env python3
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
import os

class ShortcutPopup(Gtk.Window):
    def __init__(self):
        super().__init__(title="KEYBOARD SHORTCUTS")
        
        # Pengaturan Window
        self.set_border_width(20)
        self.set_default_size(500, 500)
        self.set_position(Gtk.WindowPosition.CENTER) # Muncul di tengah layar agar mudah dibaca
        self.set_name("window-utama")

        # Main Layout (Vertical Box)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
        vbox.set_halign(Gtk.Align.CENTER)
        self.add(vbox)

        # Judul Pop-up
        title_label = Gtk.Label(label="󰌌  KEYBOARD SHORTCUTS")
        title_label.set_name("judul")
        title_label.set_halign(Gtk.Align.CENTER)
        vbox.pack_start(title_label, False, False, 0)

        # Pembuatan Tabel menggunakan Gtk.Grid
        grid = Gtk.Grid()
        grid.set_name("shortcut-table")
        grid.set_row_spacing(8)
        grid.set_column_spacing(20)
        
        # Data Shortcut (Bisa kamu edit/tambah sesuai config Hyprland-mu)
        shortcuts = [
            # ("Kombinasi Tombol", "Deskripsi Fungsi")
            ("SUPER + Q", "Menutup Aplikasi"),
            ("SUPER + Return", "Terminal: kitty"),
            ("SUPER + E", "File Manager: Nautilus"),
            ("SUPER + B", "Browser: Firefox"),
            ("SUPER + Space", "Runner: Wofi"),
            ("SUPER + R", "Runner: wmenu"),
            ("SUPER + ESC", "System Monitor: gnome-system-monitor"),
            ("SUPER + A", "Antigravity (IDE)"),
            ("SUPER + Arah Panah", "Pindah fokus aplikasi sesuai arah panah"),
            ("SUPER + CTRL + Arah Panah", "Tukar posisi aplikasi yang berdekatan sesuai arah panah"),
            ("SUPER + CTRL + N", "Consume"),
            ("SUPER + CTRL + M", "Expel"),
            ("SUPER + SHIFT + F", "Fullscreen"),
            ("SUPER + F", "Preset Lebar (hanya di Scrolling Layout)"),
            ("SUPER + V", "Mengubah Mode Jendela (Floating/Tiling)"),
            ("SUPER + P", "Pseudo Mode (Dwindle Effect,hanya di Dwindle/Tiling)"),
            ("SUPER + J", "Membagi Layout Jendela (Togglesplit)"),
            ("SUPER + 1 - 9", "Pindah ke Workspace 1 - 9"),
            ("SUPER + Shift + 1 - 9", "Pindahkan Jendela ke Workspace 1 - 9"),
            ("SUPER + CTRL + 1", "Screenshot Screen"),
            ("SUPER + CTRL + 2", "Screenshot Area atau Window Aktif")
        ]

        # Membuat Header Tabel
        header_key = Gtk.Label(label="Kombinasi Tombol")
        header_key.set_name("table-header")
        header_key.set_halign(Gtk.Align.CENTER)
        grid.attach(header_key, 0, 0, 1, 1)

        header_desc = Gtk.Label(label="Aksi / Fungsi")
        header_desc.set_name("table-header")
        header_desc.set_halign(Gtk.Align.CENTER)
        grid.attach(header_desc, 1, 0, 1, 1)
        
        # Memasukkan Data ke Tabel dengan Efek Baris Belang-Belang (Zebra Striping)
        for index, (key, desc) in enumerate(shortcuts, start=1):
            lbl_key = Gtk.Label(label=key)
            lbl_key.set_halign(Gtk.Align.START)
            lbl_key.get_style_context().add_class("key-cell")
            
            lbl_desc = Gtk.Label(label=desc)
            lbl_desc.set_halign(Gtk.Align.START)
            lbl_desc.get_style_context().add_class("desc-cell")

            # Berikan class tambahan untuk baris genap agar bisa di-style berbeda (zebra effect)
            # if index % 2 == 0:
            #     lbl_key.get_style_context().add_class("row-even")
            #     lbl_desc.get_style_context().add_class("row-even")
            # else:
            #     lbl_key.get_style_context().add_class("row-odd")
            #     lbl_desc.get_style_context().add_class("row-odd")

            grid.attach(lbl_key, 0, index, 1, 1)
            grid.attach(lbl_desc, 1, index, 1, 1)

        # Memasukkan tabel ke dalam ScrolledWindow agar bisa di-scroll jika datanya banyak
        scroll_window = Gtk.ScrolledWindow()
        scroll_window.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scroll_window.add(grid)
        vbox.pack_start(scroll_window, True, True, 0)

        # Tombol Tutup di bagian bawah
        btn_close = Gtk.Button(label="Tutup")
        btn_close.set_name("tombol")
        btn_close.set_halign(Gtk.Align.CENTER)
        btn_close.connect("clicked", Gtk.main_quit)
        vbox.pack_start(btn_close, False, False, 0)

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

if __name__ == "__main__":
    win = ShortcutPopup()
    # Menutup pop-up jika menekan tombol ESC
    win.connect("key-press-event", lambda w, e: Gtk.main_quit() if e.keyval == Gdk.KEY_Escape else False)
    # Menutup jika klik di luar window (fokus hilang)
    # win.connect("focus-out-event", lambda w, e: Gtk.main_quit())
    Gtk.main()