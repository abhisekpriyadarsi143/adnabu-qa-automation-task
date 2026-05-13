# Manual Test Cases — AdNabuTestStore

## Task 1: Product Search

---

### TC-S01 | Positive | Search for a valid product

| Field | Detail |
|---|---|
| **Test ID** | TC-S01 |
| **Module** | Product Search |
| **Type** | Positive |
| **Priority** | High |

**Steps:**
1. Open the store homepage
2. Click the search icon
3. Enter "Selling Plans Ski Wax"
4. Press Enter / click Search

**Expected Result:** Results page displays at least 1 product card containing "Selling Plans Ski Wax" in the title.

---

### TC-S02 | Negative | Search for a non-existent product

| Field | Detail |
|---|---|
| **Test ID** | TC-S02 |
| **Module** | Product Search |
| **Type** | Negative |
| **Priority** | High |

**Steps:**
1. Click the search icon
2. Enter "xyznonexistentproduct999"
3. Press Enter

**Expected Result:** A "no results found" message is shown. Zero product cards displayed.

---

### TC-S03 | Negative | Submit empty search

| Field | Detail |
|---|---|
| **Test ID** | TC-S03 |
| **Module** | Product Search |
| **Type** | Negative |
| **Priority** | Medium |

**Steps:**
1. Click the search icon
2. Leave the field empty
3. Press Enter

**Expected Result:** Page does not crash. Either shows all products or empty state — no JS error.

---

### TC-S04 | Positive | Case-insensitive search

| Field | Detail |
|---|---|
| **Test ID** | TC-S04 |
| **Module** | Product Search |
| **Type** | Positive |
| **Priority** | Medium |

**Steps:**
1. Search "SELLING PLANS SKI WAX" (all caps)

**Expected Result:** Same results as lowercase search. "Selling Plans Ski Wax" appears in results.

---

### TC-S05 | Negative | Special characters in search

| Field | Detail |
|---|---|
| **Test ID** | TC-S05 |
| **Module** | Product Search |
| **Type** | Negative |
| **Priority** | Medium |

**Steps:**
1. Search "!@#$%^&*()"

**Expected Result:** No server error (no HTTP 500). Page returns "no results" gracefully.

---

### TC-S06 | Edge | Extremely long search query

| Field | Detail |
|---|---|
| **Test ID** | TC-S06 |
| **Module** | Product Search |
| **Type** | Edge |
| **Priority** | Low |

**Steps:**
1. Search a 300-character string

**Expected Result:** Page does not crash or timeout. Handles gracefully.

---

## Task 1: Add to Cart

---

### TC-C01 | Positive | Add to Cart button visible on product page

| Field | Detail |
|---|---|
| **Test ID** | TC-C01 |
| **Module** | Add to Cart |
| **Type** | Positive |
| **Priority** | High |

**Steps:**
1. Search for "Selling Plans Ski Wax"
2. Click product from results

**Expected Result:** Product detail page loads. "Add to Cart" button is visible and enabled.

---

### TC-C02 | Positive | Cart count increments after adding product

| Field | Detail |
|---|---|
| **Test ID** | TC-C02 |
| **Module** | Add to Cart |
| **Type** | Positive |
| **Priority** | High |

**Steps:**
1. Navigate to product page
2. Note cart count (e.g., 0)
3. Click "Add to Cart"

**Expected Result:** Cart icon count increments by 1.

---

### TC-C03 | Positive | Success notification appears

| Field | Detail |
|---|---|
| **Test ID** | TC-C03 |
| **Module** | Add to Cart |
| **Type** | Positive |
| **Priority** | High |

**Steps:**
1. Click "Add to Cart" on product page

**Expected Result:** A notification/drawer appears confirming the item was added.

---

### TC-C04 | Positive | Correct product appears in cart

| Field | Detail |
|---|---|
| **Test ID** | TC-C04 |
| **Module** | Add to Cart |
| **Type** | Positive |
| **Priority** | High |

**Steps:**
1. Add "Selling Plans Ski Wax" to cart
2. Navigate to /cart

**Expected Result:** Cart page shows "Selling Plans Ski Wax" as a line item.

---

### TC-C05 | Negative | Cart not empty after adding

| Field | Detail |
|---|---|
| **Test ID** | TC-C05 |
| **Module** | Add to Cart |
| **Type** | Negative |
| **Priority** | Medium |

**Steps:**
1. Add product to cart
2. Open cart page

**Expected Result:** "Your cart is empty" message is NOT shown.

---

### TC-C06 | Edge | Add same product twice

| Field | Detail |
|---|---|
| **Test ID** | TC-C06 |
| **Module** | Add to Cart |
| **Type** | Edge |
| **Priority** | Medium |

**Steps:**
1. Add "Selling Plans Ski Wax" to cart
2. Go back to same product
3. Add to cart again

**Expected Result:** Cart either shows quantity = 2 for one line item, or two separate line items — but does not error.
