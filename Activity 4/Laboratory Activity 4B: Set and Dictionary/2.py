def parse_currency_data(document_content):
    currency_dict = {}
    lines = document_content.strip().split("\n")
    
    for line in lines[3:]: 
        parts = line.strip().split()
        if len(parts) >= 2:
            rate_str = parts[-1]
            code = parts[0]
            
            if rate_str == "########":
                continue
                
            try:
                rate = float(rate_str)
                currency_dict[code] = rate
            except ValueError:
                continue
    
    return currency_dict

def currency_converter():
    """
    A program that converts USD to a specified currency.
    """
    document_content = """
Page
1
of 3
code name rate
EUR Euro ########
GBP U.K. Pound Sterling########
JPY Japanese Yen131.1995
AUD Australian Dollar1.439774
CHF Swiss Franc########
CAD Canadian Dollar1.342308
NZD New Zealand Dollar1.583391
TRY Turkish Lira 18.83403
NGN Nigerian Naira460.3864
KGS Kyrgyzstan Som86.20469
MGA Malagasy ariary4304.102
SRD Surinamese dollar32.59911
GHS Ghanaian Cedi12.17178
CUP Cuban peso 1
NOK Norwegian Krone10.29228
QAR Qatari Rial 3.647457
CZK Czech Koruna22.1512
HRK Croatian Kuna7.362268
RSD Serbian Dinar108.5081
NIO Nicaraguan C�rdoba36.54561
SBD Solomon Islands dollar8.41428
MWK Malawian kwacha1026.17
YER Yemeni rial 250.1646
VES Venezuelan Bolivar23.11958
BDT Bangladeshi taka105.5536
RON Romanian New Leu4.561703
DZD Algerian Dinar136.0871
ARS Argentine Peso189.5406
STN S�o Tom� and Pr�ncipe Dobra23.01514
BIF Burundian franc2075.047
MMK Myanma Kyat2099.762
MUR Mauritian Rupee45.34362
AED U.A.E Dirham3.672926
IDR Indonesian Rupiah15094.63
MXN Mexican Peso18.93037
UAH Ukrainian Hryvnia36.47195
CRC Costa Rican Col�n582.307
BZD Belize dollar 2.015272
GNF Guinean franc8608.203
SZL Swazi lilangeni17.51749
SOS Somali shilling568.3301
INR Indian Rupee82.61622
NPR Nepalese Rupee132.223
XAF Central African CFA Franc611.4473
AZN Azerbaijan Manat1.696962
PYG Paraguayan Guaran�7285.405
GYD Guyanese dollar210.951
RWF Rwandan franc1084.498
ERN Eritrean nakfa15.07319
WST Samoan tala2.691706
BRL Brazilian Real5.197908
LKR Sri Lanka Rupee366.2309
TND Tunisian Dinar3.065955
VND Vietnamese Dong23535.79
IQD Iraqi dinar 1459.945
AFN Afghan afghani90.14747
NAD Namibian dollar17.51749
SYP Syrian pound2448.556
MOP Macanese pataca8.082523
BAM Bosnia and Herzegovina convertible1.823727
DKK Danish Krone6.931757
PKR Pakistani Rupee268.4966
BGN Bulgarian Lev1.821638
RUB Russian Rouble73.13025
TMT New Turkmenistan Manat3.499199
SVC Salvadoran colon8.753525
XCD East Caribbean Dollar2.705752
LAK Lao kip 16822.14
GTQ Guatemalan Quetzal7.840954
SAR Saudi Riyal 3.752211
PLN Polish Zloty 4.412869
GIP Gibraltar pound########
GEL Georgian lari2.650754
MKD Macedonian denar57.30296
AWG Aruban florin1.809872
AOA Angolan kwanza512.4884
MVR Maldivian rufiyaa15.45372
BHD Bahrain Dinar########
EGP Egyptian Pound30.36481
KRW South Korean Won1260.469
MRO Mauritanian Ouguiya36.02011
COP Colombian Peso4746.429
BBD Barbadian Dollar2.018595
DJF Djiboutian franc177.9833
HNL Honduran Lempira24.64989
KES Kenyan shilling124.8661
HKD Hong Kong Dollar7.848811
MAD Moroccan Dirham10.22721
ZAR South African Rand17.71922
MDL Moldova Lei 18.7962
PAB Panamanian Balboa 1
FJD Fiji Dollar 2.201279
CDF Congolese franc2074.071
MZN Mozambican metical64.24781
UGX Ugandan shilling3672.833
KWD Kuwaiti Dinar########
THB Thai Baht 33.40044
TWD New Taiwan Dollar30.06651
IRR Iranian rial 41997.79
BOB Bolivian Boliviano6.884075
LRD Liberian dollar156.847
SDG Sudanese pound565.0513
TOP Tongan pa?anga2.38032
VUV Vanuatu vatu121.4193
OMR Omani Rial ########
ILS Israeli New Sheqel3.482746
PEN Peruvian Nuevo Sol3.854426
UZS Uzbekistan Sum11278.03
ETB Ethiopian birr53.68331
TTD Trinidad Tobago Dollar6.777487
PGK Papua New Guinean kina3.524228
BWP Botswana Pula12.92493
SEK Swedish Krona10.58459
SGD Singapore Dollar1.325506
HUF Hungarian Forint361.7083
BYN Belarussian Ruble2.786553
TJS Tajikistan Ruble10.29429
GMD Gambian dalasi63.23386
CVE Cape Verde escudo102.9766
ZMW Zambian kwacha19.22111
KHR Cambodian riel4096.097
DOP Dominican Peso56.407
CNY Chinese Yuan6.78789
ISK Icelandic Krona141.0982
LYD Libyan Dinar4.781246
CLP Chilean Peso796.7963
BSD Bahamian Dollar 1
XPF CFP Franc 110.9561
ALL Albanian lek 107.9663
SCR Seychelles rupee13.61569
ANG Neth. Antillean Guilder1.795904
LBP Lebanese Pound4634.157
MYR Malaysian Ringgit4.292053
KZT Kazakhstani Tenge455.425
HTG Haitian gourde150.6194
BND Brunei Dollar1.323345
KMF Comoro franc460.7359
LSL Lesotho loti 17.51749
TZS Tanzanian shilling2336.903
JOD Jordanian Dinar########
PHP Philippine Peso54.81473
XOF West African CFA Franc611.3128
AMD Armenia Dram395.6928
UYU Uruguayan Peso39.19278
JMD Jamaican Dollar154.6456
SSP South Sudanese pound741.9865
MRU Mauritanian ouguiya36.36469
MNT Mongolian togrog3506.285
"""
    
    currency_dict = parse_currency_data(document_content)
    

    
    try:

        dollar_amount = float(input("How much dollar do you have? "))
        currency_code = input("What currency you want to have? ").upper()
        
        if currency_code in currency_dict:
            rate = currency_dict[currency_code]
            converted_amount = dollar_amount * rate
            
            print(f"Dollar: {dollar_amount} USD")
            print(f"{get_currency_name(currency_code, document_content)}: {converted_amount}")
        else:
            print(f"Currency code {currency_code} not found or exchange rate not available.")
    
    except ValueError:
        print("Please enter a valid dollar amount.")

def get_currency_name(code, document_content):
    """Get the full name of a currency given its code."""
    lines = document_content.strip().split("\n")
    
    for line in lines[3:]: 
        parts = line.strip().split()
        if len(parts) >= 2 and parts[0] == code:
            return " ".join(parts[1:-1])
    
    return code

if __name__ == "__main__":
    currency_converter()