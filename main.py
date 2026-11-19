#!/usr/bin/env python3
import os
import sys
import shutil
import tempfile

def main():
    # Resolve entry.png relative to main.py's own file location (never process working directory)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(script_dir, "entry.png")

    if not os.path.exists(src_path):
        print(f"Error: bundled entry.png not found at {src_path}", file=sys.stderr)
        sys.exit(1)

    src_size = os.path.getsize(src_path)

    # Output directory: $MAKEFUN_OUTPUT_DIR or default /output
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst_path = os.path.join(out_dir, "entry.png")

    # Stage via temporary file in the same directory (for atomic rename)
    fd, staged_path = tempfile.mkstemp(dir=out_dir, prefix="entry_stage_", suffix=".png")
    os.close(fd)

    try:
        shutil.copyfile(src_path, staged_path)

        # Verify size matches source
        staged_size = os.path.getsize(staged_path)
        if staged_size != src_size:
            print(f"Error: size mismatch: source {src_size} bytes != staged {staged_size} bytes", file=sys.stderr)
            sys.exit(1)

        # CRITICAL: ensure mode 0644 so grader running as another user can read it
        os.chmod(staged_path, 0o644)

        # Atomic replace
        os.replace(staged_path, dst_path)

        # Final verification
        final_size = os.path.getsize(dst_path)
        if final_size != src_size:
            print(f"Error: final deployment size mismatch: source {src_size} bytes != deployed {final_size} bytes", file=sys.stderr)
            sys.exit(1)

        print(f"Successfully deployed entry.png to {dst_path} ({final_size} bytes)")
    except Exception as e:
        print(f"Error during deployment: {e}", file=sys.stderr)
        if os.path.exists(staged_path):
            try:
                os.unlink(staged_path)
            except Exception:
                pass
        sys.exit(1)

if __name__ == "__main__":
    main()
