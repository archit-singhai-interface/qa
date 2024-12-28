---
title: Create display logic on customizations
url: https://sellercentral.amazon.com/help/hub/reference/GZRLFLSBNRKK4VKL
section: General Documentation
---

Display logic refers to a condition a customer must select in order to see a
customization or surface. This feature helps create a dynamic and tailored
shopping experience for every customer by showing relevant customizations or
hiding irrelevant customizations based on what the customer selects within the
customization experience. For example, you may want to show a text
customization on the back of a listing only if the customer selected front and
back personalizations.

## Create display logic

Display logic refers to the technique of showing or hiding certain elements on
your listing.

While adding display logic there are two concepts:

  * **Condition** , which is controls the display logic
  * **Values** , which are the subsequent statements that are shown/hidden based on the set condition

For example, if you want to offer vertical or horizontal options for a picture
frame and the customer selects horizontal then you would only show the
corresponding customizations related to that selection (5X7, 4X6 sizes)

You can set display logic for any custom listing that offers more than one
customizable option or more than one custom surface.  

  1. Select **Add display logic** in the customizations or surface title bar that is dependent on a condition.
  2. In the display logic modal, the customization labels and options value lists will automatically populate in the dropdowns.
  3. Set the display logic by selecting the condition from the first drop down and the subsequent branches that must show/hide based on the customers actions. For example, if a listing offers 12 oz and 16 oz size, and the multi-color options are not available in small, then for the small size, the applicable colors would be selected so customers see a dynamic color display depending on the chosen size.
  4. Select **Save** to apply the display logic to the customization. The display logic will show inside the customization container.
  5. Select the **Preview** feature to validate that the display logic is correct before publishing the listing.

**Note:** Order matters when applying display logic.

     * If display logic is applied to a customization statement and the condition it relies upon moves below this customization, then the following error will appear, "The customizations linked to this display logic are out of order. Reorder, edit, or delete this display logic."
     * If a condition is deleted that controls whether or not a customization is displayed, then the following error will appear, "A customization linked to this display logic was deleted. Edit or delete this display logic."

## Edit or remove display logic

  

  1. You can edit the display logic at any time by selecting **Edit display logic** in the customization title bar or selecting the display logic summary in the customization container.
  2. You can delete the display logic at any time by either editing the display logic and clicking the trash can icon in the display logic modal or deleting the entire customization using the trash can icon in the customization container.
  3. You can cancel or close the modal at any point. 

**Note:** Unsaved changes will not be applied to your listing.

## Display logic and .xlsx template files

Your display logic will not appear in the .xlsx template file, but it will
persist after the template is applied to a new listing, where you can edit or
remove the logic as required. The display logic will appear with the same
values that the template was generated from. To learn more about setting up a
custom template, go to [Customization templates](/gp/help/GNDXUC2C7DM3SRMK).

