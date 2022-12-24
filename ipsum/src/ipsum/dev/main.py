import typer

from ipsum.dev.manage_models import build_model, build_models_all
from ipsum.dev.model_diagnostics import (
    model_diagnostics,
    model_diagnostics_all,
)
from ipsum.dev.most_common import most_common_characters, most_common_words
from ipsum.dev.parser_diagnostics import (
    parser_diagnostics,
    parser_diagnostics_all,
)


app = typer.Typer(add_completion=False, no_args_is_help=True)
app.command()(most_common_characters)
app.command()(most_common_words)
app.command()(parser_diagnostics_all)
app.command()(parser_diagnostics)
app.command()(build_model)
app.command()(build_models_all)
app.command()(model_diagnostics_all)
app.command()(model_diagnostics)


if __name__ == "__main__":
    app()
