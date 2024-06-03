import spacy

# Load the spaCy large model
nlp = spacy.load('en_core_web_lg')

# Define the keywords related to the product
keywords = ['fruit']

# Function to extract relevant sentences
def extract_relevant_sentences(doc, keywords):
    relevant_sentences = []
    for sentence in doc.sents:
        if any(keyword.lower() in sentence.text.lower() for keyword in keywords):
            relevant_sentences.append(sentence.text)
    return relevant_sentences

# Sample document text
text = """
10 THE GAZETTE OF INDIA : EXTRAORDINARY [PART III—SEC. 4]
MINISTRY OF HEALTH AND FAMILY WELFARE
(Food Safety and Standards Authority of India)
Notification
 New Delhi, dated the 1st August, 2011
F.No. 2-15015/30/2010 Whereas in exercise of the powers conferred by clause (l) of subsection (2) of section 92 read with
section 26 of Food Safety and Standards Act, 2006 (34 of 2006) the Food Safety and Standards Authority of India proposes
to make Food Safety and Standards Regulations in so far as they relates to Food Safety and Standards (Prohibition and
Restrictions on sales) Regulations, 2011, and;
 Whereas these draft Regulations were published in consolidated form at pages 1 to 776 in the Gazette of India
Extraordinary Part III – Sec. 4 dated 20th October 2010 inviting objections and suggestions from all persons likely to be
affected thereby before the expiry of the period of thirty days from the date on which the copies of the Gazette containing
the said notification were made available to the public;
And whereas the copies of the Gazette were made available to the public on the 21st October 2010;
And whereas objections and suggestions received from the stakeholders within the specified period on the said
draft Regulations have been considered and finalized by the Food Safety and Standards Authority of India.
Now therefore, the Food Safety and Standards Authority of India hereby makes the following Regulations, namely,—
FOOD SAFETY AND STANDARDS (PROHIBITION AND RESTRICTIONS ON SALES) REGULATIONS, 2011
CHAPTER 1
GENERAL
1.1: Title and commencement1.1.1: These regulations may be called the Food Safety and Standards (Prohibition and Restrictions on sales)
Regulations, 2011.
1.1.2: These regulations shall come into force on or after 5th August, 2011.
1.2: DefinitionsIn these regulations unless the context otherwise requires:
1. “ingredient” means any substance, including a food additive used in the manufacture or preparation of
food and present in the final product, possibly in a modified form;
CHAPTER 2
PROHIBITION AND RESTRICTIONS ON SALES
2.1 Sale of certain admixtures prohibited
2.1.1 Notwithstanding the provisions of 2.7 of labelling and packaging regulations no person shall either by himself
or by any servant or agent sell—
(1) cream which has not been prepared exclusively from milk or which contains less than 25 per cent. of milk
fat;
(2) milk which contains any added water;
(3) ghee which contains any added matter not exclusively derived from milk fat;
(4) skimmed milk (fat abstracted) as milk;
(5) a mixture of two or more edible oils as an edible oil;
(6) vanaspati to which ghee or any other substance has been added;
(7) turmeric containing any foreign substance;
(8) mixture of coffee and any other substance except chicory;
(9) dahi or curd not prepared from boiled, pasteurised or sterilized milk;
¹Hkkx III—[k.M 4º Hkkjr dk jkti=k % vlk/kj.k 11
(10) milk or a milk product specified in Food Safety and Standards (Food Products Standards and Food
Additives) regulations, 2011 containing a substance not found in milk, except as provided in the regulations.
Provided that the Central Government or the Food Authority may, by notification in the Official Gazette exempt
any preparations made of soluble extracts of coffee from the operation of this regulation.
Provided further that proprietary food articles relating to Regulation 2.1.1(8) shall be exempted from the
operation of this Regulation
Provided further that in respect of regulation 2.1.1(5), a maximum tolerance of 15.0 red units in 1 cm. Cell of
Lovibond scale is permitted when oil is tested for Boudouin test without dilution that is to say by shaking vigorously
for 2 minutes, 5 ml. Of the sample with 5 ml. of the hydrochloric acid (specific gravity 1.19) and 0.3 ml. of 2 percent
alcoholic solution of furfural and allowing to standing for 5 miutes.
Provided further that in respect of Regulation 2.1.1(5) a maximum tolerance limit of 10 red units in one cm. cell
on Lovibond scale is permitted when the oil is tested for Halphen’s test without dilution, that is to say, by shaking
5 ml. of the sample with 5 ml. of sulphur solution (one per cent (w/v) solution of sulphur in carbon-di-sulphide mixed
with equal volume of amyl alcohol), in a closed system (test tube 250 x 25 Cm.) heating in hot water (700
C- 80°C) for
a few minutes with occasional shaking until carbon-di-sulphide is boiled off and the sample stops foaming and then
placing the tube on saturated brine bath, capable of being regulated at 1100
C-1150
C for 2.5 hours
Provided also that prohibition in Regulation 2.1.1 (5) shall remain inoperative in respect of admixture of any
two edible vegetable oils as one edible vegetable oil, where –
(a) the proportion by weight of any vegetable oil used in the admixture is not less than 20 per cent. by
weight; and
(b) the admixture of edible vegetable oils, is processed or packed and sold, by the Department of Civil
Supplies, Government of India (Directorate of Vanaspati, Vegetable Oils and Fats) or by the agencies in
public, private or Joint Sector authorized by the Department, or by the National Dairy Development Board or
by the State Cooperative Oilseeds Growers Federation or Regional and District Cooperative Oilseeds Growers
Union set up under National Dairy Development Board’s Oilseeds and Vegetable Oil Project or by the Public
Sector undertakings of Central and State Governments, in sealed packages weighing not more than 15 litres
under Agmark Certification Mark compulsorily and bearing the label declaration as laid down in the Regulation
2.4.2 (11) of Food Safety and Standards (Packaging and Labelling) Regulations, 2011 and
(c) the quality of each edible oil used in the admixture conforms to the relevant standard prescribed by
these regulations.
2.2: Restriction on use of certain ingredient:
2.2.1: No person in any State shall, with effect from such date as the state government concerned may by
notification in the official gazette specify in this behalf, sell or offer or expose for sale, or have in his possession for
the purpose of sale, under any description or for use as an ingredient in the preparation of any article of food
intended for sale:—
(a) Kesari gram (Lathyrus sativus) and its products.
(b) Kesari dal (Lathyrus sativus) and its products.
(c) Kesari dal flour (Lathyrus sativus) and its products.
(d) A mixture of Kesari gram (Lathyrus sativus) and Bengal-gram (Cicer arietinum) or any other gram.
(e) A mixture of Kesari dal (Lathyrus sativus) and Bengal-gram dal (Cicer arietinum) or any other dal.
(f) A mixture of Kesari dal (Lathyrus sativus) flour and Bengal-gram (Cicer arietinum) flour or any other
flour.
Explanation.—The equivalent of kesari gram in some of the Indian Languages are as follows:—
1. Assamese Khesari, Teora.
2. Bengali Khesari, Teora, Kassur, Batura.
3. Bihari Khesari, Teora, Kassur, Batura.
4. English Chikling vetch.
5. Gujarati Lang.
12 THE GAZETTE OF INDIA : EXTRAORDINARY [PART III—SEC. 4]
6. Hindi Khesari, Kessur, Kesari, Kassartiuri,Batura, Chapri, Dubia, Kansari, Kesori, Latri, Tinra,
Tiuri, Kassor.
7. Kannada Laki Bele, Kessari Bele.
8. Malyalam Kesari, Lanki, Vattu.
9. Tamil Muku.
10. Marathi Lakheri, Batri, Lakhi, Lang, Mutra, Teora, Botroliki-dal, Lakh.
11. Oriya Khesra, Khesari, Khesari dal.
12. Persian Masang.
13. Punjabi Kisari, Chural, Karas, Karil, Kasa Kesari, Chapa.
14. Sanskrit Sandika, Triputi.
15. Sindhi Matter.
16. Telugu Lamka
2.3 Prohibition and Restriction on sale of certain products
2.3.1: Prohibition on sale of food articles coated with mineral oil: No person shall sell or offer or expose for sale or
have in his premises for the purpose of sale under any description, food articles which have been coated with mineral oil,
except where the addition of mineral oil is permitted in accordance with the standards laid down in these Regulations and
Food Safety and Standards (Food Products Standards and Food Additives) regulations, 2011.
2.3.2: Restriction on sale of Carbia Callosa and Honey dew.:Carbia Callosa and Honey dew shall be sold only in
sealed containers bearing Agmark seal.
2.3.3: Food resembling but not pure honey not be marketed as honey: No person shall use the word ‘honey’ or any
word, mark, illustration or device that suggests honey on the label or any package of, or in any advertisement for, any food
that resembles honey but is not pure honey.
2.3.4: Product not to contain any substance which may be injurious to health: Tobacco and nicotine shall not be
used as ingredients in any food products.
2.3.5: Prohibition of use of carbide gas in ripening of fruits: No person shall sell or offer or expose for sale or have in
his premises for the purpose of sale under any description, fruits which have been artificially ripened by use of acetylene
gas, commonly known as carbide gas.
2.3.6: Sale of Fresh Fruits and Vegetables: The Fresh Fruits and Vegetables shall be free from rotting and free from
coating of waxes, mineral oil and colours.
Provided that fresh fruits may be coated with bees wax (white and yellow) or carnauba wax or shellac wax at level not
exceeding Good Manufacturing Practices under proper label declaration as provided in Regulation 2.4.5 (44) of Food
Safety and Standards (Packaging and Labelling) regulations, 2011.
2.3.7: Sale or use for sale of admixtures of ghee or butter prohibited: No person shall sell or have in his possession
for the purpose of sale or for use as an ingredient in the preparation of an article of food for sale a mixture of ghee or butter
and any substance
(1) prepared in imitation of or as a substitute for ghee or butter, or
(2) consisting of or containing any oil or fat which does not conform to the definition of ghee;
Provided that where a mixture prohibited by this regulation is required for the preparation of an article of food,
such mixture shall be made only at the time of the preparation of such article of food.
2.3.8: Restriction on sale of ghee having less Reichert value than that specified for the area where such ghee is sold.
(1) The ghee having less Reichert value and a different standard for Butyro-refractometer reading at 400
 C than
that specified for the area in which it is imported for sale or storage shall not be sold or stored in that area except
under the ‘AGMARK’ seal:
Provided that such ghee may be (i) sold lose, after opening the ‘AGMARK’ sealed container, in quantities not
exceeding two kilograms at a time, and (ii) used in the preparation of confectionery (including sweetmeats).
¹Hkkx III—[k.M 4º Hkkjr dk jkti=k % vlk/kj.k 13
(2) A person selling:—
(i) ghee in such manner as specified in Regulation 2.3.8 (1) and
(ii) confectionery (including sweetmeats) in the preparation of which such ghee is used, shall give a
declaration, in the Form A, to the Food Safety Officer when a sample thereof is taken by him for analysis under
Section 47 of the Act and also to a purchaser desiring to have the sample analysed under Section 40 of the Act.
(iii) If on analysis such sample is found to be conforming to the standards of quality prescribed for the
area where it is alleged to have been produced, the ghee shall not be deemed to be adulterated by reason only
that it does not conform to the standards of quality prescribed for the area where it is sold.
2.3.9 : Restriction on sale of Til Oil produced in Tripura, Assam and West Bengal.
Til Oil (Sesame Oil) obtained from white sesame seeds, grown in Tripura, Assam and West Bengal having
different standards than those specified for til oil shall be sold in sealed containers bearing Agmark label. Where this
til oil is sold or offered for sale without bearing an Agmark label, the standard given for til oil shall apply.
2.3.10 Restriction on sale of Kangra tea.
Kangra tea shall be sold or offered for sale only after it is graded and marked in accordance with the provisions
of the Agricultural Produce (Grading and Marking) Act, 1937 (1 of 1937) and the regulations made there under.
2.3.11: Condition for sale of flavoured tea: Flavoured tea shall be sold or offered for sale only by those manufacturers
who are registered with Tea Board. Registration number shall be mentioned on the label. It shall be sold only in packed
conditions with label declaration as provided in the Regulation 2.4.5 (23) of Food Safety and Standards (Packaging and
Labelling) regulations, 2011.
2.3.12: Restriction on sale of common salt – No person shall sell or offer or expose for sale or have in his premises for
the purpose of sale, the common salt, for direct human consumption unless the same is iodized:
Provided that common salt may be sold or exposed for sale or stored for sale for iodization, iron fortification,
animal use, preservation, manufacturing medicines, and industrial use, under proper label declarations, as specified
in the Regulation 2.4.5 (21 & 42) of Food Safety and Standards (Packaging and Labelling) regulations, 2011.
2.3.13: Use of flesh of naturally dead animals or fowls prohibited.
No person shall sell or use as an ingredient in the preparation of any article of food intended for sale, the flesh
of any animal or fowl which has died on account of natural causes.
2.3.14: Restrictions relating to conditions for sale
(1) No person shall store, expose for sale or permit the sale of any insecticide in the same premises where
articles of food are stored, manufactured or exposed for sale:
Provided that nothing in this regulation shall apply to the approved household insecticides which have been
registered as such under the Insecticides Act 1968 (46 of 1968).
Explanation.—For the purpose of this regulation, the word ‘insecticide’ has the same meaning as assigned to
it in the Insecticides Act, 1968 (46 of 1968).
(2) No person shall sell or serve food in any “commercial establishment” in plastic articles used in catering and
cutlery, unless the plastic material used in catering and cutlery articles, conform to the food grade plastic, specified
in these regulations.
Explanation:- For the purpose of the Regulation 2.3.14 (2), “commercial establishment” means any establishment,
called by whatever name, being run\ managed by any person or by any authority of the Government\ Semi-Government
or by any corporate\ registered body which deals in the business of selling or serving food.
(3) Iron fortified common salt shall be sold only in high density polyethylene bag (HDPE) 14 mesh, density
100 kg/m3
, unlaminated package which shall bear the lable as specified in the Regulation 2.4.5 (21 & 42) of Food
Safety and Standards (Packaging and Labelling) regulations, 2011.
14 THE GAZETTE OF INDIA : EXTRAORDINARY [PART III—SEC. 4]
(4) No person shall manufacture, sell, store or exhibit for sale, an infant milk food, infant formula and milk cereal
based weaning food, processed cereal based weaning food and follow up formula except under Bureau of Indian
Standards Certification Mark.
(5) Condensed milk sweetened, condensed skimmed milk sweetened, milk powder, skimmed milk powder,
partly skimmed milk powder and partly skimmed sweetened condensed milk shall not be sold except under Indian
Standards Institution Certification Mark.
(6) Every package of cheese (hard), surface treated with Natamycin, shall bear the label as specified in the
Regulation 2.4.5 (33) of Food Safety and Standards (Packaging and Labelling) regulations, 2011.
(7) No person shall sell protein rich atta and protein rich maida except in packed condition mentioning the
names of ingredients on the label.
(8) No person shall sell sal-seed fat for any other purpose except for bakery and confectionery and it shall be
refined and shall bear the label declaration as specified in the Regulation 2.4.5 (19) of Food Safety and Standards
(Packaging and Labelling) regulations, 2011.
(9) No person shall sell confectionery weighing more than 500 gms. except in packed condition and confectionery
sold in pieces shall be kept in glass or other suitable containers.
Explanation.—for the purposes of regulation 2.3.14 (9) “Confectionery, shall mean sugar boiled confectionery,
lozenges and chewing gum and bubble gum”;
(10) All edible oils, except coconut oil, olive oil, imported in crude, raw or unrefined form shall be subjected to
the process of refining before sale for human consumption. Such oil shall bear a label declaration as laid down in the
Regulation 2.4.2 of Food Safety and Standards (Packaging and Labelling) regulations, 2011.
(11) The Blended Edible Vegetable Oils shall not be sold in loose form. It shall be sold in sealed package
weighing not more than 15 litres. The container having blended edible vegetable oil shall be tamper proof. It shall
also not be sold under the common or generic name of the oil used in the blend but shall be sold as “Blended Edible
Vegetable Oil”. The sealed package shall be sold or offered for sale only under AGMARK certification mark bearing
the label declarations as provided in the Regulations besides other labelling requirements under the Regulation
2.4.2 of Food Safety and Standards (Packaging and Labelling) regulations, 2011.
(12) Coloured and flavoured table margarine shall only be sold in a sealed package weighing not more than 500
gms, with a label declaring addition of colour and flavour as required under these regulations.
(13) The fat spread shall not be sold in loose form. It shall be sold in sealed packages weighing not more than
500 gms. The word ‘butter’ shall not be associated while labelling the product. The sealed package shall be sold or
offered for sale only under AGMARK Certification mark bearing the label declaration as provided under Regulation
2.4.2 of Food Safety and Standards (Packaging and Labelling) regulations, 2011 beside other labelling requirements
under these regulations.
(14) No person shall sell compounded asafoetida exceeding one kilogram in weight except in a sealed container
with a label.
(15) No person shall sell powdered spices and condiments except ‘under packed conditions.
Explanation:— For the purpose of regulation 2.3.14 (15) “Spices and Condiments” means the spices and
condiments as specified in 2.9 of Food Safety and Standards (Food Products Standards and Food Additives)
Regulations, 2011.
(16) The katha prepared by bhatti method shall be conspicuously marked as “Bhatti Katha”
(17) No person shall manufacture, sell or exhibit for sale packaged drinking water except under the Bureau of
Indian Standards Certification Mark.
(18) No person shall manufacture, sell or exhibit for sale mineral water except under the Bureau of Indian
Standards Certification Mark”;
Explanation:— For the purpose of regulation 2.3.14 (18), the expression “mineral water” shall have the same
meaning as assigned to it in the Regulation 2.9.7 of Food Safety and Standards (Food Products Standards and Food
Additive) Regulations, 2011.
(19) No person shall sell any food product wherein artificial sweetener is permitted under these regulations,
except under packed condition and as per the labelling requirements prescribed under the regulation 2.4.5 (24, 25, 26,
28 & 29) of Food Safety and Standards (Packaging and Labelling) regulations, 2011.
¹Hkkx III—[k.M 4º Hkkjr dk jkti=k % vlk/kj.k 15
(20) Conditions for sale of irradiated food.- All irradiated food shall be sold in pre-packed conditions only. The
type of packaging material used for irradiated food for sale or for stock for sale or for exhibition for sale or for storage
for sale shall conform to the packaging and labelling requirements specified in the regulation 2.4.4 of Food Safety
and Standards (Packaging and Labelling) regulations, 2011.
2.3.15: Special provisions relating to sale of vegetable oil and fat
(1) No person shall sell or expose for sale, or distribute, or offer for sale, or dispatch, or deliver to any person for the
purpose of sale any edible oil –
(a) Which does not conform to the standards of quality as provided in the Food Safety and Standards Act,
2006 (34 of 2006) and rules/regulations made there under; and
(b) Which is not packed in a container, marked and labelled in the manner as specified in FSSAI regulations
Provided that the State Government may, in the public interest, for reasons to be recorded in writing, in
specific circumstances and for a specific period by a notification in the Official Gazette, exempt any edible oil from
the provisions of this Act.
(2) No vegetable oil shall contain any harmful colouring, flavouring or any other matter deleterious to health;
(3) No vegetable oil other than those specified under the list below or oil or fat of animal or mineral origin shall be
used in the manufacture of the products or shall otherwise be present therein;
List of vegetable oils Vanaspati shall be prepared from:
(a) Coconut oil
(b) Cottonseed oil
(c) Dhupa oil
(d) Groundnut oil
(e) Kokrum oil
(f) Linseed oil
(g) Mahua oil
(h) Maize (Corn) oil
(i) Mango kernel oil
(j) Mustard/Rapeseed oil
(k) Nigerseed oil
(l) Palm oil
(m) Phulwara oil
(n) Rice bran oil
(o) Sunflower (Kard/seed) oil
(p) Salseed oil (up to 10%)
(q) Sesame oil
(r) Soyabean oil
(s) Sunflower oil
(t) Watermelon seed oil
(u) Vegetable oils imported for edible purposes.
(4) No colour shall be added to hydrogenated vegetable oil unless so authorized by Food Authority, but in no event
any colour resembling the colour of ghee shall be added. If any flavour is used, it shall be distinct from that of ghee, in
accordance with a list of permissible flavours and such quantities as may be prescribed by the Food Authority
(5) No anti-oxidant, synergist, emulsifier or any other such substance other than those permitted by these regulations
be added to any vegetable oil except with the prior sanction of the Food Authority.
(6) Restriction on the use of solvent.
16 THE GAZETTE OF INDIA : EXTRAORDINARY [PART III—SEC. 4]
No solvent other than n-Hexane (Food Grade) shall be used in the extraction of cocoa butter, oils and fats and edible
soya flour.
The quantity solvent mentioned in the column (1) of the Table below, in the food mentioned in column (2) of
the said Table, shall not exceed the tolerance limits prescribed in column (3) of the said Table:
Name of Solvent Article of food Tolerance limits mg/kg (ppm)
Hexane (Food Grade) (a) Refined solvent extracted cocoa butter 5.00
(b) Refined solvent extracted oils and fats 5.00
(c) solvent extracted edible soya flour 10.00
FORM A
(Refer Regulation 2.3.8 (2))
Declaration
I/ We on behalf of ................................................................. solemnly declare that the ghee sold by me / us/ on behalf of
............ ....../ ghee used by me / us / on behalf of ............................ in the preparation of .................................. .Confectionary
(including sweetmeats) is / was from a tin containing ghee of ..................... origin and having “AGMARK” seal. The said
tin pertains to batch number.......................... from Shri/ Shrimati/ Kumari/ Sarvsri ......................................................... on the
....................... as per invoice / cash/ credit memo.
No...................... Dated.......................
Signature of Trader/ Traders
Date..................................
Place.................................
[F.No. 2-15015/30/2010]
V.N. GAUR,
Chief Executive Officer
"""

# Process the document
doc = nlp(text)

# Extract relevant sentences
relevant_sentences = extract_relevant_sentences(doc, keywords)

# Print the relevant sentences
for sentence in relevant_sentences:
    print(sentence+"\n")
