-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here
return {
  {
    "neovim/nvim-lspconfig",
    opts = function(_, opts)
      local keys = require("lazyvim.plugins.lsp.keymaps").get()
      for i, key in ipairs(keys) do
        if key[1] == "gd" then
          keys[i] = {
            "gd",
            "<cmd>lua require('telescope.builtin').lsp_definitions()<CR>",
            desc = "Telescope LSP Definitions",
          }
        end
      end
    end,
  },
}
