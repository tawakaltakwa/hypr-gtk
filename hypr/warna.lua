-- warna.lua
-- File ini mengatur warna Hyprland berdasarkan preset aktif.
-- Diganti otomatis oleh ganti-warna.sh

local warna = require("preset-warna.merah")

-- Expand 3-digit hex (#0ff) ke format rgba Hyprland (rgba(00ffffffee))
local function hex_to_rgba(hex, alpha)
    alpha = alpha or "ff"
    hex = hex:gsub("#", "")
    if #hex == 3 then
        hex = hex:sub(1,1):rep(2) .. hex:sub(2,2):rep(2) .. hex:sub(3,3):rep(2)
    end
    return "rgba(" .. hex .. alpha .. ")"
end

-- Terapkan warna ke border Hyprland
hl.config({
    general = {
        col = {
            active_border   = { colors = {hex_to_rgba(warna.warna1), hex_to_rgba(warna.warna2)}, angle = 45 },
            inactive_border = hex_to_rgba(warna.warna3, "aa"),
        },
    },
})

return warna
