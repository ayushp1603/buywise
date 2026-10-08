# BuyWise — Project Blueprint

## 1. Project Identity

**Project Name:** BuyWise

**Tagline:** Compare Everything. Buy Wise.

**Project Type:** Universal Product & Service Comparison Platform

**Initial Category:** Smartphones

---

# 2. Product Vision

BuyWise is an intelligent comparison and decision-support platform that helps users discover, compare, understand, and choose products based on their requirements, specifications, prices, reviews, historical pricing, and personal priorities.

The long-term vision is to build a universal comparison engine that can support multiple product and service categories through a common architecture.

---

# 3. Core Problem

Users currently need to visit multiple websites to answer simple buying questions.

For example, when buying a smartphone, a user may need to:

1. Search for products.
2. Check specifications.
3. Visit manufacturer websites.
4. Compare Amazon prices.
5. Compare Flipkart prices.
6. Check reviews.
7. Search historical prices.
8. Find alternatives.
9. Decide which product fits their needs.

BuyWise aims to bring these activities into one platform.

---

# 4. Core Solution

BuyWise will provide:

- Product discovery
- Product search
- Requirement-based search
- Specification comparison
- Seller price comparison
- Price history
- Reviews and ratings
- Product alternatives
- Personalized recommendations
- Transparent trade-off explanations

---

# 5. V1 Scope

The first production-oriented version will focus on smartphones.

## V1 Features

### Discovery

- Global search
- Product search
- Requirement-based search
- Search suggestions
- Filters
- Sorting

### Product Pages

- Product name
- Brand
- Product images
- Product variants
- Key highlights
- Specifications
- Ratings
- Reviews
- Availability

### Price Intelligence

- Current price
- Seller
- Discount
- Offer information
- Delivery information where available
- Last updated timestamp
- Historical price
- Lowest recorded price

### Comparison

- Side-by-side comparison
- Specification differences
- Price differences
- Feature differences
- Key advantages
- Trade-offs

### Recommendation

- Requirement extraction
- Budget constraints
- Priority extraction
- Product matching
- Weighted scoring
- Recommendation explanation
- Alternatives

### User Features

- Wishlist
- Saved comparisons
- Recently viewed products

---

# 6. Product Identity Model

BuyWise must distinguish between:

## Product Family

Example:

iPhone 17

## Product Variant

Example:

iPhone 17 — 256GB — Black

## Seller Offer

Example:

Amazon — ₹79,999

The conceptual relationship is:

Product Family
↓
Product Variant
↓
Seller Offer
↓
Price History

This prevents different variants from being incorrectly treated as the same product.

---

# 7. Data Principles

Every important piece of external data should maintain:

- Value
- Source
- Timestamp
- Validation status

Example:

Price:
₹79,999

Source:
Seller / Authorized Feed

Updated:
Timestamp

Status:
Verified / Unverified / Stale

BuyWise must not present stale information as live information.

Missing information must remain missing rather than being invented.

---

# 8. Data Pipeline

The planned data pipeline is:

Permitted Data Source
↓
Collector
↓
Raw Data
↓
Parser
↓
Product / Variant Matcher
↓
Normalizer
↓
Validator
↓
Database
↓
Search / Cache
↓
Frontend

Production data sources must be legally and technically permitted, such as:

- Official manufacturer data
- Authorized APIs
- Affiliate feeds
- Merchant feeds
- Other permitted sources

---

# 9. Search Architecture

BuyWise will support two major search modes.

## Direct Product Search

Example:

iPhone 17

The system identifies relevant products.

## Requirement Search

Example:

Phone under ₹50,000 for gaming and camera

The system extracts:

Budget:
≤ ₹50,000

Priorities:
Gaming
Camera

The recommendation engine then evaluates eligible products.

---

# 10. Recommendation Architecture

The recommendation pipeline will be:

User Requirement
↓
Intent Extraction
↓
Structured Constraints
↓
Eligible Products
↓
Weighted Criteria
↓
Product Evaluation
↓
Trade-off Analysis
↓
Recommendation
↓
Explanation

Recommendations should be transparent.

The system should explain:

- Why a product matches
- Which requirements it satisfies
- Where it performs well
- Where it has trade-offs
- Which alternatives exist

The AI layer must not invent product facts.

---

# 11. High-Level System Architecture

```text
                        USER
                          |
                          v
                 Next.js Frontend
                          |
                          v
                    FastAPI API
                          |
        +-----------------+-----------------+
        |                 |                 |
        v                 v                 v
   Search Service   Product Service   Price Service
        |                 |                 |
        +-----------------+-----------------+
                          |
        +-----------------+-----------------+
        |                 |                 |
        v                 v                 v
 Comparison Service  Recommendation     User Service
                          Service
                          |
                          v
                    PostgreSQL
                          |
                          v
                  Data Ingestion
                          |
                          v
                External Data Sources