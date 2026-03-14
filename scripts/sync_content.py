from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ENGLISH_FILES = [
    "00-front-matter.md",
    "01-introduction-enduring-imprints-of-the-longer-past.md",
    "02-the-tokugawa-polity.md",
    "03-social-and-economic-transformations.md",
    "04-the-intellectual-world-of-late-tokugawa.md",
    "05-the-overthrow-of-the-tokugawa.md",
    "06-the-samurai-revolution.md",
    "07-participation-and-protest.md",
    "08-social-economic-and-cultural-transformations.md",
    "09-empire-and-domestic-order.md",
    "10-economy-and-society.md",
    "11-democracy-and-empire-between-the-world-wars.md",
    "12-the-depression-crisis-and-responses.md",
    "13-japan-in-wartime.md",
    "14-occupied-japan-new-departures-and-durable-structures.md",
    "15-economic-and-social-transformations.md",
    "16-political-struggles-and-settlements-of-the-high-growth-era.md",
    "17-global-power-in-a-polarized-world-japan-in-the-1980s.md",
    "18-beyond-the-postwar-era.md",
    "appendix-a-prime-ministers-of-japan-1885-2001.md",
    "appendix-b-vote-totals-and-seats-by-party-1945-2000-lower-house-elections.md",
    "select-bibliography.md",
]

CHINESE_FILES = [
    "zh/00-front-matter.md",
    "zh/01-introduction-enduring-imprints-of-the-longer-past.md",
    "zh/02-the-tokugawa-polity.md",
    "zh/03-social-and-economic-transformations.md",
    "zh/04-the-intellectual-world-of-late-tokugawa.md",
    "zh/05-the-overthrow-of-the-tokugawa.md",
    "zh/06-the-samurai-revolution.md",
    "zh/07-participation-and-protest.md",
    "zh/08-social-economic-and-cultural-transformations.md",
    "zh/09-empire-and-domestic-order.md",
    "zh/10-economy-and-society.md",
    "zh/11-democracy-and-empire-between-the-world-wars.md",
    "zh/12-the-depression-crisis-and-responses.md",
    "zh/13-japan-in-wartime.md",
    "zh/14-occupied-japan-new-departures-and-durable-structures.md",
    "zh/15-economic-and-social-transformations.md",
    "zh/16-political-struggles-and-settlements-of-the-high-growth-era.md",
    "zh/17-global-power-in-a-polarized-world-japan-in-the-1980s.md",
    "zh/18-beyond-the-postwar-era.md",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Sync manuscript Markdown and image assets into the MkDocs project."
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path.home() / "Documents" / "a-modern-history-of-japan",
        help="Path to the source manuscript repository.",
    )
    return parser.parse_args()


def ensure_exists(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Missing required source path: {path}")


def normalize_english_markdown(text: str) -> str:
    return text.replace("(images/", "(../images/")


def write_file(destination: Path, text: str) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(text, encoding="utf-8")


def copy_markdown_files(source_root: Path, project_root: Path) -> None:
    docs_root = project_root / "docs"

    for relative in ENGLISH_FILES:
        source_path = source_root / relative
        ensure_exists(source_path)
        destination_path = docs_root / "en" / relative
        content = source_path.read_text(encoding="utf-8")
        content = normalize_english_markdown(content)
        write_file(destination_path, content)

    book_index_source = source_root / "index.md"
    ensure_exists(book_index_source)
    book_index_destination = docs_root / "en" / "book-index.md"
    content = book_index_source.read_text(encoding="utf-8")
    write_file(book_index_destination, content)

    for relative in CHINESE_FILES:
        source_path = source_root / relative
        ensure_exists(source_path)
        destination_path = docs_root / relative
        content = source_path.read_text(encoding="utf-8")
        write_file(destination_path, content)


def copy_images(source_root: Path, project_root: Path) -> None:
    source_images = source_root / "images"
    destination_images = project_root / "docs" / "images"
    ensure_exists(source_images)

    if destination_images.exists():
        shutil.rmtree(destination_images)

    shutil.copytree(source_images, destination_images)


def main() -> None:
    args = parse_args()
    source_root = args.source.expanduser().resolve()
    project_root = Path(__file__).resolve().parents[1]

    copy_markdown_files(source_root, project_root)
    copy_images(source_root, project_root)

    print(f"Synchronized content from {source_root} into {project_root / 'docs'}")


if __name__ == "__main__":
    main()
