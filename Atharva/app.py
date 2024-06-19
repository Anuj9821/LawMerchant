import spacy

# Load the large English language model
nlp = spacy.load('en_core_web_lg')

def extract_proper_nouns(text):
    # Process the text with spaCy
    doc = nlp(text)
    
    # Extract proper nouns (PROPN)
    proper_nouns = [token.text for token in doc if token.pos_ == "PROPN"]
    
    return proper_nouns

text_content = """
PART- 1 Preliminary

Regulation 1.1 Short title, application and commencement:
(1) These regulations may be called the Food Safety and Standards (Alcoholic Beverages) Regulations, 2018.  
(2) The standards specified in these regulations shall apply to distilled and un-distilled alcoholic beverages.  
(3) They shall come into force on the date of their publication in the Official Gazette and Food Business Operator shall comply with all the provisions of these regulations by 1st April, 2019.  

Regulation 1.2 Definitions:  
In these regulations, unless the context otherwise requires:  

Regulation 1.2.1: “Act” means Food Safety and Standards Act, 2006(34 of 2006);  
Regulation 1.2.2: “alcohol by volume (abv)” means ethyl alcohol (ethanol) content in an alcoholic beverage expressed as per cent. of total volume;  
Regulation 1.2.3: “alcoholic beverage” means a beverage or a liquor or a brew containing more than 0.5 per cent. abv. The ethanol used in the production of alcoholic beverage shall be of agricultural origin;  
Regulation 1.2.4: “alcohol proof” means 1.75131 times the ethanol content in an alcoholic beverage by volume;  
Regulation 1.2.5: “distilled alcoholic beverage” means a distilled beverage, spirit, or liquor containing ethanol that is made by distilling ethanol produced by fermentation of cereal grains, fruits, vegetables, molasses or any other source of carbohydrates of agricultural origin;  
Regulation 1.2.6: “ethyl alcohol or ethanol” means a transparent, colourless, flammable, volatile liquid miscible with water, ether or chloroform and obtained by the fermentation of carbohydrates with yeast. Ethyl alcohol has the chemical formula C2H5OH, has a burning taste, and causes intoxication on consumption;  
Regulation 1.2.7: “hops” means the female flowers or seed cones or strobiles of the hop plant (Humuluslupulus), or its products used to impart a bitter taste or flavour to beer;  
Regulation 1.2.8: “methyl alcohol or methanol” means a clear, colourless, flammable liquid having chemical formula, CH3OH, consumption of which above the specified limits may cause blindness or death;  
Regulation 1.2.9: “neutral spirit or neutral alcohol or neutral grain spirit or pure grain alcohol or extra neutral alcohol (ENA)” means a product obtained by distillation and rectification, with a minimum alcoholic strength of 96 per cent. abv, after alcoholic fermentation of cereal grains, fruits, vegetables, molasses or any other source of carbohydrates of agricultural origin;  
Regulation 1.2.10: “pot-still or column distilled spirit” means the product of distillation done either in a pot-still in batches, or in continuous columns;  
Regulation 1.2.11: “psychotropic substance” means substance as defined in the Schedule of the Narcotic Drugs and Psychotropic Substances Act, 1985 (61 of 1985) and rules made thereunder, and substances listed in Schedule E and E1 of the Drugs and Cosmetic Rules, 1945;  
Regulation 1.2.12: “rectified spirit” means spirit purified by distillation to achieve strength of not less than 95 per cent.abv;  
Regulation 1.2.13: “standard” means as defined in the Act;  
Regulation 1.2.14: “table” means the tables appended to these regulations;  
Regulation 1.2.15: “un-distilled alcoholic beverage or fermented beverage” means fermented un-distilled alcoholic beverage such as beer, wine, cider, or any other similar products;  
Regulation 1.2.16: “yeast” means a unicellular micro-organism responsible for fermentation of sugars to produce ethanol and carbon dioxide.  

Regulation 1.3 General requirements:  
Regulation 1.3.1: Alcoholic beverages shall be free from chloral hydrate, ammonium chloride, paraldehyde, pyridine, diazepam or narcotic, psychotropic substances including caffeine except naturally-occurring caffeine.  
Regulation 1.3.2: The tolerance limit for ethyl alcohol content shall be ± 0.3 per cent (± 0.5 in case of wines) for upto 20 per cent, and ±1.0 per cent for more than 20 per cent abv of the declared strength.  
Regulation 1.3.3: Sugar may be added for rounding off of the alcoholic beverage.  
Regulation 1.3.4: The water used for dilution to bottling strength shall meet the requirements as specified in Indian Standards for Drinking Water, IS:10500 as amended from time to time.  
Regulation 1.3.5: Alcoholic beverage may contain additives, enzymes and processing aids as permitted under the Food Safety and Standards (Food Products Standards and Food Additives) Regulations, 2011.  
Regulation 1.3.6: Any alcoholic beverage when labelled as "matured”, shall be matured for a period of not less than one year in oak or other suitable wood vats or barrels or with wooden chips.  
Regulation 1.3.7: Where an age claim is made in conjunction with the word “aged”, the age must refer to the youngest spirit in the blend.  
Regulation 1.3.8: The test methods prescribed in the FSSAI “Manual of Methods of Analysis of Foods-Alcoholic Beverages” as amended from time to time shall be used for analysis.  
Regulation 1.3.9: Alcoholic beverage shall be packed in suitable containers as specified in the Food Safety and Standards (Packaging and Labelling) Regulations, 2011:  
Provided that bulk containers shall have no upper limit for alcohol content, and shall meet the safety parameters of the product standards. Such products shall also carry a label declaring, “For Manufacturer of Alcoholic Beverages only”.  
Alcoholic beverage containing not more than 8.0 per cent. abv may be called as low alcoholic beverage, and shall conform to the requirements of table 1 except for residue on evaporation.  

Regulation 1.4: The words and expressions used but not defined in these regulations shall have the same meaning assigned to them in the Act and the rules made thereunder.  

Part 2 Distilled Alcoholic Beverages

Regulation 2.1 Brandy:  
Brandy is an alcoholic beverage made by distillation of wine. Brandy may be aged or matured to possess aroma and taste characteristic of brandy. Brandy may be of the following types:  

Regulation 2.1.1 Grape brandy: Grape brandy shall be an alcoholic distillate obtained solely from the fermented juice of grapes. Distillation shall be carried out to a suitable strength in such a way that the distillate has an aroma and taste characteristics derived from the grapes used and the constituents formed during fermentation.  
In case of brandy made from any fruit other than grapes, the name of the fruit shall be pre-fixedwith the word ‘Brandy’.  

Regulation 2.1.2 Blended brandy: Blended brandy is a mixture of minimum 2 per cent. of pure grape brandy with any other fruit or flower brandy or neutral spirit or rectified spirit of agricultural origin. If any other fruit brandy is used for blending, the name of such fruit shall be pre-fixed with the word ‘Brandy’. It shall possess the characteristic aroma and taste of brandy.  
The Brandy shall also conform to the general requirement specified in Part 1 and requirements specified in Table – 1.  

Regulation 2.2 Country liquors: 
Country liquors or spirits are alcoholic beverages obtained from distillation

 of fermented broth. Country liquors are either distilled alcoholic beverage made in wooden pot-still or column still. Country liquors are further categorised as Plain Country Liquor and Blended Country Liquor. The products shall conform to the general requirement specified in Part 1 and requirements specified in Table 1.  

Regulation 2.2.1: Plain Country Liquor is distilled alcoholic beverage made in wooden pot-still and/or column still from fermentation of molasses or from any carbohydrate of agricultural origin. The plain country liquor shall have the taste and characteristic aroma of the originating material.  

Regulation 2.2.2: Blended Country Liquor is a blend of 1.0 per cent of matured spirit of 3 years or more maturity with rectified spirit of agricultural origin, plain country liquor or neutral spirit, with or without caramel.  

Regulation 2.3 Fenny or Feni: 
Fenny or Feni is an alcoholic beverage made by distillation of fermented juice of cashew apple (Anacardium occidentale) or from coconut toddy. The products shall conform to the general requirement specified in Part 1 and requirements specified in Table – 1.  

Regulation 2.4 Gin: 
Gin is an alcoholic beverage made by distillation of a fermented mash of malt or grain and/or neutral alcohol of agricultural origin and/or in such a manner that the distillate is flavoured with juniper berries (Juniperus communis L.) and/or other aromatics and/or other flavouring substances.  
Gin may be of two types- Distilled Gin and London Gin. Gin shall also conform to the general requirement specified in Part 1 and the requirements specified in Table – 1.  

Regulation 2.4.1 Distilled gin: Distilled gin shall be produced by redistilling ethanol of agricultural origin with an initial strength of minimum 96 percent abv in the presence of juniper berries (Juniperus communis L.) and other natural botanicals, where the juniper taste is predominant.  

Regulation 2.4.2 London gin: London gin is a type of distilled gin and shall be produced exclusively from ethanol of agricultural origin with a maximum methanol content of 5 grams per hectolitre of 100 percent abv equivalent, whose flavour is introduced exclusively through the redistillation in traditional stills of ethanol in the presence of all the natural plant materials used.  

Regulation 2.5 Rum: 
Rum is an alcoholic distillate from the fermented juice of sugarcane, sugarcane syrup, sugarcane molasses or other sugarcane by-products, and shall possess the characteristic aroma and taste of rum. It shall be of two types, plain and matured rum. Rum shall also conform to the general requirement specified in Part 1 and the requirements specified in Table – 1.  

Regulation 2.5.1 Plain rum: Plain rum is an alcoholic beverage made from the distillate of fermented molasses with or without caramel.  

Regulation 2.5.2 Matured rum: Matured rum is rum aged for not less than one year in oak or other suitable wooden cask and with or without the addition of caramel.  

Regulation 2.6 Vodka:  
Vodka is a potable alcoholic beverage made from rectified spirit or neutral alcohol of agricultural origin with or without characteristic taste, aroma and flavour. It shall be of the following two types: Plain Vodka and Flavoured Vodka. It shall also conform to the general requirements specified in Part 1 and the requirements specified in Table – 1.  

Regulation 2.6.1 Plain Vodka: Plain Vodka is a colourless neutral alcoholic beverage without definite aroma or taste, and free from flavouring substances except permitted additives.  

Regulation 2.6.2 Flavoured Vodka: Flavoured Vodka is a potable alcoholic beverage made from plain vodka with natural flavouring substances conforming to the requirements of the Food Safety and Standards (Food Products Standards and Food Additives) Regulations, 2011.  

Regulation 2.7 Liqueur or Cordial or Aperitifs:  
Liqueur or Cordial or Aperitifs are potable alcoholic beverages made from distilled spirit or neutral alcohol of agricultural origin, flavoured with natural ingredients like fruit juices, fruit peels, herbs, spices, and other plant materials, with or without the addition of sugar, dextrose, laevulose, or other natural sweeteners. These products shall conform to the general requirements specified in Part 1 and the requirements specified in Table 1.  

Regulation 2.8 Whisky:  
Whisky is an alcoholic distillate obtained from the fermented mash of malted and/or unmalted cereals or grains with or without added flavouring, and aged in oak or other suitable wooden casks for a period of not less than one year. The whisky shall possess the characteristic aroma and taste of whisky. It shall also conform to the general requirements specified in Part 1 and the requirements specified in Table – 1.  

Part 3 Wine and Other Fermented Beverages

Regulation 3.1 Wine:  
Wine is the alcoholic beverage obtained by fermentation of freshly crushed grapes or fruit juices or concentrates. It includes Table Wine, Sparkling Wine, Fortified Wine, and Aromatized Wine. It shall conform to the general requirements specified in Part 1 and the requirements specified in Table – 2.  

Regulation 3.2 Fruit Wine:  
Fruit Wine is an alcoholic beverage obtained by fermentation of the juice of fruit other than grapes. It includes Cider, Perry, and other similar beverages. It shall conform to the general requirements specified in Part 1 and the requirements specified in Table – 2.  

Regulation 3.3 Wine from Other Agricultural and Plant Sources: 
This includes wines made from sources such as palm sap, bamboo sap, and other plant materials. It shall conform to the general requirements specified in Part 1 and the requirements specified in Table – 2.  

Part 4 Beer

Regulation 4.1 Beer:  
Beer is a fermented alcoholic beverage made from malted barley and other cereal grains, hops, and water. Beer may be of different types based on alcohol content and fermentation process, including Lager, Ale, Stout, Porter, and Wheat Beer. It shall conform to the general requirements specified in Part 1 and the requirements specified in Table – 3.  

Regulation 4.2 Draught Beer: 
Draught Beer is beer served from a pressurised keg or cask and is typically unpasteurised. It shall conform to the general requirements specified in Part 1 and the requirements specified in Table – 3.  

Part 5 Specific Labelling Requirements

Regulation 5.1 Alcohol Content Declaration:  
The label of an alcoholic beverage shall declare the alcohol content as per cent abv or as proof.  

Regulation 5.2 Standard Drink Labelling:  
The label shall indicate the approximate number of standard drinks contained in the package.  

Regulation 5.3 Geographical Indicators:  
Labels may include geographical indicators subject to relevant laws and conditions.  

Regulation 5.4 Imported Beverages: 
Imported alcoholic beverages shall comply with the Food Safety and Standards (Import) Regulations, 2017.  

Regulation 5.5 Nutritional Information and Health Claims:  
No nutritional information or health claims shall be made on the label of an alcoholic beverage.  

Regulation 5.6 Non-Intoxicating Terminology: 
No terms such as "non-intoxicating" shall be used for beverages containing more than 0.5% abv.  

Regulation 5.7 Allergen Warnings:  
Labels must include allergen warnings for the presence of sulfur dioxide and processing aids of animal origin in wine.


"""

if __name__ == "__main__":
    proper_nouns = extract_proper_nouns(text_content)
    
    print("Extracted Proper Nouns:")
    for noun in proper_nouns:
        print(noun)
