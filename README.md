# Orthodox Catechism

> **Beta (v0.9.1)** — This edition is under active review. Text, numbering, and prooftexts may change before the 1.0 release. Feedback and corrections are welcome via [GitHub Issues](https://github.com/BaptistSymbolics/OrthodoxCatechism/issues).

## Downloads

[Versioned releases can be found here.](https://github.com/BaptistSymbolics/OrthodoxCatechism/releases)

## Project Overview

This project serves as a collaborative, open-source hub for maintaining and preserving Hercules Collins' *Orthodox Catechism* (1680), a Particular Baptist adaptation of the Heidelberg Catechism. Our goal is to provide a publicly accessible, freely distributable version of this important theological document that can be improved and shared by the community.

## Background

The Orthodox Catechism was written by Hercules Collins, pastor of the Wapping congregation in London. Collins adapted the Heidelberg Catechism for a Particular Baptist audience, retaining most of the Heidelberg's structure while replacing the sections on infant baptism with distinctly Baptist teaching on believer's baptism, and adding sections on laying on of hands and hymn-singing.

### This Edition

This edition is a conservative modernization of Collins' original text:
- Archaic pronouns modernized (thy/thee/thou to your/you)
- Archaic verb forms updated (hath/doth/maketh to has/does/makes)
- False friends and dead words clarified (presently to immediately, commodity to benefit, etc.)
- Mid-sentence Germanic-style capitalization retained (Soul, Body, Sin) as a stylistic feature
- Collins' long compound Baptist questions split into catechetical question-and-answer sequences for readability
- All of Collins' original text is preserved; no content has been removed

### Question Count

This edition contains 159 questions:
- 149 in the standard published edition
- 6 optional questions on laying on of hands
- 4 optional questions on hymn-singing

Collins' original had fewer questions because several long Baptist arguments were presented as single Q&As. These have been split into multiple questions following standard catechetical form, where each subsequent question elucidates the one before it.

## Features

- Structured data maintained in TOML format
- Version-controlled document history
- Publicly accessible PDF generation
- Open collaboration model
- Creative Commons licensed
- Modernized language with scholarly fidelity
- Optional sections (laying on of hands, hymn-singing) tagged for filtering
- Proper footnote structure with biblical references

## TOML Structure

### Format

Each question is a separate TOML file in `src/`. The format uses multiple `[[sections]]` blocks to create numbered footnotes in the final PDF output:

```toml
id = "1"
question = "What is your only comfort in Life and Death?"

[[sections]]
text = "That both in Soul and"
verses = "1 Corinthians 6:19; 1 Thessalonians 5:10"

[[sections]]
text = "Body, whether I live or die"
verses = "Romans 14:8"
```

Sections concatenate with spaces at render time. Each section's `verses` field becomes a footnote.

### Optional Sections

Questions on laying on of hands and hymn-singing are tagged:

```toml
id = "84"
optional = true
section = "laying-on-of-hands"
question = "What Principle of Christ's Doctrine follows Baptism?"
```

These are available for scholars but excluded from the default published catechism.

## Releases

Current releases include downloadable PDF versions of the Orthodox Catechism. Future plans include:
- Multiple print-ready formats
- Versioned releases
- Build options for including/excluding optional sections

## License

This project is released under the Creative Commons Zero v1.0 Universal (CC0-1.0) license.

[![License: CC0-1.0](https://licensebuttons.net/l/zero/1.0/80x15.png)](http://creativecommons.org/publicdomain/zero/1.0/)

You are free to:
- Use the document for any purpose
- Modify and distribute the work
- Use commercially or non-commercially

## Contributing

Contributions are welcome! Here's how you can help:
- Review existing questions and answers against the original text
- Propose improvements to modernization
- Discuss theological interpretations
- Help with formatting and documentation

Please open an issue or submit a pull request with your suggestions.

## Future Vision

This project is part of a broader initiative to:
- Maintain important Baptist theological documents
- Provide open, accessible resources
- Foster community engagement with theological texts

## Contact

For questions, suggestions, or discussions, please open an issue in the GitHub repository.
