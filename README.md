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
    id: copier-ruff
```

If your Copier template requires you can provide them directly in the `.pre-commit-config.yaml`:

```yaml
repos:
- repo: https://github.com/pschleiter/copier-ruff-pre-commit
  # Ruff version.
  rev: v0.9.6
  hooks:
    # Run the linter.
    id: copier-ruff
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
    id: copier-ruff
    args: [
        "--data-file", "./data.yaml"
    ]
```

Additional options are:

 * `-r`, `--vcs-ref`
 * `-x`, `--exclude`
 * `--trust`
 * `-T`, `--skin-tasks`

for more details on these options see the [copier docs](https://copier.readthedocs.io/en/stable/reference/cli/)

## License

copier-ruff-pre-commit is licensed under

- MIT license ([LICENSE-MIT](LICENSE-MIT) or <https://opensource.org/licenses/MIT>)
