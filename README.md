# purwadhika.capstone1.jundi
# Hospital Patient Management System  
**Purwadhika Data Science Bootcamp - Capstone 1**  

## 🏥 Project Overview
A command-line interface (CLI) application for hospital patient data management with full CRUD (Create, Read, Update, Delete) operations. This project demonstrates core Python fundamentals in real-world scenarios.
## ✨ Key Features

## Key Features
1. **Patient Data Management**:
   - Add new patients with automatic validation
   - View data with name sorting option
   - Partial updates (modify specific fields only)
   - Delete data with double confirmation

2. **Smart Validation System**:
   - Automatic input standardization (uppercase names, blood types)
   - Allowlist for gender (Male/Female) and blood types (A/B/AB/O)
   - Numeric validation for age (0-120 years)
   - Duplicate Patient ID prevention

##  Validation Rules
| Field         | Rules                                   | Example Handling              |
|---------------|-----------------------------------------|--------------------------------|
| Patient ID    | Uppercase conversion, Unique check      | `p123` → `P123` (auto-fixed)  |
| Name          | Mandatory, Uppercase enforced           | `john` → `JOHN`               |
| Gender        | Strict Male/Female selection            | `male` → `Male`               |
| Age           | 0-120 numeric range                     | `150` → Rejected              |
| Blood Type    | Medical-standard values (A/B/AB/O)      | `a+` → Rejected               |
| Address       | Non-empty text input                    | Empty → Retry prompt          |

