# Regular Expressions (Regex) - Comprehensive Guide

## Table of Contents

- [Regular Expressions (Regex) - Comprehensive Guide](#regular-expressions-regex---comprehensive-guide)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Basic Concepts](#basic-concepts)
    - [Literal Characters](#literal-characters)
    - [Metacharacters](#metacharacters)
  - [Common Metacharacters](#common-metacharacters)
  - [Quantifiers](#quantifiers)
  - [Character Classes](#character-classes)
  - [Anchors](#anchors)
  - [Grouping and Capturing](#grouping-and-capturing)
  - [Lookahead and Lookbehind](#lookahead-and-lookbehind)
  - [Flags/Modifiers](#flagsmodifiers)
  - [Practical Examples](#practical-examples)
    - [Email Validation](#email-validation)
    - [URL Matching](#url-matching)
    - [Date Format (YYYY-MM-DD)](#date-format-yyyy-mm-dd)
    - [HTML Tags](#html-tags)
    - [Password Requirements (8+ chars, 1 upper, 1 lower, 1 number)](#password-requirements-8-chars-1-upper-1-lower-1-number)
  - [Performance Considerations](#performance-considerations)
  - [Common Pitfalls](#common-pitfalls)
  - [Resources](#resources)
    - [Learning](#learning)
    - [Tools](#tools)
    - [Cheat Sheets](#cheat-sheets)

## Introduction

Regular expressions (regex) are powerful sequences of characters that define search patterns, primarily used for pattern matching within strings. Developed in the 1950s by mathematician Stephen Cole Kleene, regex has become an essential tool in programming, text processing, and data validation.

Key characteristics:

- Used for searching, replacing, and validating text patterns
- Supported in most programming languages (Python, JavaScript, Java, etc.)
- Implemented through dedicated regex engines
- Can match simple or extremely complex patterns

## Basic Concepts

### Literal Characters

The simplest regex pattern consists of literal characters that match themselves:

- `cat` matches "cat" in "concatenate"
- `123` matches "123" in "abc123def"

### Metacharacters

Special characters with reserved meanings:

- `. ^ $ * + ? { } [ ] \ | ( )`

To match these literally, escape them with backslash:

- `\.` matches a literal period
- `\\` matches a single backslash

## Common Metacharacters

| Character | Description                          | Example                     |
|-----------|--------------------------------------|-----------------------------|
| `.`       | Matches any single character         | `a.c` matches "abc", "a c"  |
| `^`       | Start of string (or line)            | `^Hello` matches start      |
| `$`       | End of string (or line)              | `end$` matches at end       |
| `\|`      | OR operator                          | `cat\|dog` matches either  |
| `\`       | Escape special character             | `\.` matches literal .     |
| `[]`      | Character class (match any inside)   | `[aeiou]` matches vowels   |

## Quantifiers

Quantifiers specify how many instances of a character or group must be present:

| Quantifier | Description                          | Example                     |
|------------|--------------------------------------|-----------------------------|
| `*`        | 0 or more                            | `a*` matches "", "a", "aa"  |
| `+`        | 1 or more                            | `a+` matches "a", "aa"      |
| `?`        | 0 or 1 (optional)                    | `colou?r` matches both spellings |
| `{n}`      | Exactly n times                      | `a{3}` matches "aaa"        |
| `{n,}`     | n or more times                      | `a{2,}` matches "aa", "aaa" |
| `{n,m}`    | Between n and m times                | `a{2,4}` matches "aa"-"aaaa"|

## Character Classes

Special notations for matching character sets:

| Pattern    | Description                          | Equivalent               |
|------------|--------------------------------------|--------------------------|
| `\d`       | Any digit                            | `[0-9]`                  |
| `\D`       | Any non-digit                        | `[^0-9]`                 |
| `\w`       | Word character (letter, digit, _)    | `[a-zA-Z0-9_]`           |
| `\W`       | Non-word character                   | `[^a-zA-Z0-9_]`          |
| `\s`       | Whitespace (space, tab, newline)     | `[ \t\n\r\f\v]`          |
| `\S`       | Non-whitespace                       | `[^ \t\n\r\f\v]`         |
| `[abc]`    | Any of a, b, or c                    |                          |
| `[^abc]`   | Any character except a, b, or c      |                          |
| `[a-z]`    | Any lowercase letter                 |                          |
| `[A-Z]`    | Any uppercase letter                 |                          |
| `[0-9]`    | Any digit                            |                          |

## Anchors

Assert positions without consuming characters:

| Anchor     | Description                          | Example                     |
|------------|--------------------------------------|-----------------------------|
| `^`        | Start of string/line                 | `^Start`                    |
| `$`        | End of string/line                   | `end$`                      |
| `\b`       | Word boundary                        | `\bword\b`                  |
| `\B`       | Not word boundary                    | `\Bword\B`                  |
| `\A`       | Start of string (ignores multiline)  | `\AStart`                   |
| `\Z`       | End of string (ignores multiline)    | `end\Z`                     |

## Grouping and Capturing

Parentheses create capturing groups:

```regex
(abc){3}       # Matches "abcabcabc"
(ab|cd)        # Matches "ab" or "cd"
```

Non-capturing groups (use `?:`):

```regex
(?:abc){3}     # Groups but doesn't capture
```

Named capturing groups:

```regex
(?P<name>pattern)   # Python-style named group
\k<name>            # Reference named group
```

## Lookahead and Lookbehind

Zero-width assertions (match without consuming):

| Assertion       | Description                          | Example                     |
|-----------------|--------------------------------------|-----------------------------|
| `(?=...)`       | Positive lookahead                   | `foo(?=bar)` matches "foo" only if followed by "bar" |
| `(?!...)`       | Negative lookahead                   | `foo(?!bar)` matches "foo" not followed by "bar" |
| `(?<=...)`      | Positive lookbehind                  | `(?<=foo)bar` matches "bar" only if preceded by "foo" |
| `(?<!...)`      | Negative lookbehind                  | `(?<!foo)bar` matches "bar" not preceded by "foo" |

## Flags/Modifiers

Change how the pattern is interpreted:

| Flag | Description                          | Example                     |
|------|--------------------------------------|-----------------------------|
| `i`  | Case insensitive                     | `/hello/i` matches "Hello"  |
| `m`  | Multiline mode (^/$ match line boundaries) | `/^start/m` |
| `s`  | Dot matches newline                  | `/a.b/s` matches "a\nb"     |
| `x`  | Verbose (ignore whitespace/comments) | Allows formatting complex regex |
| `g`  | Global search (find all matches)     | Standard in most languages  |

## Practical Examples

### Email Validation

```regex
^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
```

### URL Matching

```regex
https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)
```

### Date Format (YYYY-MM-DD)

```regex
^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$
```

### HTML Tags

```regex
<([a-z]+)([^<]+)*(?:>(.*)<\/\1>|\s+\/>)
```

### Password Requirements (8+ chars, 1 upper, 1 lower, 1 number)

```regex
^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$
```

## Performance Considerations

1. **Avoid backtracking**: Greedy quantifiers can cause performance issues
   - Prefer lazy quantifiers (`*?`, `+?`) when possible
   - Be specific with patterns to reduce ambiguity

2. **Compile patterns**: When reusing regex, compile them first

   ```python
   pattern = re.compile(r'\d+')  # Better for repeated use
   ```

3. **Use atomic groups**: `(?>...)` prevents backtracking

   ```regex
   (?>\d+)foo  # Once digits are matched, won't backtrack
   ```

4. **Benchmark complex patterns**: Test with realistic input sizes

## Common Pitfalls

1. **Over-matching**: Greedy quantifiers match more than intended
   - Solution: Use lazy quantifiers or be more specific

2. **Catastrophic backtracking**: Complex patterns with many possibilities

   ```regex
   (a+)+b  # Can cause exponential backtracking
   ```

3. **Escaping special characters**: Forgetting to escape regex metacharacters

   ```regex
   \.  # Correct for literal period
   ```

4. **Anchoring patterns**: Forgetting `^` and `$` can lead to partial matches

5. **Case sensitivity**: Forgetting to account for different cases
   - Solution: Use `i` flag or `[aA]` patterns

## Resources

### Learning

- [Regex101](https://regex101.com/) - Interactive regex tester and debugger
- [Regular-Expressions.info](https://www.regular-expressions.info/) - Comprehensive tutorial
- [RexEgg](http://www.rexegg.com/) - Advanced regex techniques

### Tools

- [Regexr](https://regexr.com/) - Online regex testing tool
- [Debuggex](https://www.debuggex.com/) - Regex visualizer
- [Pythex](https://pythex.org/) - Python-specific regex tester

### Cheat Sheets

- [Regex Cheat Sheet (PDF)](https://www.rexegg.com/regex-quickstart.html)
- [Python re module docs](https://docs.python.org/3/library/re.html)

---

This README provides a comprehensive overview of regular expressions, from basic concepts to advanced techniques. The examples and explanations should help both beginners understand regex fundamentals and experienced users refine their pattern-matching skills.
