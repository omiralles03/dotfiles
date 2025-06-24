return {
	"ThePrimeagen/harpoon",
	branch = "harpoon2",
	dependencies = { "nvim-lua/plenary.nvim" },
	keys = {
		{
			"<leader>M",
			function()
				local harpoon = require("harpoon")
				harpoon.ui:toggle_quick_menu(harpoon:list())
			end,
			desc = "Harpoon [M]arks",
		},
		{
			"<leader>m",
			function()
				require("harpoon"):list():add()
			end,
			desc = "Harpoon [m]ark file",
		},
		{
			"<A-1>",
			function()
				require("harpoon"):list():select(1)
			end,
			desc = "Harpoon mark 1",
		},
		{
			"<A-2>",
			function()
				require("harpoon"):list():select(2)
			end,
			desc = "Harpoon mark 2",
		},
		{
			"<A-3>",
			function()
				require("harpoon"):list():select(3)
			end,
			desc = "Harpoon mark 3",
		},
		{
			"<A-4>",
			function()
				require("harpoon"):list():select(4)
			end,
			desc = "Harpoon mark 4",
		},
	},
	opts = {
		settings = {
			save_on_toggle = true,
			save_on_change = true,
		},
	},
}
