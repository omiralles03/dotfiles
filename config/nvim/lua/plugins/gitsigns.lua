local symbols = {
	add = { text = "+" },
	change = { text = "~" },
	delete = { text = "-" },
	topdelete = { text = "^" },
	changedelete = { text = "~" },
	untracked = { text = "#" },
}

return {
	"lewis6991/gitsigns.nvim",
	lazy = false,
	enabled = true,
	opts = {
		signs = symbols,
		signs_staged = symbols,
		current_line_blame = true,
	},
}
