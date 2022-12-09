#! /usr/local/bin pyhton3

import time
import os
import typer
import shutil
from git.repo.base import Repo
from rich import print
from rich.progress import track
from rich.progress import Progress, SpinnerColumn, TextColumn

def main():
    total = 0
    current_dir = os.getcwd()

    print(current_dir)

    print("-----------------------------------------------------------------------")
    print("[bold #f7912a]SMILES CLI FOR TYPESCRIPT PROJECTS[/bold #f7912a]")
    print("-----------------------------------------------------------------------")
    repo_name = typer.prompt("Nome do projeto")
    if len(repo_name) <= 5:
        print(f"[bold red]Parece que esse nome não satisfaz os padrões smiles![/bold red]")
        return None

    print(f"[bold]Buscando...[/bold] :eyes: ")
    Repo.clone_from("git@github.com:smiles-sa/smiles-engenhariasoftware.git", "temp", branch="master")
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Configurando Arquivos", total=None)
        shutil.rmtree(f"{current_dir}/temp/.git", ignore_errors=False, onerror=None)
        shutil.rmtree(f"{current_dir}/temp/README.md", ignore_errors=False, onerror=None)

        source_folder = f"{current_dir}/temp/"

        for file_name in os.listdir(source_folder):
            source = source_folder + file_name
            destination = f"{current_dir}/{file_name}" # so i don't know why here i need to do this way, because using + won't go

            shutil.move(source, destination)

        progress.add_task(description="Finalizando...", total=None)
        old_cfn = f"{current_dir}/smiles-engenhariasoftware.yml"
        new_cfn = f"{current_dir}/{repo_name}.yml"

        os.rename(old_cfn, new_cfn)
        time.sleep(5)

    print("--------------------------------------------------")
    print(f"[green]Repo [#f7912a]{repo_name}[/#f7912a] Criado![/green]")
    print("----------------------------------------------------------")
    print(f"[bold f7912a]Tudo Pronto por aqui :)[/bold f7912a]")

if __name__ == "__main__":
    typer.run(main)
