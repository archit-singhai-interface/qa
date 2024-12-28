---
title: Fix spreadsheet errors in coupon uploads
url: https://sellercentral.amazon.com/help/hub/reference/GXRK7QW9Y7WZJ4MM
section: General Documentation
---

After our system processes your uploaded spreadsheet, you can download a
status file that details upload status and errors on each coupon. See details
on possible errors and how to correct them below:

**Error:** Invalid ASIN. Correct the ASIN before uploading the spreadsheet
again.

You have provided a value in column A that is not a valid ASIN. Review the
semi-colon separated ASIN list to make sure all ASINs are valid.

**Error:** Maximum ASIN limit (2900 child ASINs) exceeded. Remove some ASINs
to adhere to child ASIN limit and submit again.

A single coupon has a limit of 2900 child ASINs. If you're adding more than
2900 child ASINs to the coupon, your coupon will not be created. Remove some
child ASINs to stay within the 2900 limit and submit the spreadsheet again.

Adding only parent ASINs or a mix of parent ASINs: When you add a parent ASIN
to a coupon, your coupon will not be created. You have to make sure only child
ASINs (max up to 2900) are added to create a Coupon.

**Error:** Maximum number of rows exceeded.

You can create up to 100 coupons in each spreadsheet you upload. Do not enter
any data in row 120 and beyond.

**Error:** An ASIN can only have one active coupon at a time.

At least one of your ASINs is already scheduled for another coupon at an
overlapping time. Either cancel the existing coupon that is scheduled or
remove the ASIN with the overlapping coupon from the spreadsheet and upload
the spreadsheet again.

**Error:** Start date of coupon cannot be more than 180 days from the day of
creation.

Coupons can be created up to six months in advance. Update your start date to
fall within this time frame.

**Error:** Coupon title must only have alphanumeric characters.

Coupon titles must contain only alphanumeric characters. Remove any special
characters or symbols from the coupon title.

**Error:** Spreadsheet is missing input in required columns. Provide all
required information and submit again.

All required columns are in red in the spreadsheet and must be filled in
before you upload it.

**Error:** Maximum title character limit (80 characters) exceeded.

Coupon title must not contain more than 80 characters. Reduce the length of
the coupon title.

**Error:** Start date must not be in the past.

The earliest start date for a coupon must be the date of creation.

**Error:** The end date of the coupon cannot be more than “n” days from the
coupon start date.

A standard coupon can run for a maximum of 30 days (or 365 days for Subscribe
& Save coupons, 180 days for reorder coupons).

**Error:** Coupon end date must not be same as start date.

The earliest end date for a coupon must be one day after the coupon start
date.

**Error:** Maximum budget allowed is $10,000,000. Revise the budget and upload
again.

Revise the coupon budget to be within the maximum limit.

**Error:** Minimum budget required is $100. Revise the budget and upload
again.

Increase the coupon budget to at least the minimum required.

**Error:** Invalid date.

****Adding non-duplicate ASINs:**** Make sure that you remove duplicate ASINs
from the spreadsheet. Having duplicate ASINs will make your spreadsheet fail
to upload.

