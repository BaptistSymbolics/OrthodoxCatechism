#!/usr/bin/env python3
"""
Convert Orthodox Catechism OCR text to TOML format.
This script processes the OCR text to extract Q&A pairs and modernize spelling.
"""
import re
import os
import sys
from pathlib import Path
from typing import List, Tuple, Dict, Optional

def modernize_text(text: str) -> str:
    """
    Modernize 1600s spelling and OCR artifacts.
    
    Args:
        text: Original text with archaic spelling
        
    Returns:
        Modernized text
    """
    # Dictionary of common 1600s -> modern spelling replacements
    replacements = {
        # Long s (ſ) replacements
        'ſ': 's',
        'Chriſt': 'Christ',
        'Goſpel': 'Gospel',
        'Jeſus': 'Jesus',
        'ſhall': 'shall',
        'ſhould': 'should',
        'ſin': 'sin',
        'ſins': 'sins',
        'ſoul': 'soul',
        'ſpirit': 'spirit',
        'ſpiritual': 'spiritual',
        'ſacred': 'sacred',
        'ſatisfy': 'satisfy',
        'ſatisfied': 'satisfied',
        'ſatisfaction': 'satisfaction',
        'ſalvation': 'salvation',
        'ſaviour': 'saviour',
        'ſaved': 'saved',
        'ſervant': 'servant',
        'ſerve': 'serve',
        'ſervice': 'service',
        'ſee': 'see',
        'ſeek': 'seek',
        'ſelf': 'self',
        'ſelves': 'selves',
        'ſame': 'same',
        'ſuch': 'such',
        'ſure': 'sure',
        'ſurely': 'surely',
        'ſuffer': 'suffer',
        'ſuffered': 'suffered',
        'ſuffering': 'suffering',
        'ſufferings': 'sufferings',
        'ſubject': 'subject',
        'ſubmit': 'submit',
        'ſubstance': 'substance',
        'ſon': 'son',
        'ſons': 'sons',
        'ſpeak': 'speak',
        'ſpoken': 'spoken',
        'ſpirit': 'spirit',
        'ſpirits': 'spirits',
        'ſpiritual': 'spiritual',
        'ſtand': 'stand',
        'ſtate': 'state',
        'ſtrength': 'strength',
        'ſtrong': 'strong',
        
        # Common archaic spellings
        'haue': 'have',
        'vnto': 'unto',
        'vpon': 'upon',
        'vſe': 'use',
        'vſed': 'used',
        'vſeth': 'uses',
        'vſing': 'using',
        'vſual': 'usual',
        'vſually': 'usually',
        'vndoubtedly': 'undoubtedly',
        'vnderstood': 'understood',
        'vnderstand': 'understand',
        'vnion': 'union',
        'vnited': 'united',
        'vnite': 'unite',
        'vnity': 'unity',
        'vniversal': 'universal',
        'vnworthy': 'unworthy',
        'vp': 'up',
        'vphold': 'uphold',
        'vpholdeth': 'upholds',
        'vtterly': 'utterly',
        'vvhat': 'what',
        'vvhen': 'when',
        'vvhere': 'where',
        'vvherefore': 'wherefore',
        'vvhich': 'which',
        'vvho': 'who',
        'vvhy': 'why',
        'vvill': 'will',
        'vvith': 'with',
        'vvithout': 'without',
        'vvord': 'word',
        'vvords': 'words',
        'vvork': 'work',
        'vvorks': 'works',
        'vvorld': 'world',
        'vvorship': 'worship',
        'vvould': 'would',
        
        # Other common replacements
        'thinke': 'think',
        'beleive': 'believe',
        'receaue': 'receive',
        'giue': 'give',
        'liue': 'live',
        'loue': 'love',
        'aboue': 'above',
        'moue': 'move',
        'proue': 'prove',
        'serue': 'serve',
        'preserue': 'preserve',
        'obserue': 'observe',
        'deserue': 'deserve',
        'conuert': 'convert',
        'conuersion': 'conversion',
        'conuersation': 'conversation',
        'euery': 'every',
        'euer': 'ever',
        'euerlasting': 'everlasting',
        'neuer': 'never',
        'ouer': 'over',
        'vnder': 'under',
        'after': 'after',
        'before': 'before',
        'therefore': 'therefore',
        'wherefore': 'wherefore',
        'moreouer': 'moreover',
        'howsoeuer': 'howsoever',
        'whatsoeuer': 'whatsoever',
        'wheresoeuer': 'wheresoever',
        'whensoeuer': 'whensoever',
        'whosoeuer': 'whosoever',
        
        # Fix common OCR errors
        'Gbd': 'God',
        'Cbrist': 'Christ',
        'Cbristian': 'Christian',
        'Cburch': 'Church',
        'Gommandment': 'Commandment',
        'Gommandments': 'Commandments',
        'Gant': 'Commandment',
        'Queſt': 'Quest',
        'Anſw': 'Answ',
        'Q.': 'Q.',
        'A.': 'A.',
        
        # Fix punctuation issues
        ' ;': ';',
        ' :': ':',
        ' ,': ',',
        ' .': '.',
        ' ?': '?',
        ' !': '!',
        
        # Fix spacing issues
        '  ': ' ',
        '   ': ' ',
    }
    
    # Apply replacements
    modernized = text
    for old, new in replacements.items():
        modernized = modernized.replace(old, new)
    
    # Additional regex-based fixes
    modernized = re.sub(r'\bſ([a-z])', r's\1', modernized)  # Catch remaining long s
    modernized = re.sub(r'([a-z])ſ\b', r'\1s', modernized)  # Long s at word end
    modernized = re.sub(r'([a-z])ſ([a-z])', r'\1s\2', modernized)  # Long s in middle
    
    return modernized.strip()

