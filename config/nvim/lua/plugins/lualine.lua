return {
	"nvim-lualine/lualine.nvim",
	dependencies = { "nvim-tree/nvim-web-devicons" },
	opts = {
		options = {
			theme = "auto",
			component_separators = { left = "", right = "" },
			section_separators = { left = "", right = "" },
			globalstatus = true,
		},
		sections = {
			lualine_a = {
				{ "mode" },
			},
			lualine_b = {
				{ "branch" },
			},
			lualine_c = {
				{ "diff" },
				{ "diagnostics" },
				{ "filename" },
			},
			lualine_x = {
				{
					"lsp_status",
					symbols = {
						done = "",
					},
				},
			},
			lualine_y = {
				{ "progress" },
			},
			lualine_z = {
				{ "location" },
			},
		},
	},
}
