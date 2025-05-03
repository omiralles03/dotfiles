-- ~/.config/nvim/lua/plugins/colorscheme.lua
return {
  {
    "olimorris/onedarkpro.nvim",
    lazy = false, -- load immediately
    priority = 1000, -- load before LazyVim’s defaults
    opts = {
      dark_theme = "onedark", -- choose one of: onedark, onelight, onedark_vivid, onedark_dark, vaporwave
      light_theme = "onelight",

      styles = {
        comments = "italic",
        keywords = "bold",
        functions = "NONE",
        variables = "NONE",
      },

      options = {
        transparency = true,
        cursorline = true,
        terminal_colors = true,
      },
    },
    config = function(_, opts)
      require("onedarkpro").setup(opts)
      vim.cmd("colorscheme onedark")
    end,
  },

  -- 2) Tell LazyVim to use colorscheme by default
  {
    "LazyVim/LazyVim",
    opts = {
      colorscheme = "onedark",
    },
  },
}
