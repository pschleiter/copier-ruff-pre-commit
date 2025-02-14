# copier-ruff-pre-commit

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border.json)](https://github.com/copier-org/copier)

A [pre-commit](https://pre-commit.com/) hook for [Ruff](https://github.com/astral-sh/ruff) applied on [Copier](https://github.com/copier-org/copier) template project.

### Using Copier-Ruff with pre-commit

To run Ruff's [linter](https://docs.astral.sh/ruff/linter) on a Copier template via pre-commit, add the following to your `.pre-commit-config.yaml`:

```yaml
repos:
- repo: https://github.com/pschleiter/copier-ruff-pre-commit
  # Ruff version.
  rev: v0.9.6
  hooks:
    # Run the linter.
    - id: copier-ruff
```

If ruff should be executed in a sub path of the template you can provide the path in the `.pre-commit-config.yaml`:

```yaml
repos:
- repo: https://github.com/pschleiter/copier-ruff-pre-commit
  # Ruff version.
  rev: v0.9.6
  hooks:
    # Run the linter.
    - id: copier-ruff
      args: [
        "--sub_path", "sub/dir"
      ]
```

If your Copier template requires you can provide them directly in the `.pre-commit-config.yaml`:

```yaml
repos:
- repo: https://github.com/pschleiter/copier-ruff-pre-commit
  # Ruff version.
  rev: v0.9.6
  hooks:
    # Run the linter.
    - id: copier-ruff
      args: [
        "--data", "VARIABLE1=VALUE1"
        "--data", "VARIABLE2=VALUE2"
      ]
```

This data could also be loaded from a yaml file:

```yaml
repos:
- repo: https://github.com/pschleiter/copier-ruff-pre-commit
  # Ruff version.
  rev: v0.9.6
  hooks:
    # Run the linter.
    - id: copier-ruff
      args: [
        "--data-file", "./data.yaml"
      ]
```

Additional options are:

```
Usage: copier-ruff [OPTIONS]

Options:
  -p, --sub-path TEXT  Sub path within the generated template to run `ruff`
                       in.
  -r, --vcs-ref TEXT   Git reference to checkout in `template_src`. If you do
                       not specify it, it will try to checkout the latest git
                       tag, as sorted using the PEP 440 algorithm. If you want
                       to checkout always the latest version, use `--vcs-
                       ref=HEAD`.
  -d, --data TEXT      Make VARIABLE available as VALUE when rendering the
                       template; may be given multiple times
  --data-file PATH     Load data from a YAML file
  -x, --exclude TEXT   A name or shell-style pattern matching files or folders
                       that must not be copied; may be given multiple times
  --trust              Allow templates with unsafe features (Jinja extensions,
                       migrations, tasks)
  -T, --skip-tasks     Skip template tasks execution
  --help               Show this message and exit.
```

for more details on these options see the [copier docs](https://copier.readthedocs.io/en/stable/reference/cli/)

## License

copier-ruff-pre-commit is licensed under

- MIT license ([LICENSE-MIT](LICENSE-MIT) or <https://opensource.org/licenses/MIT>)
