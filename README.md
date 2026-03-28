# File Organizer by ClaudineAI

A Python-based file organizer that automatically sorts files from any folder (including all subfolders) into categorized folders based on file type. No more messy directories — just point it at a folder and let it do the work.

---

## What It Does

- Scans a folder and **all its subfolders** recursively
- Detects each file's type by its extension
- Moves files into category folders inside `D:\Organized By ClaudineAI`
- **Auto-creates** category folders if they don't exist yet
- Handles **duplicate filenames** by appending `(1)`, `(2)`, etc. — no files are overwritten
- **Deletes empty subfolders** from the source path after organizing
- Prints a live status log and a final summary

---

## File Categories

| Folder | File Types |
|---|---|
| Images | jpg, jpeg, png, gif, bmp, svg, webp, heic, psd, ai, raw... |
| Videos | mp4, mkv, avi, mov, wmv, flv, webm... |
| Audio | mp3, wav, flac, aac, ogg, wma, m4a... |
| Documents | pdf, doc, docx, txt, rtf, odt, md, log... |
| Spreadsheets | xls, xlsx, csv, ods, numbers... |
| Presentations | ppt, pptx, odp, key... |
| Archives | zip, rar, 7z, tar, gz, iso, dmg... |
| Executables | exe, msi, bat, cmd, sh, apk... |
| Code | py, js, ts, html, css, java, cpp, json, sql, yaml... |
| Fonts | ttf, otf, woff, woff2... |
| Ebooks | epub, mobi, azw, fb2, djvu... |
| 3D & CAD | stl, obj, fbx, blend, dwg, dxf... |
| Databases | db, sqlite, mdb, accdb... |
| Others | Anything not matched above |

---

## Usage

### Option 1 — Run the EXE (No Python needed)
1. Download `FileOrganizerByClaudineAI.exe`
2. Double-click to run
3. Enter the folder path you want to organize when prompted
4. Done — check `D:\Organized By ClaudineAI` for the results

> On first launch, Windows Defender may show a security warning. Click **More info → Run anyway** to proceed.

### Option 2 — Run the Python Script
**Requirements:** Python 3.6+

```bash
python main.py
```

When prompted, enter the full path to the folder you want to organize:
```
Enter the folder path to organize: C:\Users\You\Downloads
```

---

## Example Output

```
=======================================================
      File Organizer — by ClaudineAI
=======================================================
Destination: D:\Organized By ClaudineAI

Enter the folder path to organize: C:\Users\You\Desktop\Mess

Found 42 file(s). Organizing...

  [OK] photo.jpg         ->  Images/
  [OK] report.pdf        ->  Documents/
  [OK] song.mp3          ->  Audio/
  [OK] archive.zip       ->  Archives/
  [OK] script.py         ->  Code/
  ...
  [DEL] Removed empty folder: old_stuff
  [DEL] Removed empty folder: old_stuff\archive

Done! 42 moved, 0 skipped, 0 error(s), 2 empty folder(s) removed.
Files organized in: D:\Organized By ClaudineAI
```

---

## Destination Folder

All organized files are saved to:
```
D:\Organized By ClaudineAI
```
This folder and its category subfolders are created automatically if they don't exist.

---

## Notes

- The original folder structure is flattened — files from all subfolders are moved into their category folder directly
- Files are **moved**, not copied — the source files will no longer be in their original location
- Files that cannot be moved (e.g. locked or permission-denied) are skipped and reported
- Empty subfolders in the source path are automatically deleted after all files are moved; folders that still contain files are left untouched

---

*Built with Python | Organized by ClaudineAI*