def extract_scripture_references(text: str) -> Tuple[str, str]:
    """
    Extract scripture references from text and return cleaned text + references.
    
    Args:
        text: Text that may contain scripture references
        
    Returns:
        Tuple of (cleaned_text, scripture_references)
    """
    # Look for scripture reference blocks that start with citations like (a), (b), etc.
    # These usually appear at the end of answers
    
    # Pattern to find the start of scripture references
    # Look for patterns like "(a) Rom. 3. 20" or "{.-) 1 Cor. 6. 19"
    ref_start_pattern = r'[\(\{\[][-\.\w]*[\)\}\]]\s*(?:\d+\s*)?[A-Z][a-z]*\.?\s*\d+'
    
    # Find where scripture references start
    ref_match = re.search(ref_start_pattern, text)
    
    if ref_match:
        # Split text at the reference point
        main_text = text[:ref_match.start()].strip()
        scripture_refs = text[ref_match.start():].strip()
        
        # Clean up the main text
        main_text = re.sub(r'\s+', ' ', main_text)
        
        # Clean up scripture references
        scripture_refs = re.sub(r'[\(\{\[][-\.\w]*[\)\}\]]\s*', '', scripture_refs)
        scripture_refs = re.sub(r'\s+', ' ', scripture_refs)
        
        return main_text, scripture_refs
    
    # If no clear scripture references found, return text as-is
    cleaned_text = re.sub(r'\s+', ' ', text.strip())
    return cleaned_text, ""

def extract_qa_pairs(ocr_text: str) -> List[Dict[str, str]]:
    """
    Extract question-answer pairs from the OCR text.
    
    Args:
        ocr_text: Full OCR text
        
    Returns:
        List of dictionaries with 'question' and 'answer' keys
    """
    qa_pairs = []
    
    # Find the start of the catechism Q&A section
    catechism_start = ocr_text.find("A Catechiſm containing the ſum of")
    if catechism_start == -1:
        print("Could not find catechism start marker")
        return qa_pairs
    
    # Extract the catechism section
    catechism_text = ocr_text[catechism_start:]
    
    # Look for the actual first question which starts with "Queſt, VV7"
    first_q_start = catechism_text.find("Queſt, VV7")
    if first_q_start != -1:
        catechism_text = catechism_text[first_q_start:]
    
    # Split the text into Q&A blocks more carefully
    # Use a more specific pattern that matches the actual format
    qa_blocks = re.split(r'\n\s*(?=Q\.|\bQueſt\.|\bQuest\.)', catechism_text)
    
    print(f"Found {len(qa_blocks)} potential Q&A blocks")
    
    for i, block in enumerate(qa_blocks):
        if not block.strip():
            continue
            
        # Look for question pattern at start of block
        q_match = re.match(r'(?:Q\.|Queſt\.|Quest\.)\s*([^A]*?)(?=A\.|Anſw\.)', block, re.DOTALL)
        if not q_match:
            continue
            
        question = q_match.group(1).strip()
        
        # Look for answer pattern in the same block
        a_match = re.search(r'(?:A\.|Anſw\.)\s*(.*?)(?=\n\s*(?:Q\.|Queſt\.|Quest\.)|$)', block, re.DOTALL)
        if not a_match:
            continue
            
        answer = a_match.group(1).strip()
        
        if question and answer:
            # Clean up the text
            question = modernize_text(question)
            answer = modernize_text(answer)
            
            # Extract scripture references
            answer_clean, scripture_refs = extract_scripture_references(answer)
            
            qa_pairs.append({
                'question': question,
                'answer': answer_clean,
                'scripture_refs': scripture_refs
            })
            
            print(f"Extracted Q{len(qa_pairs)}: {question[:50]}...")
    
    return qa_pairs

