---
title: Inbound Defects and Guardrails
url: https://sellercentral.amazon.com/help/hub/reference/GVBKGXPUDX8CYNKM
section: General Documentation
---

  * **Misroute defect:** If you select a different destination region on Shipper Central than you first selected on the Seller Central inbound placement selection, you will be charged the FBA inbound placement service fee for the updated region, and the FBA misroute defect fee. Refer to the [FBA inbound defect fee page](/help/hub/reference/external/GL5XA3MNXAJKJE8E) for details on defect fees for shipments delivered to the wrong location. No misroute defect fee will be charged for routing changes triggered by Amazon Global Logistics (AGL).
  * **Misuse defect:** Do not ship AGL AMP purchase orders with non-AGL providers. This deviation will be tracked as a defect. Repeat deviations from the plans may lead to temporary or permanent suspension of your AGL account.
  * **Change plan defect:** You are guided to implement following:
    * Do not change the placement option.
    * Do not ship AGL AMP purchase orders with non-AGL providers.
    * Do not ship Minimal shipment splits and Partial shipment splits purchase orders with AGL AMP. You can ship Amazon optimized shipment splits (AOSS) with AMP as long as you ship all purchase orders associated to the shipping plan with AMP.

These deviations deter AGL from optimizing the placement costs thus we will
track this as a defect. Repeat deviations from the plans may lead to temporary
or permanent suspension of your AGL account.

  * **Splitting purchase orders:** If you divide your purchase orders across multiple AGL and non-AGL bookings using different inbound placement options, you will be charged the inbound placement service fee for the region based on the original plan. Any deviation from the planned region will result in a misroute defect fee (see above) and inbound placement service fee is charged as per actual inbound.

**Shipping scenarios examples:** The following table lists shipping scenario
examples where a defect fee may or may not be charged and other guardrails
apply. These scenarios are tracked specifically when you make a booking in
Seller Central and make changes in Shipper Central.

**Note:**

  * Seller Central booking are automatically validated during shipment creation. We have clarified how any deviations will be tracked or invoiced.
  * ">" represents "shipping as" or "shipping with."

