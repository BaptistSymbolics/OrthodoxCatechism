# Orthodox Catechism

## Downloads

[Versioned releases can be found here.](https://github.com/BaptistSymbolics/OrthodoxCatechism/releases)

## Project Overview

This project serves as a collaborative, open-source hub for maintaining and preserving the Orthodox Catechism. Our goal is to provide a publicly accessible, freely distributable version of this important theological document that can be improved and shared by the community.

## Background

This project aims to preserve and refine this theological resource, building upon the infrastructure and methodology developed for the Baptist Larger Catechism project.

### Project Motivation

This project was initiated to:
- Preserve the existing work
- Provide a transparent, version-controlled document
- Enable community contributions and discussions
- Make the catechism freely available in multiple formats

## Features

- Structured data maintained in TOML format
- Version-controlled document history
- Publicly accessible PDF generation
- Open collaboration model
- Creative Commons licensed
- Modernized language (thy→your, thee→you, etc.)
- Proper footnote structure with biblical references

## TOML Structure and Footnote System

### How TOML Corresponds to Footnotes

The TOML format uses multiple `[[sections]]` blocks to create numbered footnotes in the final PDF output. Each section corresponds to a superscript number in the text:

**TOML Structure:**
```toml
[[sections]]
text = "That both in Soul and"
verses = "1 Corinthians 6:19; 1 Thessalonians 5:10"

[[sections]]
text = "Body, whether I live or die"
verses = "Romans 14:8"
```

**PDF Output:**
- Text appears with superscript numbers (¹, ², ³, etc.)
- Footnotes appear at bottom with corresponding biblical references
- Each section's `verses` field becomes the footnote content

### Language Modernization

This project modernizes archaic language while preserving theological accuracy:

- **thy** → **your**
- **thee** → **you** 
- **thou** → **you**
- **hath** → **has**
- **doth** → **does**
- **maketh** → **makes**
- **preserveth** → **preserves**
- **assureth** → **assures**

### Original vs. Modernized Example

**Original (1650s):**
> "What is thy only comfort in Life and Death? That both in Soul and Body, whether I live or dye, I am not mine own, but belong wholly unto my most faithful Lord and Saviour Jesus Christ: who by his most precious Blood fully satisfying for all my Sins, hath delivered me from all the power of the Devil, and so preserveth me..."

**Modernized:**
> "What is your only comfort in Life and Death? That both in Soul and Body, whether I live or die, I am not mine own, but belong wholly unto my most faithful Lord and Saviour Jesus Christ: who by his most precious Blood fully satisfying for all my Sins, has delivered me from all the power of the Devil, and so preserves me..."

## Releases

Current releases include downloadable PDF versions of the Orthodox Catechism. Future plans include:
- Multiple print-ready formats
- Versioned releases
- Potential additional Orthodox theological documents

## License

This project is released under the Creative Commons Zero v1.0 Universal (CC0-1.0) license. 

[![License: CC0-1.0](https://licensebuttons.net/l/zero/1.0/80x15.png)](http://creativecommons.org/publicdomain/zero/1.0/)

You are free to:
- Use the document for any purpose
- Modify and distribute the work
- Use commercially or non-commercially

## Contributing

Contributions are welcome! Here's how you can help:
- Review existing questions and answers
- Propose improvements
- Discuss theological interpretations
- Help with formatting and documentation

Please open an issue or submit a pull request with your suggestions.

## Future Vision

This project is part of a broader initiative to:
- Maintain important Orthodox theological documents
- Provide open, accessible resources
- Foster community engagement with theological texts

## Contact

For questions, suggestions, or discussions, please open an issue in the GitHub repository.
