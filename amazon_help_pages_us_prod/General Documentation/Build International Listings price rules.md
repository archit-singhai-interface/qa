---
title: Build International Listings price rules
url: https://sellercentral.amazon.com/help/hub/reference/G202121610
section: General Documentation
---

## Build International Listings price rules  
  
**Build International Listings price synchronization:** You can synchronize
the **List price** or **List price and sale price** from your source store to
your target stores. The price rule will let you automatically adjust prices to
account for the fulfillment fee, including fuel and inflation surcharges, and
currency difference between the source and target stores.

The same method will be used to calculate the list price and sale price. If
you change the price of an offer that is inactive in the source store, the
price will be updated in the target store.

A sale price in the source store will initiate a sale in the target store. The
sale price is synchronized only during the defined sale period. The sale price
stops synchronizing when the sale period is complete or you remove the sale
price from the source store.

**Price my offers:** You can set up a price rule for each target store and
fulfillment method from the options shown in the tables below.

If the target store has a different currency than the source store, Build
International Listings will convert the price based on exchange rates. After
you connect the source and target stores, prices in the target store are
updated periodically to reflect changes in the exchange rate. The frequency of
these updates may vary from daily to weekly.

**Store price rules** apply to your entire inventory for the combination of
target store and fulfillment method. Store price rules cannot be set for
individual ASINs or SKUs.

If you make a manual change to your ASIN price in your target store or stores,
the connection to your US price will be broken, and your prices must be set
manually. When you manually set your prices, make sure to account for the
exchange rate difference between US, Canadian, and Mexican currencies to avoid
pricing errors.

## Store price rules and examples

For the examples below, we are assuming that the source store is the US and
the target store is Mexico. You have a source store price of USD 10, and the
currency exchange rate is USD 1 = MXN 19.5.

Price rule options | You enter or select: | Price in source store | Price calculation | Final price in target store  
---|---|---|---|---  
Same price as the source store | - | 10 | see pricing example below | MXN 199   
Fixed amount above the source store price | 1 | 10 | 199 + (1 x 19.5) | MXN 218.5  
Percentage above the source store price | \+ 5% | 10 | 199 x 1.05 | MXN 208.95  
Percentage below the source store price | \- 5% | 10 | 199 x .95 | MXN 189.05  
  
**Note:** You can [edit your target store settings](/gp/help/G202121650) at
any time. The tool will recalculate the prices of your offer in target stores
whenever you update a price rule. It may take up to four hours before the
price changes are reflected in each target store.

**Remote Fulfillment with FBA price rule:** The "same as the source store,
adjust for fulfillment fees" pricing rule applies to inventory in the Remote
Fulfillment with FBA program. Once the price rule is enabled, it will let you
automatically adjust prices to account for the fulfillment fee, including fuel
and inflation surcharges, and currency differences between the source and
target stores.

The pricing rule calculates fulfillment fees based on the following factors:

  * Predicted location from where next customer order will be fulfilled, applicable fulfillment program, and fees (for example, domestic or cross-border fulfillment). 
  * Item type, weight and dimensions to calculate specific fulfillment and referral fees based on FBA fees.

If the offer qualifies for fee promotions, the pricing rule applies the
promotional value.

For example, if you ship inventory to the FBA local destination (e.g Canada
FBA) , then for your ASINs in US FBA, the offer price in target stores will
synchronize with the source store price (adjusted for estimated fulfillment
fee and tax rate differences).

Your prices will not automatically adjust if either of these conditions apply:

  * You use automated pricing rules outside of Build International Listings
  * You set prices manually, by bulk upload, or through Marketplace Web Services APIs

## Pricing example

You offer a product in the US for USD 10 that you also want to offer in
Mexico. The current exchange rate is USD 1 equals MXN 19.5, with an Amazon
Currency Converter for Sellers (ACCS) fee of 2.6%.

For the US, the fulfillment fee is USD 1, and the referral fee is 10%. For
Mexico, the fulfillment fee is MXN 40, and the referral fee is 20%.

