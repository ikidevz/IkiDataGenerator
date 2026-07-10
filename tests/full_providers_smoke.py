"""
Full providers smoke test.
This script will attempt to instantiate every registered provider from the public schema
and generate one value from each provider to detect runtime import or execution errors.

Requirements:
    pip install iki-data-generator

Usage:
    python -m tests.full_providers_smoke

Note: Running this may require many third-party dependencies declared by the package.
"""

import importlib
import traceback

from ikidatagen.schema_registry import KEY_LABEL_REGISTRY
from ikidatagen.provider_factory import ProviderFactory


def provider_keys():
    # KEY_LABEL_REGISTRY maps key_label -> group
    return list(KEY_LABEL_REGISTRY.keys())


def main():
    errors = []
    ok = []
    for key in provider_keys():
        group = None
        try:
            # attempt to create provider instance with minimal options
            provider = ProviderFactory.create(key_label=key, group=group)
            # call generate_non_blank (safe default row_data)
            value = provider.generate_non_blank(row_data={})
            ok.append((key, repr(value)))
        except Exception as e:
            tb = traceback.format_exc()
            errors.append((key, str(e), tb))

    print(f"Providers OK: {len(ok)}")
    for k, v in ok[:20]:
        print(f"  {k}: {v}")

    print(f"\nProviders FAIL: {len(errors)}")
    for k, msg, tb in errors[:50]:
        print(f"---\n{k} -> {msg}\n{tb}")

    if errors:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
