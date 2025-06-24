return {
	"olimorris/persisted.nvim",
	lazy = false,
	event = "BufReadPre",
	opts = {
		autoload = true,
		allowed_dirs = {
			"~/Desktop/Projects",
			"~/.config",
		},
	},
}
