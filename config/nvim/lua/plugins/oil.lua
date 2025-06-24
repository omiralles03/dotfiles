return {
	"stevearc/oil.nvim",
	dependencies = { "nvim-tree/nvim-web-devicons" },
	lazy = false,
	keys = {
		{
			"<leader>ee",
			"<cmd>Oil<CR>",
			desc = "[e]explorer [e]explorer",
		},
		-- TODO: Foking ENTER TO SAVE LMAOi
	},
	opts = {
		default_file_explorer = true,
		columns = {
			"icon",
		},
		delete_to_trash = true,
		keymaps = {
			["<CR>"] = "actions.select",
			["g."] = { "actions.toggle_hidden", mode = "n" },
		},
		use_default_keymaps = true,
		view_options = {
			show_hidden = true,
			is_hidden_file = function(name, _)
				local m = name:match("^%.")
				return m ~= nil
			end,
			natural_order = "fast",
			case_insensitive = false,
			sort = {
				{ "type", "asc" },
				{ "name", "asc" },
			},
		},
	},
}
