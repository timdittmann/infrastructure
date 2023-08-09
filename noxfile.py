import nox

nox.options.reuse_existing_virtualenvs = True

BUILD_COMMAND = ["-b", "dirhtml", "docs", "docs/_build/dirhtml"]


@nox.session(venv_backend="conda")
def docs(session):
    session.install("-r", "docs/requirements.txt")
    session.run("sphinx-build", *BUILD_COMMAND)


@nox.session(name="docs-live", venv_backend="conda")
def docs_live(session):
    install_deps(session)

    cmd = ["sphinx-autobuild"]
    for path in ["*/_build/*", "*/tmp/*"]:
        cmd.extend(["--ignore", path])
    cmd.extend(BUILD_COMMAND)
    session.run(*cmd)
