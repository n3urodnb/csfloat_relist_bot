# CSFloat Relist Bot 🏆

**Production-grade Python automation** for CSFloat marketplace. Automatically relists all stall items.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)

## 🚀 Quick Start

```bash
git clone https://github.com/n3urodnb/csfloat-relist-bot
cd csfloat-relist-bot
pip install -r requirements.txt
python relist.py
Add your CSFloat API key and description for all listing
```

## ✨ Features
  ✅ Async API calls - GET stall → DELETE → CREATE listings

  🔄 Production retry logic (5x attempts)

  🔐 Secure .env API key management

  📦 Includes csfloat_api fork with new methods

## 📋 Tech Stack
    Main: relist.py (your automation)

    Fork: csfloat_api/ [Albert-Bruun-Thomsen fork](https://github.com/Albert-Bruun-Thomsen/csfloat_api)

    Deps: python-dotenv (requirements.txt)

## 🙏 Credits & Acknowledgments

**Fork used**: [![Albert-Bruun-Thomsen/csfloat_api](https://img.shields.io/badge/Fork-Albert--Bruun--Thomsen%2Fcsfloat--api-blue)](https://github.com/Albert-Bruun-Thomsen/csfloat_api)  
**Original library**: [![Rushifakami/csfloat_api](https://img.shields.io/badge/Original-Rushifakami%2Fcsfloat--api-green)](https://github.com/Rushifakami/csfloat_api)  

---

*This project includes the full csfloat_api fork locally for reliable deployment. All credits to the original authors!*

**Made with ❤️ for CSFloat trading automation**


