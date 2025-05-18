# Real-World Use Cases for Regular Expressions

## Practical Examples with Real-World Scenarios

### 1. Email Validation

**Regex:** `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`

#### Use Case: User Registration System

```python
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        print(f"✅ Valid email: {email}")
        return True
    else:
        print(f"❌ Invalid email: {email}")
        return False

# Test cases from real-world scenarios
validate_email("john.doe@company.com")  # Standard work email
validate_email("sales+2023@store.com")  # Email with plus addressing
validate_email("user@sub.domain.co.uk")  # Multi-level domain
validate_email("invalid@.com")  # Missing domain name
validate_email("name@domain")  # Missing TLD
```

**Why it matters:**

- Prevents invalid email formats from entering your database
- Reduces bounce rates in email marketing campaigns
- Ensures proper formatting before sending verification emails

### 2. URL Matching

**Regex:** `https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)`

#### Use Case: Web Scraper for Product Links

```python
import re

def extract_product_links(html):
    url_pattern = r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)'
    product_links = re.findall(url_pattern, html)
    
    # Filter for product pages only
    product_links = [link[0] for link in product_links 
                    if '/product/' in link[0] or '/item/' in link[0]]
    
    print(f"Found {len(product_links)} product links")
    return product_links

# Example HTML content from an e-commerce site
sample_html = """
<div class="products">
    <a href="https://www.example.com/product/123">Product 1</a>
    <a href="/deals">Today's Deals</a>
    <img src="https://cdn.example.com/images/logo.png">
    <a href="http://sub.example.com/item/abc-xyz">Product 2</a>
</div>
"""

extract_product_links(sample_html)
```

**Why it matters:**

- Ensures you only collect valid URLs during web scraping
- Helps filter out non-product links (images, stylesheets, etc.)
- Handles both HTTP and HTTPS protocols

### 3. Date Format (YYYY-MM-DD)

**Regex:** `^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$`

#### Use Case: Data Pipeline Date Validation

```python
import re
from datetime import datetime

def validate_and_convert_dates(data_records):
    date_pattern = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$'
    valid_records = []
    
    for record in data_records:
        if re.match(date_pattern, record['date']):
            try:
                # Additional validation using datetime
                datetime.strptime(record['date'], '%Y-%m-%d')
                valid_records.append(record)
            except ValueError:
                print(f"Invalid calendar date: {record['date']}")
        else:
            print(f"Malformed date format: {record['date']}")
    
    return valid_records

# Sample data from a CSV import
records = [
    {'date': '2023-05-15', 'value': 100},
    {'date': '2023-13-01', 'value': 200},  # Invalid month
    {'date': '2023-02-30', 'value': 300},  # Invalid day for February
    {'date': '15-05-2023', 'value': 400},  # Wrong format
    {'date': '2023-11-31', 'value': 500}   # November only has 30 days
]

clean_records = validate_and_convert_dates(records)
```

**Why it matters:**

- Ensures consistent date formatting in databases
- Prevents "February 30th" type errors
- Validates dates before they enter analytics systems

### 4. HTML Tags

**Regex:** `<([a-z]+)([^<]+)*(?:>(.*)<\/\1>|\s+\/>)`

#### Use Case: Content Sanitization

```python
import re

def sanitize_html(html_content, allowed_tags=['p', 'br', 'strong', 'em']):
    pattern = r'<([a-z]+)([^<]+)*(?:>(.*)<\/\1>|\s+\/>)'
    
    def tag_replacer(match):
        tag = match.group(1)
        if tag in allowed_tags:
            return match.group(0)  # Keep allowed tags
        else:
            return ''  # Remove disallowed tags
    
    clean_html = re.sub(pattern, tag_replacer, html_content)
    
    # Additional XSS protection
    clean_html = clean_html.replace('javascript:', '')
    return clean_html

# User-generated content with potential XSS
user_content = """
<p>Hello world!</p>
<script>alert('XSS');</script>
<img src="x" onerror="alert(1)">
<strong>Important</strong> text
<div style="dangerous: expression()">
"""

safe_content = sanitize_html(user_content)
print(safe_content)
```

