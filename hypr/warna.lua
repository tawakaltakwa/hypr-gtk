-- warna.lua
-- File ini mengatur warna Hyprland berdasarkan preset aktif.
-- Diganti otomatis oleh ganti-warna.sh

local warna = require("preset-warna.ungu")

-- Terapkan warna ke border Hyprland
hl.config({
    general = {
        col = {
            active_border   = { colors = {warna.warna1, warna.warna2}, angle = 45 },
            inactive_border = warna.abu
        },
    },
})

return warna
