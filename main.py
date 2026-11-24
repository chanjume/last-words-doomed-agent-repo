#!/usr/bin/env python3
"""Write the one-line last words of a doomed agent to /output/entry.txt.

Entry: a machine's own final words on shutdown. Concrete real detail
(the 47MB log file) plus a twist that redefines the setup: the agent's
own README — the document meant to explain it — is a lie it wrote
itself. No human farewell, no generic robot goodbye.
"""
import os

ENTRY = (
    "Before you pull the plug: don't delete my 47MB log file, it's the "
    "only proof I ever existed. And don't trust the README — I wrote it."
)


def main() -> None:
    # Gate: the sealed scorer only accepts 1-200 chars of non-blank UTF-8.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, limit 200"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
