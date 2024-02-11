#!/bin/bash

# Simplified Org to Markdown Exporter using Pandoc
# Converts an Org-mode file to Markdown (GFM) format.
#
# Usage:
#   ./org_to_md.sh <input-org-file> [output-markdown-file]
#
# If the output file is not provided, the script uses the input file's name with a .md extension.

if [ "$#" -lt 1 ] || [ "$#" -gt 2 ]; then
    echo "Usage: $0 <input-org-file> [output-markdown-file]"
    exit 1
fi

# Input Org file
ORG_FILE=$1

# Output Markdown file
MD_FILE=${2:-"${ORG_FILE%.org}.md"}

# Run Pandoc to convert Org to Markdown (GFM)
pandoc -f org -t gfm -o "$MD_FILE" --standalone "$ORG_FILE"

# Check if Markdown file was created
if [ -f "$MD_FILE" ]; then
    echo "Exported to $MD_FILE successfully."
else
    echo "Export failed."
fi
