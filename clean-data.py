"""Simple HXL command-line script"""

import sys, hxl


def clean_data(filename_or_url, output_stream):
    """
    Clean a HXL dataset
    1. Remove personally-identifiable data (#contact)
    2. Replace "BRC" with "British Red Cross" in the #org column
    """
    source = hxl.data(filename_or_url, True) # True means it's OK to use local files
    filtered = source .without_columns('contact').replace_data('BRC', 'British Red Cross', pattern='#org')
    hxl.io.write_hxl(output_stream, filtered)


# If launched as a script, read the input filename/URL from the first parameter
if __name__ == '__main__':
    if len(sys.argv) > 1:
        clean_data(sys.argv[1], sys.stdout)
    else:
        sys.stderr.write("Usage: python hxl-sample.py <input-file-or-url>\n")
        exit(2)

# end
