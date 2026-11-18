"""Results overview: the static page published to GitHub Pages.

Rules for any notebook that gets exported (the site is PUBLIC); see AGENTS.md:
  * Read only aggregate files from results/ -- never data/ or artifacts/.
  * Never display raw chat text, not even a "sample message".
  * Code is stripped from the export (--no-include-code). Opt a cell in with
    mo.show_code(...) only when it strengthens a point or informs the reader.
"""

import marimo

app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(
        """
        # Catching grooming early, and what it costs kids' privacy

        Roblox Sentinel vs. Liquid AI d1-omni-600M (and a cascade of the two) on PAN-2012.
        The datasets can't be redistributed, so this page shows **aggregate results only**.
        """
    )
    return


@app.cell
def _():
    from pathlib import Path

    # results/ sits next to notebooks/; resolve from this file so cwd doesn't matter.
    results_dir = Path(__file__).resolve().parents[1] / "results"
    result_files = sorted(results_dir.glob("*.csv"))
    return (result_files,)


@app.cell
def _(mo, result_files):
    if not result_files:
        status = mo.callout(
            mo.md("No aggregate results committed yet. Experiments will appear here."),
            kind="info",
        )
    else:
        status = mo.md("**Result files:** " + ", ".join(f"`{p.name}`" for p in result_files))
    status
    return


if __name__ == "__main__":
    app.run()
