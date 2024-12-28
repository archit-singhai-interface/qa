---
title: Missing carrier or ship method in Buy Shipping
url: https://sellercentral.amazon.com/help/hub/reference/TQMVHPB94LP2355
section: General Documentation
---

Eligibility of a carrier and ship method within Buy Shipping is dependent upon
a number of factors. The most common reason a ship method is ineligible is
that the delivery date of the ship method is after the order’s promised
delivery date. For more information, go to [Use Buy Shipping
services](/gp/help/200202220).

The following steps will help you troubleshoot an ineligible ship method or
carrier within Buy Shipping.  

  1. If the following ship methods are ineligible, review the shipping restrictions that limit their availability in Buy Shipping:  

    1. USPS Priority Cubic: This ship method has a maximum dimensional restriction, confirm that your package is below the threshold. For more information, go to [USPS shipping services and restrictions](/gp/help/200204090).
    2. USPS Priority Flat Rate: This ship method has a maximum dimensional restriction, confirm that your package is below the threshold. For more information, go to [USPS shipping services and restrictions](/gp/help/200204090).
    3. FedEx One Rate: You must link your FedEx account in Buy Shipping preferences and ship your package in [FedEx One Rate packaging](/gp/help/KNFZNQADBCUNX9C). If your package dimensions do not match FedEx One Rate package dimensions, the ship methods will not be eligible in Buy Shipping. For more information, go to [Manage your carrier accounts](/gp/help/G200785170).
  2. If you are purchasing shipping via the Seller Central user interface, confirm the following:  

    1. After entering the package dimensions and weight, confirm your ship method is not available when you click **See all options** under **Selected shipping service** in the Buy Shipping user interface.
    2. Confirm the carrier is added to your **Carrier prioritization** in [Buy Shipping preferences](/sbr/buyShippingPreferences). If a carrier is prioritized, then only prioritized carriers will be eligible in Buy Shipping. Carriers not prioritized will not be eligible in Buy Shipping.
    3. Confirm all ‘Ship from’ addresses contain an email address and phone number in Buy Shipping [preferences](/sbr/buyShippingPreferences). If a ship from location does not include an email address and phone number, and a carrier requires that information, then the carrier will not be eligible in Buy Shipping.
    4. Review the following additional actions associated with the Buy Shipping ineligible message in Seller Central.
Ineligible Message | Action  
---|---  
This ship method is not eligible for this order. | For information, go to [How does Buy Shipping work?](/gp/help/GLXKP5E6P6QTSSU8).  
The 'Ship to' address is not supported by the carrier. Please choose an alternative ship method. | Buy Shipping conducts address validation and the address provided by the buyer was not supported by the carrier. If the buyer is unable to revise their address, request that they cancel the order and repurchase or choose an alternative ship method.  
A phone number is required in 'Ship from' details Buy Shipping preferences. | Refer to step 2c above.  
The 'Ship from' address is not supported. Please review 'Ship from' address in Buy Shipping preferences. | The carrier does not support the ship from address as it has been entered in [Buy Shipping preferences](/sbr/buyShippingPreferences), update the ship from address or choose an alternative carrier.  
Invalid phone number for 'Ship from' address in Buy Shipping preferences. | The phone provided in the ship from address in [Buy Shipping preferences](/sbr/buyShippingPreferences) is formatted incorrectly, update the phone number.  
Not a preferred carrier per your carrier prioritization in Buy Shipping preferences. | Refer to step 2b above.  
This carrier does not ship to a PO Box. Please choose an alternate carrier. | Some carriers will not ship to a PO Box, you must choose an alternate carrier from Buy Shipping.  
This carrier does not ship from a PO Box. Please choose an alternate carrier. | Some carriers will not ship from a PO Box, you must choose an alternate carrier from Buy Shipping.  
Package weight exceeds the maximum weight for this ship method. | To learn more, go to the carrier-specific restrictions in [USPS](/gp/help/200204090), [FedEx](/gp/help/G201276510), [UPS](/gp/help/G200785110), [OnTrac](/gp/help/3YDQYBJR85QFETF).  
Package dimension exceeds the maximum dimension for this ship method. | To learn more, go to the carrier-specific restrictions in [USPS](/gp/help/200204090), [FedEx](/gp/help/G201276510), [UPS](/gp/help/G200785110), [OnTrac](/gp/help/3YDQYBJR85QFETF).  
An unknown error occurred, try again. | An intermittent, one-time error has occurred, attempting to repurchase shipping through Buy Shipping should resolve the issue.  
The 'Ship date' is in the past. Choose a future 'Ship date'. | You may modify the ship date by clicking the date in the 'Ship date' field in the Buy Shipping user interface.  
Does not meet business operating hours | This is a business order and shipping services with high probability of delivering outside recipient operating hours have been excluded. You must choose an alternate carrier or ship method from Buy Shipping.  
  3. Refer to [Buy Shipping](https://developer-docs.amazon.com/sp-api/docs/sp-api-seller-use-cases#buy-shipping) section for buying Shipping through SP-API.

