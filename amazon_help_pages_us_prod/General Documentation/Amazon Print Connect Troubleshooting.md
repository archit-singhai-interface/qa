---
title: Amazon Print Connect: Troubleshooting
url: https://sellercentral.amazon.com/help/hub/reference/HHCDEF3QS9P5TW7
section: General Documentation
---

## Common Known Issues

The following are known issues with Amazon Print Connect:

  * FedEx label size does not print properly: If you are not using a thermal printer to print shipping label, make sure you are using the “Default (PNG)” option for the label print orientation.
  * Amazon Print Connect does not support PDF.
  * Additional dialog box while printing with Firefox: This is a Firefox limitation that the dialog box shows up every time.
  * Amazon Print Connect does not work with reprint. If you chose Default (ZPL) as your label orientation, you might not be able to re-print the label.
  * You cannot reprint a label in a different format than the original format.
  * The Bulk UI does not currently support Amazon Print Connect (APC). Uninstall APC if you use the Bulk UI.

**Note:** The app does not support changing formats or printer settings. It
takes the format and label orientation from "Buy Shipping" page and uses your
printer settings

## Verify Setup

If you encounter issues when using Amazon Print Connect, verify the below
options to ensure the application is set-up correctly.

**Note:** Amazon Print Connect does not currently support printer LP 2844. If
you have connected this printer, select another printer or uninstall Amazon
Print Connect and print labels as per previous process.

## Verify installation

  

  1. Go to your System Tray within your taskbar.
  2. If Amazon Print Connect is enabled, the icon ![](https://m.media-amazon.com/images/G/01/rainier/printer_icon._CB1533892852_.png) will appear in the System Tray.

**Note:** If Amazon Print Connect is not enabled, go to the _[Amazon Print
Connect](/gp/help/GQ8WSSALNXZJEW3S)_ page for installation instructions.

## Verify preferred printer selection

  

  1. Go to your System Tray within your taskbar.
  2. Click the ![](https://m.media-amazon.com/images/G/01/rainier/printer_icon._CB1533892852_.png) icon.
  3. Choose the **Printer Setup** option.
  4. From the **Printer Setup** option, the highlighted printer is your default printer.

**Note:** If no printer is highlighted, select one to set as your default for
printing Buy Shipping labels.

## Verify access key and secret key

  

  1. Go to your System Tray within your taskbar.
  2. Click the ![](https://m.media-amazon.com/images/G/01/rainier/printer_icon._CB1533892852_.png) icon.
  3. Choose the Account Setup option.
  4. Ensure that the **access key** and **secret key** are populated.

**Note:** If you need to verify your **access key** and **secret key** , go to
the [Amazon Print Connect access key and secret key](/buy-shipping/amazon-
print-connect) page.

## Update print settings and improve print quality

## Update print orientation

Is your thermal not printing the label with the correct print orientation.

**Thermal Printers** : When purchasing a shipping label with a thermal
printer, confirm the selection in the **Label print orientation** drop-down is
set to “Default (ZPL)”. Choosing any other option will print the wrong size or
not print at all.

**Non-Thermal Printers** : When purchasing a shipping label without a thermal
printer, confirm the selection in the **Label print orientation** drop-down is
not set to “Default (ZPL)”. If you print a shipping label with the ZPL print
orientation, cancel the shipping label, and repurchase with “Default (PNG)”,
“Left”, “Right”, or “With Receipt”.

## Update Paper Format

Is the label generated too large or too small on a thermal/label printer? Is
the label only printing on the left upper corner of the page? Follow below
steps to update paper format.  

  1. Click the **Windows** button.
  2. Go to **Control Panel**. 
  3. Go to **Devices and Printers**. 
  4. Right click on the preferred printer. 
  5. Click **Printing Preferences**.
  6. Set **Paper Format (size)** to
     * Width: 4.00 inch
     * Height: 6.00 inch

## Update Printer Options

Is the barcode generated not scanning properly on a thermal or label printer?
Is the quality of the shipping label poor? Follow below steps to update
printer options.

**Note:** The location of the below settings within ‘Printer Preferences’ may
vary based on printer company and model.

#### Option 1: Adjust Dithering Settings

  

  1. Click the **Windows** button.
  2. Go to **Control Panel**. 
  3. Go to **Devices and Printers**. 
  4. Right click on the preferred printer.
  5. Click **Printer Preferences**.
  6. Go to **Dithering** tab and select **None**. 
  7. Click **apply**.

#### Option 2: Adjust Darkness Settings

  

  1. Click the **Windows** button.
  2. Go to **Control Panel**. 
  3. Go to **Devices and Printers**. 
  4. Right click on the preferred printer. 
  5. Click **Printer Preferences**.
  6. Go to **Options** tab and set **Darkness** to highest option
  7. Click apply.

#### Option 3: Adjust Printing Speed

  

  1. Click the **Windows** button.
  2. Go to **Control Panel**. 
  3. Go to **Devices and Printers**. 
  4. Right click on the preferred printer. 
  5. Click **Printer Preferences**.
  6. Go to **Options** tab and set **Speed** to lowest option.
  7. Click **apply**.

## Details required for Seller Support ticket

Prior to contacting Selling Partner Support, retrieve logs and have the below
details on hand to ensure that the team can assist you in a timely manner.

  * Browser used to print label.
  * Error messages that they see (if any).
  * Screenshots for the issue (if any).
  * Logs from the seller. To get the log, follow the below steps.
  * Click the **Windows** button and go to **Run** OR Use the Windows Search functionality,
    * Search for: %localappdata%
    * Go to Amazon.com, Inc
    * Go to Amazon Print Connect
    * Select the text file ‘client’

## Uninstall Amazon Print Connect

  

  1. Click the **Windows** button.
  2. Go to **Control Panel**. 
  3. Go to **Programs and Features**.
  4. Go to **Amazon Print Connect**.
  5. Select **Uninstall**.

