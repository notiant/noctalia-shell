#!/usr/bin/env python3
"""
Translation Period Mismatch Checker

This script finds entries that end with a period (.) in de.json
but don't end with a period in en.json.

Usage:
    python3 check_translation_periods.py [--format=json|markdown|text]
"""

import json
import sys
from typing import Dict, List, Tuple


def flatten_json(obj, parent_key='', sep='.'):
    """
    Flatten nested JSON into dot-separated keys.
    
    Args:
        obj: The JSON object to flatten
        parent_key: The parent key for nested objects
        sep: The separator to use between nested keys
    
    Returns:
        A flattened dictionary with dot-separated keys
    """
    items = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(flatten_json(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
    return dict(items)


def find_period_mismatches(de_file: str, en_file: str) -> List[Dict[str, str]]:
    """
    Find entries that end with '.' in de.json but not in en.json.
    
    Args:
        de_file: Path to the German translation file
        en_file: Path to the English translation file
    
    Returns:
        A list of dictionaries containing mismatched entries
    """
    # Load both JSON files
    with open(de_file, 'r', encoding='utf-8') as f:
        de_data = json.load(f)
    
    with open(en_file, 'r', encoding='utf-8') as f:
        en_data = json.load(f)
    
    # Flatten both JSONs
    de_flat = flatten_json(de_data)
    en_flat = flatten_json(en_data)
    
    # Find mismatches
    mismatches = []
    for key, de_value in de_flat.items():
        if isinstance(de_value, str) and de_value.endswith('.'):
            en_value = en_flat.get(key, '')
            if isinstance(en_value, str) and not en_value.endswith('.'):
                mismatches.append({
                    'key': key,
                    'de': de_value,
                    'en': en_value
                })
    
    return mismatches


def format_as_text(mismatches: List[Dict[str, str]]) -> str:
    """Format mismatches as plain text."""
    output = []
    output.append(f"Found {len(mismatches)} entries that end with '.' in de.json but don't in en.json:\n")
    
    for i, match in enumerate(mismatches, 1):
        output.append(f"{i}. Key: {match['key']}")
        output.append(f"   DE: {match['de']}")
        output.append(f"   EN: {match['en']}")
        output.append("")
    
    return "\n".join(output)


def format_as_markdown(mismatches: List[Dict[str, str]]) -> str:
    """Format mismatches as Markdown."""
    output = []
    output.append("# Translation Period Mismatches\n")
    output.append(f"**Total mismatches:** {len(mismatches)}\n")
    output.append("## Entries\n")
    
    for i, match in enumerate(mismatches, 1):
        output.append(f"### {i}. `{match['key']}`\n")
        output.append(f"**German:** {match['de']}\n")
        output.append(f"**English:** {match['en']}\n")
        output.append("---\n")
    
    return "\n".join(output)


def format_as_json(mismatches: List[Dict[str, str]]) -> str:
    """Format mismatches as JSON."""
    return json.dumps({
        'total': len(mismatches),
        'mismatches': mismatches
    }, indent=2, ensure_ascii=False)


def main():
    """Main function."""
    # Parse command line arguments
    format_type = 'text'
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg.startswith('--format='):
            format_type = arg.split('=', 1)[1]
    
    # File paths
    de_file = 'Assets/Translations/de.json'
    en_file = 'Assets/Translations/en.json'
    
    try:
        # Find mismatches
        mismatches = find_period_mismatches(de_file, en_file)
        
        # Format and print output
        if format_type == 'json':
            print(format_as_json(mismatches))
        elif format_type == 'markdown':
            print(format_as_markdown(mismatches))
        else:
            print(format_as_text(mismatches))
        
        # Exit with code 1 if mismatches found
        sys.exit(1 if mismatches else 0)
        
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        print("Make sure you're running this script from the repository root.", file=sys.stderr)
        sys.exit(2)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}", file=sys.stderr)
        sys.exit(2)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(2)


if __name__ == '__main__':
    main()