_Examples #_ | _Shipping Scenario(s)_ | Deviations tracking and invoicing  
---|---|---  
**_AGL Shipment examples_**  
Example 1 |  **a) AGL AMP > AGL AMP** "I booked an AMP FBA shipment, and shipped it as an AMP shipment". **b) AGL Minimal shipment splits (West or East) > AGL Minimal shipment splits (West or East)** "I booked an AGL Minimal shipment splits West shipment, and shipped it with no change". OR "I booked an AGL Minimal shipment splits East shipment, and shipped it with no change". |  This is the proper procedure as you have shipped as originally planned.  
Example 2 |  **AGL****AMP > AGL Minimal shipment splits (West)** "I booked an AGL AMP shipment, but on Shipper Central, I changed it and shipped as AGL Minimal shipment splits West destination". | This is a change plan defect. You will be charged the AGL Minimal shipment splits West shipping rate and the FBA inbound placement service fee according to the actual inbound region.  
Example 3 |  **AGL AMP > AGL Minimal shipment splits (East)** "I booked an AGL AMP shipment, but on Shipper Central, I changed it and shipped as AGL Minimal shipment splits East destination". | This is a change plan and misroute defect. You will be charged the AGL Minimal shipment splits East shipping rate and the FBA inbound placement service fee according to the East destination region. You will also be charged the misroute defect fee.  
Example 4 |  **AGL Minimal shipment splits (West) > AGL AMP** "I booked an AGL Minimal shipment splits West shipment, but on Shipper Central, I changed it and shipped as an AGL AMP shipment". | This is a change plan defect. In this case, you will be charged the AGL AMP shipment rate and the FBA inbound placement service fee for Minimal shipment splits according to actual inbound region. Note that accounts with repeat violations may be suspended.  
Example 5 |  **AGL Minimal shipment splits (East) > AGL AMP** "I booked an AGL Minimal shipment splits East shipment, but on Shipper Central, I changed it and shipped as an AGL AMP shipment". | This is a change plan defect. You will be charged the AGL AMP shipment rate and the FBA inbound placement service fee for Minimal shipment splits according to the East destination region. Note that accounts with repeat violations may be suspended.  
Example 6 |  **AGL Minimal shipment splits (East or West) > AGL Minimal shipment splits (West or East) ** "I booked an AGL Minimal shipment splits East shipment, but on Shipper Central, I changed it and shipped as an AGL Minimal shipment splits West shipment". OR "I booked an AGL Minimal shipment splits West shipment, but wanted to change it to AGL Minimal shipment splits East shipment". | This is a misroute defect. You will be charged the AGL Minimal shipment splits shipping rate and the FBA inbound placement service fee for minimal shipment splits according to the actual r inbound region. You will also be charged the misroute defect fee. Note that accounts with repeat violations may be suspended.  
**_3PL Shipment examples with an AGL Purchase Order (PO)_**  
Example 8 |  **AGL AMP purchase order (PO) > Non-AGL Provider (3PL) (West) ** "I booked an AGL AMP shipment, but actually shipped it with another provider (non-AGL) to the West region".  | This is a misuse defect. You will be charged the FBA inbound placement service fee for Minimal shipment splits according to the West region destination. Note that accounts with repeat violations may be suspended.  
Example 9 |  **AGL purchase order (PO) for Minimal shipment splits (West) > Non-AGL Provider (3PL) (West) ** "I booked an AGL PO for Minimal shipment splits West shipment but actually shipped with another provider (non-AGL) to the West region". | You will be charged the FBA inbound placement service fee for Minimal shipment splits according to the West region destination.  
Example 10 |  **AGL purchase order (PO) for Minimal shipment splits (East) > Non-AGL Provider (3PL) (West) ** "I booked an AGL PO for Minimal shipment splits East shipment, but actually shipped with another provider (non-AGL) to the West region". |  This is a misroute defect. You will be charged the FBA inbound placement service fee for Minimal shipment splits according to the West region destination. You will also be charged the misroute defect fee.  
**_Shipment examples without an AGL Purchase Order (PO)_**  
Example 11 |  **Non-AGL Minimal shipment splits (West) > AGL AMP ** "I booked a non-AGL PO for Minimal shipment splits West, but actually shipped it as an AGL AMP shipment." | This is a change plan defect. You will be charged the AGL AMP shipping rate and the FBA inbound placement service fee for Minimal shipment splits according to the destination region.  
Example 12 |  **Non-AGL Minimal shipment splits (West) > AGL Minimal shipment splits (East****)** "I booked a non-AGL PO for Minimal shipment splits West, but actually shipped it as an AGL Minimal shipment splits East shipment." | This is a misroute defect. You will be charged the AGL Minimal shipment splits shipping rate and the FBA inbound placement service fee according to the East region destination. You will also be charged misroute defect fee.  
Example 13 |  **Non-AGL Minimal shipment splits (East) > AGL AMP** "I booked a non-AGL PO for Minimal shipment splits East, but actually shipped it as an AGL AMP shipment." | This is a change plan defect. You will be charged the AGL AMP shipping rate and the FBA inbound placement service fee according to the East region destination.  
Example 14 |  **Non-AGL Minimal shipment splits (East) > AGL Minimal shipment splits (West) ** "I booked a non-AGL PO for Minimal shipment splits East, but actually shipped it as AGL Minimal shipment splits West." | This is a misroute defect. You will be charged the AGL Minimal shipment splits shipping rate and the FBA inbound placement service fee according to the West region destination. You will also be charged the misroute defect fee.  
Example 15 |  **Non-AGL partial shipment splits (West) > AGL AMP** "I booked a non-AGL PO for partial shipment splits West shipment, but actually shipped it as AGL AMP."  | This is a change plan defect. You will be charged the AGL AMP shipment rate and the FBA inbound placement service fee according to the actual inbound locations and number of received shipments which may be higher than estimated fees at the time of shipment creation.  
Example 16 |  **Non-AGL partial shipment splits (West) > AGL Minimal shipment splits (East)** "I booked a non-AGL PO for partial shipment splits West shipment, but actually shipped it as AGL Minimal shipment splits East shipment." | This is a misroute defect. You will be charged the AGL Minimal shipment splits shipping rate and the FBA inbound placement service fee according to the actual inbound locations and number of received shipments which may be higher than estimated fees at the time of shipment creation. You will also be charged the misroute defect fee.  
**Shipment examples for non-AGL Amazon-optimized shipment splits (AOSS) (West)
switch to AGL**  
Example 17 |  **Non-AGL Amazon-optimized shipment splits > AGL AMP** "I booked a non-AGL PO for AOSS shipment, but actually shipped it as an AGL AMP shipment."  | We allow AOSS shipments with AGL AMP if you ship entire AOSS shipment with AGL AMP. If you do not ship the entire shipment with AGL AMP, this is a change plan defect. You will be charged the AGL AMP shipping rate for shipments sent with AGL AMP. Additionally, you might be charged Inbound placement service fees for shipments you don’t send with AGL AMP for non-compliant shipping plans (including misrouted or abandoned shipments).  
Example 18 |  **Non-AGL Amazon-optimized shipment splits > AGL Minimal shipment splits ** "I booked a non-AGL PO for AOSS shipment but actually shipped it as an AGL Minimal shipment splits shipment." | This is not a recommended approach to inbound AOSS PO. If one or more of the shipment deviates from the planned region, you will be charged FBA inbound placement service fee according to the actual inbound locations and number of received shipments which may be higher than estimated fees at the time of shipment creation. You will also be charged the misroute defect fee for the deviated PO.

