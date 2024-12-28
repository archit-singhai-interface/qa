---
title: Review file status and history
url: https://sellercentral.amazon.com/help/hub/reference/G200828080
section: General Documentation
---

## Build your Return Attribute Overrides file

Download the [SKU Override Template](https://images-na.ssl-images-
amazon.com/images/G/01/rainier/help/ff/Flat.File.ReturnRequestAuthorization.xlsx)
and use it to build your Return Attribute Overrides file.

The Return Attribute Overrides file consists of a list of SKUs and their
associated actions. This file has two rows that define the header, as well as
multiple rows that contain the actual records. Each record should contain a
SKU, and an action that you should take for that SKU, with a tab separating
the two fields. The SKUs should not contain any special control characters,
such as newline characters.

SKUs can be at most 40 characters long. A Return Attribute Overrides file can
have a maximum of 50,000 SKUs. For more details on how to create this file,
please see the instructions and sample data in the template file above.

## Upload your Return Attribute Overrides file

Click on the [Return Attribute
Overrides](https://sellercentral.amazon.com/returns/attribute-overrides) link
on the [Return Settings](https://sellercentral.amazon.com/gp/returns/settings)
page where you can upload the completed Return Attribute Override file.

After you upload this file, Amazon will generate a processing report that will
indicate the status of each SKU override.

The processing report is a tab-delimited text file you can open and read in a
program such as Microsoft Excel or Notepad. Each line in the spreadsheet
containing data is referred to as a record. At the top of the processing
report you see a summary of records that were or were not successfully
processed.

For example:

    
    
                   
    Feed Processing Summary: 
    Number of records processed: 1045
    Number of records successful: 1030 
                
    

If there are errors with individual records, you see the following information
for each error:

Element | Description  
---|---  
original-record-number | The row number in the original file you uploaded where the error occurred. Row 0 refers to any general file errors or errors with the header, therefore Row 1 is actually the 3rd row in the file, and the 1st row with actual data.  
error-code | A number used by Amazon to identify the error message. This is the number to use when reviewing **Error code explanations**.  
error-type | One of two values: error or fatal. Errors refer to invalid data that affects only the specified record. Fatals refer to invalid data that affects the entire file. Fatals cause the entire file to not be processed.  
error-message | A brief explanation of the error. The error message might suggest corrective measures.  
  
After reviewing the error messages in the processing report, you can modify
your Return Attribute Overrides file with any corrections. For more help in
correcting the errors you receive, refer to the **Error code explanations**
sections below.

## Error code explanations

Code | Severity | Description  
---|---|---  
41001 | Fatal | The file is too big. The maximum allowable file size is 60 MB.  
41002  | Fatal | The file has too many records. The maximum allowable number of records is 50,000.  
41003  | Fatal | The file is empty or all records in the file are invalid.  
41004  | Error | There is no SKU in this row.  
41006  | Error | The SKU in this row is too long. The maximum length is 40 characters.  
41007  | Fatal | You have exceeded the upload quota and therefore the file will not be processed. You may upload 20 files in a 24 hour period.  
41008  | Fatal | The header for this file is invalid. This could be due to a missing header, or the wrong columns defined in the header.  
41009  | Error | This row contains the wrong number of fields. All rows must contain 2 fields.  
41010  | Error | The action in this row is invalid. It must be **AUTOMATIC** , **MANUAL** , or **DELETE**.  
  
**Note:** The Return Attribute Overrides upload history only includes override
files submitted within the last 90 days.

Refer to [Set your return preferences](/gp/help/200828040) for additional
information.

