# BuyWise — Development Roadmap

## Project Status

**Project:** BuyWise  
**Tagline:** Compare Everything. Buy Wise.

**Current Phase:** Phase 1 — Repository & Architecture

---

# Phase 0 — Product Definition

Status: COMPLETE

- [x] Project name finalized
- [x] Tagline finalized
- [x] Product vision defined
- [x] Target users defined
- [x] V1 scope defined
- [x] Product identity model defined
- [x] Data principles defined
- [x] Search philosophy defined
- [x] Recommendation philosophy defined
- [x] Data-source strategy defined
- [x] V1 out-of-scope defined
- [x] Long-term expansion strategy defined

---

# Phase 1 — Repository & Architecture

Status: IN PROGRESS

## 1.1 Local Project Foundation

- [x] Create BuyWise project folder
- [x] Open project in VS Code
- [x] Create frontend directory
- [x] Create backend directory
- [x] Create database directory
- [x] Create data directory
- [x] Create docs directory
- [x] Create scripts directory
- [x] Create tests directory
- [x] Create .env.example
- [x] Create .gitignore
- [x] Create README.md
- [x] Create docker-compose.yml
- [x] Create PROJECT_BLUEPRINT.md
- [ ] Create ROADMAP.md

## 1.2 Development Environment

- [ ] Verify Node.js
- [ ] Verify npm
- [ ] Verify Python
- [ ] Create Python virtual environment
- [ ] Verify PostgreSQL/Docker availability
- [ ] Configure environment variables
- [ ] Configure development scripts

## 1.3 Frontend Foundation

- [ ] Initialize Next.js
- [ ] Configure TypeScript
- [ ] Configure frontend structure
- [ ] Create initial layout
- [ ] Create basic homepage
- [ ] Verify local frontend server

## 1.4 Backend Foundation

- [ ] Create Python virtual environment
- [ ] Install FastAPI
- [ ] Create backend application
- [ ] Create health endpoint
- [ ] Configure environment variables
- [ ] Verify backend server
- [ ] Verify API documentation

## 1.5 Database Foundation

- [ ] Decide local PostgreSQL setup
- [ ] Create BuyWise database
- [ ] Configure database connection
- [ ] Create initial migration system
- [ ] Verify backend → database connection

## Phase 1 Exit Criteria

Phase 1 is complete when:

- Frontend runs locally
- Backend runs locally
- Database runs locally
- Backend can connect to database
- Environment variables are configured
- Project structure is stable
- Documentation foundation exists

---

# Phase 2 — UI/UX Design

Status: NOT STARTED

- [ ] Define design system
- [ ] Define typography
- [ ] Define colors
- [ ] Define spacing
- [ ] Define buttons
- [ ] Define cards
- [ ] Define tables
- [ ] Design homepage
- [ ] Design search results
- [ ] Design product page
- [ ] Design comparison page
- [ ] Design category page
- [ ] Design wishlist
- [ ] Design account page
- [ ] Design loading states
- [ ] Design empty states
- [ ] Design error states
- [ ] Design mobile layouts

## Phase 2 Exit Criteria

All major V1 screens have a clear UI specification.

---

# Phase 3 — Frontend Development

Status: NOT STARTED

- [ ] Application layout
- [ ] Navbar
- [ ] Search bar
- [ ] Homepage
- [ ] Search results
- [ ] Product cards
- [ ] Product detail page
- [ ] Specification table
- [ ] Seller price cards
- [ ] Price history component
- [ ] Comparison interface
- [ ] Alternative products
- [ ] Recommendation card
- [ ] Wishlist
- [ ] Responsive design
- [ ] Loading states
- [ ] Error states

Initially frontend will use controlled seed/mock data.

---

# Phase 4 — Backend + Database

Status: NOT STARTED

- [ ] FastAPI architecture
- [ ] Database models
- [ ] Database migrations
- [ ] Product API
- [ ] Variant API
- [ ] Seller API
- [ ] Price API
- [ ] Search API
- [ ] Comparison API
- [ ] Recommendation API
- [ ] Category API
- [ ] User API
- [ ] API validation
- [ ] API tests

## Phase 4 Exit Criteria

Frontend → API → Database workflow works with seeded smartphone data.

---

# Phase 5 — Smartphone Data Engine

Status: NOT STARTED

Pipeline:

Source
↓
Collector
↓
Raw Data
↓
Parser
↓
Product Matcher
↓
Normalizer
↓
Validator
↓
Database

Tasks:

- [ ] Define smartphone schema
- [ ] Define source schema
- [ ] Build source adapter structure
- [ ] Build raw-data storage
- [ ] Build parser
- [ ] Build normalization
- [ ] Build product matching
- [ ] Build variant matching
- [ ] Build duplicate detection
- [ ] Build validation
- [ ] Track source timestamps
- [ ] Track data freshness
- [ ] Detect suspicious prices
- [ ] Store verified data

---

# Phase 6 — Search Engine

Status: NOT STARTED

- [ ] Product search
- [ ] Search normalization
- [ ] Autocomplete
- [ ] Fuzzy matching
- [ ] Filters
- [ ] Sorting
- [ ] Search ranking
- [ ] Requirement search
- [ ] Intent extraction
- [ ] Zero-result handling
- [ ] Search performance optimization

