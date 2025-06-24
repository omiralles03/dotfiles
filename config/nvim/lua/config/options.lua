-- SETTINGS --
vim.o.wrap = false
vim.o.cursorline = true
vim.o.cursorcolumn = false
vim.o.swapfile = true

vim.o.number = true
vim.o.relativenumber = true
vim.o.scrolloff = 10

vim.o.clipboard = "unnamedplus"
vim.o.termguicolors = true

vim.o.tabstop = 4
vim.o.shiftwidth = 4
vim.o.expandtab = true

local highlight_group = vim.api.nvim_create_augroup("YankHighlight", { clear = true })
vim.api.nvim_create_autocmd("TextYankPost", {
	callback = function()
		vim.highlight.on_yank()
	end,
	group = highlight_group,
	pattern = "*",
})
