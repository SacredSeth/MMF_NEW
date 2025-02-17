# Functions
def make_statement(statement, decoration="", lines=1):
    """Decorates headings
    (headings : 3 lines, subheadings : 2 lines, mini headings : 1 line)
    with chosen emoji/ASCII character, only use emoji for single line"""

    middle = f"{decoration * 3} {statement} {decoration * 3}"
    top_bottom = decoration * len(middle)

    # prints statement with decorations over a certain number of lines
    if lines == 1:
        print(middle)
    elif lines == 2:
        print(middle)
        print(top_bottom)
    else:
        print(top_bottom)
        print(middle)
        print(top_bottom)


# Main
make_statement("Instructions", "ℹ️")