Current currency exchange rate | Applicable exchange rate | ACCS fee rate* | Price in source store | FBA fulfillment fee in source store | FBA surcharge in source store | Referral fee rate in source store | Source store price without source store fees |  Expected price in target store with applicable exchange rate  | Remote Fulfillment fee in target store | Fulfillment fee adjusted price in target store | Referral fee rate in target store | Final price in target store  
---|---|---|---|---|---|---|---|---|---|---|---|---  
USD 1 = MXN 19.5 | MXN 20  | 2.60% | USD 10  | USD 1 | 5% of FBA fee | 10% | USD 7.95 | MXN 159 | MXN 40 | MXN 199 | 20% | MXN 248.75  
  
**How the numbers are calculated**

1\. The applicable exchange rate is determined through this formula:

Applicable exchange rate = current exchange rate* (1 + Amazon Currency
Converter for Sellers fee)

In the example above, MXN 20 = MXN 19.5 (1 + 2.6%)

2\. The source store price without source store fees is calculated by
subtracting the source store fulfillment and referral fees, including FBA
surcharges, as a percentage of the FBA fee:

Source store price without fees = price in source store – fulfillment fee in
source store with surcharge – referral fee in source store

In the example above, USD 7.95 = USD 10 – (USD 1 x 1.05) – (USD 10 x 10%)

3\. The expected price in the target store is determined by using the
applicable exchange rate, as calculated in step 1:

Expected price in target store with applicable exchange rate = source store
price without fees x applicable exchange rate

In the example above, MXN 159 = USD 7.95 x MXN 20

4\. The adjusted fulfillment fee in the target store is then calculated by
adding the fulfillment fee in target store:

Target store price adjusted for fulfillment fee = expected price in target
store with applicable exchange rate + fulfillment fee in target store

In the example above, MXN 199 = MXN 159 + MXN 40

5\. The final price in the target store is determined by accounting for the
referral fee in the target store:

Final price with referral fee in target store = target store price adjusted
for fulfillment fee / (1 – referral fee in target store)

In the example above, MXN 248.75 = MXN 199 / (1 – 20%)

**Note:** If you don't use the Amazon Currency Converter for Sellers, the
related fee isn't part of the calculation. Step 1 is skipped, and the current
exchange rate is used as the applicable exchange rate.

## European pricing rule

This is a special pricing rule that applies to European FBA inventory,
including inventory that is fulfilled through the European Fulfillment Network
and Pan-European FBA.

You can apply it to Pan-European FBA inventory only, or to all EU FBA
inventory except for Pan-European FBA. You can also add a custom adjustment
for additional costs that aren’t covered by this rule, with different values
for Pan-European FBA and offers via other fulfillment programs.

Once this pricing rule is enabled, prices adjust automatically to account for
the following:

  * Estimated fulfillment fees, based on the dimensions, fulfillment program and estimated location of the inventory
  * Estimated VAT
  * Custom adjustments 
  * Currency differences between the source and target stores

If you use the Amazon Currency Converter for Sellers to receive your proceeds
in your local currency, the currency difference will be based on the estimated
rate used in the converter when the price was calculated. Fees, VAT, and
currency conversion rates used in Build International Listings can differ from
the final fees, VAT, and currency conversion rate used at disbursement.

**Price calculation steps:** Build International Listings will first deduct
the predicted fulfillment fee and VAT from your source store price to get the
fee- and tax-exclusive price. Then the tool will convert this price to the
target store currency, add currency converter costs and any custom
adjustments, and add the estimated target store fulfillment fee and tax to set
the target store price.

If your source or target store has a referral fee different from the rest of
the EU, for example, Poland and Turkey, the tool will also remove the referral
fee from the source store price and add the referral fee for the target store.

The pricing rule calculates fulfillment fees based on the following factors:

  * Predicted location from where next customer order will be fulfilled, applicable fulfillment program, and fees (for example, domestic or cross-border fulfillment)
  * Item type, weight and dimensions to calculate specific fulfillment and referral fees based on FBA fees

If the offer qualifies for fee promotions, the pricing rule applies the
promotional value.

If you apply this pricing rule only to Pan-European FBA inventory, the
estimated target fulfillment fee will be the target store domestic fulfillment
fee, in line with Pan-European FBA benefits.

