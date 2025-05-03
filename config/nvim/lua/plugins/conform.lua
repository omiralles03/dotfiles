-- lua/plugins/conform.lua
return {
  "stevearc/conform.nvim",
  opts = function(_, opts)
    -- Prettier config
    opts.formatters = opts.formatters or {}
    opts.formatters.prettier = {
      prepend_args = {
        "--single-quote",
        "--jsx-single-quote",
      },
      -- FORCE IT to always be available regardless
      condition = function()
        return true
      end,
    }

    -- Clang-Format for C/C++
    opts.formatters.clang_format = {
      -- Indent 4 spaces
      prepend_args = {
        "--style={BasedOnStyle: LLVM, IndentWidth: 4}",
      },
    }

    -- Filetype mappings for formatters
    opts.formatters_by_ft = opts.formatters_by_ft or {}

    -- Prettier for web and markup fyletypes
    for _, ft in ipairs({
      "javascript",
      "javascriptreact",
      "typescript",
      "typescriptreact",
      "css",
      "html",
      "json",
      "markdown",
    }) do
      opts.formatters_by_ft[ft] = { "prettier" }
    end

    -- C/C++ lang
    opts.formatters_by_ft.c = { "clang_format" }
    opts.formatters_by_ft.cpp = { "clang_format" }

    return opts
  end,
}