def create_toml_file(qa_pair: Dict[str, str], question_num: int, output_dir: str) -> bool:
    """
    Create a TOML file for a single Q&A pair.
    
    Args:
        qa_pair: Dictionary with question, answer, and scripture references
        question_num: Question number for the filename
        output_dir: Directory to save the TOML file
        
    Returns:
        True if successful, False otherwise
    """
    try:
        filename = f"{question_num:03d}.toml"
        filepath = os.path.join(output_dir, filename)
        
        # Split long answers into sections if needed
        answer_text = qa_pair['answer']
        sections = []
        
        # For now, put the entire answer in one section
        # This can be enhanced to intelligently split long answers
        sections.append({
            'text': answer_text,
            'verses': qa_pair['scripture_refs'] if qa_pair['scripture_refs'] else ""
        })
        
        # Generate TOML content
        toml_content = f'id = "{question_num}"\n'
        toml_content += f'question = "{qa_pair["question"]}"\n\n'
        
        for section in sections:
            toml_content += '[[sections]]\n'
            toml_content += f'text = "{section["text"]}"\n'
            toml_content += f'verses = "{section["verses"]}"\n\n'
        
        # Write to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(toml_content)
        
        print(f"Created {filename}")
        return True
        
    except Exception as e:
        print(f"Error creating TOML file for question {question_num}: {e}")
        return False

def main():
    """Main function to process the OCR text and generate TOML files."""
    # Paths
    script_dir = Path(__file__).parent
    project_dir = script_dir.parent
    ocr_file = project_dir / "original" / "orthodox-catechism-ocr.txt"
    output_dir = project_dir / "src"
    
    # Ensure output directory exists
    output_dir.mkdir(exist_ok=True)
    
    # Read OCR text
    try:
        with open(ocr_file, 'r', encoding='utf-8') as f:
            ocr_text = f.read()
    except Exception as e:
        print(f"Error reading OCR file: {e}")
        return 1
    
    print(f"Read {len(ocr_text)} characters from OCR file")
    
    # Extract Q&A pairs
    qa_pairs = extract_qa_pairs(ocr_text)
    
    if not qa_pairs:
        print("No Q&A pairs found!")
        return 1
    
    print(f"Extracted {len(qa_pairs)} Q&A pairs")
    
    # For pilot, limit to first 10 questions to test the system
    pilot_limit = 10
    qa_pairs = qa_pairs[:pilot_limit]
    
    print(f"Processing first {len(qa_pairs)} questions for pilot")
    
    # Generate TOML files
    success_count = 0
    for i, qa_pair in enumerate(qa_pairs, 1):
        if create_toml_file(qa_pair, i, str(output_dir)):
            success_count += 1
    
    print(f"\nSuccessfully created {success_count}/{len(qa_pairs)} TOML files")
    
    # Show first few questions for review
    print("\nFirst few questions extracted:")
    for i, qa_pair in enumerate(qa_pairs[:3], 1):
        print(f"\n{i}. {qa_pair['question']}")
        print(f"   Answer: {qa_pair['answer'][:100]}...")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
