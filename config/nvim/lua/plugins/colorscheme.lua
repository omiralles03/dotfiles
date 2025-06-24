return {

	-- Tokyonight
	{
		"folke/tokyonight.nvim",
		lazy = false,
		priority = 1000,
		config = function()
			-- vim.cmd.colorscheme("tokyonight")
		end,
	},

	-- Transparent Nvim
	{
		"xiyaowong/transparent.nvim",
		lazy = false,
		opts = {},
		config = function() end,
	},

	-- Catppuccin
	{
		"catppuccin/nvim",
		name = "catppuccin",
		priority = 1000,
		opts = {},
		config = function()
			-- vim.cmd.colorscheme("catppuccin")
		end,
	},

	-- Rose-pine
	{
		"rose-pine/neovim",
		name = "rose-pine",
		config = function()
			-- vim.cmd("colorscheme rose-pine")
		end,
	},

	-- Gruvbox
	{
		"sainnhe/gruvbox-material",
		lazy = false,
		priority = 1000,
		config = function()
			vim.g.gruvbox_material_background = "medium"
			vim.g.gruvbox_material_foreground = "material"
			vim.g.gruvbox_material_ui_contrast = "high"
			vim.g.gruvbox_material_transparent_background = 1
			vim.g.gruvbox_material_enable_italic = true
			vim.g.gruvbox_material_enable_bold = true
			vim.cmd.colorscheme("gruvbox-material")
		end,
	},
}