**Why it matters:**

- Prevents XSS (Cross-Site Scripting) attacks
- Allows only safe HTML tags in user-generated content
- Maintains formatting while removing dangerous elements

### 5. Password Requirements

**Regex:** `^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$`

#### Use Case: Account Security Enforcement

```python
import re

def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$'
    
    if len(password) < 8:
        return "Password must be at least 8 characters"
    if not re.search(r'[a-z]', password):
        return "Password needs at least one lowercase letter"
    if not re.search(r'[A-Z]', password):
        return "Password needs at least one uppercase letter"
    if not re.search(r'\d', password):
        return "Password needs at least one number"
    if re.search(r'[^a-zA-Z\d]', password):
        return "Password should only contain letters and numbers"
    
    return "Password is valid"

# User password attempts
passwords = [
    "Secret123",  # Valid
    "weak",       # Too short
    "nocaps123",  # Missing uppercase
    "NOLOWERS1",  # Missing lowercase
    "NoNumbers",  # Missing digits
    "Valid!123"   # Contains special character
]

for pwd in passwords:
    print(f"'{pwd}': {validate_password(pwd)}")
```

**Why it matters:**

- Enforces strong password policies
- Provides specific feedback about requirements
- Reduces vulnerability to brute force attacks

## Performance Considerations in Production

### 1. Compiled Patterns in a Web Application

```python
# In application initialization
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

# In request handler
def handle_signup(request):
    email = request.POST.get('email')
    if not EMAIL_REGEX.match(email):
        return HttpResponse("Invalid email format", status=400)
    # Process signup...
```

**Why compile?**

- 3-5x faster for repeated use
- Especially important in high-traffic web apps

### 2. Avoiding Catastrophic Backtracking

```python
# Dangerous pattern (exponential backtracking)
dangerous_pattern = r'^(a+)+$'

# Safer alternative
safe_pattern = r'^a+$'

# Test with malicious input
malicious_input = 'a' * 100 + '!'

# This could hang your application
# re.match(dangerous_pattern, malicious_input)

# This fails fast
re.match(safe_pattern, malicious_input)
```

**Real-world impact:**

- Malicious inputs can DOS your server
- AWS WAF uses regex limits to prevent this

## Common Pitfalls in Business Applications

### 1. Over-Matching in Log Analysis

```python
# Trying to extract order IDs from logs
log_line = "2023-05-15 ORDER #AB12345 processed by user123"

# Bad approach - too greedy
bad_pattern = r'#.*\d'
print(re.findall(bad_pattern, log_line))  # ['#AB12345 processed by user123']

# Better approach - be specific
good_pattern = r'#[A-Z]{2}\d{5}'
print(re.findall(good_pattern, log_line))  # ['#AB12345']
```

**Impact:**

- Incorrect data extraction leads to bad analytics
- May capture sensitive information unintentionally

### 2. Anchoring Issues in Configuration Files

```python
# Validating API keys in config
config = """
api_key = abc123-xyz456
temp_key = old123-abc456
"""

# Without anchors - matches partial keys
no_anchor = r'\b[a-z]{3}\d{3}-[a-z]{3}\d{3}\b'
print(re.findall(no_anchor, config))  # ['abc123-xyz456', 'old123-abc456']

# With anchors - matches whole keys only
with_anchor = r'^[a-z]{3}\d{3}-[a-z]{3}\d{3}$'
for line in config.split('\n'):
    key = line.split('=')[-1].strip()
    if re.match(with_anchor, key):
        print(f"Valid key: {key}")
```

**Impact:**

- Prevents partial matches of sensitive keys
- Ensures strict format compliance

These examples demonstrate how regex is used in real production environments, showing both proper implementations and common mistakes to avoid.
