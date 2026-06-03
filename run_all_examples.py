#!/usr/bin/env python3
"""
Execute all examples in the examples/ folder.
Runs each example script and reports results.
"""

import os
import sys
import subprocess
import time
from pathlib import Path
from datetime import datetime

if sys.platform.startswith("win"):
    os.system("chcp 65001 > nul")
    sys.stdout.reconfigure(encoding="utf-8")


def run_examples(examples_dir="examples", pattern="*.py", verbose=True):
    """
    Execute all example scripts in the examples directory.
    """
    # Get the directory where this script is located
    script_dir = Path(__file__).parent.absolute()

    # Resolve examples directory relative to the script
    examples_path = (script_dir / examples_dir).resolve()

    if not examples_path.exists():
        print(f"❌ Error: Examples directory not found at {examples_path}")
        return None

    # Find all matching files
    example_files = sorted(examples_path.glob(pattern))
    example_files = [f for f in example_files if f.is_file()
                     and f.suffix == ".py"]

    if not example_files:
        print(f"⚠️  No Python files found in {examples_path}")
        return None

    print(f"\n{'='*70}")
    print(f"🚀 Running {len(example_files)} Examples")
    print(f"{'='*70}")
    print(f"📁 Directory: {examples_path}")
    print(f"⏰ Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*70}\n")

    passed = 0
    failed = 0
    skipped = 0
    start_time = time.time()
    failed_files = []

    for idx, example_file in enumerate(example_files, 1):
        filename = example_file.name

        print(
            f"  [{idx:2d}/{len(example_files)}] ▶️  RUN   {filename}...", end="", flush=True)

        try:
            # Run using absolute path to avoid cwd issues
            result = subprocess.run(
                [sys.executable, str(example_file)],  # Use full path
                capture_output=True,
                text=True,
                timeout=300,
                cwd=script_dir.parent  # Optional: set cwd to project root
            )

            if result.returncode == 0:
                print(" ✅ OK")
                passed += 1
            else:
                print(" ❌ FAILED")
                failed += 1
                failed_files.append({
                    "file": filename,
                    "error": result.stderr or result.stdout
                })
                if verbose:
                    print(
                        f"      Error: {result.stderr if result.stderr else result.stdout}")

        except subprocess.TimeoutExpired:
            print(" ⏱️  TIMEOUT")
            failed += 1
            failed_files.append(
                {"file": filename, "error": "Execution timed out (>5 minutes)"})
        except Exception as e:
            print(" ⚠️  ERROR")
            failed += 1
            failed_files.append({"file": filename, "error": str(e)})

    # Summary...
    elapsed_time = time.time() - start_time
    total = len(example_files)

    print(f"\n{'='*70}")
    print(f"📊 Summary")
    print(f"{'='*70}")
    print(f"✅ Passed:  {passed}/{total}")
    print(f"❌ Failed:  {failed}/{total}")
    print(f"⏭️  Skipped: {skipped}/{total}")
    print(f"⏱️  Time:    {elapsed_time:.2f}s")
    print(f"{'='*70}\n")

    if failed_files and verbose:
        print("Failed Examples:")
        for item in failed_files:
            print(f"  • {item['file']}")
            if item.get('error'):
                print(f"    └─ {str(item['error']).splitlines()[0][:100]}")

    return {
        "total": total, "passed": passed, "failed": failed,
        "skipped": skipped, "time": elapsed_time, "failed_files": failed_files
    }


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Execute all example scripts in the examples/ folder",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run_all_examples.py                    # Run all examples
  python run_all_examples.py --dir examples     # Specify examples folder
  python run_all_examples.py --pattern "0*.py" # Run specific pattern
  python run_all_examples.py --quiet            # Minimal output
        """
    )

    parser.add_argument(
        "--dir",
        default="examples",
        help="Path to examples directory (default: examples)"
    )

    parser.add_argument(
        "--pattern",
        default="*.py",
        help="File pattern to match (default: *.py)"
    )

    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Minimal output"
    )

    args = parser.parse_args()

    # Run examples
    stats = run_examples(
        examples_dir=args.dir,
        pattern=args.pattern,
        verbose=not args.quiet
    )

    # Exit with appropriate code
    if stats:
        sys.exit(0 if stats["failed"] == 0 else 1)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