Initial search can use PostgreSQL capabilities.

Advanced search infrastructure can be added later if required.

---

# Phase 7 — Comparison Engine

Status: NOT STARTED

- [ ] Comparison API
- [ ] Product selection
- [ ] Specification normalization
- [ ] Side-by-side comparison
- [ ] Difference highlighting
- [ ] Price comparison
- [ ] Category-specific attributes
- [ ] Trade-off detection

---

# Phase 8 — Price Intelligence

Status: NOT STARTED

- [ ] Price snapshots
- [ ] Current price
- [ ] Historical price
- [ ] Lowest price
- [ ] Average price
- [ ] Price changes
- [ ] Seller comparison
- [ ] Price history chart
- [ ] Data freshness
- [ ] Price anomaly detection
- [ ] Price alerts architecture

---

# Phase 9 — AI Recommendation Engine

Status: NOT STARTED

Pipeline:

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
Evaluation
↓
Trade-offs
↓
Recommendation
↓
Explanation

Tasks:

- [ ] Define recommendation schema
- [ ] Define user preference model
- [ ] Build requirement extraction
- [ ] Build budget constraints
- [ ] Build priority extraction
- [ ] Build weighted scoring
- [ ] Build product matching
- [ ] Build explanation generation
- [ ] Build alternatives
- [ ] Add AI layer
- [ ] Validate AI output against database facts

---

# Phase 10 — User Features

Status: NOT STARTED

- [ ] User registration
- [ ] Login
- [ ] Authentication
- [ ] User profile
- [ ] Wishlist
- [ ] Saved comparisons
- [ ] Recently viewed
- [ ] User preferences
- [ ] Price alerts
- [ ] Social authentication

---

# Phase 11 — Admin Dashboard

Status: NOT STARTED

- [ ] Admin authentication
- [ ] Product management
- [ ] Variant management
- [ ] Product merge/split
- [ ] Seller management
- [ ] Source monitoring
- [ ] Failed ingestion jobs
- [ ] Price anomaly review
- [ ] Data quality monitoring
- [ ] Category management
- [ ] User management
- [ ] System health

---

# Phase 12 — Testing & Security

Status: NOT STARTED

## Testing

- [ ] Unit tests
- [ ] API tests
- [ ] Integration tests
- [ ] Data validation tests
- [ ] Data quality tests
- [ ] Frontend tests
- [ ] End-to-end tests
- [ ] Regression tests

## Security

- [ ] Secret management
- [ ] Authentication security
- [ ] Authorization
- [ ] Input validation
- [ ] SQL injection protection
- [ ] XSS protection
- [ ] CSRF protection where applicable
- [ ] Rate limiting
- [ ] Secure error handling
- [ ] Dependency security
- [ ] Database permissions
- [ ] Backup strategy

---

# Phase 13 — Deployment

Status: NOT STARTED

- [ ] Choose domain
- [ ] Frontend hosting
- [ ] Backend hosting
- [ ] Managed PostgreSQL
- [ ] Worker infrastructure
- [ ] Environment configuration
- [ ] HTTPS
- [ ] Database migrations
- [ ] Backups
- [ ] CI/CD
- [ ] Health checks
- [ ] Logging
- [ ] Analytics

---

# Phase 14 — Monitoring & Improvements

Status: NOT STARTED

Monitor:

- Website uptime
- Frontend performance
- API latency
- API errors
- Database performance
- Data-source failures
- Data freshness
- Price anomalies
- Search failures
- Zero-result searches
- Recommendation quality
- Infrastructure health

---

# Phase 15 — Category Expansion

Status: FUTURE

## V2

- [ ] Laptops
- [ ] Tablets
- [ ] TVs
- [ ] Headphones
- [ ] Cameras
- [ ] Monitors

## V3

- [ ] Cars
- [ ] Bikes
- [ ] EVs

## V4

- [ ] Appliances
- [ ] Fashion
- [ ] General shopping

## V5

- [ ] Food
- [ ] Travel
- [ ] Services

Each new category must have:

- Category schema
- Product identity model
- Variant model
- Specification model
- Data sources
- Normalization rules
- Comparison attributes
- Search intent
- Recommendation criteria
- Data quality tests

---

# Development Protocol

Every development session follows:

TASK
↓
BUILD
↓
TEST
↓
COMMIT
↓
REVIEW
↓
NEXT TASK

## Rules

1. Complete the current task before moving ahead.
2. Do not modify unrelated code.
3. Inspect before changing.
4. Make the smallest correct change.
5. Test after changes.
6. Fix the actual failing layer.
7. Document important changes.
8. Keep the architecture scalable.
9. Never invent external data.
10. Never expose secrets in source code.

---

# Definition of Done

A task is considered complete only when:

- Implementation is complete.
- Relevant tests pass.
- Existing functionality still works.
- Documentation is updated when required.
- No unnecessary changes were introduced.
- The work is ready for the next task.

---

# Current Next Task

**Phase 1 → Task 1.2**

Verify and configure the local development environment:

- Node.js
- npm
- Python
- Python virtual environment
- PostgreSQL / Docker
- Environment variables

Do not start feature development until the environment foundation is ready.