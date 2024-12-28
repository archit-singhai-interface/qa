---
title: Review a Processing Report
url: https://sellercentral.amazon.com/help/hub/reference/G200194300
section: General Documentation
---

**Note:** Individual sellers: This feature is available for Professional
selling plans only. [Learn more](/gp/help/64491).

The processing report is a tab-delimited text file you can open and read in a
program such as Microsoft Excel or Notepad. Processing reports are
downloadable files that let you review the status of your inventory file
uploads.

To download and review a processing report, follow the below steps:  

  1. Under **Catalog** , select **Add Products**.
  2. Go to the **Spreadsheet** tab, then click [Check Upload Status](/product-search/bulk/status). 

Each line in the spreadsheet containing data is referred to as a "record." At
the top of the processing report, there is a summary of records (listings)
with the total number of records processed and those processed successfully.
The difference is the number of records processed unsuccessfully (or processed
with errors).

  3. (Optional) Filter or sort the **error-type** column to view only error messages (and not info or warning messages)
  4. For each error, refer to the **original-record-number** and **SKU** columns to determine which record in your inventory file resulted in the error

**Note:** The first two rows of your inventory file are not considered
records. Therefore, an error in Record 1 in the processing report corresponds
to Line 3 in your inventory file.

In the example given below, 1,045 records were processed, of which 1,030
records were processed successfully and 15 were unsuccessful because of
errors:

    
    
    Feed Processing Summary
    Number of records processed: 1045
    Number of records successful: 1030

The processing report displays errors in the following format. You can use
this report to make necessary corrections in your inventory file, and then
reload the file to correct your listings. For more information, see the **Data
Definitions** tab in your inventory template file, or review our [Error Code
Explanations](/gp/help/17781).

Element | Description  
---|---  
original-record-number | The record number in which the error occurred.The first two rows of your inventory file template are not considered as records. Therefore, an error in Record 1 corresponds to Line 3 in your inventory file.  
error-code | The ID number of the error message. Look for this ID when referring to [Error Code Explanations](/gp/help/17781).  
error-type | One of the following two values: 

  * **Warnings:** The data was successfully processed but might not appear as intended.
  * **Errors:** The data is inadequate or flawed in a way that prevents the record from processing successfully.

  
error-message | A brief explanation of the error, possibly including corrective measures.

