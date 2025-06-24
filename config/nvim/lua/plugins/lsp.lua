return {
	{
		"mason-org/mason-lspconfig.nvim",
		opts = {},
		dependencies = {
			{ "mason-org/mason.nvim", opts = {} },
			"neovim/nvim-lspconfig",
		},
	},

	{
		"neovim/nvim-lspconfig",
		dependencies = {
			{
				"saghen/blink.cmp",
				version = "1.*",
			},
			{
				"folke/lazydev.nvim",
				ft = "lua",
				opts = {
					library = {
						{ path = "${3rd}/luv/library", words = { "vim%.uv" } },
						"nvim-dap-ui",
					},
				},
			},
		},
		opts = {
			inlay_hints = {
				enabled = true,
				exclude = { "vue" },
			},
			codelens = {
				enabled = false,
			},
			capabilities = {
				workspace = {
					fileOperations = {
						didRename = true,
						willRename = true,
					},
				},
			},
			diagnostics = {
				underline = true,
				update_in_insert = false,
				virtual_text = {
					spacing = 4,
					source = "if_many",
					prefix = nil,
					virt_text_pos = "eol",
				},
				severity_sort = true,
				signs = {
					text = {
						[vim.diagnostic.severity.ERROR] = "",
						[vim.diagnostic.severity.WARN] = "",
						[vim.diagnostic.severity.HINT] = "",
						[vim.diagnostic.severity.INFO] = "",
					},
				},
			},
			servers = {
				lua_ls = {},
				vtsls = {},
				gopls = {},
				clangd = {},
				tailwindcss = {},
				html = {},
				cssls = {},
				jsonls = {},
				tinymist = {},
				intelephense = {},
				jdtls = {},
				csharp_ls = {},
			},
		},
		config = function(_, opts)
			local capabilities = vim.tbl_deep_extend(
				"force",
				{},
				vim.lsp.protocol.make_client_capabilities(),
				require("blink.cmp").get_lsp_capabilities() or {},
				opts.capabilities or {}
			)

			vim.diagnostic.config(vim.deepcopy(opts.diagnostics))

			local lspconfig = require("lspconfig")
			for server, config in pairs(opts.servers) do
				config.capabilities = capabilities
				lspconfig[server].setup(config)
			end
		end,
	},
}
