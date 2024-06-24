import spacy
import re
import inflect

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

# Define the keywords related to the product
keywords = ['noodles' ,'cereals', 'pasta']


p = inflect.engine()




# ////////// split sections further to check each individual point separately within a section.
# def get_singular_and_plural_forms(word):
#     """Generate both singular and plural forms of a word."""
#     singular = p.singular_noun(word)
#     plural = p.plural(word)
    
#     if singular == False:  # The word is already singular
#         singular = word
#     if plural == word:  # The word is already plural
#         plural = p.plural(word + 's')
    
#     return singular, plural

# def extract_relevant_sections(text, keywords):
#     doc = nlp(text)
#     relevant_sections = set()  # Using a set to avoid repetition
    
#     # Generate keyword pattern including both singular and plural forms
#     all_forms = []
#     for keyword in keywords:
#         singular, plural = get_singular_and_plural_forms(keyword)
#         all_forms.append(singular)
#         all_forms.append(plural)
    
#     keyword_pattern = re.compile(r'\b(?:' + '|'.join(re.escape(form) for form in all_forms) + r')\b', re.IGNORECASE)
    
#     # Split text into regulation sections
#     sections = text.split('\n\n')

#     for section in sections:
#         # Further split sections into individual points
#         points = re.split(r'(?<!\d)\.\s(?=[A-Z])', section)
#         for point in points:
#             # Check for keywords in each point
#             keyword_matches = keyword_pattern.findall(point)
#             if len(keyword_matches) >= 2:
#                 # Add the whole point to the set
#                 relevant_sections.add(point.strip())
#             elif len(keywords) <= 2 and len(keyword_matches) > 0:
#                 # If there are two or fewer keywords, add the point if it matches any keyword
#                 relevant_sections.add(point.strip())

#     return list(relevant_sections)





# ////// do not split sections further to check each individual point separately within a section.
def get_singular_and_plural_forms(word):
    """Generate both singular and plural forms of a word."""
    singular = p.singular_noun(word)
    plural = p.plural(word)
    
    if singular == False:  # The word is already singular
        singular = word
    if plural == word:  # The word is already plural
        plural = p.plural(word + 's')
    
    return singular, plural

def extract_relevant_sections(text, keywords):
    doc = nlp(text)
    relevant_sections = set()  # Using a set to avoid repetition
    
    # Generate keyword pattern including both singular and plural forms
    all_forms = []
    for keyword in keywords:
        singular, plural = get_singular_and_plural_forms(keyword)
        all_forms.append(singular)
        all_forms.append(plural)
    
    # Compile the keyword patterns
    keyword_patterns = [re.compile(r'\b' + re.escape(form) + r'\b', re.IGNORECASE) for form in all_forms]
    
    # Split text into regulation sections
    sections = text.split('\n\n')

    for section in sections:
        matches = sum(1 for pattern in keyword_patterns if pattern.search(section))
        if (len(keywords) <= 2 and matches > 0) or (len(keywords) > 2 and matches >= 2):
            # Add the whole section to the set
            relevant_sections.add(section.strip())

    return list(relevant_sections)

