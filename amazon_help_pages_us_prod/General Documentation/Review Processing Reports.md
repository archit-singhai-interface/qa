---
title: Review Processing Reports
url: https://sellercentral.amazon.com/help/hub/reference/G201576740
section: General Documentation
---

Processing reports are downloadable files that let you review the status of
your inventory file uploads. The processing report is a tab-delimited text
file you can open and read in a program such as Microsoft Excel or Notepad.

**Individual sellers:** This feature is available to sellers with
[Professional selling plans](/gp/help/64491).

To download the processing report, follow the below steps:  

  1. Under Inventory, select **Add Products via Upload**. 
  2. In the **Inventory file upload** status section download the report. 

At the top of the processing report, there is a summary of records (listings)
with the total number of records processed, and the total number processed
successfully. The difference is the number of records not processed
successfully (or processed with errors).

In the example given below, 1,045 records were processed, of which 1,030
records were processed successfully and 15 were unsuccessful because of
errors:

>
>     Feed Processing Summary
>  
>     Number of records processed: 1045
>  
>     Number of records successful: 1030
>  
>  
>  
> ---  
  
The processing report displays errors in the following format. You can use
this report to make necessary corrections in your inventory file, and then
reload the file to correct your listings. For more information, see the **Data
Definitions** tab in your inventory template file, or review our[Error Code
Explanations](/gp/help/17781).

Element | Description  
---|---  
original-record-number | The record number in which the error occurred.The first two rows of your inventory file template are not considered as records. Therefore, an error in Record 1 corresponds to Line 3 in your inventory file.  
error-code |  The ID number of the error message. Look for this ID when referring to [Error Code Explanations. ](/gp/help/17781)  
error-type  | One of the following two values: 

  * **Warnings:** The data was successfully processed but might not appear as intended. 
  * **Errors:** The data is inadequate or flawed in a way that prevents the record from processing successfully.

  
error-message |  A brief explanation of the error, possibly including corrective measures.

