import os
import shutil
from pathlib import Path

DESTINATION_ROOT = r"D:\Organized By ClaudineAI"

CATEGORIES = {
    "Images": {
        "jpg", "jpeg", "png", "gif", "bmp", "svg", "webp", "ico",
        "tiff", "tif", "raw", "cr2", "nef", "heic", "heif", "psd",
        "ai", "eps", "indd"
    },
    "Videos": {
        "mp4", "avi", "mkv", "mov", "wmv", "flv", "webm", "m4v",
        "3gp", "3g2", "mpeg", "mpg", "rmvb", "vob", "ts", "mts"
    },
    "Audio": {
        "mp3", "wav", "flac", "aac", "ogg", "wma", "m4a", "opus",
        "aiff", "alac", "mid", "midi", "amr", "ape"
    },
    "Documents": {
        "pdf", "doc", "docx", "txt", "rtf", "odt", "pages",
        "tex", "md", "rst", "log", "nfo"
    },
    "Spreadsheets": {
        "xls", "xlsx", "csv", "ods", "numbers", "tsv"
    },
    "Presentations": {
        "ppt", "pptx", "odp", "key"
    },
    "Archives": {
        "zip", "rar", "7z", "tar", "gz", "bz2", "xz", "iso",
        "dmg", "tgz", "cab", "lzh", "lz", "z"
    },
    "Executables": {
        "exe", "msi", "bat", "cmd", "sh", "ps1", "app", "apk",
        "deb", "rpm", "run", "bin", "com"
    },
    "Code": {
        "py", "js", "ts", "html", "htm", "css", "java", "cpp", "c",
        "h", "cs", "php", "rb", "go", "rs", "swift", "kt", "r",
        "sql", "xml", "json", "yaml", "yml", "toml", "ini", "cfg",
        "env", "ipynb", "lua", "pl", "dart", "vue", "jsx", "tsx"
    },
    "Fonts": {
        "ttf", "otf", "woff", "woff2", "eot", "fon"
    },
    "Ebooks": {
        "epub", "mobi", "azw", "azw3", "fb2", "djvu", "lit"
    },
    "3D & CAD": {
        "stl", "obj", "fbx", "blend", "3ds", "dae", "gltf", "glb",
        "dwg", "dxf", "step", "stp", "iges", "igs"
    },
    "Databases": {
        "db", "sqlite", "sqlite3", "mdb", "accdb", "sql", "bak"
    },
}

def get_category(extension: str) -> str:
    ext = extension.lower().lstrip(".")
    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category
    return "Others"

def get_unique_path(destination: Path) -> Path:
    if not destination.exists():
        return destination
    stem = destination.stem
    suffix = destination.suffix
    parent = destination.parent
    counter = 1
    while True:
        new_name = f"{stem} ({counter}){suffix}"
        new_path = parent / new_name
        if not new_path.exists():
            return new_path
        counter += 1

def organize_files(source_folder: str):
    source = Path(source_folder)

    if not source.exists():
        print(f"[ERROR] Path does not exist: {source_folder}")
        return
    if not source.is_dir():
        print(f"[ERROR] Path is not a folder: {source_folder}")
        return

    dest_root = Path(DESTINATION_ROOT)
    dest_root.mkdir(parents=True, exist_ok=True)

    files = [f for f in source.rglob("*") if f.is_file()]

    if not files:
        print("No files found in the specified folder.")
        return

    print(f"\nFound {len(files)} file(s). Organizing...\n")

    moved = 0
    skipped = 0
    errors = 0

    for file in files:
        try:
            category = get_category(file.suffix)
            category_folder = dest_root / category
            category_folder.mkdir(parents=True, exist_ok=True)

            destination = get_unique_path(category_folder / file.name)
            shutil.move(str(file), str(destination))

            print(f"  [OK] {file.name}  ->  {category}/")
            moved += 1
        except Exception as e:
            print(f"  [SKIP] {file.name} — {e}")
            if isinstance(e, PermissionError):
                skipped += 1
            else:
                errors += 1

    # Delete empty subfolders (deepest first, skip the root source folder)
    subfolders = sorted(
        [f for f in source.rglob("*") if f.is_dir()],
        key=lambda p: len(p.parts),
        reverse=True
    )
    deleted_folders = 0
    for folder in subfolders:
        try:
            folder.rmdir()  # only removes if empty
            print(f"  [DEL] Removed empty folder: {folder.relative_to(source)}")
            deleted_folders += 1
        except OSError:
            pass  # folder not empty or permission denied, skip

    print(f"\nDone! {moved} moved, {skipped} skipped, {errors} error(s), {deleted_folders} empty folder(s) removed.")
    print(f"Files organized in: {DESTINATION_ROOT}")

def main():
    print("=" * 55)
    print("      File Organizer — by ClaudineAI")
    print("=" * 55)
    print(f"Destination: {DESTINATION_ROOT}\n")

    folder = input("Enter the folder path to organize: ").strip().strip('"').strip("'")

    if not folder:
        print("[ERROR] No path entered.")
        return

    organize_files(folder)

if __name__ == "__main__":
    main()
