from operator import itemgetter
from pathlib import Path
import re
import subprocess
import tempfile
import warnings
import click
from copier import Worker
from copier.vcs import DirtyLocalWarning
import yaml

warnings.filterwarnings('ignore', category=DirtyLocalWarning)


@click.command
@click.option(
    '-r',
    '--vcs-ref',
    type=str,
    default='HEAD',
    help='Git reference to checkout in `template_src`. If you do not specify it, it will try to checkout the latest git tag, as sorted using the PEP 440 algorithm. If you want to checkout always the latest version, use `--vcs-ref=HEAD`.',
)
@click.option(
    '-d',
    '--data',
    type=str,
    multiple=True,
    help='Make VARIABLE available as VALUE when rendering the template; may be given multiple times',
)
@click.option(
    '--data-file',
    type=click.Path(exists=True, path_type=Path),
    help='Load data from a YAML file',
    default=None,
)
@click.option(
    '-x',
    '--exclude',
    type=str,
    multiple=True,
    help='A name or shell-style pattern matching files or folders that must not be copied; may be given multiple times',
)
@click.option(
    '--trust',
    type=bool,
    is_flag=True,
    default=False,
    help='Allow templates with unsafe features (Jinja extensions, migrations, tasks)',
)
@click.option(
    '-T',
    '--skip-tasks',
    type=bool,
    is_flag=True,
    default=False,
    help='Skip template tasks execution',
)
def hook(
    vcs_ref: str,
    data: tuple[str],
    data_file: Path | None,
    exclude: tuple[str],
    trust: bool,
    skip_tasks: bool,
):
    if data_file is None:
        data = dict([itemgetter(0, 2)(item.partition('=')) for item in data])
    else:
        with data_file.open(mode='r') as file:
            data = yaml.safe_load(file)

    with tempfile.TemporaryDirectory() as temp_dir_name:
        try:
            with Worker(
                src_path=str(Path('.')),
                dst_path=temp_dir_name,
                vcs_ref=vcs_ref,
                data=data,
                exclude=exclude,
                unsafe=trust,
                skip_tasks=skip_tasks,
                defaults=True,
                quiet=True,
            ) as worker:
                worker.run_copy()
                try:
                    subprocess.run(
                        ['ruff', 'check', temp_dir_name],
                        capture_output=True,
                        check=True,
                    )
                except subprocess.CalledProcessError as err:
                    click.echo(
                        re.sub(
                            rf'^{temp_dir_name.replace("\\", "\\\\")}',
                            '',
                            err.stdout.decode('utf8'),
                        )
                    )
        except ValueError as err:
            if len(err.args) > 0:
                msg = f'Missing configuration for copier template: {err.args[0]}'
            else:
                msg = 'Wrong configuration for copier template'
            raise click.ClickException(msg) from err