# Sample document text from repositories
text = """
 I. Regulations for Iodized Salt and Double Fortified Salt
1. Iodized Salt: When fortified with iodine, the iodine content must be between 15-30 parts per million (ppm) on a dry weight basis, sourced from potassium iodate.
2. Iron Fortified Iodized Salt (Double Fortified Salt): When fortified with both iron and iodine, the following conditions apply:
   a. Iodine content: 15-30 ppm on a dry weight basis, sourced from potassium iodate.
   b. Iron content (as Fe): 850-1100 ppm, sourced from ferrous sulphate or ferrous fumarate.

3. Additional Specifications:
   a. The total matter insoluble in water, with an added anticaking agent, shall not exceed 2.2%.
   b. Sodium chloride content on a dry basis shall not be less than 97.0% by weight, and it must conform to other parameters specified in clause (1) of sub-regulation 2.9.30 of the Food Safety and Standards (Food Product Standards and Food Additives) Regulations, 2011.
   c. Double fortified salt may contain Hydroxypropyl Methyl Cellulose, Titanium Dioxide, fully Hydrogenated Soybean Oil, and Sodium Hexametaphosphate (all food grade), and anticaking agents not exceeding 2.0% on a dry weight basis. The water-insoluble matter, when an anticaking agent is used, shall not exceed 2.2%.

II. Regulations for Fortified Oil
1. Vegetable oil, when fortified, shall contain the following micronutrients:
   a. Vitamin A: 6 µg RE - 9.9 µg RE per gram of oil, sourced from retinyl acetate or retinyl palmitate.
   b. Vitamin D: 0.11 µg - 0.16 µg per gram of oil, sourced from cholecalciferol or ergocalciferol (only from plant sources).

III. Regulations for Fortified Milk
1. Species-identified milk (buffalo, cow, goat, sheep, and camel milk), full cream milk, toned milk, double toned milk, skimmed milk, and standardized milk, when fortified, shall contain the following micronutrients:
   a. Vitamin A: 270-450 µg RE per liter, sourced from retinyl acetate or retinyl palmitate.
   b. Vitamin D: 5-7.5 µg per liter, sourced from cholecalciferol or ergocalciferol (only from plant sources).

IV. Regulations for Fortified Milk Powder
1. Fortified milk powder, when reconstituted, must comply with the micronutrient levels specified for fortified milk.
2. It shall only be used in Government Funded Programs for the preparation of reconstituted fortified milk.
3. The label of fortified milk powder must carry the following statements:
   a. Not recommended for direct consumption.
   b. Only for use under the specified Government Funded Programme.
   c. To be consumed only after reconstitution of the entire content as per the directions on the label.
   d. Pack once opened, to be consumed on the same day.

V. Regulations for Fortified Atta
1. Fortified atta shall contain added iron, folic acid, and Vitamin B-12 at the following levels:
   a. Iron: 28 mg-42.5 mg per kg (sourced from ferrous citrate, ferrous lactate, ferrous sulphate, ferric pyrophosphate, electrolytic iron, ferrous fumarate, or ferrous bisglycinate) or 14 mg-21.25 mg per kg (sourced from sodium iron (III) ethylene diamine tetraacetate trihydrate, Na Fe EDTA).
   b. Folic Acid: 75 µg-125 µg per kg.
   c. Vitamin B12: 0.75 µg-1.25 µg per kg (sourced from cyanocobalamin or hydroxycobalamin).
2. Fortified atta may also contain the following micronutrients:
   a. Zinc: 10 mg-15 mg per kg (sourced from zinc sulphate).
   b. Vitamin A: 500 µg RE-750 µg RE per kg (sourced from retinyl acetate or retinyl palmitate).
   c. Thiamine (Vitamin B1): 1 mg-1.5 mg per kg (sourced from thiamine hydrochloride or thiamine mononitrate).
   d. Riboflavin (Vitamin B2): 1.25 mg-1.75 mg per kg (sourced from riboflavin or riboflavin 5’-phosphate sodium).
   e. Niacin (Vitamin B3): 12.5 mg-20 mg per kg (sourced from nicotinamide or nicotinic acid).
   f. Pyridoxine (Vitamin B6): 1.5 mg-2.5 mg per kg (sourced from pyridoxine hydrochloride).

3. Multigrain atta containing more than 50% wheat flour may also be fortified at the same levels specified for fortified atta.

VI. Regulations for Fortified Maida
1. Fortified maida shall contain added iron, folic acid, and Vitamin B-12 at the following levels:
   a. Iron: 28 mg-42.5 mg per kg (sourced from ferrous citrate, ferrous lactate, ferrous sulphate, ferric pyrophosphate, electrolytic iron, ferrous fumarate, or ferrous bisglycinate) or 14 mg-21.25 mg per kg (sourced from sodium iron (III) ethylene diamine tetraacetate trihydrate, Na Fe EDTA).
   b. Folic Acid: 75 µg-125 µg per kg.
   c. Vitamin B12: 0.75 µg-1.25 µg per kg (sourced from cyanocobalamin or hydroxycobalamin).
2. Fortified maida may also contain the following micronutrients:
   a. Zinc: 10 mg-15 mg per kg (sourced from zinc sulphate).
   b. Vitamin A: 500 µg RE-750 µg RE per kg (sourced from retinyl acetate or retinyl palmitate).
   c. Thiamine (Vitamin B1): 1 mg-1.5 mg per kg (sourced from thiamine hydrochloride or thiamine mononitrate).
   d. Riboflavin (Vitamin B2): 1.25 mg-1.75 mg per kg (sourced from riboflavin or riboflavin 5’-phosphate sodium).
   e. Niacin (Vitamin B3): 12.5 mg-20 mg per kg (sourced from nicotinamide or nicotinic acid).
   f. Pyridoxine (Vitamin B6): 1.5 mg-2.5 mg per kg (sourced from pyridoxine hydrochloride).

VII. Regulations for Fortified Rice
1. Fortified rice shall contain added iron, folic acid, and Vitamin B-12 at the following levels:
   a. Iron: 28 mg-42.5 mg per kg (sourced from ferric pyrophosphate) or 14 mg-21.25 mg per kg (sourced from sodium iron (III) ethylene diamine tetraacetate trihydrate, Na Fe EDTA).
   b. Folic Acid: 75 µg-125 µg per kg.
   c. Vitamin B12: 0.75 µg-1.25 µg per kg (sourced from cyanocobalamin or hydroxycobalamin).
2. Fortified rice may also contain the following micronutrients:
   a. Zinc: 10 mg-15 mg per kg (sourced from zinc oxide).
   b. Vitamin A: 500 µg RE-750 µg RE per kg (sourced from retinyl palmitate).
   c. Thiamine (Vitamin B1): 1 mg-1.5 mg per kg (sourced from thiamine hydrochloride or thiamine mononitrate).
   d. Riboflavin (Vitamin B2): 1.25 mg-1.75 mg per kg (sourced from riboflavin or riboflavin 5’-phosphate sodium).
   e. Niacin (Vitamin B3): 12.5 mg-20 mg per kg (sourced from nicotinamide or nicotinic acid).
   f. Pyridoxine (Vitamin B6): 1.5 mg-2.5 mg per kg (sourced from pyridoxine hydrochloride).



I. Regulations for Fortified Cereal Products
1. Cereal products, including breakfast cereals, pasta, and noodles, when fortified, shall contain added iron, folic acid, and Vitamin B12 at the levels specified below:
   a. Iron: 1.4-2.7 mg per 100 g (sourced from ferrous citrate, ferrous lactate, ferrous sulphate, ferric pyrophosphate, electrolytic iron, ferrous fumarate, ferrous bisglycinate, or sodium iron (III) ethylene diamine tetraacetate trihydrate (Na Fe EDTA)).
   b. Folic Acid: 8-16 µg per 100 g.
   c. Vitamin B12: 0.08-0.16 µg per 100 g (sourced from cyanocobalamin or hydroxycobalamin).

2. Additionally, fortified cereal products may also contain the following micronutrients, singly or in combination:
   a. Zinc: 1.0-1.9 mg per 100 g (sourced from zinc sulphate).
   b. Vitamin A: 48-96 µg RE per 100 g (sourced from retinyl acetate or retinyl palmitate).
   c. Thiamine (Vitamin B1): 0.1-0.19 mg per 100 g (sourced from thiamine hydrochloride or thiamine mononitrate).
   d. Riboflavin (Vitamin B2): 0.11-0.22 mg per 100 g (sourced from riboflavin or riboflavin 5’-phosphate sodium).
   e. Niacin (Vitamin B3): 1.3-2.6 mg per 100 g (sourced from nicotinamide or nicotinic acid).
   f. Pyridoxine (Vitamin B6): 0.2-0.3 mg per 100 g (sourced from pyridoxine hydrochloride).

II. Regulations for Fortified Bakery Wares
1. Bakery wares, including bread, biscuits, rusks, and buns, when fortified, shall contain added iron, folic acid, and Vitamin B12 at the levels specified below:
   a. Iron: 1.4-2.7 mg per 100 g (sourced from ferrous citrate, ferrous lactate, ferrous sulphate, ferric pyrophosphate, electrolytic iron, ferrous fumarate, ferrous bisglycinate, or sodium iron (III) ethylene diamine tetraacetate trihydrate (Na Fe EDTA)).
   b. Folic Acid: 8-16 µg per 100 g.
   c. Vitamin B12: 0.08-0.16 µg per 100 g (sourced from cyanocobalamin or hydroxycobalamin).

2. Additionally, fortified bakery wares may also contain the following micronutrients, singly or in combination:
   a. Zinc: 1.0-1.9 mg per 100 g (sourced from zinc sulphate).
   b. Vitamin A: 48-96 µg RE per 100 g (sourced from retinyl acetate or retinyl palmitate).
   c. Thiamine (Vitamin B1): 0.1-0.19 mg per 100 g (sourced from thiamine hydrochloride or thiamine mononitrate).
   d. Riboflavin (Vitamin B2): 0.11-0.22 mg per 100 g (sourced from riboflavin or riboflavin 5’-phosphate sodium).
   e. Niacin (Vitamin B3): 1.3-2.6 mg per 100 g (sourced from nicotinamide or nicotinic acid).
   f. Pyridoxine (Vitamin B6): 0.2-0.3 mg per 100 g (sourced from pyridoxine hydrochloride).

III. Regulations for Fortified Fruit Juices
1. Fruit juices, when fortified, shall contain Vitamin C at the level specified below:
   a. Vitamin C: 6-12 mg per 100 mL (sourced from ascorbic acid).

Note: The principal regulations were published in the Gazette of India, Extraordinary, Part III, Section 4, vide notification number File No. 11/03/Reg/Fortification/2014, dated the 21st August, 2018, and subsequently amended.

"""

# Extract relevant sections based on keywords
relevant_sections = extract_relevant_sections(text, keywords)

# Print the relevant sections
for section in relevant_sections:
    print(section + "\n")
