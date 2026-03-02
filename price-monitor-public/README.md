# 💰 Price Monitor - Automated E-commerce Price Tracking System

A professional-grade **web scraping** and **automation** solution that monitors product prices across e-commerce platforms in real-time, detects price changes, and sends instant alerts. Perfect for competitive pricing analysis, deal hunting, and price optimization.

![Python](https://img.shields.io/badge/Python-3.7+-blue?style=flat-square&logo=python)
![BeautifulSoup](https://img.shields.io/badge/Web%20Scraping-BeautifulSoup-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## 🎯 Features

✅ **Automated Web Scraping** - Extract real-time product prices and stock status from e-commerce websites  
✅ **Price Change Detection** - Monitors price fluctuations with customizable percentage thresholds  
✅ **Stock Status Tracking** - Get alerted instantly when products go out of stock  
✅ **Email Notifications** - Sends HTML-formatted alerts directly to your inbox  
✅ **Price History Logging** - Maintains comprehensive CSV records of all price changes  
✅ **Automated Reports** - Generates Excel reports for data analysis  
✅ **Scheduled Execution** - Easily integrate with cron jobs for continuous monitoring  

---

## 🛠️ Tech Stack

- **Python 3.7+** - Core language
- **BeautifulSoup** - Web scraping & HTML parsing
- **Requests** - HTTP client for fetching web pages
- **Pandas** - Data processing & CSV/Excel handling
- **SMTP** - Gmail integration for email alerts
- **Cron** - Task scheduling for automated execution

---

## 📋 Project Structure

```
price_monitor/
├── main.py              # Core orchestration script
├── scraper.py           # Web scraping logic
├── alert.py             # Email notification system
├── reporter.py          # Excel report generation
├── products.csv         # Product URLs & price thresholds
├── price_history.csv    # Historical price data
└── logs/                # Execution logs
```

---

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager
- Gmail account (for email notifications)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/price-monitor.git
   cd price-monitor
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install requests beautifulsoup4 pandas openpyxl
   ```

4. **Configure your products**
   
   Edit `products.csv` and add your monitoring targets:
   ```csv
   product_name,url,threshold_percent
   Laptop A,https://example.com/product/1,5
   Phone B,https://example.com/product/2,3
   ```

5. **Set up email notifications**
   
   Update credentials in `main.py`:
   ```python
   SENDER = "your-email@gmail.com"
   PASSWORD = "your-app-password"  # Use Google App Password for security
   RECEIVER = "alert-recipient@gmail.com"
   ```

   🔒 **Security Tip**: Use [Google App Passwords](https://myaccount.google.com/apppasswords) instead of your actual Gmail password.

---

## 📖 Usage

### Run Once
```bash
python main.py
```

### Schedule Automated Monitoring

Set up cron job to run every 30 minutes:
```bash
crontab -e
```

Add this line:
```bash
*/30 * * * * cd /path/to/price-monitor && python main.py >> logs/execution.log 2>&1
```

### Generate Reports
```bash
python reporter.py
```

Creates `report.xlsx` with the latest prices for all monitored products.

---

## 📊 How It Works

1. **Scraping** → Fetches product pages and extracts prices using BeautifulSoup
2. **Comparison** → Compares current prices with historical data
3. **Detection** → Identifies price changes beyond configured thresholds (e.g., 5% drop = alert)
4. **Notification** → Sends formatted HTML email with detailed price information
5. **Logging** → Records all changes in `price_history.csv` for analysis

### Alert Example
When a price drops 5% or more:
```
📉 Laptop A price dropped 7.50%
Old: $1200 → New: $1110
```

---

## 🎨 Email Alert Format

Alerts are sent in professional HTML format including:
- Product name and price change percentage
- Old vs. new pricing
- Stock status updates
- Timestamp information

---

## 💡 Use Cases

### Freelancing & Business Applications
- **Price Comparison Services** - Monitor competitors' pricing strategies
- **Deal Aggregation** - Build deal notification platforms
- **Inventory Management** - Track stock levels across vendors
- **Market Analysis** - Gather real-time pricing data for reports
- **Arbitrage** - Identify pricing discrepancies across platforms
- **Customer Alerts** - Notify users about price drops on their wishlists

### Money-Making Opportunities
- Offer price monitoring as a service
- Create premium alert systems with custom thresholds
- Bundle with price optimization consulting
- Develop browser extensions using this logic

---

## 🔧 Customization

### Adjusting Price Thresholds
Edit `products.csv` - the `threshold_percent` column controls alert sensitivity:
```csv
product_name,url,threshold_percent
Gaming Laptop,https://...,2      # Alert on 2% change (sensitive)
Budget Phone,https://...,10      # Alert on 10% change (less sensitive)
```

### Adding New Products
Simply add rows to `products.csv`:
```bash
echo "New Product,https://example.com/product,5" >> products.csv
```

### Changing Alert Recipients
Modify `main.py` to send alerts to multiple recipients or different emails based on product category.

---

## 📈 Performance & Scalability

- **Lightweight** - Minimal resource usage, efficient scraping
- **Scalable** - Monitor 100+ products simultaneously
- **Error Handling** - Gracefully handles network failures and timeouts
- **Logging** - Track execution history in `cron_log.log` for debugging

---

## ⚠️ Legal & Ethical Considerations

- Always check a website's `robots.txt` and Terms of Service before scraping
- Respect rate limits - add delays between requests if monitoring many sites
- Use appropriate User-Agent headers (included in this project)
- Consider reaching out to websites for API access first
- Some sites explicitly prohibit scraping - respect those boundaries

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Email not sending | Verify Gmail credentials, enable 2FA, use App Password |
| Prices not updating | Check URL format, verify HTML structure hasn't changed |
| Scraping errors | Add requests with retry logic, increase timeout value |
| CSV errors | Ensure `products.csv` has correct column headers |

---

## 📝 Sample Output

**Console Output:**
```
Price history updated.
Alerts sent.
```

**Generated Files:**
- `price_history.csv` - Complete price tracking database
- `report.xlsx` - Latest prices in Excel format
- `logs/execution.log` - Cron execution history

---

## 🚦 Future Enhancements

- [ ] Web dashboard for price visualization
- [ ] Multiple website template support
- [ ] Advanced filtering (category-based alerts)
- [ ] Price trend predictions using ML
- [ ] Browser extension
- [ ] REST API for integration

---

## 💼 Freelancing Benefits

This project showcases:
- **Web Scraping Expertise** - Real-world data extraction
- **Full-Stack Automation** - From scraping to notifications
- **Data Processing** - CSV/Excel handling with Pandas
- **Error Handling** - Production-ready code
- **System Integration** - Scheduled execution with cron
- **Professional Code** - Clean, modular, maintainable

Perfect for:
- Freelance automation projects
- Web scraping service offerings
- Data collection consulting
- E-commerce optimization services

---

## 📄 License

MIT License - Feel free to use this for commercial or personal projects.

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

---

## 📧 Contact

For inquiries about custom scraping solutions or automation services, reach out!

---

## 🙏 Acknowledgments

Built with:
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) - HTML parsing
- [Pandas](https://pandas.pydata.org/) - Data manipulation
- [Requests](https://requests.readthedocs.io/) - HTTP library

---

**⭐ If this helps you, consider starring the repository!**
