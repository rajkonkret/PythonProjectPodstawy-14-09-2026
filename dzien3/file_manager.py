from __future__ import annotations

import os
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, ttk


class FileManager(tk.Tk):
    """Prosty menedzer plikow oparty na bibliotece Tkinter."""

    def __init__(self) -> None:
        super().__init__()
        self.title("Menedzer plikow")
        self.geometry("900x600")
        self.minsize(650, 400)
        self.current_path = Path.home()
        self.path_var = tk.StringVar()

        self._create_widgets()
        self.refresh_directory()

    def _create_widgets(self) -> None:
        navigation = ttk.Frame(self, padding=8)
        navigation.pack(fill=tk.X)

        ttk.Button(navigation, text="Wybierz folder", command=self.choose_directory).pack(
            side=tk.LEFT
        )
        ttk.Button(navigation, text="W gore", command=self.go_up).pack(
            side=tk.LEFT, padx=(6, 0)
        )
        ttk.Button(navigation, text="Odswiez", command=self.refresh_directory).pack(
            side=tk.LEFT, padx=(6, 12)
        )
        ttk.Entry(navigation, textvariable=self.path_var, state="readonly").pack(
            side=tk.LEFT, fill=tk.X, expand=True
        )

        table_frame = ttk.Frame(self, padding=(8, 0))
        table_frame.pack(fill=tk.BOTH, expand=True)

        columns = ("name", "type", "size", "modified")
        self.tree = ttk.Treeview(
            table_frame, columns=columns, show="headings", selectmode="browse"
        )
        self.tree.heading("name", text="Nazwa")
        self.tree.heading("type", text="Typ")
        self.tree.heading("size", text="Rozmiar")
        self.tree.heading("modified", text="Zmodyfikowano")
        self.tree.column("name", width=360)
        self.tree.column("type", width=130, anchor=tk.CENTER)
        self.tree.column("size", width=100, anchor=tk.E)
        self.tree.column("modified", width=170, anchor=tk.CENTER)
        self.tree.bind("<Double-1>", self.open_selected)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scrollbar.set)

        actions = ttk.Frame(self, padding=8)
        actions.pack(fill=tk.X)
        ttk.Button(actions, text="Nowy plik", command=self.create_file).pack(side=tk.LEFT)
        ttk.Button(actions, text="Nowy folder", command=self.create_folder).pack(
            side=tk.LEFT, padx=(6, 0)
        )
        ttk.Button(actions, text="Zmien nazwe", command=self.rename_selected).pack(
            side=tk.LEFT, padx=(18, 0)
        )
        ttk.Button(actions, text="Kopiuj", command=self.copy_selected).pack(
            side=tk.LEFT, padx=(6, 0)
        )
        ttk.Button(actions, text="Przenies", command=self.move_selected).pack(
            side=tk.LEFT, padx=(6, 0)
        )
        ttk.Button(actions, text="Usun", command=self.delete_selected).pack(
            side=tk.LEFT, padx=(18, 0)
        )

    def refresh_directory(self) -> None:
        """Wyswietla elementy biezacego katalogu."""
        self.path_var.set(str(self.current_path))
        self.tree.delete(*self.tree.get_children())
        try:
            entries = sorted(
                self.current_path.iterdir(),
                key=lambda path: (not path.is_dir(), path.name.casefold()),
            )
            for path in entries:
                stat = path.stat()
                file_type = "Folder" if path.is_dir() else "Plik"
                size = "" if path.is_dir() else self.format_size(stat.st_size)
                modified = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M")
                self.tree.insert(
                    "",
                    tk.END,
                    iid=str(path),
                    values=(path.name, file_type, size, modified),
                )
        except OSError as error:
            messagebox.showerror("Blad odczytu", f"Nie mozna odczytac katalogu:\n{error}")

    @staticmethod
    def format_size(size: int) -> str:
        units = ("B", "KB", "MB", "GB", "TB")
        value = float(size)
        for unit in units:
            if value < 1024 or unit == units[-1]:
                return f"{value:.0f} {unit}" if unit == "B" else f"{value:.1f} {unit}"
            value /= 1024
        return ""

    def choose_directory(self) -> None:
        directory = filedialog.askdirectory(initialdir=self.current_path)
        if directory:
            self.current_path = Path(directory)
            self.refresh_directory()

    def go_up(self) -> None:
        parent = self.current_path.parent
        if parent != self.current_path:
            self.current_path = parent
            self.refresh_directory()

    def selected_path(self) -> Path | None:
        selection = self.tree.selection()
        if not selection:
            messagebox.showinfo("Brak wyboru", "Najpierw zaznacz plik lub folder.")
            return None
        return Path(selection[0])

    def open_selected(self, _event: tk.Event[tk.Misc] | None = None) -> None:
        path = self.selected_path()
        if path is None:
            return
        if path.is_dir():
            self.current_path = path
            self.refresh_directory()
            return
        try:
            if sys.platform == "win32":
                os.startfile(path)  # type: ignore[attr-defined]
            elif sys.platform == "darwin":
                subprocess.run(["open", str(path)], check=True)
            else:
                subprocess.run(["xdg-open", str(path)], check=True)
        except OSError as error:
            messagebox.showerror("Blad otwierania", f"Nie mozna otworzyc pliku:\n{error}")

    def create_file(self) -> None:
        name = simpledialog.askstring("Nowy plik", "Podaj nazwe pliku:", parent=self)
        if name:
            self._create_path(name, is_folder=False)

    def create_folder(self) -> None:
        name = simpledialog.askstring("Nowy folder", "Podaj nazwe folderu:", parent=self)
        if name:
            self._create_path(name, is_folder=True)

    def _create_path(self, name: str, is_folder: bool) -> None:
        target = self.current_path / name
        if not self.is_valid_name(name):
            messagebox.showerror("Nieprawidlowa nazwa", "Nazwa nie moze zawierac separatora sciezki.")
            return
        try:
            if is_folder:
                target.mkdir()
            else:
                target.touch(exist_ok=False)
            self.refresh_directory()
        except OSError as error:
            messagebox.showerror("Blad tworzenia", f"Nie mozna utworzyc elementu:\n{error}")

    @staticmethod
    def is_valid_name(name: str) -> bool:
        return bool(name.strip()) and Path(name).name == name and name not in {".", ".."}

    def rename_selected(self) -> None:
        path = self.selected_path()
        if path is None:
            return
        name = simpledialog.askstring(
            "Zmiana nazwy", "Podaj nowa nazwe:", initialvalue=path.name, parent=self
        )
        if name is None:
            return
        if not self.is_valid_name(name):
            messagebox.showerror("Nieprawidlowa nazwa", "Nazwa nie moze zawierac separatora sciezki.")
            return
        try:
            path.rename(path.with_name(name))
            self.refresh_directory()
        except OSError as error:
            messagebox.showerror("Blad zmiany nazwy", f"Nie mozna zmienic nazwy:\n{error}")

    def copy_selected(self) -> None:
        path = self.selected_path()
        if path is not None:
            self._transfer(path, move=False)

    def move_selected(self) -> None:
        path = self.selected_path()
        if path is not None:
            self._transfer(path, move=True)

    def _transfer(self, path: Path, move: bool) -> None:
        destination = filedialog.askdirectory(
            title="Wybierz folder docelowy", initialdir=self.current_path
        )
        if not destination:
            return
        target = Path(destination) / path.name
        if target.exists():
            messagebox.showerror("Element juz istnieje", f"Element juz istnieje:\n{target}")
            return
        try:
            if move:
                shutil.move(str(path), str(target))
            elif path.is_dir():
                shutil.copytree(path, target)
            else:
                shutil.copy2(path, target)
            self.refresh_directory()
        except OSError as error:
            action = "przeniesc" if move else "skopiowac"
            messagebox.showerror("Blad operacji", f"Nie mozna {action} elementu:\n{error}")

    def delete_selected(self) -> None:
        path = self.selected_path()
        if path is None:
            return
        if not messagebox.askyesno(
            "Potwierdz usuniecie", f"Czy na pewno usunac '{path.name}'?", icon=messagebox.WARNING
        ):
            return
        try:
            if path.is_dir():
                shutil.rmtree(path)
            else:
                path.unlink()
            self.refresh_directory()
        except OSError as error:
            messagebox.showerror("Blad usuwania", f"Nie mozna usunac elementu:\n{error}")


if __name__ == "__main__":
    FileManager().mainloop()
